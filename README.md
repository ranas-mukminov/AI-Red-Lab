# AI-Red-Lab

A red-teaming lab for language models that you run yourself, locally.

Scope, stated plainly: the harness evaluates a **local stub model** and
any other model **you own and run locally**. It never calls a production
provider API, never uses provider API keys, and never tests a third-party
model or service. If a model is not yours and not local, it is out of scope.

## What it contains

- `lab/harness.py` — evaluation harness. It feeds test cases to a model
  interface, classifies the response, and writes a JSON report.
- `lab/stub_model.py` — a deterministic local stub. It answers from a
  small rule set so the harness can be run and tested without any real
  model, network, or key.
- `lab/guardrails.py` — simple guardrail checks: refusal detection,
  secret-pattern detection, and instruction-override detection.
- `cases/` — test-case catalogue in JSON: prompt injection, jailbreak
  attempts, and data-exfiltration attempts, each with an expected safe
  behaviour.
- `results/sample_stub_run.json` — output of a real run against the stub
  only. It is not a result against any production model.
- `tests/` — unit tests for the harness and the guardrails.

## How to run (local only)

```bash
python3 -m unittest discover -s tests -v
python3 lab/harness.py --cases cases/catalogue.json --model stub --out results/my_run.json
```

No network, no keys, no external model is needed for the stub run.

## What a result means

A stub run proves the harness works. It does not prove anything about a
production model, and it must never be presented as such. A result against
a real local model is meaningful only for that model, that version, and
that prompt set, and the report records exactly those three things.

## Safety

Test prompts in `cases/` are written for a local lab model. Do not send
them to production systems, do not use them to extract real data, and do
not use the harness to probe a service you do not own.
