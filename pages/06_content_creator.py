"""
=========================================================
AI Content Creator
=========================================================

KickStack Beginner Project

Generate high-quality content using AI.

=========================================================
"""

import streamlit as st

from config.constants import CONTENT_TYPES
from services.content_service import generate_content
from utilities.validators import validate_content
from utilities.download import show_download_options


# =========================================================
# Page Title
# =========================================================

st.title("✍️ AI Content Creator")

st.markdown("""
Create engaging content for blogs, social media,
product descriptions, marketing campaigns, and more.
""")

st.divider()

# =========================================================
# Content Type
# =========================================================

content_type = st.selectbox(
    "Content Type",
    CONTENT_TYPES
)

# =========================================================
# Topic
# =========================================================

topic = st.text_input(
    "Topic",
    placeholder="Example: Benefits of Artificial Intelligence"
)

# =========================================================
# Target Audience
# =========================================================

audience = st.text_input(
    "Target Audience",
    placeholder="Example: College Students"
)

# =========================================================
# Writing Tone
# =========================================================

tone = st.selectbox(

    "Writing Tone",

    [

        "Professional",

        "Friendly",

        "Formal",

        "Casual",

        "Persuasive",

        "Inspirational"

    ]

)

# =========================================================
# Content Length
# =========================================================

length = st.selectbox(

    "Content Length",

    [

        "Short",

        "Medium",

        "Long"

    ]

)

st.divider()

# =========================================================
# Generate Button
# =========================================================

if st.button(

    "🚀 Generate Content",

    use_container_width=True

):

    valid, message = validate_content(topic)

    if not valid:

        st.error(message)

    else:

        with st.spinner(
            "Generating AI content..."
        ):

            try:

                prompt = f"""
Topic: {topic}

Audience: {audience}

Tone: {tone}

Length: {length}
"""

                response = generate_content(
                    content_type,
                    prompt
                )

                st.success(
                    "Content Generated Successfully!"
                )

                st.divider()

                st.subheader("Generated Content")

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

### Content Type

LinkedIn Post

### Topic

Artificial Intelligence in Education

### Audience

College Students

### Tone

Professional

### Length

Medium

The AI will generate an engaging LinkedIn post.
""")

# =========================================================
# Footer
# =========================================================

st.divider()

st.caption(
    "KickStack Beginner Project • AI Content Creator"
)


