

from llm.llm_service import ask_llm
from llm.prompt_templates import meeting_notes


def generate_meeting_notes(transcript: str) -> str:
    """
    Generate meeting notes
    """

    if not transcript.strip():
        return "Please paste meeting transcript."

    prompt = meeting_notes(transcript)

    return ask_llm(prompt)



    