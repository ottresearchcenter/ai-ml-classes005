"""
In a typical application, you might have code that directly instantiates different LLM clients based on some configuration or user input. For example:
if provider == "openai":
    client = OpenAIClient()
elif provider == "vertex":
    client = VertexAIClient()
elif provider == "claude":
    client = ClaudeClient()

We centralize creation logic inside a factory.

"""


from typing import Protocol


class LLMClient(Protocol):
    def generate(self, prompt: str) -> str:
        ...


class OpenAIClient:
    def generate(self, prompt: str) -> str:
        return f"OpenAI response for: {prompt}"


class VertexAIClient:
    def generate(self, prompt: str) -> str:
        return f"Vertex AI response for: {prompt}"


class ClaudeClient:
    def generate(self, prompt: str) -> str:
        return f"Claude response for: {prompt}"


class LocalLlamaClient:
    def generate(self, prompt: str) -> str:
        return f"Local Llama response for: {prompt}"


class LLMClientFactory:
    @staticmethod
    def create(provider: str) -> LLMClient:
        provider = provider.lower()

        if provider == "openai":
            return OpenAIClient()

        if provider == "vertex":
            return VertexAIClient()

        if provider == "claude":
            return ClaudeClient()

        if provider == "llama":
            return LocalLlamaClient()

        raise ValueError(f"Unsupported LLM provider: {provider}")


class AIService:
    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client

    def answer(self, question: str) -> str:
        return self.llm_client.generate(question)

import json
with open("C:\\KripaDev\\AIML_Batch_005\\design-patterns\\config.json") as f:
    config = json.load(f)

client = LLMClientFactory.create(config["provider"])
service = AIService(client)

print(service.answer("Explain RAG"))

'''class LLMIntegration:

    def __init__(self, provider: str):
        self.config = {'url': 'https://api.llm.com', 'api_key': 'secret_key', 'timeout': 30, 'headers': {'Content-Type': 'application/json'}  }

    def request_to_llm(self, prompt: str) -> str:
        return self.llm_client.generate(prompt)'''