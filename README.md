# Personal AI Productivity & Automation Agent

A modular AI-powered productivity platform built using **Python, Streamlit, and the Groq API**. The application streamlines everyday productivity tasks such as email writing, meeting-note generation, content creation, task planning, grammar correction, and PDF summarization through a clean multi-page interface.

---

<p align="center">
  <img src="assests/thumbnail.png" alt="Personal AI Productivity & Automation Agent" width="900">
</p>

---

## 📌 Overview

The **Personal AI Productivity & Automation Agent** is designed to simplify repetitive productivity tasks using Large Language Models (LLMs).

The project follows a modular architecture that separates configuration, business logic, services, utilities, and user-interface components, making the application easier to maintain, extend, and scale.

The application provides multiple AI-powered productivity tools through a user-friendly multi-page Streamlit interface.

---

## ✨ Features

- 🤖 AI Email Generator
- 📧 Email Summarizer
- 📝 Meeting Notes Generator
- ✅ Task Planner
- ✍️ AI Content Creator
- 🔤 Grammar & Text Rewriter
- 📄 PDF Summarizer
- ⚙️ Settings Management
- 🖥️ Multi-page Streamlit Application
- ⚡ Groq API Integration
- 🧠 Llama 3 Language Model
- 📱 Responsive User Interface

---

## 🏗️ System Architecture

```text
                    User
                      │
                      ▼
             Streamlit Frontend
                      │
                      ▼
                Service Layer
                      │
                      ▼
                 LLM Service
                      │
                      ▼
                  Groq API
                      │
                      ▼
                Llama 3 Model
```

---

## 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Framework | Streamlit |
| AI Provider | Groq API |
| Language Model | Llama 3 |
| Data Processing | Pandas |
| PDF Processing | PyPDF |
| Environment Management | python-dotenv |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```text
Personal_AI_Productivity_Chatbot/
│
├── assests/
├── config/
├── llm/
├── pages/
├── services/
├── utils/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/tadikondavyshnavi/Personal_AI_Productivity_Chatbot.git
```

### 2. Navigate to the Project Directory

```bash
cd Personal_AI_Productivity_Chatbot
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuration

Create a `.env` file in the project root directory.

Add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

> **Security:** Never commit your `.env` file or API keys to GitHub.

Make sure `.env` is included in your `.gitignore` file.

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

Open the URL in your browser to access the application.

---

## 📸 Screenshots

### Application Architecture

<p align="center">
  <img src="assests/architecture.png" alt="Application Architecture" width="900">
</p>

### Home Dashboard

_Add screenshot here._

### AI Email Generator

_Add screenshot here._

### Task Planner

_Add screenshot here._

### PDF Summarizer

_Add screenshot here._

---

## 🧠 Key Learning Outcomes

This project helped strengthen practical knowledge in:

- Python application development
- Streamlit multi-page application development
- Prompt engineering
- REST API integration
- Large Language Model (LLM) integration
- Modular software architecture
- Environment variable management
- Git and GitHub workflow
- API-based application development
- Building AI-powered productivity tools

---

## 💡 Challenges & Learnings

During development, several practical software engineering challenges were addressed, including:

- Designing a scalable and maintainable project structure
- Managing Python virtual environments
- Organizing Git and GitHub workflows
- Protecting API credentials using environment variables
- Designing a responsive Streamlit user interface
- Integrating the Groq API with modular service components
- Structuring AI functionality into reusable services
- Managing dependencies for an AI-powered Python application

---

## 🔮 Future Enhancements

Potential future improvements include:

- 🔐 User authentication
- 💬 Conversation history
- 🧠 Support for multiple LLM providers
- 🎙️ Voice command integration
- ☁️ Cloud deployment
- 🗄️ Database integration
- 📄 PDF and DOCX export
- 🌙 Dark mode
- 📊 AI-powered analytics dashboard
- 🔄 Persistent user preferences

---

## 👩‍💻 Developer

### Tadikonda Vyshnavi

**Bachelor of Technology (Information Technology)**

Interested in:

- Artificial Intelligence
- Python Development
- Software Engineering
- Intelligent Automation
- LLM-powered Applications

### GitHub

[https://github.com/tadikondavyshnavi](https://github.com/tadikondavyshnavi)

---

## 📄 License

This project is intended for **educational, learning, and portfolio purposes**.
