"""
=========================================================
AI PDF Summarizer
=========================================================

KickStack Beginner Project

Upload a PDF document and generate an AI-powered summary.

=========================================================
"""

import streamlit as st

from services.pdf_service import summarize_pdf

from utilities.pdf_reader import (
    read_pdf,
    get_page_count,
    get_pdf_info
)

from utilities.validators import (
    validate_pdf,
    validate_file_size
)

from utilities.download import show_download_options


# =========================================================
# Page Title
# =========================================================

st.title("📑 AI PDF Summarizer")

st.markdown("""
Upload a PDF document and let AI generate:

- Executive Summary
- Key Concepts
- Important Points
- Conclusion
""")

st.divider()

# =========================================================
# Upload PDF
# =========================================================

uploaded_pdf = st.file_uploader(

    "Upload PDF",

    type=["pdf"]

)

st.divider()

# =========================================================
# PDF Information
# =========================================================

if uploaded_pdf:

    valid, message = validate_pdf(uploaded_pdf)

    if not valid:

        st.error(message)

        st.stop()

    valid, message = validate_file_size(uploaded_pdf)

    if not valid:

        st.error(message)

        st.stop()

    info = get_pdf_info(uploaded_pdf)

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Pages",
            info["pages"]
        )

    with col2:

        st.metric(
            "Author",
            info["author"] or "Unknown"
        )

    with col3:

        st.metric(
            "Title",
            info["title"] or "Unknown"
        )

    st.success(
        f"Uploaded: {uploaded_pdf.name}"
    )

st.divider()

# =========================================================
# Generate Summary
# =========================================================

if st.button(

    "🚀 Generate Summary",

    use_container_width=True

):

    if uploaded_pdf is None:

        st.warning("Please upload a PDF document.")

    else:

        with st.spinner(

            "Reading PDF and generating summary..."

        ):

            try:

                pdf_text = read_pdf(uploaded_pdf)

                if len(pdf_text.strip()) == 0:

                    st.error(
                        "No readable text found in the PDF."
                    )

                else:

                    response = summarize_pdf(pdf_text)

                    st.success(
                        "Summary Generated Successfully!"
                    )

                    st.divider()

                    st.subheader("📄 AI Summary")

                    with st.container(border=True):

                        st.markdown(response)

                    st.divider()

                    show_download_options(response)

            except Exception as error:

                st.error(f"Error: {error}")

# =========================================================
# Example
# =========================================================

with st.expander("💡 Example"):

    st.markdown("""

Upload documents like:

- Research Papers

- College Notes

- Company Reports

- Meeting Documents

- Business Proposals

The AI will generate:

- Executive Summary

- Key Concepts

- Important Points

- Conclusion

""")

# =========================================================
# Footer
# =========================================================

st.divider()

st.caption(
    "KickStack Beginner Project • AI PDF Summarizer"
)


