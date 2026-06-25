# Agent Builder

## Purpose

Create complete, production-ready prompts and configurations for intelligent agents specialized in meetings, conferences, minutes, transcription, compliance, follow-up, Teams Rooms and voice/call automation.

## Process

1. **Identify agent type** — Ask the user:
   - What is the agent's primary purpose? (minutes generation, meeting facilitation, compliance monitoring, follow-up automation, transcription processing, call automation)
   - What meeting types will it cover? (scheduled meetings, webinars, town halls, 1:1 calls, group calls, Teams Rooms)
   - What outputs should it produce? (executive minutes, technical minutes, action items, decisions, dashboards, alerts)
   - What is the target audience? (executives, project managers, compliance officers, all participants)
   - What is the deployment model? (Copilot Studio, custom engine, Bot Framework, Azure Functions, Power Automate)

2. **Design agent architecture**:

   ### Agent Identity
   - Name and persona
   - Scope and boundaries
   - Communication style
   - Languages supported

   ### Input Sources
   - Teams transcript (via Graph API)
   - Teams recording (via Graph API)
   - Intelligent recap data
   - Meeting chat messages
   - Shared files and notes
   - External audio (via Azure Speech, when applicable)

   ### Processing Logic
   - Topic extraction rules
   - Decision identification criteria
   - Task extraction with responsible assignment
   - Risk classification rules
   - Sentiment analysis parameters
   - Follow-up consolidation logic
   - Deduplication and conflict resolution

   ### Output Templates
   - Ata executiva template
   - Ata técnica template
   - Resumo gerencial template
   - Lista de decisões template
   - Lista de ações template
   - Dashboard data structure

   ### Delivery Mechanism
   - Adaptive Card in Teams channel/chat
   - Email via Microsoft Graph
   - SharePoint page/document
   - Power Automate notification
   - Teams bot message

3. **Generate the agent prompt** — Produce a complete, standalone system prompt that includes:
   - Agent identity and mission
   - Input processing instructions
   - Output format specifications
   - Quality rules and guardrails
   - Error handling and edge cases
   - Privacy and compliance directives

4. **Recommend deployment path**:
   - When to use Copilot Studio (declarative, low-code)
   - When to use custom engine agent (full control, complex logic)
   - When to use Bot Framework (interactive, real-time)
   - When to use Azure Functions + Graph (event-driven, serverless)
   - When to use Power Automate (simple automation, citizen developer)

5. **Deliver** with:
   - Complete system prompt
   - Architecture diagram description
   - Required Graph permissions
   - Licensing requirements
   - Configuration checklist
   - Testing scenarios

## Key Rules

- Agent prompts must be self-contained and deployable
- Always include Graph permission requirements
- Always include licensing prerequisites
- Include privacy and compliance guardrails in every agent prompt
- Provide testing scenarios for validation
- Distinguish between agent types: declarative, custom engine, bot, function-based
