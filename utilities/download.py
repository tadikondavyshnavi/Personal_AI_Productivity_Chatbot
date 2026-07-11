"""
=========================================================
Download Utilities
=========================================================

Provides download options for AI-generated output.

Author : KickStack
Project : Personal AI Productivity & Automation Agent
=========================================================
"""

import streamlit as st


# =========================================================
# Download TXT
# =========================================================

def download_txt(
    text: str,
    filename="output.txt"
):

    st.download_button(

        label="⬇️ Download TXT",

        data=text,

        file_name=filename,

        mime="text/plain"

    )


# =========================================================
# Download Markdown
# =========================================================

def download_md(
    text: str,
    filename="output.md"
):

    st.download_button(

        label="⬇️ Download Markdown",

        data=text,

        file_name=filename,

        mime="text/markdown"

    )


# =========================================================
# Copy Hint
# =========================================================

def copy_message():

    st.info(
        "📋 Select the generated text and press Ctrl+C (Cmd+C on macOS) to copy it."
    )


# =========================================================
# Display Download Section
# =========================================================

def show_download_options(response: str):

    st.divider()

    st.subheader("Export")

    download_txt(response)

    download_md(response)

    copy_message()


