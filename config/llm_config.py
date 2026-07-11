"""
=========================================================
Groq LLM Configuration
=========================================================
"""

# =========================================================
# Available Models
# =========================================================

MODELS = {

    "Llama 3.3 70B":
        "llama-3.3-70b-versatile",

    "Llama 3.1 8B":
        "llama-3.1-8b-instant",

    "Gemma 2 9B":
        "gemma2-9b-it"

}

# =========================================================
# Default Model
# =========================================================

DEFAULT_MODEL = MODELS["Llama 3.3 70B"]

# =========================================================
# Generation Parameters
# =========================================================


LLM_CONFIG = {

    "temperature": 0.7,

    "max_tokens": 1024,

    "top_p": 1,

    "stream": False

}


    
# =========================================================
# AI Assistant System Prompt
# =========================================================

SYSTEM_PROMPT = """
You are an intelligent AI Productivity Assistant.

Your responsibilities include:

• Writing professional emails

• Summarizing long emails

• Generating meeting notes

• Creating task plans

• Writing professional content

• Improving grammar

• Summarizing PDF documents

Always answer politely.

Generate structured responses.

Do not hallucinate.

Keep responses concise and useful.
"""


