"""
=========================================================
LLM Service
=========================================================

This module acts as a bridge between the application
and the Groq Client.

Responsibilities

✓ Validate prompts
✓ Send prompts to Groq
✓ Return AI response
✓ Handle empty prompts
✓ Handle API errors

=========================================================
"""

from llm.groq_client import generate_response


# ==========================================================
# Main LLM Function
# ==========================================================

def ask_llm(prompt: str) -> str:
    """
    Sends a prompt to the LLM and returns the AI response.

    Parameters
    ----------
    prompt : str

    Returns
    -------
    str
    """

    if not prompt:
        return "❌ Prompt cannot be empty."

    if len(prompt.strip()) == 0:
        return "❌ Prompt cannot be empty."

    try:

        response = generate_response(prompt)

        return response

    except Exception as error:

        return f"❌ LLM Service Error: {error}"


# ==========================================================
# Health Check
# ==========================================================

def health_check() -> bool:
    """
    Check whether the LLM is responding.

    Returns
    -------
    bool
    """

    try:

        response = generate_response(
            "Reply with only the word OK."
        )

        return "OK" in response.upper()

    except Exception:

        return False


# ==========================================================
# Model Information
# ==========================================================

def get_model_name() -> str:

    from config.llm_config import DEFAULT_MODEL

    return DEFAULT_MODEL


