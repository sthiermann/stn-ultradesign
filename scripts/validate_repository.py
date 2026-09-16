#!/usr/bin/env python3
"""Check this repository's package invariants without fetching dependencies.

This is an original, deliberately narrow repository check. It does not replace
client manifest validators, install the plugin, inspect an app, or grade UX.
"""

import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
NAME = "stn-ultradesign"
SKILL = ROOT / "skills" / NAME
REQUIRED = (
    "README.md", "LICENSE", "CONTRIBUTING.md", "PRIVACY.md",
    "docs/installation.md",
    ".codex-plugin/plugin.json", ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json", f"skills/{NAME}/SKILL.md",
    f"skills/{NAME}/agents/openai.yaml", f"skills/{NAME}/references/project-research.md",
    f"skills/{NAME}/references/delivery-workflow.md",
    f"skills/{NAME}/scripts/audit_coverage.py",
)


def srcset_urls(value):
    """Read candidate URLs without splitting commas inside data URLs.

    This only discovers dependencies; it does not validate image descriptors.
    """
    position = 0
    while position < len(value):
        while position < len(value) and value[position] in " \t\n\r\f,":
            position += 1
        start = position
        while position < len(value) and value[position] not in " \t\n\r\f":
            position += 1
        url = value[start:position]
        if not url:
            break
        yield url.rstrip(",")
        if not url.endswith(","):
            # Ordinary width/density descriptors end at the candidate separator.
            while position < len(value) and value[position] != ",":
                position += 1


