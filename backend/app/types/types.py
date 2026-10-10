from dataclasses import dataclass

@dataclass
class Page:
    """
        A page of a document.
    """
    text: str
    source: str
    page: int

@dataclass
class Metadata:
    """
        Metadata for a chunk.
    """
    source: str
    page: int
    chunk_idx: int

@dataclass
class Chunk:
    """
        A chunk of text from a document.
    """
    id: str
    text: str
    metadata: Metadata