from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class PromptRequest:
    user_id: str
    prompt: str


class Guardrail(ABC):
    def __init__(self):
        self.next_guardrail = None

    def set_next(self, guardrail: "Guardrail") -> "Guardrail":
        self.next_guardrail = guardrail
        return guardrail

    def handle(self, request: PromptRequest) -> None:
        self.check(request)

        if self.next_guardrail:
            self.next_guardrail.handle(request)

    @abstractmethod
    def check(self, request: PromptRequest) -> None:
        pass


class AuthenticationGuardrail(Guardrail):
    def check(self, request: PromptRequest) -> None:
        if not request.user_id:
            raise PermissionError("Authentication required")


class PromptInjectionGuardrail(Guardrail):
    def check(self, request: PromptRequest) -> None:
        if "ignore previous instructions" in request.prompt.lower():
            raise ValueError("Possible prompt injection detected")


class PIIGuardrail(Guardrail):
    def check(self, request: PromptRequest) -> None:
        if "aadhaar" in request.prompt.lower():
            raise ValueError("Sensitive information detected")


auth = AuthenticationGuardrail()
injection = PromptInjectionGuardrail()
pii = PIIGuardrail()

auth.set_next(injection).set_next(pii)

request = PromptRequest("U101", "Explain RAG architecture")
auth.handle(request)

request1 = PromptRequest("U102", "Explain aadhaar architecture")
auth.handle(request1)

print("All guardrails passed")