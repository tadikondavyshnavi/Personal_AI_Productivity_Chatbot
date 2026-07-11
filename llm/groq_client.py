"""
=========================================================
Groq Client
=========================================================

This module is responsible for:

1. Connecting to the Groq API
2. Sending prompts to the LLM
3. Returning AI responses
4. Handling API exceptions

=========================================================
"""

from groq import Groq

from config.settings import GROQ_API_KEY
from config.llm_config import (
    DEFAULT_MODEL,
    LLM_CONFIG,
    SYSTEM_PROMPT
)


# =========================================================
# Create Groq Client
# =========================================================

client = Groq(api_key=GROQ_API_KEY)


# =========================================================
# Generate AI Response
# =========================================================

def generate_response(user_prompt: str) -> str:
    """
    Sends a prompt to the Groq LLM and returns the response.

    Parameters
    ----------
    user_prompt : str
        User input or generated prompt.

    Returns
    -------
    str
        AI-generated response.
    """

    try:

        response = client.chat.completions.create(

            model=DEFAULT_MODEL,

            messages=[

                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },

                {
                    "role": "user",
                    "content": user_prompt
                }

            ],

            **LLM_CONFIG

        )

        return response.choices[0].message.content.strip()

    except Exception as e:

        return f"❌ Error : {str(e)}"

