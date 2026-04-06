# RceCarCopilot
# 🏎️ AI Race Engineering Copilot

## Overview
A multi-agent AI system designed for professional race engineers and drivers.

## Agents
- Telemetry Agent
- Setup Agent
- Strategy Agent
- Document Agent (RAG)
- Maintenance Agent
- Copilot Agent (Orchestrator)

## Architecture
Each agent processes domain-specific inputs and outputs structured insights.
The Copilot aggregates all outputs into actionable intelligence.

## Features
- CSV telemetry analysis
- Dynamic setup generation
- Strategy optimization
- Document Q&A (RAG)
- Maintenance insights
- Chat interface with memory

## Local Setup

```bash
pip install -r requirements.txt
streamlit run app.py
