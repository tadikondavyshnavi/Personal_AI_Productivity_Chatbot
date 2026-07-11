"""
=========================================================
Validators Utility
=========================================================

This module contains reusable validation functions
used across the application.

Author : KickStack
Project : Personal AI Productivity & Automation Agent
=========================================================
"""

from pathlib import Path


# =========================================================
# Validate Text Input
# =========================================================

def validate_text(text: str):
    """
    Validate text input.

    Returns:
        (bool, message)
    """

    if text is None:
        return False, "Input cannot be empty."

    if len(text.strip()) == 0:
        return False, "Please enter some text."

    return True, ""


# =========================================================
# Validate Email Generator
# =========================================================

def validate_email_inputs(
    recipient: str,
    purpose: str
):
    """
    Validate email generator inputs.
    """

    if not recipient.strip():
        return False, "Recipient is required."

    if not purpose.strip():
        return False, "Purpose is required."

    return True, ""


# =========================================================
# Validate Meeting Notes
# =========================================================

def validate_meeting_notes(transcript: str):

    if not transcript.strip():
        return False, "Please paste meeting transcript."

    return True, ""


# =========================================================
# Validate Task Planner
# =========================================================

def validate_goal(goal: str):

    if not goal.strip():
        return False, "Please enter your goal."

    return True, ""


# =========================================================
# Validate Content Creator
# =========================================================

def validate_content(
    topic: str
):

    if not topic.strip():
        return False, "Please enter a topic."

    return True, ""


# =========================================================
# Validate Grammar Rewriter
# =========================================================

def validate_grammar(text: str):

    if not text.strip():
        return False, "Please enter text."

    return True, ""


# =========================================================
# Validate Uploaded PDF
# =========================================================

def validate_pdf(uploaded_file):

    if uploaded_file is None:

        return False, "Please upload a PDF."

    extension = Path(uploaded_file.name).suffix.lower()

    if extension != ".pdf":

        return False, "Only PDF files are supported."

    return True, ""


# =========================================================
# Validate Uploaded TXT
# =========================================================

def validate_text_file(uploaded_file):

    if uploaded_file is None:

        return False, "Please upload a TXT file."

    extension = Path(uploaded_file.name).suffix.lower()

    if extension != ".txt":

        return False, "Only TXT files are supported."

    return True, ""


# =========================================================
# Validate File Size
# =========================================================

def validate_file_size(
    uploaded_file,
    max_size_mb=10
):
    """
    Validate uploaded file size.

    Default:
        10 MB
    """

    if uploaded_file is None:

        return False, "No file selected."

    file_size = uploaded_file.size / (1024 * 1024)

    if file_size > max_size_mb:

        return (
            False,
            f"Maximum file size is {max_size_mb} MB."
        )

    return True, ""


# =========================================================
# Validate Prompt Length
# =========================================================

def validate_prompt_length(
    prompt: str,
    max_characters=10000
):

    if len(prompt) > max_characters:

        return (
            False,
            f"Prompt exceeds {max_characters} characters."
        )

    return True, ""


# =========================================================
# Validate AI Response
# =========================================================

def validate_response(response: str):

    if not response:

        return False, "No response received."

    if len(response.strip()) == 0:

        return False, "Empty response returned."

    return True, ""


