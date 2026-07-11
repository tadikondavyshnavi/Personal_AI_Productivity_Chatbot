

from llm.llm_service import ask_llm
from llm.prompt_templates import summarize_email


def summarize(email: str) -> str:
    """
    Summarize email
    """

    if not email.strip():
        return "Please paste an email."

    prompt = summarize_email(email)

    return ask_llm(prompt)



