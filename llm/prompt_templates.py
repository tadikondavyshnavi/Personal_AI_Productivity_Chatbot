"""
=========================================================
Prompt Templates
=========================================================

This module contains reusable prompt templates
for all AI features.

Author : KickStack
Project : Personal AI Productivity & Automation Agent
=========================================================
"""


# =========================================================
# Email Generator
# =========================================================

def email_prompt(
    recipient: str,
    purpose: str,
    tone: str,
    length: str
) -> str:

    return f"""
You are a professional email writing assistant.

Write an email using the following details.

Recipient:
{recipient}

Purpose:
{purpose}

Tone:
{tone}

Length:
{length}

Instructions:

- Write a clear subject.
- Begin with a professional greeting.
- Keep the language natural.
- End with a professional closing.
- Generate only the email.
"""


# =========================================================
# Email Summarizer
# =========================================================

def summarize_email(email: str) -> str:

    return f"""
You are an expert email summarizer.

Summarize the following email.

Email:

{email}

Return the response in this format.

## Summary

## Key Points

## Action Items

## Deadlines
"""


# =========================================================
# Meeting Notes Generator
# =========================================================

def meeting_notes(transcript: str) -> str:

    return f"""
You are an AI Meeting Assistant.

Convert the meeting transcript into professional meeting notes.

Meeting Transcript

{transcript}

Return

## Meeting Summary

## Discussion Points

## Decisions

## Action Items

## Next Steps
"""


# =========================================================
# Task Planner
# =========================================================

def task_planner(goal: str) -> str:

    return f"""
You are an AI Productivity Coach.

Create a detailed task plan.

Goal

{goal}

Return

## Objective

## Daily Tasks

## Weekly Plan

## Milestones

## Estimated Timeline
"""


# =========================================================
# Content Creator
# =========================================================

def content_creator(
    content_type: str,
    topic: str
) -> str:

    return f"""
You are a professional content writer.

Generate a

{content_type}

Topic

{topic}

Write engaging and original content.

Keep it well structured.
"""


# =========================================================
# Grammar Rewriter
# =========================================================

def grammar_rewriter(
    text: str,
    style: str
) -> str:

    return f"""
You are an English writing expert.

Rewrite the following text.

Writing Style

{style}

Text

{text}

Correct grammar.

Improve sentence structure.

Do not change the meaning.
"""


# =========================================================
# PDF Summarizer
# =========================================================

def pdf_summary(text: str) -> str:

    return f"""
You are an AI Document Analyst.

Read the document below.

{text}

Generate

## Executive Summary

## Key Concepts

## Important Points

## Conclusion
"""

