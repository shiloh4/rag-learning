from sentence_transformers import SentenceTransformer
from app.types.types import Chunk
import json
import pathlib

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def load_chunks(input_dir: str) -> list[Chunk]:
    with open(input_dir, "r") as file:
        return [Chunk(**obj) for obj in json.load(file)]

def embed(text: str) -> list[float]:
    return model.encode(text)

def embed_chunks(chunks: list[Chunk]) -> list[list[float]]:
    return [embed(chunk.text) for chunk in chunks]

def save_embeddings(embeddings: list[list[float]], output_dir: str):
    #clear file
    with open(output_dir, "w") as file:
        file.write("[\n")

        for i, embedding in enumerate(embeddings):
            if i:
                file.write(",\n")
            json.dump(list(embedding), file, indent=4)

        file.write("\n]")

def __main__(input_dir: str, output_dir: str):
    chunks = load_chunks(input_dir)
    embeddings = embed_chunks(chunks)
    # print(embeddings.shape)
    save_embeddings(embeddings, output_dir)

if __name__ == "__main__":
    __main__("extracted_docs/CS3510/L1.json", "extracted_docs/CS3510/L1_embeddings.json")