"""
=========================================================
AI Grammar & Rewrite Assistant
=========================================================

KickStack Beginner Project

Correct grammar and rewrite text using AI.

=========================================================
"""

import streamlit as st

from config.constants import GRAMMAR_STYLES
from services.grammar_service import rewrite_text
from utilities.validators import validate_grammar
from utilities.download import show_download_options


# =========================================================
# Page Title
# =========================================================

st.title("📚 AI Grammar & Rewrite Assistant")

st.markdown("""
Improve grammar, sentence structure, clarity,
and professionalism while preserving the original meaning.
""")

st.divider()

# =========================================================
# User Input
# =========================================================

text = st.text_area(
    "Enter Your Text",
    placeholder="""
Example:

hi sir,

i want leave tomorrow because i have family function.
please approve my leave.

thank you.
""",
    height=250
)

# =========================================================
# Rewrite Style
# =========================================================

style = st.selectbox(
    "Rewrite Style",
    GRAMMAR_STYLES
)

# =========================================================
# Additional Options
# =========================================================

col1, col2 = st.columns(2)

with col1:

    fix_grammar = st.checkbox(
        "Correct Grammar",
        value=True
    )

with col2:

    improve_clarity = st.checkbox(
        "Improve Readability",
        value=True
    )

st.divider()

# =========================================================
# Generate Button
# =========================================================

if st.button(
    "🚀 Rewrite Text",
    use_container_width=True
):

    valid, message = validate_grammar(text)

    if not valid:

        st.error(message)

    else:

        with st.spinner(
            "Improving your text..."
        ):

            try:

                rewrite_request = f"""
Text

{text}

Rewrite Style

{style}

Correct Grammar

{fix_grammar}

Improve Readability

{improve_clarity}
"""

                response = rewrite_text(
                    rewrite_request,
                    style
                )

                st.success(
                    "Text Rewritten Successfully!"
                )

                st.divider()

                st.subheader("Rewritten Text")

                with st.container(border=True):

                    st.markdown(response)

                st.divider()

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
### Original Text

hi sir,

i want leave tomorrow because i have family function.

thank you

### Rewrite Style

Professional

The AI will:

- Correct grammar
- Improve sentence structure
- Make the writing more professional
- Preserve the original meaning
""")

# =========================================================
# Footer
# =========================================================

st.divider()

st.caption(
    "KickStack Beginner Project • AI Grammar & Rewrite Assistant"
)


