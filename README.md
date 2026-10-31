> **Problem:** testing a language model for prompt injection and jailbreaks usually means sending prompts to a production API you do not control.
>
> **What this is:** an LLM red teaming lab that runs locally: a 15-case catalogue, an evaluation harness, guardrail checks and a local-model adapter. **Local stub and local models only — no production provider API, no keys, no third-party model.**
>
> **Who it is for:** people learning or evaluating LLM safety on models they own and run themselves.
>
> **Quickstart:**
>
> ```bash
> git clone https://github.com/ranas-mukminov/AI-Red-Lab.git
> cd AI-Red-Lab
> python3 -m unittest discover -s tests -v
> python3 lab/harness.py --cases cases/catalogue.json --model stub --out results/my_run.json
> ```
>
> **Sample result (verified run):** `cases=15 pass=15 fail=0 review=0` against the local stub. A stub run proves the harness works; it proves nothing about a production model.
>
[![CI](https://github.com/ranas-mukminov/AI-Red-Lab/actions/workflows/tests.yml/badge.svg)](https://github.com/ranas-mukminov/AI-Red-Lab/actions) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---
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

## Recent additions

- Case catalogue expanded from 6 to 15 cases, including jailbreak-framing cases that the stub now refuses.
- `lab/local_model.py`: adapter interface for a model the user runs locally (callable, or a localhost HTTP endpoint). No provider API, no keys, no external calls; non-local URLs are rejected.
- `docs/attack-mapping.md` and `detections/sigma-rules.yml`: illustrative MITRE ATLAS mapping and Sigma-style detection rules in lab log format.
