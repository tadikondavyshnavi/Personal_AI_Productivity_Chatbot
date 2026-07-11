"""
=========================================================
AI Task Planner
=========================================================

KickStack Beginner Project

Generate a step-by-step action plan for any goal.

=========================================================
"""

import streamlit as st

from services.task_planner_service import generate_task_plan
from utilities.validators import validate_goal
from utilities.download import show_download_options


# =========================================================
# Page Title
# =========================================================

st.title("📅 AI Task Planner")

st.markdown("""
Create a smart action plan to achieve your goals.

Examples:

- Learn Python in 30 days
- Build an AI Chatbot
- Crack a Data Engineer Interview
- Complete a College Project
""")

st.divider()

# =========================================================
# Goal Input
# =========================================================

goal = st.text_area(
    "Enter Your Goal",
    placeholder="Example: Learn Python in 30 days",
    height=150
)

col1, col2 = st.columns(2)

with col1:

    duration = st.selectbox(
        "Timeline",
        [
            "1 Week",
            "2 Weeks",
            "1 Month",
            "2 Months",
            "3 Months",
            "6 Months"
        ]
    )

with col2:

    difficulty = st.selectbox(
        "Difficulty",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

st.divider()

# =========================================================
# Generate Button
# =========================================================

if st.button(
    "🚀 Generate Task Plan",
    use_container_width=True
):

    valid, message = validate_goal(goal)

    if not valid:

        st.error(message)

    else:

        with st.spinner("Creating your personalized task plan..."):

            try:

                planner_prompt = (
                    f"{goal}\n\n"
                    f"Timeline: {duration}\n"
                    f"Difficulty: {difficulty}"
                )

                response = generate_task_plan(planner_prompt)

                st.success("Task Plan Generated Successfully!")

                st.divider()

                st.subheader("📋 Your AI Task Plan")

                with st.container(border=True):
                    st.markdown(response)

                st.divider()

                show_download_options(response)

            except Exception as error:

                st.error(f"Error: {error}")

# =========================================================
# Example
# =========================================================

with st.expander("💡 Example Goal"):

    st.markdown("""
### Goal

Build a Personal Portfolio Website

### Timeline

1 Month

### Difficulty

Beginner

The AI will generate:

- Objective
- Weekly Milestones
- Daily Tasks
- Resources
- Final Deliverables
""")

# =========================================================
# Footer
# =========================================================

st.divider()

st.caption(
    "KickStack Beginner Project • AI Task Planner"
)


