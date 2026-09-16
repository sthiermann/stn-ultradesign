# Synthetic evaluations

These files were independently created while developing STN Ultradesign. They contain no real customer application, valid credentials or production integrations.

| Task | Input | Archived result |
| --- | --- | --- |
| Conduct a full audit and disclose limitations | [Task](audit-fixture/task.md), [deliberately defective mini application](audit-fixture/index.html) | [Audit report](audit-result.md) |
| Develop a concept before production approval | [Brief](concept-fixture/brief.md) | [Concept](concept-output/index.html), [review](concept-output/review.md), [contract](concept-output/design-contract.md), [verification record](concept-output/verification.md) |
| Review component semantics and preservation in an operations concept | [Task](interaction-fixture/task.md), [baseline](interaction-fixture/baseline.json), [candidate](interaction-fixture/proposal.html) | [Independent source-only review](interaction-review.md), [input snapshot](interaction-snapshot.json); no rendering or user test claimed |
| Review task completeness in a logistics concept | [Task](flow-fixture/task.md), [source fixture](flow-fixture/index.html) | [Independent source-only review](flow-review.md); no rendering or user test claimed |

For an independent repeat, provide only the relevant task, the skill and the inputs named by that task. Do not give the evaluating agent the archived result as a model answer. Save new results under `work/evaluation/` to preserve the development evaluation recorded here.

The audit fixture intentionally contains defects. It is neither a production starter nor a recommended component implementation. If needed, serve it locally from the repository root:

```sh
python3 -m http.server 8767 --bind 127.0.0.1 --directory evals/audit-fixture
```

The HTML files require no external resources. Record current browser/tool availability and the tests actually performed when repeating a task. The [quality overview](../docs/quality/evaluation.md) explains the limits of earlier results. Prompts and reports are published in English; translation does not turn historical observations into a new evaluation run.
