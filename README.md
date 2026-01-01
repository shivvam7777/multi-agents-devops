# 🚀 Multi-Agent DevOps System

An AI-powered **multi-agent orchestration system** that simulates a complete DevOps pipeline.  
Agents collaborate step by step: **Planner → Coder → Tester → CI/CD → Monitor**, with a custom FastAPI backend and HTML UI.

---
![Python](https://img.shields.io/badge/python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![License](https://img.shields.io/badge/license-MIT-yellow)

## 📖 Overview
This project demonstrates how multiple AI agents can work together to automate a DevOps workflow.  
It is designed as a **portfolio project** to showcase system-level innovation for AI/ML engineering roles.

---

## 🛠 Features
- 🤖 **Planner Agent** – breaks down tasks into actionable steps  
- 💻 **Coder Agent** – generates and updates code automatically  
- ✅ **Tester Agent** – runs linting and unit tests  
- 🔄 **CI/CD Agent** – simulates deployment pipeline  
- 📊 **Monitor Agent** – tracks logs and performance metrics  
- 🌐 **FastAPI + HTML UI** – interactive interface for orchestration  

---

## 📂 Project Structure

---

## ⚙️ Setup & Installation
```bash
# Clone the repository
git clone https://github.com/shivvam7777/multi-agents-devops.git
cd multi-agents-devops

# Create virtual environment
python -m venv venv
source venv/Scripts/activate   # Windows
source venv/bin/activate       # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run FastAPI server
uvicorn orchestrator.main:app --reload
