"""
Second Brain Agent - Main Entry Point
Orchestrates document scanning, style learning, and template generation.
"""

import os
from scanner import DocumentScanner
from brain import SecondBrain

def run_agent():
    print("=" * 50)
    print("🧠 SECOND BRAIN AGENT | V1.0 INITIALIZING...")
    print("=" * 50)

    # 1. Pārbaudām Dropzone mapi
    scanner = DocumentScanner(dropzone_path="./dropzone")
    documents = scanner.scan_documents()

    if not documents:
        print("\n⚠️  Dropzone mapē nav atrasti dokumenti (.txt vai .md).")
        print("💡 Ievieto dažus iepriekšējos piedāvājumus vai piezīmes './dropzone' mapē, lai aģents iemācītos Tavu stilu!")
        return

    print(f"\n✅ Atrasti {len(documents)} parauga dokumenti. Sākam stila analīzi...")
    
    # 2. Sagatavojam tekstus LLM analīzei
    doc_texts = [doc["content"] for doc in documents]

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("\n⚠️  Nav atrasta GEMINI_API_KEY vides mainīgā vērtība.")
        print("Iestati API atslēgu, lai palaistu inteliģento moduli.")
        return

    brain = SecondBrain(api_key=api_key)
    
    print("\n🔍 Sintezējam Tavu unikālo Stila Profilu (Style DNA)...")
    style_profile = brain.extract_style_profile(doc_texts)
    
    print("\n" + "=" * 50)
    print("📊 TAVS STILA PROFILS:")
    print("=" * 50)
    print(style_profile)
    print("=" * 50)

    # 3. Pārbaudes ģenerēšana
    task = input("\n✍️  Ievadi jaunu uzdevumu (piem., 'Piedāvājums jaunam B2B klientam par servisa apkalpošanu'): ")
    if task.strip():
        print("\n⚡ Ģenerējam jaunu karkasu Tavā personīgajā stilā...")
        draft = brain.generate_draft(task_description=task, style_profile=style_profile)
        print("\n" + "=" * 50)
        print("📑 ĢENERĒTAIS DOKUMENTS:")
        print("=" * 50)
        print(draft)

if __name__ == "__main__":
    run_agent()
