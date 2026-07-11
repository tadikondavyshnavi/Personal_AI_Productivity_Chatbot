from llm.llm_service import ask_llm
from llm.prompt_templates import content_creator


def generate_content(
    content_type: str,
    topic: str
) -> str:
    """
    Generate AI Content
    """

    if not topic.strip():
        return "Please enter topic."

    prompt = content_creator(
        content_type,
        topic
    )

    return ask_llm(prompt)




