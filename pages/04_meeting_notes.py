"""
=========================================================
AI Meeting Notes Generator
=========================================================

KickStack Beginner Project

Convert meeting transcripts into professional
meeting notes.

=========================================================
"""

import streamlit as st

from services.meeting_service import generate_meeting_notes
from utilities.validators import validate_meeting_notes
from utilities.download import show_download_options


# =========================================================
# Page Title
# =========================================================

st.title("📝 AI Meeting Notes Generator")

st.markdown(
    """
Transform raw meeting transcripts into structured
meeting notes using AI.
"""
)

st.divider()

# =========================================================
# Meeting Transcript Input
# =========================================================

meeting_transcript = st.text_area(

    "Meeting Transcript",

    placeholder="""
Paste your meeting transcript here...

Example:

John:
Let's complete the dashboard this week.

Sarah:
I'll finish the frontend by Wednesday.

Alex:
Backend API will be ready by Friday.
""",

    height=320

)

st.divider()

# =========================================================
# Generate Notes
# =========================================================

if st.button(

    "🚀 Generate Meeting Notes",

    use_container_width=True

):

    valid, message = validate_meeting_notes(
        meeting_transcript
    )

    if not valid:

        st.error(message)

    else:

        with st.spinner(
            "Generating meeting notes..."
        ):

            try:

                response = generate_meeting_notes(
                    meeting_transcript
                )

                st.success(
                    "Meeting Notes Generated Successfully!"
                )

                st.divider()

                st.subheader("Generated Meeting Notes")

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

with st.expander("💡 Example Transcript"):

    st.markdown("""

**John**

We need to finish the analytics dashboard by Friday.

**Sarah**

Frontend will be completed by Wednesday.

**Alex**

Backend API integration is almost done.

**David**

QA testing starts on Thursday.

The AI will generate:

- Meeting Summary
- Discussion Points
- Decisions
- Action Items
- Next Steps

""")

# =========================================================
# Footer
# =========================================================

st.divider()

st.caption(
    "KickStack Beginner Project • AI Meeting Notes Generator"
)


