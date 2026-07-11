"""
=========================================================
Helper Functions
=========================================================

Common reusable helper functions used throughout
the application.

Author : KickStack
Project : Personal AI Productivity & Automation Agent
=========================================================
"""

from datetime import datetime
import re


# =========================================================
# Current Date & Time
# =========================================================

def get_current_datetime():
    """
    Returns current date and time.
    """

    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# =========================================================
# Current Date
# =========================================================

def get_current_date():
    """
    Returns current date.
    """

    return datetime.now().strftime("%d-%m-%Y")


# =========================================================
# Character Count
# =========================================================

def character_count(text: str):

    if not text:
        return 0

    return len(text)


# =========================================================
# Word Count
# =========================================================

def word_count(text: str):

    if not text:
        return 0

    return len(text.split())


# =========================================================
# Estimated Reading Time
# =========================================================

def reading_time(text: str):

    words = word_count(text)

    minutes = max(1, round(words / 200))

    return minutes


# =========================================================
# Clean Text
# =========================================================

def clean_text(text: str):

    if not text:
        return ""

    text = re.sub(r"\s+", " ", text)

    return text.strip()


# =========================================================
# Short Preview
# =========================================================

def preview(text: str, length=120):

    if len(text) <= length:
        return text

    return text[:length] + "..."


# =========================================================
# Token Estimate
# =========================================================

def estimate_tokens(text: str):

    words = word_count(text)

    return int(words * 1.3)


# =========================================================
# Greeting
# =========================================================

def greeting():

    hour = datetime.now().hour

    if hour < 12:
        return "Good Morning ☀️"

    elif hour < 18:
        return "Good Afternoon 🌤️"

    return "Good Evening 🌙"


