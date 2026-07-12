"""
==========================================================
Personal AI Productivity & Automation Agent
app.py - Main Streamlit Bootstrap
==========================================================
"""

import sys
import logging
from typing import Dict, Any

import streamlit as st

# Configure basic logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Try importing project configurations
try:
    from config.settings import APP_NAME, APP_VERSION
except ImportError:
    APP_NAME = "Personal AI Productivity & Automation Agent"
    APP_VERSION = "1.0.0"

# Try importing health check function
try:
    from llm.llm_service import health_check
except ImportError:
    def health_check() -> bool:
        """Fallback health check if module is not found."""
        return True


def configure_page() -> None:
    """Configures the main Streamlit page settings."""
    st.set_page_config(
        page_title=APP_NAME,
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )


def inject_custom_css() -> None:
    """Injects custom CSS for a premium SaaS UI look."""
    css = """
    <style>
        /* Base Theme */
        :root {
            --primary-teal: #14B8A6;
            --primary-teal-hover: #0D9488;
            --background-main: #FFFFFF;
            --background-card: #F8FAFC;
            --text-main: #0F172A;
            --text-muted: #64748B;
            --border-color: #E2E8F0;
            --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
            --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
            --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
        }

        /* Global Background and Text */
        .stApp {
            background-color: var(--background-main);
            color: var(--text-main);
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }

        /* Hide Top Padding */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1200px;
        }

        /* Custom Cards */
        .premium-card {
            background-color: var(--background-card);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: var(--shadow-sm);
            transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
            height: 100%;
        }
        
        .premium-card:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
            border-color: var(--primary-teal);
        }

        .card-icon {
            font-size: 2rem;
            margin-bottom: 1rem;
            color: var(--primary-teal);
        }

        .card-title {
            font-size: 1.125rem;
            font-weight: 600;
            color: var(--text-main);
            margin-bottom: 0.5rem;
        }

        .card-desc {
            font-size: 0.875rem;
            color: var(--text-muted);
            line-height: 1.5;
        }

        /* Buttons */
        .stButton>button {
            background-color: var(--primary-teal);
            color: white;
            border-radius: 8px;
            border: none;
            padding: 0.5rem 1rem;
            font-weight: 600;
            transition: all 0.2s ease;
            box-shadow: var(--shadow-sm);
        }
        
        .stButton>button:hover {
            background-color: var(--primary-teal-hover);
            color: white;
            transform: translateY(-1px);
            box-shadow: var(--shadow-md);
        }

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #F1F5F9;
            border-right: 1px solid var(--border-color);
        }
        
        [data-testid="stSidebar"] .stMarkdown h1, 
        [data-testid="stSidebar"] .stMarkdown h2, 
        [data-testid="stSidebar"] .stMarkdown h3 {
            color: var(--text-main);
        }

        /* Custom Expanders */
        .streamlit-expanderHeader {
            background-color: var(--background-card);
            border-radius: 8px;
            border: 1px solid var(--border-color);
            color: var(--text-main) !important;
            font-weight: 600;
        }

        /* Success/Warning/Error/Info Boxes */
        .stSuccess, .stInfo, .stWarning, .stError {
            border-radius: 8px;
            border-left-width: 4px;
        }

        /* Typography */
        h1, h2, h3, h4, h5, h6 {
            color: var(--text-main);
            font-weight: 700;
            letter-spacing: -0.025em;
        }

        .hero-title {
            font-size: 2.5rem;
            font-weight: 800;
            background: linear-gradient(to right, #0F172A, #14B8A6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }

        .hero-subtitle {
            font-size: 1.25rem;
            color: var(--text-muted);
            margin-bottom: 2rem;
        }
        
        /* Badges */
        .tech-badge {
            display: inline-block;
            background-color: #E2E8F0;
            color: #334155;
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 600;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
            border: 1px solid #CBD5E1;
        }
        
        /* Metric Styling */
        [data-testid="stMetricValue"] {
            color: var(--primary-teal);
            font-weight: 700;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def initialize_session_state() -> None:
    """Initializes Streamlit session state variables with default values."""
    defaults: Dict[str, Any] = {
        "chat_history": [],
        "theme": "light",
        "selected_model": "Llama 3.3 70B",
        "temperature": 0.7,
        "max_tokens": 1024,
        "generated_output": None,
        "current_page": "Home"
    }

    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val


def render_sidebar() -> None:
    """Renders the professional SaaS sidebar."""
    with st.sidebar:
        st.markdown(f"## 🤖 {APP_NAME}")
        st.caption(f"Version {APP_VERSION}")
        st.divider()

        st.markdown("### Navigation")
        st.markdown(
            """
            This application uses multi-page navigation. 
            Please use the **Pages** menu above to access different AI tools.
            """
        )

        st.divider()
        st.markdown("### AI Engine")
        st.info(f"**Model:** {st.session_state['selected_model']}")
        
        # Health Check
        is_connected = False
        try:
            is_connected = health_check()
        except Exception as e:
            logger.error(f"Health check failed: {e}")
            
        if is_connected:
            st.success("✅ Groq Status: Online")
        else:
            st.error("❌ Groq Status: Offline")

        st.divider()
        st.markdown("### About")
        st.caption(
            "KickStack Beginner GenAI Project built with clean architecture, "
            "Python, Streamlit, and the Groq API."
        )


def render_hero_section() -> None:
    """Renders the top hero section of the application."""
    st.markdown('<div class="hero-title">Personal AI Productivity & Automation Agent</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Boost your productivity with AI-powered automation.</div>', unsafe_allow_html=True)
    
    st.image("assests/thumbnail.png", use_container_width=True)
    
    st.info("💡 **Tip:** Use the sidebar pages to access specialized AI tools like Email Generation, Task Planning, and Document Summarization.")


def render_feature_cards() -> None:
    """Renders the available features as premium cards."""
    st.markdown("### ✨ Available AI Tools")
    
    # Define features
    features = [
        {"icon": "✉️", "title": "Email Generator", "desc": "Draft professional emails in seconds tailored to your specific context."},
        {"icon": "📄", "title": "Email Summarizer", "desc": "Condense long email threads into actionable bullet points."},
        {"icon": "📝", "title": "Meeting Notes", "desc": "Generate structured meeting minutes and extract key action items."},
        {"icon": "📅", "title": "Task Planner", "desc": "Break down complex goals into organized, daily actionable steps."},
        {"icon": "✍️", "title": "Content Creator", "desc": "Create engaging blog posts, social media updates, and articles."},
        {"icon": "📚", "title": "Grammar Rewriter", "desc": "Polish your text for perfect grammar, tone, and clarity."},
        {"icon": "📑", "title": "PDF Summarizer", "desc": "Extract key insights and summaries from lengthy PDF documents."}
    ]

    # Create rows of 3 columns
    for i in range(0, len(features), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(features):
                feat = features[i + j]
                html_card = f"""
                <div class="premium-card">
                    <div class="card-icon">{feat['icon']}</div>
                    <div class="card-title">{feat['title']}</div>
                    <div class="card-desc">{feat['desc']}</div>
                </div>
                """
                cols[j].markdown(html_card, unsafe_allow_html=True)
            else:
                # Empty placeholder for grid alignment
                cols[j].write("")
    
    st.divider()


def render_tech_stack() -> None:
    """Renders the technology stack used in the project."""
    st.markdown("### 🛠️ Technology Stack")
    
    techs = [
        "Python", "Streamlit", "Groq API", "Llama 3.3", 
        "Prompt Engineering", "AI Productivity", "Clean Architecture"
    ]
    
    badges_html = "".join([f'<span class="tech-badge">{tech}</span>' for tech in techs])
    st.markdown(f"<div>{badges_html}</div>", unsafe_allow_html=True)
    st.write("")


def render_architecture_diagram() -> None:
    """Renders the system architecture diagram."""
    st.markdown("### 🏗️ System Architecture")
    with st.expander("View Clean Architecture Diagram", expanded=True):
        st.image("assests/architecture.png", use_container_width=True)


def render_notifications() -> None:
    """Renders a section for system notifications and alerts."""
    st.markdown("### 🔔 System Status")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("System is fully operational and ready to process requests.")
    with col2:
        st.info("Tip: You can adjust token limits and temperature in the sidebar settings on individual tool pages.")


def render_quick_tips() -> None:
    """Renders an expandable section for quick tips."""
    st.markdown("### 💡 Quick Tips & Guides")
    
    with st.expander("Prompt Engineering Tips"):
        st.markdown("""
        - **Be Specific:** Clearly state your objective, target audience, and desired tone.
        - **Provide Context:** The more background information you provide, the better the output.
        - **Iterate:** If the first result isn't perfect, tweak your prompt and try again!
        """)
        
    with st.expander("Productivity Tips"):
        st.markdown("""
        - **Batching:** Use the Email Generator to draft multiple emails in one session.
        - **Delegation:** Let the Task Planner break down big goals into manageable chunks.
        """)
        
    with st.expander("PDF Upload Tips"):
        st.markdown("""
        - Ensure your PDFs contain text data (not just scanned images) for the best results.
        - Very large PDFs might take longer to process due to token limits.
        """)


def render_footer() -> None:
    """Renders the professional footer."""
    st.divider()
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown(
           f"""
           <div style='text-align: center; color: var(--text-muted); font-size: 0.875rem; line-height: 1.6;'>
              © 2026 KickStack | {APP_NAME} v{APP_VERSION}<br>
              Designed & Developed by <strong>Vyshnavi</strong><br>
              Built with 🐍 Python • 🌐 Streamlit • ⚡ Groq
            </div>
            """,
            unsafe_allow_html=True
    )

def main() -> None:
    """Main application bootstrap."""
    configure_page()
    inject_custom_css()
    initialize_session_state()
    
    render_sidebar()
    
    # Main Content Area
    render_hero_section()
    render_feature_cards()
    
    # Lower Sections
    st.write("")
    col_a, col_b = st.columns([2, 1])
    
    with col_a:
        render_tech_stack()
        render_architecture_diagram()
        
    with col_b:
        render_notifications()
        render_quick_tips()
        
    render_footer()


if __name__ == "__main__":
    main()