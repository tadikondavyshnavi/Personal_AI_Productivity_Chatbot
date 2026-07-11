"""
=========================================================
Response Formatter Utility
=========================================================

This module formats AI responses before displaying
them to the user.

Author : KickStack
Project : Personal AI Productivity & Automation Agent
=========================================================
"""

import textwrap


# =========================================================
# Remove Extra Spaces
# =========================================================

def clean_text(text: str) -> str:
    """
    Remove unnecessary spaces and blank lines.
    """

    if not text:
        return ""

    lines = text.splitlines()

    cleaned_lines = [line.strip() for line in lines if line.strip()]

    return "\n".join(cleaned_lines)


# =========================================================
# Format Paragraph Width
# =========================================================

def wrap_text(
    text: str,
    width: int = 100
) -> str:
    """
    Wrap long text into readable paragraphs.
    """

    if not text:
        return ""

    paragraphs = text.split("\n")

    wrapped = []

    for paragraph in paragraphs:

        wrapped.append(
            textwrap.fill(
                paragraph,
                width=width
            )
        )

    return "\n\n".join(wrapped)


# =========================================================
# Markdown Formatter
# =========================================================

def markdown_response(text: str) -> str:
    """
    Return markdown-friendly response.
    """

    text = clean_text(text)

    return text


# =========================================================
# Character Count
# =========================================================

def character_count(text: str) -> int:
    """
    Count total characters.
    """

    if not text:
        return 0

    return len(text)


# =========================================================
# Word Count
# =========================================================

def word_count(text: str) -> int:
    """
    Count total words.
    """

    if not text:
        return 0

    return len(text.split())


# =========================================================
# Reading Time
# =========================================================

def estimated_read_time(text: str) -> int:
    """
    Estimate reading time in minutes.

    Average reading speed:
    200 words / minute
    """

    words = word_count(text)

    minutes = max(1, round(words / 200))

    return minutes


# =========================================================
# Response Statistics
# =========================================================

def response_statistics(text: str) -> dict:
    """
    Return useful response statistics.
    """

    return {

        "Characters": character_count(text),

        "Words": word_count(text),

        "Estimated Reading Time (mins)": estimated_read_time(text)

    }


# =========================================================
# Display Title
# =========================================================

def title(title: str) -> str:
    """
    Generate a formatted title.
    """

    return f"# {title}"


# =========================================================
# Display Subtitle
# =========================================================

def subtitle(subtitle: str) -> str:
    """
    Generate markdown subtitle.
    """

    return f"## {subtitle}"


# =========================================================
# Bullet List
# =========================================================

def bullet_list(items: list) -> str:
    """
    Convert list into markdown bullets.
    """

    if not items:
        return ""

    return "\n".join(
        [f"- {item}" for item in items]
    )


# =========================================================
# Divider
# =========================================================

def divider() -> str:
    """
    Markdown divider.
    """

    return "\n---\n"


