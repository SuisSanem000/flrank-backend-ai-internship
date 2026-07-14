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
- **Explain thoroughly (Inline):** Do not put detailed code explanations in the README. Code explanation should *only* be above each line of code as a comment. 
- **README Documentation:** For each assignment, the README must contain a summarized yet detailed enough explanation of what the assignment is (based on our chat), the date it was implemented, and a direct link to it. Update the README of the assignment with this information derived directly from our chat interaction.
- **Cross-platform awareness:** Always account for Windows/PowerShell quirks (like the `curl` alias and JSON escaping) when providing terminal commands. 
- **Repository hygiene:** Never commit `.pyc` files, `__pycache__`, or sensitive API keys.
- **Language Requirements:** Always implement a TypeScript equivalent for all assignments alongside the Python version.
- **Package Manager:** Always use `pnpm` exclusively for Node.js/TypeScript projects (never `npm` or `yarn`).

---

## 2. Assignment Workflow & Completion Checklist

### 🚀 Start Assignment Prompt (How We Work)
1. **User Setup:** The user will always manually create the new assignment folder appropriately nested (e.g., inside `week 1`, `week 2`, etc.).
2. **Spec Delivery:** The user will manually add a `README.md` inside that new folder containing the precise assignment specifications.
3. **Kickoff:** The user will explicitly tell the AI in the chat which assignment to work on next. The AI should read the specs and begin implementation *only* after this kickoff.

### ✅ Assignment Completion Steps
- **Root Index Dashboard:** Upon completing each assignment, you MUST update the root `README.md` file. Add a new row to the markdown index table containing headers `| Assignment # | Topic | Description | Link |` for the newly completed assignment. Ensure the relative link accurately reflects the week nesting (e.g., `./assignments/week 1/02-ai-workflow-audit-and-tool-setup`).

---

## 3. Current Repository State

*   **Current Week:** Week 1
*   **Last Implemented Assignment:** `01-backend-basics` (Completed in Python and TypeScript)
*   **Week 1 Status:** **In Progress** (Week 1 has two pending assignments).
*   **AI State Checking Rule:** To independently verify if a week is finished, the AI should inspect the manually created assignment folders for that specific week. If a folder only contains the initial specification `README.md`, the assignment is pending. If it contains actual code/implementation files, it is completed.
