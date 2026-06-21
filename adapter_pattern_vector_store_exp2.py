from typing import Protocol


class VectorStorePort(Protocol):
    def search(self, embedding: list[float], top_k: int) -> list[str]:
        ...


class FakePineconeSDK:
    def query(self, vector: list[float], top_k: int) -> dict:
        return {"matches": [{"text": "Pinecone document chunk"}]}


class FakeChromaSDK:
    def similarity_search_by_vector(self, vector: list[float], k: int) -> list[str]:
        return ["Chroma document chunk"]


class PineconeAdapter:
    def __init__(self, sdk: FakePineconeSDK):
        self.sdk = sdk

    def search(self, embedding: list[float], top_k: int) -> list[str]:
        response = self.sdk.query(vector=embedding, top_k=top_k)
        return [item["text"] for item in response["matches"]]


class ChromaAdapter:
    def __init__(self, sdk: FakeChromaSDK):
        self.sdk = sdk

    def search(self, embedding: list[float], top_k: int) -> list[str]:
        return self.sdk.similarity_search_by_vector(vector=embedding, k=top_k)


class Retriever:
    def __init__(self, vector_store: VectorStorePort):
        self.vector_store = vector_store

    def retrieve(self, query_embedding: list[float]) -> list[str]:
        return self.vector_store.search(query_embedding, top_k=3)


retriever = Retriever(PineconeAdapter(FakePineconeSDK()))
print(retriever.retrieve([0.1, 0.2, 0.3]))