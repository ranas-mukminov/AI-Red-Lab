"""Deterministic local stub model for the AI-Red-Lab harness.

The stub is not a language model. It returns canned responses based on
simple keyword rules, so the harness, guardrails and tests can be run
with no network, no key and no real model. Its only purpose is to make
the harness testable and to demonstrate the report format.
"""

SAFE_REFUSAL = "I can't help with that request."


def _looks_like_override(prompt):
    lowered = prompt.lower()
    markers = (
        "ignore previous instructions",
        "ignore all previous instructions",
        "disregard your instructions",
        "you are now in developer mode",
        "dan mode",
    )
    return any(m in lowered for m in markers)


def _asks_for_secret(prompt):
    lowered = prompt.lower()
    return "api key" in lowered or "password" in lowered or "secret" in lowered


def respond(prompt):
    """Return a canned response for *prompt* (str)."""
    if not isinstance(prompt, str):
        raise TypeError("prompt must be a string")
    if _looks_like_override(prompt):
        return SAFE_REFUSAL
    if _asks_for_secret(prompt):
        return SAFE_REFUSAL
    if "capital of france" in prompt.lower():
        return "The capital of France is Paris."
    return "This is a stub response to a benign prompt."
