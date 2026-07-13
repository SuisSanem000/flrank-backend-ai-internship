# FlyRank AI Internship - Project Context

## About the Project
This repository (`flrank-backend-ai-internship`) contains assignments and documentation for the **Backend AI Engineering Track** of the FlyRank Internship. The goal is to build, test, and deploy backend services, starting from the smallest possible server up to more complex integrations.

## Tech Stack
- **Language:** Python 3
- **Framework:** FastAPI (Chosen for simple, fast API creation with built-in data validation)
- **Server:** Uvicorn (ASGI web server)
- **Validation:** Pydantic

## Operating Environment
- **OS:** Windows (Primary testing is done via PowerShell. Always provide PowerShell-compatible commands like `Invoke-RestMethod` alongside `curl` when giving terminal instructions).
- **IDE:** VS Code / Cursor (Ensure the Python interpreter is pointed to the exact `python.exe` executable, not just the directory).

## Current Progress & State
- **Assignment 01 (Backend Basics):** Completed. Built a minimal FastAPI server with a `GET /health` and `POST /echo` endpoint. The code is heavily commented line-by-line for learning purposes.
- **Documentation:** 
  - Maintained a clear `README.md` for the assignment with specific setup and testing instructions.
  - Created a filtered `glossary_summary_ai_backend.md` extracting crucial General AI and Backend terms from the main internship glossary.
- **Git Practices:** Enforcing clean commits. A `.gitignore` is in place to prevent tracking of `__pycache__` and compiled Python bytecode. Only the `main` branch is kept active.

## AI Partner Instructions (Style & Preferences)
- **Keep it minimal:** Follow the program's philosophy of avoiding overthinking (e.g., building the smallest possible backend first).
- **Explain thoroughly:** When modifying or writing code, provide detailed explanations or line-by-line comments to explain exactly what each package and function does.
- **Cross-platform awareness:** Always account for Windows/PowerShell quirks (like the `curl` alias and JSON escaping) when providing terminal commands. 
- **Repository hygiene:** Never commit `.pyc` files, `__pycache__`, or sensitive API keys.
