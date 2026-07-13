# Glossary Summary: General AI & Backend Engineering

This document is a filtered summary of the main `glossary.pdf`, extracting only the crucial terms relevant to General AI fluency and Backend Engineering.

## General AI & Prompting

*   **Agent:** An AI that can take a few steps toward a goal on its own, not just answer once. It decides what to do based on the resources it has.
*   **AI model / "the brain":** The core intelligence (like Claude, ChatGPT, or Gemini) that has read vast amounts of data but has no memory of you. It thinks and writes only when asked.
*   **AI workspace / Context doc:** A saved space or single document holding your context (instructions, style, stack) so the AI remembers your specific project instead of starting cold every chat.
*   **Chatbot vs assistant vs model:** The *model* is the engine; the *chatbot* is the window you talk through; the *assistant* is the engine framed to help you get things done.
*   **Context / context window:** Everything the AI can "see" while answering (your instructions, files, the chat history). The window is how much information it can hold at once.
*   **Discernment:** The underrated skill of judging whether AI output is actually good, rather than just accepting whatever it generates.
*   **Few-shot / showing examples:** Giving the AI examples of the desired output so it copies the exact shape and format you want. Showing is often better than telling.
*   **Hallucination:** When the AI confidently states something wrong because it would rather invent an answer than admit ignorance. This is why human verification is required.
*   **Human in the loop:** The principle that you remain the author, judge, and owner of what ships. The AI drafts, but you decide.
*   **Iterating (on a prompt):** Refining your instructions and trying again. The first AI answer is a draft to react to, not a final verdict.
*   **Multimodal:** An AI capable of processing more than just text—it can look at images, read screenshots, and sometimes hear voice.
*   **Prompt & Prompt engineering:** The instructions you give the AI. Prompt engineering is the skill of giving clear, structured instructions (who the AI is, what you want, providing examples) to get better results.
*   **System prompt / custom instructions:** The standing setup given to the AI once so it behaves consistently in every reply (like a job description for a new hire).
*   **The four Ds:** A framework for working with AI: **D**elegation (what to hand over), **D**escription (asking clearly), **D**iscernment (judging results), and **D**iligence (checking and owning the work).
*   **Token:** The small chunks (roughly pieces of words) that the AI brain reads and writes in. Usage and cost are measured in tokens.

## Backend Engineering & Hosting

*   **API:** A doorway that allows software to communicate with other software (like a drive-through window where you place an order and get data back).
*   **API key:** A secret password allowing your build to use a service (like an AI model). It must be kept private and never pasted into public repos.
*   **Backend:** The part of the app that remembers data or performs complex logic a plain web page cannot (e.g., storing messages, capturing emails, running AI models).
*   **Database:** The brain's notebook. A place where a build writes things down so it remembers them across sessions (e.g., Supabase, Firebase).
*   **Deploy / publish:** Pushing your latest code version live so that it is accessible via a public URL.
*   **DNS:** The internet's address book that connects your human-readable domain name to the server where your site actually lives.
*   **Hosting / host:** The service (like GitHub Pages, Netlify, Vercel) that puts your site on the internet at a specific address.
*   **Repository (repo) / GitHub:** A structured folder that holds your project and tracks every version of it. GitHub is where this folder lives online.
