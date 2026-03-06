import re

def clean_text(text: str) -> str:

    text = re.sub(r"\s+", " ", text)

    text = re.sub(r"\[\d+\]", "", text)

    text = re.sub(r"\(.*?\)", "", text)

    text = re.sub(r" +", " ", text)

    return text.strip()

def chunk_text(text: str, chunk_size: int = 800, overlap: int = 100):

    chunks = []

    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks