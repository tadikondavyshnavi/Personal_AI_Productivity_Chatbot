

from llm.llm_service import ask_llm
from llm.prompt_templates import email_prompt


def generate_email(
    recipient: str,
    purpose: str,
    tone: str,
    length: str
) -> str:
    """
    Generate professional email
    """

    if not recipient.strip():
        return "Please enter recipient."

    if not purpose.strip():
        return "Please enter email purpose."

    prompt = email_prompt(
        recipient,
        purpose,
        tone,
        length
    )

    return ask_llm(prompt)



