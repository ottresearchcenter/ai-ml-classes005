from typing import Protocol


class RetrievalStrategy(Protocol):
    def retrieve(self, query: str) -> list[str]:
        ...


class KeywordRetrieval:
    def retrieve(self, query: str) -> list[str]:
        return [
            f"Keyword match document for query: {query}",
            "Exact policy clause match"
        ]


class VectorRetrieval:
    def retrieve(self, query: str) -> list[str]:
        return [
            f"Semantic match document for query: {query}",
            "Similar meaning document chunk"
        ]


class HybridRetrieval:
    def __init__(
        self,
        keyword_retrieval: RetrievalStrategy,
        vector_retrieval: RetrievalStrategy,
    ):
        self.keyword_retrieval = keyword_retrieval
        self.vector_retrieval = vector_retrieval

    def retrieve(self, query: str) -> list[str]:
        keyword_results = self.keyword_retrieval.retrieve(query)
        vector_results = self.vector_retrieval.retrieve(query)

        return keyword_results + vector_results


class RAGService:
    def __init__(self, retrieval_strategy: RetrievalStrategy):
        self.retrieval_strategy = retrieval_strategy

    def answer(self, question: str) -> str:
        docs = self.retrieval_strategy.retrieve(question)
        return f"Generated answer using context: {docs}"



obj1 = RAGService(KeywordRetrieval())
print(obj1.answer("What is RAG?"))



"""
retrieval_strategy = HybridRetrieval(
    keyword_retrieval=KeywordRetrieval(),
    vector_retrieval=VectorRetrieval(),
)

rag_service = RAGService(retrieval_strategy)

print(rag_service.answer("What are the policy exclusions?"))"""