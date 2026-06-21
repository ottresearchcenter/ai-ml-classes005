from typing import Protocol

class SearchClient(Protocol):
    def search(self, query: str) -> list[str]:
        ...


class PostgresSearchClient:
    def search(self, query: str) -> list[str]:
        return [f"Postgres result for: {query}"]
    
class MysqlSearchClient:
    def search(self, query: str) -> list[str]:
        return [f"MySQL result for: {query}"]
    
class MongodbSearchClient:
    def search(self, query: str) -> list[str]:
        return [f"MongoDB result for: {query}"]
    

class SearchClientFactory:
    @staticmethod
    def create(provider: str) -> SearchClient:
        provider = provider.lower()

        if provider == "postgres":
            return PostgresSearchClient()

        if provider == "mysql":
            return MysqlSearchClient()

        if provider == "mongodb":
            return MongodbSearchClient()

        raise ValueError(f"Unsupported search provider: {provider}")

obj1 = SearchClientFactory.create("postgres")
obj1.search("SELECT * FROM users")


class A:

    def __init__(self, search_client: SearchClient):
        self.search_client = search_client

    def perform_search(self, query: str) -> list[str]:
        return self.search_client.search(query)
    
    class _B:
        def b_method(self):
            return "Method from class B"
    
    def create_object():
        ojb_b = A.B()
        return ojb_b


obj = A(SearchClientFactory.create("mysql"))
obj.perform_search("SELECT * FROM products")

obj_b = A.B()
