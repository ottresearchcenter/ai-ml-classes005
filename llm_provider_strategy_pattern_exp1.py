from typing import Protocol


class LLMStrategy(Protocol):
    def generate(self, prompt: str) -> str:
        ...


class OpenAIStrategy:
    def generate(self, prompt: str) -> str:
        return f"OpenAI response for: {prompt}"


class VertexAIStrategy:
    def generate(self, prompt: str) -> str:
        return f"Vertex AI response for: {prompt}"


class ClaudeStrategy:
    def generate(self, prompt: str) -> str:
        return f"Claude response for: {prompt}"


class LocalLlamaStrategy:
    def generate(self, prompt: str) -> str:
        return f"Local Llama response for: {prompt}"


class HuggingFaceStrategy:
    def generate(self, prompt: str) -> str:
        return f"Hugging Face response for: {prompt}"


class LLMService:
    def __init__(self, strategy: LLMStrategy):
        self.strategy = strategy

    def ask(self, question: str) -> str:
        prompt = f"Answer the following question:\n{question}"
        return self.strategy.generate(prompt)


obj1 = LLMService(OpenAIStrategy())
print(obj1.ask("What is Python?"))

obj2 = LLMService(HuggingFaceStrategy())
print(obj2.ask("What is Hugging Face?"))

#service = LLMService(OpenAIStrategy())
#print(service.ask("What is RAG?"))

#service = LLMService(VertexAIStrategy())
#print(service.ask("Explain transformers."))