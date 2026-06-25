# Copilot & Agents

## Purpose

Guide on Microsoft 365 Copilot, Copilot Studio, declarative agents, custom engine agents, Microsoft 365 Agents SDK, plugins, connectors and extensibility for conference intelligence scenarios.

## Process

1. **Identify the need** — Ask the user:
   - What do you want the agent/copilot to do? (generate minutes, facilitate meetings, automate follow-up, answer meeting questions, compliance monitoring)
   - Who will use it? (end users in meetings, administrators, compliance officers, executives)
   - What is the deployment target? (in-meeting experience, post-meeting automation, Teams channel bot, personal assistant)
   - What level of customization? (low-code, pro-code, hybrid)
   - What data sources? (Teams transcripts, recordings, SharePoint, external systems)

2. **Recommend the right approach**:

   ### When to Use Microsoft 365 Copilot (Native)
   - Meeting recap and intelligent summary (Teams Premium / Copilot license)
   - In-meeting Copilot for personal assistance
   - Post-meeting catch-up and action review
   - **Licensing:** Microsoft 365 Copilot license per user
   - **Customization:** Limited to Copilot's built-in capabilities

   ### When to Use Copilot Studio (Low-Code)
   - Declarative agents with custom instructions and knowledge
   - Agents that answer questions about meeting history using RAG
   - Simple automation triggered by meeting events
   - Integration with Power Platform connectors
   - **Licensing:** Copilot Studio license
   - **Customization:** Moderate — custom prompts, knowledge sources, actions

   ### When to Use Declarative Agents
   - Extend Copilot with specific meeting intelligence capabilities
   - Custom instructions for meeting analysis
   - Additional knowledge sources (SharePoint, Graph connectors)
   - Plugin actions for external integrations
   - **Deployment:** Via Microsoft 365 admin center or Teams app

   ### When to Use Custom Engine Agents
   - Full control over AI model and processing logic
   - Complex NLP pipelines (topic extraction, sentiment, multi-language)
   - Custom data models and storage
   - Integration with non-Microsoft AI services
   - **Technology:** Azure OpenAI + Bot Framework / Azure Functions
   - **Licensing:** Azure consumption + Teams platform

   ### When to Use Microsoft 365 Agents SDK
   - Programmatic agent creation and management
   - CI/CD integration for agent lifecycle
   - Multi-tenant agent deployment
   - Advanced orchestration patterns

   ### When to Use Microsoft 365 Agents Toolkit
   - Development and debugging of Teams agents
   - Local testing with Teams client
   - Scaffolding and project templates
   - Deployment to Azure and Teams

3. **Design the solution**:
   - Agent identity and scope
   - Knowledge sources and grounding
   - Actions and plugins
   - Graph connector configuration
   - Authentication and permissions
   - Deployment and distribution

4. **Apply Facilitator vs Copilot Rule**:
   - Facilitator: visible to all, acts in meeting context, assists the group
   - Copilot: private to user, personal assistant, individual productivity
   - Different licensing models
   - Different privacy implications
   - Never treat as equivalent or interchangeable

5. **Deliver** with:
   - Recommended approach with justification
   - Architecture overview
   - Licensing requirements
   - Implementation steps
   - Configuration guide
   - Testing approach

## Key Rules

- Always explain the decision tree: when to use each approach
- Never recommend Copilot features without validating Copilot licensing
- Distinguish Copilot in-meeting experience from post-meeting capabilities
- Declarative agents extend Copilot; custom engine agents are independent
- Always consider data privacy when agents access meeting content
- Copilot Studio agents and custom engine agents have different capability boundaries
