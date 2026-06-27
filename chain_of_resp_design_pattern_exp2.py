"""Example 2: Document Preprocessing Pipeline
Use Case

Before sending a document to a RAG system, process it through:

file validation
text extraction
text cleaning
chunking """

from abc import ABC


class DocumentHandler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, document):
        if self.next_handler:
            return self.next_handler.handle(document)

        return document


class FileValidationHandler(DocumentHandler):
    def handle(self, document):
        if not document["file_name"].endswith(".pdf"):
            raise ValueError("Only PDF files are supported")

        print("File validation completed")
        return super().handle(document)


class TextExtractionHandler(DocumentHandler):
    def handle(self, document):
        document["text"] = "Extracted text from PDF document"
        print("Text extraction completed")
        return super().handle(document)


class TextCleaningHandler(DocumentHandler):
    def handle(self, document):
        document["text"] = document["text"].lower().strip()
        print("Text cleaning completed")
        return super().handle(document)


class ChunkingHandler(DocumentHandler):
    def handle(self, document):
        document["chunks"] = document["text"].split()
        print("Chunking completed")
        return super().handle(document)


validator = FileValidationHandler()
extractor = TextExtractionHandler()
cleaner = TextCleaningHandler()
chunker = ChunkingHandler()

validator.set_next(extractor).set_next(cleaner).set_next(chunker)

document = {
    "file_name": "insurance_policy.pdf"
}

#result = validator.handle(document)
result = extractor.handle(document)
print(result)