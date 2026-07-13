# AI Prompt State & Session Summary

## Date: July 13, 2026
**Project:** FlyRank AI Internship - Backend Engineering Track

### 1. Backend Basics (Assignment 01)
*   **Python/FastAPI:** We implemented the smallest possible backend with a `GET /health` and `POST /echo` endpoint. We configured a `requirements.txt` and `README.md` with testing instructions.
*   **TypeScript/NestJS:** We created an exact equivalent of the Python backend in a `typescript-version` subfolder. To maintain a minimal footprint, we built the entire NestJS app inside a single `main.ts` file (~25 lines). We fixed decorator compilation issues by properly configuring a `tsconfig.json`.

### 2. Environment & Tooling
*   **IDE Setup:** Resolved a VS Code / Cursor issue where the IDE was pointing to a Python installation directory rather than the exact `python.exe` executable.
*   **Git Hygiene:** Configured `.gitignore` to prevent committing compiled Python files (`__pycache__`, `*.pyc`) and Node.js dependencies (`node_modules`, `package-lock.json`). Removed the `node_modules` folder from Git.
*   **Package Management:** Established a strict rule to *always* use `pnpm` for Node.js environments.

### 3. Documentation & Research
*   **Project Context:** Created a `project_context.md` file to feed to AIs in the future. It contains rules about maintaining line-by-line comments, using PowerShell commands for Windows, building TS equivalents, and exclusively using `pnpm`.
*   **Book Summaries:** Searched the web and generated thorough, chapter-by-chapter summaries of four foundational books:
    *   *Clean Code & Clean Architecture* (Robert C. Martin)
    *   *The Pragmatic Programmer* (Andrew Hunt & David Thomas)
    *   *Eloquent JavaScript* (Marijn Haverbeke)
    *   *Designing Data-Intensive Applications* (Martin Kleppmann)
*   **LinkedIn Post:** Drafted a short, professional LinkedIn post summarizing Day 1 accomplishments to share progress online.

### 4. Testing & Verification
*   We verified both the Python (Port 8000) and TypeScript (Port 8001) backends locally.
*   We tested the endpoints via `curl` and PowerShell's `Invoke-RestMethod`.
*   We ran a browser agent to record a video navigating to both servers to visually confirm the `{"status":"ok"}` responses.
