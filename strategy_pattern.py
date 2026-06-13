"""
If you have code like this:

if provider == "openai":
    call_openai()
elif provider == "vertex":
    call_vertex()
elif provider == "claude":
    call_claude()

This becomes hard to maintain when new providers are added.
"""


from typing import Protocol


class Strategy(Protocol):
    def execute(self, data: dict) -> dict:
        ...


class ConcreteStrategyA:
    def execute(self, data: dict) -> dict:
        return {"result": "Handled by strategy A"}


class ConcreteStrategyB:
    def execute(self, data: dict) -> dict:
        return {"result": "Handled by strategy B"}

class ConcreteStrategyC:
    def execute(self, data: dict) -> dict:
        return {"result": "Handled by strategy C"}

class BusinessService:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def process(self, data: dict) -> dict:
        return self.strategy.execute(data)


service = BusinessService(ConcreteStrategyA())
print(service.process({"input": "test"}))


service = BusinessService(ConcreteStrategyB())
print(service.process({"input": "test"}))
