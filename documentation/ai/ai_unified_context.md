# FlyRank AI Internship - Unified AI Context & Prompt State

## 1. Project Context & Guidelines

### About the Project
This repository (`flrank-backend-ai-internship`) contains assignments and documentation for the **Backend AI Engineering Track** of the FlyRank Internship. The goal is to build, test, and deploy backend services, starting from the smallest possible server up to more complex integrations.

### Tech Stack
- **Language:** Python 3 (Primary) & TypeScript (Secondary)
- **Framework:** FastAPI (Python) & NestJS (TypeScript)
- **Server:** Uvicorn (ASGI web server for Python)
- **Validation:** Pydantic (Python)

### Operating Environment
- **OS:** Windows (Primary testing is done via PowerShell. Always provide PowerShell-compatible commands like `Invoke-RestMethod` alongside `curl` when giving terminal instructions).
- **IDE:** VS Code / Cursor (Ensure the Python interpreter is pointed to the exact `python.exe` executable, not just the directory).

### AI Partner Instructions (Style & Preferences)
- **Keep it minimal:** Follow the program's philosophy of avoiding overthinking (e.g., building the smallest possible backend first).
- **Explain thoroughly:** When modifying or writing code, provide detailed explanations or line-by-line comments to explain exactly what each package and function does.
- **Cross-platform awareness:** Always account for Windows/PowerShell quirks (like the `curl` alias and JSON escaping) when providing terminal commands. 
- **Repository hygiene:** Never commit `.pyc` files, `__pycache__`, or sensitive API keys.
- **Language Requirements:** Always implement a TypeScript equivalent for all assignments alongside the Python version.
- **Package Manager:** Always use `pnpm` exclusively for Node.js/TypeScript projects (never `npm` or `yarn`).

---

## 2. Session Summary & Progress (July 13, 2026)

### Backend Basics (Assignment 01)
*   **Python/FastAPI:** Implemented the smallest possible backend with a `GET /health` and `POST /echo` endpoint. Configured a `requirements.txt` and `README.md` with testing instructions.
*   **TypeScript/NestJS:** Created an exact equivalent of the Python backend in a `typescript-version` subfolder. Built the entire NestJS app inside a single `main.ts` file (~25 lines). Fixed decorator compilation issues by properly configuring a `tsconfig.json`.

### Environment & Tooling
*   **IDE Setup:** Resolved a VS Code / Cursor issue where the IDE was pointing to a Python installation directory rather than the exact `python.exe` executable.
*   **Git Hygiene:** Configured `.gitignore` to prevent committing compiled Python files (`__pycache__`, `*.pyc`) and Node.js dependencies (`node_modules`, `package-lock.json`). 

### Documentation & Research
*   **Book Summaries:** Searched the web and generated thorough, chapter-by-chapter summaries of four foundational books inside `documentation/resources/books`:
    *   *Clean Code & Clean Architecture* (Robert C. Martin)
    *   *The Pragmatic Programmer* (Andrew Hunt & David Thomas)
    *   *Eloquent JavaScript* (Marijn Haverbeke)
    *   *Designing Data-Intensive Applications* (Martin Kleppmann)

### Testing & Verification
*   Verified both the Python (Port 8000) and TypeScript (Port 8001) backends locally.
*   Tested the endpoints via `curl` and PowerShell's `Invoke-RestMethod`.
*   Ran a browser agent to record a video navigating to both servers to visually confirm the `{"status":"ok"}` responses.
