import pymupdf4llm
import pathlib
import pymupdf

def pdf_to_md(input_dir: str, output_dir: str):
    """
    Extracts the pages from a PDF file and returns a list of page contents.
    """
    doc = pymupdf.open(input_dir)
    md_text = pymupdf4llm.to_markdown(doc)
    pathlib.Path(output_dir).write_bytes(md_text.encode())

pdf_to_md("documents/CS3510/L1.pdf", "extracted/CS3510/L1.md")