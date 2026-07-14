# FlyRank AI Internship - AI Context & Assignment Rules

## 1. Project Context & Environment
- **Project:** flrank-backend-ai-internship (Backend AI Engineering Track).
- **Tech Stack:** Python 3 (FastAPI, Uvicorn, Pydantic) & TypeScript (NestJS).
- **Environment:** Windows / PowerShell / VS Code. Always use PowerShell-compatible commands (e.g., `Invoke-RestMethod`).
- **Package Manager:** Exclusively use `pnpm` for Node.js/TypeScript projects.
- **Hygiene:** Do not commit `.pyc`, `__pycache__`, or sensitive keys.

## 2. How to Implement Tasks (Strict Rules)
When instructed to start an assignment, you MUST follow these exact rules for implementation:
1. **Language:** Always implement all assignments in Python, AND also provide a TypeScript equivalent.
2. **Inline Code Comments:** Do NOT put code explanations in the README. Instead, explain the code by adding comments directly above each line of code in the actual source files.
3. **General README Explanation:** You must update the specific assignment's `README.md` to include:
    - **Do Not Delete Original Text:** You MUST preserve the exact initial text/specs the user pasted into the README. Do not remove it.
    - **Summarization:** Add a summarized, yet detailed enough explanation of what the assignment is (derived directly from the initial state of the README). This should be placed *below* the original text.
    - **Implementation Guide:** 
    - Add a step-by-step general guide and explanation of what you actually did, placed *below* the summary.
    - The date it was implemented.
    - A direct link to the implementation files.

## 3. Assignment Workflow (Start to Finish)

### Start Assignment Prompt (How We Begin)
- **User Setup:** The user will manually create a folder for the week (e.g., `week 1`), manually create the assignment folder inside it, and manually add the specification `README.md`.
- **Kickoff:** The AI will NOT start working until the user explicitly tells the AI which assignment to work on in the chat. 
- **Checking State:** The AI can tell if an assignment is pending if the folder only contains the spec README. If it contains actual code implementations, it is already completed.

### How to Actually Do Assignments
- **Receive Folder:** The user gives the name of the folder of the assignment.
- **Initial Setup:** You go read the `README.md` inside that folder. The summary of the assignment must be derived from this initial state of the README. **DO NOT remove the original text.** Keep it exactly the way the user saved it. Update the README by appending the summarized yet detailed enough explanation (and technical requirements) *below* the original text. Ensure you keep the original link to the assignment intact.
- **Implementation & Self-Review:** Start implementing the task. Update the README along the way, step-by-step, with everything you are doing.
- **Rule of 3 Checks:** Review each step you do 3 times. Judge if everything you are doing is correct and in perfect harmony with the whole project and the task itself.
- **Do Not Guess:** If anything is unclear after your review, you must ask follow-up questions. Do not just guess.

### Assignment Completion Steps (How We Finish)
- **Root Index Dashboard:** Every time the AI finishes an assignment, it MUST update the root `README.md` file. The AI must add a new row to the markdown table with headers `| Assignment # | Topic | Description | Link |`. 
- **Folder Nesting:** Ensure the link in the index table correctly points to the nested week folder (e.g., `./assignments/week 1/02-ai-workflow-audit-and-tool-setup`).

## 4. Current State
- **Current Progress:** We are in Week 1. 
- **Completed:** Assignment `01-backend-basics`.
- **Up Next:** Week 1 has pending assignments to be started upon the user's explicit command.
