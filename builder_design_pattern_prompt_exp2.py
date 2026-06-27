from dataclasses import dataclass, field


@dataclass(frozen=True)
class Prompt:
    system_instruction: str
    context: str
    examples: list[str]
    question: str
    output_format: str


class PromptBuilder:
    def __init__(self):
        self._system_instruction = ""
        self._context = ""
        self._examples = []
        self._question = ""
        self._output_format = "text"

    def with_system_instruction(self, value: str) -> "PromptBuilder":
        self._system_instruction = value
        return self

    def with_context(self, value: str) -> "PromptBuilder":
        self._context = value
        return self

    def with_example(self, value: str) -> "PromptBuilder":
        self._examples.append(value)
        return self

    def with_question(self, value: str) -> "PromptBuilder":
        self._question = value
        return self

    def with_output_format(self, value: str) -> "PromptBuilder":
        self._output_format = value
        return self

    def build(self) -> Prompt:
        if not self._system_instruction or not self._question:
            raise ValueError("System instruction and question are required")

        return Prompt(
            system_instruction=self._system_instruction,
            context=self._context,
            examples=self._examples.copy(),
            question=self._question,
            output_format=self._output_format,
        )


prompt = (
    PromptBuilder()
    .with_system_instruction("You are a healthcare policy analyst.")
    .with_context("The policy covers emergency hospitalization.")
    .with_example("Input: Dental claim; Output: Not covered")
    .with_question("Is emergency surgery covered?")
    .with_output_format("JSON")
    .build()
)

print(prompt)
print(prompt.system_instruction)

