import chromadb
import json
import pathlib
from app.types.types import Chunk

chroma_client = chromadb.PersistentClient(path="chroma_db")

def create_collection(name: str) -> chromadb.Collection:
    return chroma_client.create_collection(name=name)

def add_to_collection(input_dir: str, collection: chromadb.Collection) -> list[str]:
    with open(input_dir, "r") as file:
        chunks = [Chunk(**obj) for obj in json.load(file)]

    collection.add(
        ids=[chunk.id for chunk in chunks],
        documents=[chunk.text for chunk in chunks],
        metadatas=[chunk.metadata for chunk in chunks]
    )

def query_collection(query: str, collection: chromadb.Collection, log_dir: str, n: int) -> list[str]:
    results = collection.query(
        query_texts=[query],
        n_results=n
    )
    with open(log_dir, "w") as file:
        json.dump(results, file, indent=4)
    return results

query_collection("What is the knapsack problem?", chroma_client.get_collection(name="CS3510"), "query_log/query_results.json", 2)

# def __main__(input_dir: str, collection_name: str):
#     collection = chroma_client.get_or_create_collection(name=collection_name)

#     ids = add_to_collection(input_dir, collection)

# if __name__ == "__main__":
#     for file in pathlib.Path("extracted_docs/CS3510").glob("*.json"):
#         __main__(str(file), "CS3510")