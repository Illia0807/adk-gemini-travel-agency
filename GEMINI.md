# Building the Workshop with Gemini CLI

This workshop was built by Riccardo Carlesso with the help of [Gemini CLI](https://github.com/google-gemini/gemini-cli).

The original planning and technical notes used during the creation process have been moved to `docs/workshop-creation/GEMINI.md`.

## How Gemini CLI helped

Throughout the development of this repository, Gemini CLI acted as an AI pair programmer to:

- Draft the initial codebase for the different steps (from `step01_basic` to `step05_mcp2_nanobanana`).
- Set up the project configuration and structure the steps.
- Write and iterate on the `WORKSHOP.md` guidelines.
- Autonomously refactor code, manage imports, and update references when the repository structure evolved from `ai-friendly-agents` to the new dedicated `adk-gemini-cli-workshop` repo.
- Assist in resolving difficult bugs and integrating new ADK tools and MCP servers by reading the ADK documentation.

## Repository Migration

This codelab was migrated from the `ai-friendly-agents` repository to a standalone repository. Currently, you are viewing the code in `adk-gemini-cli-workshop`. If you are looking for specific solutions, features, or complex setups that are missing here, feel free to explore the original [ai-friendly-agents repository](https://github.com/palladius/ai-friendly-agents/tree/main/adk/workshops/simple-travel-agent) and check for solutions in there. Some branches in the old repo carry additional goodies too!

## How you can use Gemini CLI

If you are a workshop attendee, you can use Gemini CLI exactly as we did to implement the Milestone 2 ideas (vibe coding)!

Gemini can read the provided ADK documentation provided in the `rag/` folder and help you write new steps, deploy to Cloud Run or Vertex AI Agent Engine, or add any feature you want. Check out the Ideas in `WORKSHOP.md`!
