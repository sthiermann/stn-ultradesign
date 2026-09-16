# Messaging and conversation workspaces

Read when the product already includes messaging, conversation panels, support threads or a requested collaboration workflow. Map existing capabilities with [feature-parity.md](feature-parity.md) before redesigning them. These are reasoning and verification prompts, not a requirement to add a consumer messenger to every business application. Use synthetic participants and messages; an audit or concept does not authorize sending real messages.

## Understand the communication model

Establish who communicates with whom, for what work, and within which permissions. Distinguish a direct conversation, group, support case, object-linked discussion, announcement and activity log. Preserve the product's actual participant, membership, retention and search rules. Do not invent read receipts, typing indicators, end-to-end encryption, moderation or deletion promises from familiar visual patterns.

Inventory separately where present: show/hide the messenger, conversation list, search, unread filtering, new conversation, participant selection, group creation, conversation opening, history, composing, replying, sending, attachments, retry, editing/deleting, notifications and conversation settings. A working chat list does not establish a complete messenger. Map per-message actions and keyboard shortcuts as well as page-level controls.

## Give each region a clear job

On wide layouts, consider a persistent conversation list and adjacent thread when frequent switching needs both. In an operational application, a docked conversation can preserve the main workspace; its width and opening behavior must leave the primary task usable. On narrow layouts, a list → thread sequence often makes context clearer than compressing both. Choose from actual work, not visual resemblance to a reference.

Keep participant identity, conversation purpose and relevant scope visible. Distinguish direct messages from a similarly named group. Make the selected conversation, unread state, draft and failed delivery distinguishable without relying on color alone. Dates, timestamps and message grouping should explain sequence without adding repetitive labels to every message.

Define the relationship to other panels: can a person keep a chart inspector and conversation open together, does switching the main object change the thread, and is the conversation global or object-scoped? Do not replace independent panel state with one mutually exclusive menu by accident. Preserve a visible return path and relevant workspace selection.

## Compose and deliver without losing work

Keep the composer anchored to the correct conversation and its participants. Specify multiline entry, send-key behavior, explicit send, attachment selection and cancellation according to the product's existing behavior or an agreed change. Do not submit during input-method composition. Avoid surprising send behavior when keyboard or platform conventions differ.

Model draft, queued/sending, delivered, failed and retried states only as supported by the actual transport. A local optimistic message is not proof of delivery; receipt and read are different facts. Identify which message failed and offer the actual recovery action while preserving its text and attachments. Prevent duplicate sends according to the real retry contract.

Preserve drafts at their correct scope when switching conversations, closing the dock or resizing. Make any intentional clearing or expiry understandable. For reply context, keep the referenced message identifiable and define behavior when it is removed or unavailable. Never silently redirect a pending message to a newly selected conversation.

## Keep attention and reading under user control

Differentiate a new message in the active thread from activity in another thread. Preserve reading position when the person is reviewing older messages; provide a clear route to newer content instead of repeatedly jumping to the bottom. Loading earlier history should retain the visible anchor. Define unread transitions and notification dismissal from actual product semantics; opening a panel need not imply reading every message.

Notifications need a useful destination, appropriate preview privacy and user control where supported. A hidden messenger should not erase unread state or stop a required service by accident. Avoid announcing the entire transcript for every incoming message; preserve focus and use concise, proportionate accessible updates.

## Review the complete supported journey

Use safe fixtures to inspect:

- Open the messenger from the main task, choose a conversation and return with the original work intact.
- Start a permitted conversation, identify the recipient unambiguously, compose, send and observe the supported result.
- Switch threads with an unsent draft; close and reopen the panel; resize during composition.
- Read older history while new content arrives; retrieve the latest messages without losing the thread.
- Recover a failed send or unavailable attachment without losing content or duplicating delivery.
- Exercise relevant keyboard, touch, long-message, empty-list, offline and denied-participant states.
- Keep supported inspectors or overlays usable alongside the messenger; check actual content width, focus and layering.

Each listed capability remains conditional on the real product. Record gaps and proposed additions separately. A production-like conversation in a prototype is still synthetic; disclose that in the external review context while keeping in-product copy realistic.
