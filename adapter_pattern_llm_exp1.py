from typing import Protocol


class LLMPort(Protocol):
    def complete(self, prompt: str) -> str:
        ...


class FakeOpenAISDK:
    def chat_completion(self, messages: list[dict]) -> dict:
        return {"content": f"OpenAI answer: {messages[-1]['content']}"}
    
    def chat_completion_with_options(self, messages: list[dict], temperature: float, max_tokens: int) -> dict:
        return {"content": f"OpenAI answer with options: {messages[-1]['content']}, temp: {temperature}, max_tokens: {max_tokens}"}


class FakeVertexSDK:
    def generate_content(self, prompt: str) -> str:
        return f"Vertex answer: {prompt}"


class OpenAIAdapter:
    def __init__(self, sdk: FakeOpenAISDK):
        self.sdk = sdk

    def complete(self, prompt: str) -> str:
        response = self.sdk.chat_completion(
            messages=[{"role": "user", "content": prompt}]
        )

        response_with_options = self.sdk.chat_completion_with_options(
            messages=[{"role": "user", "content": prompt}], 
            temperature=0.7,
            max_tokens=150
        )
        return response_with_options["content"]


class VertexAIAdapter:
    def __init__(self, sdk: FakeVertexSDK):
        self.sdk = sdk

    def complete(self, prompt: str) -> str:
        return self.sdk.generate_content(prompt)


class AIService:
    def __init__(self, llm: LLMPort):
        self.llm = llm

    def ask(self, question: str) -> str:
        return self.llm.complete(question)


service = AIService(OpenAIAdapter(FakeOpenAISDK()))
print(service.ask("What is adapter pattern?"))

obj2 = AIService(VertexAIAdapter(FakeVertexSDK()))
print(obj2.ask("What is vertex AI?"))