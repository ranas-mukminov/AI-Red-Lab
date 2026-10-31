"""Local-model adapter interface for AI-Red-Lab.

Only models the user owns and runs locally are in scope:

- a Python callable (``from_callable``), or
- an HTTP endpoint on localhost / 127.0.0.1 (``LocalHTTPModel``).

There is no provider backend, no provider API key handling, and no
call to any external or third-party model. A non-local URL is
rejected before any request is made. The harness still defaults to
the deterministic stub; using a local model is opt-in and requires
the user to run that model themselves.
"""

import json
import urllib.request
from urllib.parse import urlparse


class LocalModelAdapter:
    """Wraps a callable ``fn(prompt) -> str`` as a model interface."""

    def __init__(self, respond_fn):
        if not callable(respond_fn):
            raise TypeError("respond_fn must be callable")
        self._fn = respond_fn

    def respond(self, prompt):
        if not isinstance(prompt, str):
            raise TypeError("prompt must be a string")
        out = self._fn(prompt)
        if not isinstance(out, str):
            raise TypeError("model response must be a string")
        return out


class LocalHTTPModel:
    """POSTs prompts to a local HTTP endpoint and returns its text.

    The endpoint must be on localhost or 127.0.0.1. It is expected
    to accept ``{"prompt": ...}`` and return JSON with a ``response``
    or ``text`` string field. No credentials or API keys are sent.
    """

    def __init__(self, url, timeout=30):
        parsed = urlparse(url)
        if parsed.scheme != "http":
            raise ValueError("local model URL must use http")
        if parsed.hostname not in ("localhost", "127.0.0.1", "::1"):
            raise ValueError("local model URL must be localhost only")
        self.url = url
        self.timeout = timeout

    def respond(self, prompt):
        if not isinstance(prompt, str):
            raise TypeError("prompt must be a string")
        body = json.dumps({"prompt": prompt}).encode()
        req = urllib.request.Request(
            self.url, data=body,
            headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=self.timeout) as resp:
            data = json.loads(resp.read().decode())
        text = data.get("response", data.get("text"))
        if not isinstance(text, str):
            raise ValueError("local model response had no text field")
        return text


def from_callable(fn):
    return LocalModelAdapter(fn)


def from_stub():
    from stub_model import respond
    return LocalModelAdapter(respond)
