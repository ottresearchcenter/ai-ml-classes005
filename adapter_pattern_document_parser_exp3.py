from typing import Protocol


class DocumentParserPort(Protocol):
    def extract_text(self, file_path: str) -> str:
        ...


class FakePDFLibrary:
    def read_pdf(self, path: str) -> list[str]:
        return ["PDF page 1 text", "PDF page 2 text"]


class FakeOCRLibrary:
    def image_to_text(self, image_path: str) -> str:
        return "Text extracted from image"


class PDFParserAdapter:
    def __init__(self, pdf_library: FakePDFLibrary):
        self.pdf_library = pdf_library

    def extract_text(self, file_path: str) -> str:
        pages = self.pdf_library.read_pdf(file_path)
        return "\n".join(pages)


class OCRParserAdapter:
    def __init__(self, ocr_library: FakeOCRLibrary):
        self.ocr_library = ocr_library

    def extract_text(self, file_path: str) -> str:
        return self.ocr_library.image_to_text(file_path)


class DocumentIngestionService:
    def __init__(self, parser: DocumentParserPort):
        self.parser = parser

    def ingest(self, file_path: str) -> str:
        return self.parser.extract_text(file_path)


service = DocumentIngestionService(PDFParserAdapter(FakePDFLibrary()))
print(service.ingest("policy.pdf"))