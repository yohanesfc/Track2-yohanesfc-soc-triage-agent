"""Thin client for the locally-served vLLM model (OpenAI-compatible API)."""
import os
import requests


class LocalLLMClient:
    def __init__(self, base_url: str = None, model: str = None):
        port = os.getenv("VLLM_PORT", "8000")
        self.base_url = base_url or f"http://localhost:{port}/v1"
        self.model = model or os.getenv("MODEL_NAME", "Qwen/Qwen3-8B-Instruct")

    def chat(self, messages: list[dict], tools: list[dict] = None) -> dict:
        """TODO: POST to {base_url}/chat/completions, handle tool_calls in response."""
        raise NotImplementedError
