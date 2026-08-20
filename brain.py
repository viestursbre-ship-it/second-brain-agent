"""
Second Brain Agent - Intelligence & Style Synthesizer
Uses LLM to analyze ingested documents, extract structural DNA, and generate customized templates.
"""

import os
from google import genai
from google.genai import types

class SecondBrain:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY is not set.")
        self.client = genai.Client(api_key=self.api_key)

    def extract_style_profile(self, document_texts: list[str]) -> str:
        """Analyzes past documents to create a persistent Tone of Voice and formatting profile."""
        combined_text = "\n\n--- DOKUMENTS ---\n\n".join(document_texts)
        
        prompt = f"""
        Tu esi inteliģents darba asistents. Izanalizē šos lietotāja iepriekš veidotos dokumentus:
        
        {combined_text}
        
        Izveido īsu, precīzu un strukturētu Lietotāja Stila Profilu (Style DNA):
        1. Tipiskais tonis un uzrunas veids (Tone of Voice).
        2. Galvenās struktūras sadaļas, ko lietotājs vienmēr iekļauj piedāvājumos/dokumentos.
        3. Biežāk lietotās frāzes, nobeigumi un noformējuma paradumi.
        """

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(temperature=0.2),
        )
        return response.text

    def generate_draft(self, task_description: str, style_profile: str) -> str:
        """Generates a new document/proposal matching the user's specific historical style."""
        prompt = f"""
        Pamatojoties uz šo lietotāja stila profilu:
        {style_profile}
        
        Sagatavo jaunu dokumenta melnrakstu/karkasu šādam uzdevumam:
        "{task_description}"
        
        Ieturi precīzi tādu pašu struktūru, nodaļu secību un valodas toni.
        """

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(temperature=0.4),
        )
        return response.text

if __name__ == "__main__":
    print("🧠 [Second Brain Agent] Brain module ready for deployment.")
