"""
=========================================================
Settings
=========================================================

KickStack Beginner Project

Configure the AI Productivity Assistant.

=========================================================
"""

import streamlit as st

from config.settings import (
    APP_NAME,
    APP_VERSION
)

from config.llm_config import (
    MODELS,
    DEFAULT_MODEL
)

from llm.llm_service import (
    health_check,
    get_model_name
)

# =========================================================
# Page Title
# =========================================================

st.title("⚙️ Settings")

st.markdown(
    "Configure your AI Productivity Assistant."
)

st.divider()

# =========================================================
# Session State Defaults
# =========================================================

if "selected_model" not in st.session_state:
    st.session_state.selected_model = DEFAULT_MODEL

if "temperature" not in st.session_state:
    st.session_state.temperature = 0.7

if "max_tokens" not in st.session_state:
    st.session_state.max_tokens = 1024

# =========================================================
# AI Configuration
# =========================================================

st.subheader("🤖 AI Configuration")

model_names = list(MODELS.keys())

current_index = model_names.index("Llama 3.3 70B")

selected_name = st.selectbox(
    "LLM Model",
    model_names,
    index=current_index
)

st.session_state.selected_model = MODELS[selected_name]

temperature = st.slider(
    "Temperature",
    0.0,
    1.0,
    value=st.session_state.temperature,
    step=0.1
)

st.session_state.temperature = temperature

max_tokens = st.slider(
    "Max Tokens",
    256,
    4096,
    value=st.session_state.max_tokens,
    step=256
)

st.session_state.max_tokens = max_tokens

st.divider()

# =========================================================
# Connection Test
# =========================================================

st.subheader("🔗 Connection")

if st.button(
    "Test Groq Connection",
    use_container_width=True
):

    with st.spinner("Checking connection..."):

        if health_check():

            st.success(
                "Successfully connected to Groq."
            )

        else:

            st.error(
                "Connection failed."
            )

st.divider()

# =========================================================
# Current Configuration
# =========================================================

st.subheader("📋 Current Configuration")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Application",
        APP_NAME
    )

    st.metric(
        "Version",
        APP_VERSION
    )

with col2:

    st.metric(
        "Current Model",
        get_model_name()
    )

    st.metric(
        "Provider",
        "Groq"
    )

st.divider()

# =========================================================
# Reset
# =========================================================

if st.button(
    "Reset Settings",
    use_container_width=True
):

    st.session_state.selected_model = DEFAULT_MODEL

    st.session_state.temperature = 0.7

    st.session_state.max_tokens = 1024

    st.success(
        "Settings reset successfully."
    )

st.divider()

# =========================================================
# About
# =========================================================

with st.expander("ℹ️ About"):

    st.markdown("""
### Personal AI Productivity & Automation Agent

A beginner-friendly Generative AI project built with:

- Python
- Streamlit
- Groq API
- Llama 3
- Prompt Engineering

Features

- Email Generator
- Email Summarizer
- Meeting Notes
- Task Planner
- Content Creator
- Grammar Rewriter
- PDF Summarizer

Developed as part of the KickStack GenAI Learning Path.
""")

# =========================================================
# Footer
# =========================================================

st.divider()

st.caption(
    "© 2026 KickStack • Beginner Generative AI Project"
)


