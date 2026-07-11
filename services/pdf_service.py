from llm.llm_service import ask_llm
from llm.prompt_templates import pdf_summary


def summarize_pdf(text: str) -> str:
    """
    Summarize PDF
    """

    if not text.strip():
        return "PDF contains no readable text."

    prompt = pdf_summary(text)

    return ask_llm(prompt)


