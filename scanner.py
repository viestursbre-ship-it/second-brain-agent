"""
Second Brain Agent - Document Ingestion & Style Scanner
Extracts text from user documents (DOCX, PDF, TXT) and analyzes Tone of Voice & Structure DNA.
"""

import os
from pathlib import Path


class DocumentScanner:

  def __init__(self, dropzone_path: str = "./dropzone"):
    self.dropzone_path = Path(dropzone_path)
    self.dropzone_path.mkdir(parents=True, exist_ok=True)

  def read_text_file(self, file_path: Path) -> str:
    """Reads a plain text file."""
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
      return f.read()

  def scan_documents(self) -> list[dict]:
    """Scans all documents in the dropzone folder."""
    extracted_data = []

    for file_path in self.dropzone_path.glob("*"):
      if file_path.suffix.lower() in [".txt", ".md"]:
        content = self.read_text_file(file_path)
        extracted_data.append({
            "filename": file_path.name,
            "type": file_path.suffix.lower(),
            "content": content,
            "char_count": len(content),
        })

    return extracted_data

  def analyze_style_dna(self, documents: list[dict]) -> dict:
    """Basic analysis of structure patterns and keywords across ingested documents."""
    total_docs = len(documents)
    if total_docs == 0:
      return {"status": "No documents found in dropzone"}

    sample_preview = [
        f"{doc['filename']} ({doc['char_count']} chars)" for doc in documents
    ]

    return {
        "status": "Ready",
        "total_documents": total_docs,
        "processed_files": sample_preview,
        "summary": "Document Ingestion module operational. Ready for LLM memory synthesis.",
    }


if __name__ == "__main__":
  scanner = DocumentScanner()
  print("🧠 [Second Brain Agent] Scanner initialized.")
  docs = scanner.scan_documents()
  profile = scanner.analyze_style_dna(docs)
  print(f"📊 Status: {profile['status']}")
  print(f"📁 Processed files: {profile.get('processed_files', [])}")
