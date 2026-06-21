print("this is my chat app")
import factory_pattern_llm_client_exp1 

class ChatApp:
    def __init__(self):
        self.messages = []

    def send_message(self, message: str):
        self.messages.append(message)
        print(f"Sent: {message}")
        requestObj = factory_pattern_llm_client_exp1.LLMClientFactory.create("openai")
        llm_service = factory_pattern_llm_client_exp1.AIService(requestObj)
        self.response = llm_service.answer(message)

    def receive_message(self, message: str):
        self.messages.append(message)
        print(f"Received: {message}")
        if self.response:
            return self.response