class ReadmeImages(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "img" and attributes.get("src"):
            self.targets.append(("img[src]", attributes["src"]))
        if tag in {"img", "source"} and attributes.get("srcset"):
            self.targets.extend((f"{tag}[srcset]", url)
                                for url in srcset_urls(attributes["srcset"]))


def validate_readme(root, versions):
    """Check current release metadata and README image dependencies, locally.

    Historical prose is not release metadata. Only explicitly version-labelled
    text in README-referenced SVGs is compared; version-free artwork is valid.
    This does not render images, measure spacing, or check remote dependencies.
    """
    readme = root / "README.md"
    if not readme.is_file():
        return [], 0  # The required-file check reports this separately.
    errors = []
    prose = re.sub(r"(?ms)^```[^\n]*\n.*?^```\s*$", "",
                   readme.read_text(encoding="utf-8"))
    releases = re.findall(r"(?m)^Release\s+\*\*v(\d+\.\d+\.\d+)\*\*(?=\s|$)", prose)
    release = releases[0] if len(releases) == 1 else None
    if release is None:
        errors.append("README.md: expected one current-release declaration: Release **vMAJOR.MINOR.PATCH**")
    else:
        for label, version in versions.items():
            if release != version:
                errors.append(f"README.md: current release {release} differs from {label} plugin {version}")

    parser = ReadmeImages()
    parser.feed(prose)
    # Include Markdown images in the same SVG check; general links stay below.
    targets = parser.targets + [
        ("Markdown image", target.strip("<>"))
        for target in re.findall(r"!\[[^\]]*\]\((<[^>]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\)", prose)
    ]
    checked_assets = 0
    svg_paths = set()
    for origin, target in targets:
        try:
            parsed = urlsplit(target)
        except ValueError as exc:
            errors.append(f"README.md: invalid {origin} URL {target!r}: {exc}")
            continue
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        destination = (root / unquote(parsed.path)).resolve()
        checked_assets += 1
        if not destination.is_relative_to(root):
            errors.append(f"README.md: {origin} escapes package: {target}")
        elif not destination.is_file():
            errors.append(f"README.md: missing local image for {origin}: {target}")
        elif destination.suffix.lower() == ".svg":
            svg_paths.add(destination)

    # Match version labels and this package's original 'DESIGN SKILL / 0.1' label.
    # XML attributes, coordinates, comments and unlabelled numbers are excluded.
    labelled_version = re.compile(
        r"\b(?:(?:version|release|v)\s*[:/]?\s*|"
        r"(?:design\s+skill|stn\s+ultradesign)\s*/\s*)"
        r"v?(\d+\.\d+(?:\.\d+)?)(?![\w.])", re.IGNORECASE)
    for path in sorted(svg_paths):
        relative = path.relative_to(root)
        try:
            svg = ET.parse(path)
        except (OSError, ET.ParseError) as exc:
            errors.append(f"{relative}: cannot parse README SVG: {exc}")
            continue
        for element in svg.iter():
            if element.tag.rsplit("}", 1)[-1] != "text":
                continue
            for version in labelled_version.findall("".join(element.itertext())):
                normalized = version + ".0" if version.count(".") == 1 else version
                if release is not None and normalized != release:
                    errors.append(f"{relative}: labelled SVG version {version} differs from README release {release}")
    return errors, checked_assets


def main():
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    def read_json(relative):
        try:
            data = json.loads((ROOT / relative).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{relative}: {exc}")
            return {}
        require(isinstance(data, dict), f"{relative}: expected a JSON object")
        return data if isinstance(data, dict) else {}

    for relative in REQUIRED:
        require((ROOT / relative).is_file(), f"Missing required file: {relative}")

    codex = read_json(".codex-plugin/plugin.json")
    claude = read_json(".claude-plugin/plugin.json")
    marketplace = read_json(".claude-plugin/marketplace.json")
    for label, manifest in (("Codex", codex), ("Claude", claude)):
        require(manifest.get("name") == NAME, f"{label}: unexpected plugin name")
        version = manifest.get("version", "")
        require(isinstance(version, str) and bool(re.fullmatch(r"\d+\.\d+\.\d+", version)),
                f"{label}: expected a release version in major.minor.patch form")
        require(manifest.get("license") == "MIT", f"{label}: license differs from package")
        require(not ({"hooks", "mcpServers", "apps"} & manifest.keys()),
                f"{label}: this package has no external integrations or hooks")
    require(codex.get("version") == claude.get("version"), "Plugin versions differ")
    require(codex.get("skills") == "./skills/", "Codex skill path differs from layout")
    require(marketplace.get("name") == NAME, "Marketplace name differs from package")
    entries = marketplace.get("plugins", [])
    require(isinstance(entries, list) and len(entries) == 1 and
            isinstance(entries[0], dict) and entries[0].get("name") == NAME and
            entries[0].get("source") == "./", "Expected one plugin at marketplace root")
    readme_errors, checked_assets = validate_readme(
        ROOT, {"Codex": codex.get("version"), "Claude": claude.get("version")})
    errors.extend(readme_errors)

    skill_path = SKILL / "SKILL.md"
    if skill_path.is_file():
        text = skill_path.read_text(encoding="utf-8")
        header = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", text, re.DOTALL)
        require(header is not None, "SKILL.md: missing frontmatter")
        if header:
            fields = dict(re.findall(r"^([a-z-]+):\s*(.+)$", header.group(1), re.MULTILINE))
            require(fields.get("name") == NAME, "Skill name differs from directory")
            require(bool(fields.get("description", "").strip()), "Skill description is empty")
        require("[TODO:" not in text, "SKILL.md: unfinished scaffold placeholder")

    metadata = SKILL / "agents/openai.yaml"
    if metadata.is_file():
        require(f"${NAME}" in metadata.read_text(encoding="utf-8"),
                "Skill starter prompt does not invoke the current skill")

    checked_links = 0
    for path in sorted(ROOT.rglob("*")):
        if ".git" in path.relative_to(ROOT).parts or "__pycache__" in path.parts:
            continue
        if path.is_symlink():
            require(path.resolve().is_relative_to(ROOT),
                    f"Symlink escapes package: {path.relative_to(ROOT)}")
        if not path.is_file() or path.suffix not in {".md", ".py", ".json", ".yaml", ".yml", ".html"}:
            continue
        relative = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        if path.suffix == ".py":
            try:
                compile(text, str(relative), "exec")
            except SyntaxError as exc:
                errors.append(f"{relative}: {exc}")
        if path.suffix == ".json":
            try:
                json.loads(text)
            except json.JSONDecodeError as exc:
                errors.append(f"{relative}: {exc}")
        if path.suffix != ".md":
            continue
        obsolete_name = "product-" + "design-excellence"
        require(obsolete_name not in text, f"{relative}: obsolete skill path/name")
        require("/Users/" not in text and "file:///" not in text,
                f"{relative}: local workstation path is not portable")
        # Inline links only; fenced examples and remote URLs are outside this check.
        prose = re.sub(r"(?ms)^```[^\n]*\n.*?^```\s*$", "", text)
        for target in re.findall(r"\]\((<[^>]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\)", prose):
            target = target.strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve()
            checked_links += 1
            require(destination.is_relative_to(ROOT), f"{relative}: link escapes package: {target}")
            require(destination.exists(), f"{relative}: missing link target: {target}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Repository validation failed ({len(errors)} issues).", file=sys.stderr)
        return 1
    print(f"Repository validation passed; {checked_links} local Markdown links and "
          f"{checked_assets} local README image references checked.")
    print("This checks package consistency, not client installation or design quality.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
