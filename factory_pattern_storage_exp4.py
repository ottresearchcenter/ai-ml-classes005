from typing import Protocol


class StorageClient(Protocol):
    def upload(self, path: str, content: bytes) -> str:
        ...


class LocalStorageClient:
    def upload(self, path: str, content: bytes) -> str:
        return f"Saved locally at {path}"


class S3StorageClient:
    def upload(self, path: str, content: bytes) -> str:
        return f"Uploaded to S3 at {path}"


class GCSStorageClient:
    def upload(self, path: str, content: bytes) -> str:
        return f"Uploaded to GCS at {path}"


class StorageClientFactory:
    @staticmethod
    def create(provider: str) -> StorageClient:
        if provider == "local":
            return LocalStorageClient()

        if provider == "s3":
            return S3StorageClient()

        if provider == "gcs":
            return GCSStorageClient()

        raise ValueError(f"Unsupported storage provider: {provider}")


storage = StorageClientFactory.create("s3")
print(storage.upload("models/fraud_model.pkl", b"model-binary-content"))