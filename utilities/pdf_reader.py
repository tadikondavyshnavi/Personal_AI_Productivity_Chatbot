"""
=========================================================
PDF Reader Utility
=========================================================

This module provides helper functions for reading
PDF documents uploaded by the user.

Author : KickStack
Project : Personal AI Productivity & Automation Agent
=========================================================
"""

from io import BytesIO
from pypdf import PdfReader


# =========================================================
# Read PDF File
# =========================================================

def read_pdf(uploaded_file) -> str:
    """
    Extract text from an uploaded PDF file.

    Parameters
    ----------
    uploaded_file : UploadedFile
        Streamlit uploaded PDF file.

    Returns
    -------
    str
        Extracted text from all pages.
    """

    try:

        pdf = PdfReader(BytesIO(uploaded_file.read()))

        extracted_text = ""

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                extracted_text += page_text + "\n"

        return extracted_text.strip()

    except Exception as error:

        raise Exception(f"Unable to read PDF: {error}")


# =========================================================
# Count PDF Pages
# =========================================================

def get_page_count(uploaded_file) -> int:
    """
    Returns the total number of pages in the PDF.
    """

    try:

        pdf = PdfReader(BytesIO(uploaded_file.read()))

        return len(pdf.pages)

    except Exception:

        return 0


# =========================================================
# Read Single Page
# =========================================================

def read_page(uploaded_file, page_number: int) -> str:
    """
    Extract text from a specific page.

    Parameters
    ----------
    uploaded_file : Uploaded PDF

    page_number : int

    Returns
    -------
    str
    """

    try:

        pdf = PdfReader(BytesIO(uploaded_file.read()))

        if page_number >= len(pdf.pages):
            return ""

        page = pdf.pages[page_number]

        return page.extract_text()

    except Exception:

        return ""


# =========================================================
# PDF Information
# =========================================================

def get_pdf_info(uploaded_file) -> dict:
    """
    Returns basic PDF metadata.
    """

    try:

        pdf = PdfReader(BytesIO(uploaded_file.read()))

        metadata = pdf.metadata

        return {

            "pages": len(pdf.pages),

            "title": metadata.title if metadata else "",

            "author": metadata.author if metadata else "",

            "creator": metadata.creator if metadata else "",

            "producer": metadata.producer if metadata else ""

        }

    except Exception:

        return {

            "pages": 0,

            "title": "",

            "author": "",

            "creator": "",

            "producer": ""

        }


# =========================================================
# Check Empty PDF
# =========================================================

def is_pdf_empty(uploaded_file) -> bool:
    """
    Returns True if no readable text exists.
    """

    text = read_pdf(uploaded_file)

    return len(text.strip()) == 0


