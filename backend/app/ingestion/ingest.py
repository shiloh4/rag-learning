import json
import pymupdf
import pathlib
from dataclasses import asdict
from app.types.types import Page, Metadata, Chunk


CHUNK_SIZE = 1000
OVERLAP = 100

def extract(input_dir: str) -> list[Page]:
    """
        Extract text from PDF file and return as text + metadata.
    """
    pages: list[Page] = []
    doc = pymupdf.open(input_dir)

    for i, page in enumerate(doc):
        pages.append(Page(text=page.get_text(), source=input_dir, page=i))
    return pages

def chunk(pages: list[Page], chunk_size: int, overlap: int) -> list[Chunk]:
    """
        Naive chunking by fixed size CHUNK_SIZE. OVERLAP only betweek chnks within a page.
    """
    chunks: list[Chunk] = []
    for i,page in enumerate(pages):
        chunk_index = 0
        for j in range(0, len(page.text), chunk_size - overlap):
            data_dict = {
                'id': f"{page.source}-{page.page}-{chunk_index}",
                'text': page.text[j:j+chunk_size],
                'metadata': asdict(Metadata(source=page.source, page=page.page, chunk_idx=chunk_index))
            }
            chunks.append(data_dict)
            chunk_index += 1
    return chunks

def save(chunks: list[Chunk], output_dir: str):
    #clear file
    with open(output_dir, "w") as file:
        file.write("[\n")

        for i, chunk in enumerate(chunks):
            if i:
                file.write(",\n")
            json.dump(chunk, file, indent=4)

        file.write("\n]")

def __main__(input_dir: str, output_dir: str):
    pages = extract(input_dir)
    chunks = chunk(pages, CHUNK_SIZE, OVERLAP)
    save(chunks, output_dir)

if __name__ == "__main__":
    for file in pathlib.Path("documents/CS3510").glob("*.pdf"):
        __main__(str(file), f"extracted_docs/CS3510/{file.stem}.json")