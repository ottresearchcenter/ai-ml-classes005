from typing import Protocol


class VectorStore(Protocol):
    def search(self, query_embedding: list[float], top_k: int) -> list[str]:
        ...


class PineconeVectorStore:
    def search(self, query_embedding: list[float], top_k: int) -> list[str]:
        return ["Pinecone result 1", "Pinecone result 2"]


class ChromaVectorStore:
    def search(self, query_embedding: list[float], top_k: int) -> list[str]:
        return ["Chroma result 1", "Chroma result 2"]


class FAISSVectorStore:
    def search(self, query_embedding: list[float], top_k: int) -> list[str]:
        return ["FAISS result 1", "FAISS result 2"]

class MongodbStore:
    def search(self, query_embedding: list[float], top_k: int) -> list[str]:
        return ["MongoDB result 1", "MongoDB result 2"]

class VectorStoreFactory:
    @staticmethod
    def create(store_type: str) -> VectorStore:
        if store_type == "pinecone":
            return PineconeVectorStore()

        if store_type == "chroma":
            return ChromaVectorStore()

        if store_type == "faiss":
            return FAISSVectorStore()
        
        if store_type == "mongodb":
            # Assuming MongodbStore is defined elsewhere
            return MongodbStore()

        raise ValueError(f"Unsupported vector store: {store_type}")


vector_store = VectorStoreFactory.create("chroma")
print(vector_store.search([0.1, 0.2, 0.3], top_k=2))