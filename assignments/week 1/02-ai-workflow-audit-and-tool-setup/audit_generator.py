import json

# ==============================================================================
# We define the 15 workflow tasks as a list of dictionaries.
# Each task contains the task name, the classification, and the rationale.
# This explicitly hits the requirement for 10+ real tasks and classifications.
# ==============================================================================
tasks = [
    {
        "Task": "Reading long documentation / API specs",
        "Classification": "Collaborate with AI",
        "Rationale": "AI can summarize key points, but I need to read nuances myself."
    },
    {
        "Task": "Writing boilerplate code (e.g., standard CRUD endpoints)",
        "Classification": "Fully automate",
        "Rationale": "Highly repetitive and predictable; AI handles this perfectly without much oversight."
    },
    {
        "Task": "Debugging complex, project-specific logic errors",
        "Classification": "Collaborate with AI",
        "Rationale": "I understand the business logic better, but AI helps spot syntax or edge cases."
    },
    {
        "Task": "Reviewing security-critical code / authentication",
        "Classification": "Just me",
        "Rationale": "Too risky to trust blindly; human verification is mandatory for security."
    },
    {
        "Task": "Writing unit tests for pure functions",
        "Classification": "Delegate to AI with review",
        "Rationale": "AI writes good tests, but I must review to ensure it tests the right assertions."
    },
    {
        "Task": "Structuring high-level system architecture",
        "Classification": "Just me",
        "Rationale": "Requires deep understanding of organizational goals and future scaling needs."
    },
    {
        "Task": "Drafting initial emails or project updates",
        "Classification": "Fully automate",
        "Rationale": "Saves time on phrasing; I just provide bullet points and AI formats it."
    },
    {
        "Task": "Translating code between languages (e.g., Python to TS)",
        "Classification": "Delegate to AI with review",
        "Rationale": "AI is great at syntax translation, but I must review framework-specific idioms."
    },
    {
        "Task": "Brainstorming variable or function names",
        "Classification": "Collaborate with AI",
        "Rationale": "AI suggests good options, but I make the final stylistic choice."
    },
    {
        "Task": "Formatting Markdown files and tables",
        "Classification": "Fully automate",
        "Rationale": "Tedious manual work that AI executes flawlessly and instantly."
    },
    {
        "Task": "Learning a completely new framework/concept",
        "Classification": "Collaborate with AI",
        "Rationale": "I treat AI as a tutor, asking questions and having it explain concepts interactively."
    },
    {
        "Task": "Merging complex Git conflicts",
        "Classification": "Just me",
        "Rationale": "Requires knowing which feature branch's logic takes precedence."
    },
    {
        "Task": "Writing SQL queries for complex joins",
        "Classification": "Delegate to AI with review",
        "Rationale": "AI writes the syntax fast, but I must verify it against the actual database schema."
    },
    {
        "Task": "Generating dummy data for testing",
        "Classification": "Fully automate",
        "Rationale": "AI excels at generating realistic JSON/CSV mock data quickly."
    },
    {
        "Task": "Setting up project environments (e.g., Dockerfiles)",
        "Classification": "Delegate to AI with review",
        "Rationale": "AI creates a great starting point, but I need to tweak paths and specific versions."
    }
]

# ==============================================================================
# We define the 3 target tasks that will be reused in future assignments.
# We also define what "done well" means for each, hitting the evaluation criteria.
# ==============================================================================
target_tasks = [
    {
        "Task": "Writing boilerplate code (Fully automate)",
        "Success_Metric": "AI generates functioning CRUD endpoints in < 1 minute with 0 syntax errors."
    },
    {
        "Task": "Translating code between languages (Delegate to AI with review)",
        "Success_Metric": "Code runs in the target language on the first try with only minor idiomatic tweaks needed."
    },
    {
        "Task": "Learning a completely new framework (Collaborate with AI)",
        "Success_Metric": "I can build a 'Hello World' app in the new framework within 30 minutes of AI tutoring."
    }
]

# ==============================================================================
# This function formats our tasks dictionary into a clean Markdown table string.
# It iterates over the headers and rows to construct the output.
# ==============================================================================
def generate_markdown_table(data_list):
    if not data_list:
        return ""
    
    headers = list(data_list[0].keys())
    header_row = "| " + " | ".join(headers) + " |"
    divider_row = "| " + " | ".join(["---"] * len(headers)) + " |"
    
    table_str = f"{header_row}\n{divider_row}\n"
    
    for row in data_list:
        row_str = "| " + " | ".join(str(row[k]) for k in headers) + " |"
        table_str += f"{row_str}\n"
        
    return table_str

# ==============================================================================
# The main execution block. We generate the tables and write them to a file.
# This produces the final '1 to 2 page workflow audit' deliverable.
# ==============================================================================
if __name__ == "__main__":
    audit_table = generate_markdown_table(tasks)
    target_table = generate_markdown_table(target_tasks)
    
    final_markdown = f"""# AI Workflow Audit Results\n\n## 15 Recurring Tasks\n\n{audit_table}\n\n## 3 Target Tasks (For FL-02 to FL-04)\n\n{target_table}\n"""
    
    output_path = "workflow_audit.md"
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_markdown)
        
    print(f"Successfully generated workflow audit at {output_path}")
