# Assignment FL-01: AI Workflow Audit

## Original Assignment Specifications
https://internship.flyrank.ai/intern/assignments/FL-01

Details
Phase: Setup | Estimated hours: 4

Why it matters: You cannot improve a workflow you have never mapped. Knowing where AI helps, where it wastes your time, and where it should never be trusted is the core fluency skill; everything else builds on this audit.

Brief:
List 10 to 15 recurring tasks from your real week (study, work, side projects). Classify each: just me, delegate to AI with review, collaborate with AI, or fully automate. One line of rationale per task.
Set up your free toolkit: Claude, ChatGPT, and Anthropic Academy accounts. Enroll in AI Fluency: Framework & Foundations and complete at least the first module.
Create one Claude Project with custom instructions: who you are, tone preferences, current goals.
Pick the three audit tasks you will reuse in FL-02 through FL-04, and define what "done well" means for each.
Deliverable: A 1 to 2 page workflow audit (table format), a screenshot of your configured Claude Project, and your three target tasks with success definitions.

Evaluation criteria (pass/revise):
- 10+ tasks are genuinely yours, not generic examples
- Every task classified with a one-line rationale
- At least two tasks honestly marked "just me" with a reason
- Three target tasks are specific with measurable success definitions
- Tool accounts and Academy enrollment evidenced

---

## Assignment Summary (Derived from Specs)
**Topic:** AI Workflow Audit & Tool Setup (FL-01)
**Date Implemented:** July 14, 2026
**Implementation Link:** `./02-ai-workflow-audit-and-tool-setup`

**What we are doing:** We are mapping out 10 to 15 real-world recurring tasks (study, work, coding) and classifying how AI should be involved in them (Just Me, Delegate, Collaborate, Automate). We must pick 3 target tasks with measurable success metrics to reuse in future assignments. We also need to evidence that we have set up Claude, ChatGPT, and enrolled in the Anthropic Academy. 
*Note: Because our strict project rule dictates we must do all assignments in Python (with a TypeScript equivalent), we will write a script that generates this audit table and the target tasks programmatically.*

---

## Step-by-Step Implementation Guide
*(To be updated as implementation progresses)*

**Step 1:** Create `audit_generator.py` to programmatically define the 15 tasks, their classifications, and rationales, and output them as a formatted Markdown table.
**Step 2:** Define the 3 target tasks with "done well" metrics inside the script.
**Step 3:** Implement the TypeScript equivalent (`auditGenerator.ts`) inside a `typescript-version` subfolder using `pnpm`.
**Step 4:** Execute the scripts to generate the final 1-to-2 page workflow audit.
**Step 5:** Note on Tool Setup: Setting up Claude, ChatGPT, and Anthropic Academy accounts is a manual user task. (I will request the user to provide screenshots of these to satisfy the deliverable).
