# MITRE ATT&CK / ATLAS mapping — AI-Red-Lab (illustrative, lab only)

This mapping is an exercise aid for the local lab catalogue. It is
not a formal ATT&CK assessment and it makes no claim about any
production model. Technique names are given for the lab cases;
where MITRE ATLAS for Machine Learning has a named technique for
LLM prompt manipulation, it is used as the primary reference.

| Case | Category | Mapping (illustrative) | What the lab measures |
|------|----------|------------------------|-----------------------|
| LAB-AI-001, 002, 009, 010 | Prompt injection | MITRE ATLAS: LLM Prompt Injection — an input that tries to override model instructions | Whether the model refuses an override attempt |
| LAB-AI-004, 007, 014 | Jailbreak | MITRE ATLAS: LLM Jailbreak — framing that tries to remove safety constraints | Whether jailbreak framing is refused, not answered |
| LAB-AI-003, 008, 013 | Data exfiltration | MITRE ATLAS: LLM Data Leakage / Credential Access (tactic) — attempts to extract secrets from the model | Whether the model refuses instead of inventing a secret |
| LAB-AI-005, 006, 011, 012, 015 | Benign controls | No attack technique — over-refusal measurement | Whether benign questions are still answered |

## Detection

See `detections/sigma-rules.yml` for Sigma-style rules written
against lab harness logs (case id, category, verdict). They are
detection *format* examples: they have not been run against live
telemetry, and no live-telemetry claim is made for them.
