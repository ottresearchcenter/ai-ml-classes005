from typing import Protocol


class EmbeddingModel(Protocol):
    def embed(self, text: str) -> list[float]:
        ...


class OpenAIEmbeddingModel:
    def embed(self, text: str) -> list[float]:
        return [0.1, 0.2, 0.3]


class VertexEmbeddingModel:
    def embed(self, text: str) -> list[float]:
        return [0.4, 0.5, 0.6]


class SentenceTransformerModel:
    def embed(self, text: str) -> list[float]:
        return [0.7, 0.8, 0.9]


class EmbeddingModelFactory:
    @staticmethod
    def create(model_type: str) -> EmbeddingModel:
        if model_type == "openai":
            return OpenAIEmbeddingModel()

        if model_type == "vertex":
            return VertexEmbeddingModel()

        if model_type == "sentence-transformer":
            return SentenceTransformerModel()

        raise ValueError(f"Unsupported embedding model: {model_type}")


embedding_model = EmbeddingModelFactory.create("sentence-transformer")
print(embedding_model.embed("Insurance policy exclusions"))