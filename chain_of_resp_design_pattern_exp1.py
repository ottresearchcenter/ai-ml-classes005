from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        print(f"Handler {self.__class__.__name__} set next to {handler.__class__.__name__}")
        return handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)

        return "Request processed successfully"


class AuthHandler(Handler):
    def handle(self, request):
        if not request.get("token"):
            return "Rejected: Missing auth token"

        print("Auth check passed")
        return super().handle(request)


class RequiredFieldHandler(Handler):
    def handle(self, request):
        if not request.get("user_id"):
            return "Rejected: Missing user_id"

        print("Required field check passed")
        return super().handle(request)


class PermissionHandler(Handler):
    def handle(self, request):
        if request.get("role") != "admin":
            return "Rejected: User does not have permission"

        print("Permission check passed")
        return super().handle(request)

class SaveDataHandler(Handler):
    def handle(self, request):
        # Simulate saving data to a database
        print(f"Data saved for user_id: {request.get('user_id')}")
        return super().handle(request)


auth = AuthHandler()
fields = RequiredFieldHandler()
permission = PermissionHandler()
save_data = SaveDataHandler()

#auth.set_next(fields).set_next(permission).set_next(save_data)
auth.set_next(fields).set_next(save_data)

request = {
    "token": "valid-token",
    "user_id": "U101",
    "role": "admin"
}

print(auth.handle(request))