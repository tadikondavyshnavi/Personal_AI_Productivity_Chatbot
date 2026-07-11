
from llm.llm_service import ask_llm
from llm.prompt_templates import grammar_rewriter


def rewrite_text(
    text: str,
    style: str
) -> str:
    """
    Rewrite text
    """

    if not text.strip():
        return "Please enter text."

    prompt = grammar_rewriter(
        text,
        style
    )

    return ask_llm(prompt)




