from dotenv import load_dotenv
import os
import json
import re
from google import genai
import time

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def extract_entities_and_relations(text_chunk: str):

    prompt = f"""
Extract entities and relationships from the following research text.

Return JSON in this format:

{{
  "entities": ["entity1","entity2"],
  "relationships": [["entity1","relation","entity2"]]
}}

TEXT:
{text_chunk}
"""

    max_retries = 3

    for attempt in range(max_retries):
        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            text = response.text

            json_text = re.search(r"\{.*\}", text, re.DOTALL).group()

            return json.loads(json_text)

        except Exception as e:

            print(f"Attempt {attempt+1} failed: {e}")

            if attempt < max_retries - 1:
                time.sleep(5)

    return {"entities": [], "relationships": []}