"""
=========================================================
AI Email Summarizer
=========================================================

KickStack Beginner Project

Summarize long emails using AI.

=========================================================
"""

import streamlit as st

from services.email_summariser_service import summarize

from utilities.validators import validate_text

from utilities.download import show_download_options


# =========================================================
# Page Title
# =========================================================

st.title("📄 AI Email Summarizer")

st.markdown(
    "Paste a long email and let AI generate a concise summary."
)

st.divider()


# =========================================================
# Email Input
# =========================================================

email = st.text_area(
    "Paste Email",
    placeholder="Paste your email here...",
    height=300
)

st.divider()


# =========================================================
# Generate Summary
# =========================================================

if st.button(
    "🚀 Summarize Email",
    use_container_width=True
):

    valid, message = validate_text(email)

    if not valid:

        st.error(message)

    else:

        with st.spinner(
            "Summarizing email..."
        ):

            try:

                response = summarize(email)

                st.success(
                    "Summary Generated Successfully!"
                )

                st.divider()

                st.subheader("Email Summary")

                with st.container(border=True):

                    st.markdown(response)

                show_download_options(response)

            except Exception as error:

                st.error(
                    f"Error: {error}"
                )


# =========================================================
# Example
# =========================================================

with st.expander("💡 Example"):

    st.markdown("""

Paste a long business email containing:

- Project updates

- Meeting schedules

- Deadlines

- Action items

The AI will generate:

- Summary

- Key Points

- Action Items

- Deadlines

""")


# =========================================================
# Footer
# =========================================================

st.divider()

st.caption(
    "KickStack Beginner Project • AI Email Summarizer"
)


    