"""
=========================================================
AI Email Generator
=========================================================

KickStack Beginner Project

Generates professional AI-powered emails.

=========================================================
"""

import streamlit as st

from config.constants import (
    EMAIL_TONES,
    EMAIL_LENGTH
)

from services.email_service import generate_email

from utilities.validators import validate_email_inputs

from utilities.download import show_download_options


# =========================================================
# Page Title
# =========================================================

st.title("✉️ AI Email Generator")

st.markdown(
    "Generate professional emails using AI."
)

st.divider()

# =========================================================
# Input Section
# =========================================================

recipient = st.text_input(
    "Recipient",
    placeholder="Example: HR Manager"
)

purpose = st.text_area(
    "Purpose",
    placeholder="Explain what the email is about...",
    height=150
)

col1, col2 = st.columns(2)

with col1:

    tone = st.selectbox(
        "Tone",
        EMAIL_TONES
    )

with col2:

    length = st.selectbox(
        "Email Length",
        EMAIL_LENGTH
    )

st.divider()

# =========================================================
# Generate Button
# =========================================================

if st.button(
    "🚀 Generate Email",
    use_container_width=True
):

    valid, message = validate_email_inputs(
        recipient,
        purpose
    )

    if not valid:

        st.error(message)

    else:

        with st.spinner(
            "Generating professional email..."
        ):

            try:

                response = generate_email(
                    recipient,
                    purpose,
                    tone,
                    length
                )

                st.success(
                    "Email Generated Successfully!"
                )

                st.divider()

                st.subheader("Generated Email")

                st.markdown(response)

                show_download_options(
                    response
                )

            except Exception as error:

                st.error(error)

# =========================================================
# Example Prompt
# =========================================================

with st.expander("💡 Example"):

    st.markdown("""
Recipient

HR Manager

Purpose

Request leave for two days due to a family function.

Tone

Professional

Length

Medium
""")

# =========================================================
# Footer
# =========================================================

st.divider()

st.caption(
    "KickStack Beginner Project • AI Email Generator"
)


