# Personal AI Productivity & Automation Agent

A modular AI-powered productivity platform built using Python, Streamlit, and the Groq API. The application helps automate everyday productivity tasks such as email writing, meeting note generation, content creation, task planning, grammar correction, and PDF summarization.

## Overview

The Personal AI Productivity & Automation Agent is designed to simplify repetitive productivity tasks using Large Language Models (LLMs).

The project uses a modular architecture that separates the user interface, services, configuration, utilities, and LLM-related functionality. This makes the application easier to maintain and extend.

## Features

- AI Email Generator
- Email Summarizer
- Meeting Notes Generator
- Task Planner
- AI Content Creator
- Grammar and Text Rewriter
- PDF Summarizer
- Settings Management
- Multi-page Streamlit Application
- Groq API Integration
- LLM-powered productivity tools

## System Architecture

```text
User
  |
  v
Streamlit Frontend
  |
  v
Service Layer
  |
  v
LLM Service
  |
  v
Groq API
  |
  v
Language Model
