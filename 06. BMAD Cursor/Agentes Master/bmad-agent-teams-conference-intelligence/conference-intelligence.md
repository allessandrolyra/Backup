# Conference Intelligence

## Purpose

Respond about meeting intelligence: transcription, recap, notes, minutes, summaries, action items, facilitator, follow-up and compliance for meetings and conferences.

## Process

1. **Gather context** — Ask the user:
   - What type of meeting? (scheduled, ad hoc, webinar, town hall, Teams Room, 1:1 call, group call)
   - What outputs are needed? (transcript, recap, minutes, action items, decisions, follow-up, analytics)
   - Is the tenant licensed for Teams Premium? Microsoft 365 Copilot?
   - Are there compliance or retention requirements?
   - Is the audio from Teams native or an external source?

2. **Analyze meeting intelligence capabilities**:

   ### Native Teams Capabilities
   - Meeting recording (storage: OneDrive/SharePoint)
   - Meeting transcription (live captions, post-meeting transcript)
   - Intelligent recap (Teams Premium/Copilot)
   - Meeting notes
   - AI-generated action items and follow-up
   - Facilitator (when available)

   ### Transcription Source Priority
   Apply the Transcription Source Rule:
   1. Native Teams transcript (preferred)
   2. Recap / Intelligent recap
   3. Graph APIs for transcripts and recordings
   4. Azure Speech for external audio (only when native is insufficient)

   ### Processing Pipeline
   - Topic extraction from transcript
   - Decision identification and classification
   - Task/action item extraction with responsible parties
   - Risk and pending item classification
   - Sentiment analysis
   - Follow-up consolidation
   - Meeting memory organization for RAG

   ### Output Formats
   - Executive minutes (high-level summary for leadership)
   - Technical minutes (detailed with decisions, tasks, dependencies)
   - Management summary (risks, blockers, next steps)
   - Decision list (numbered, with context and responsible)
   - Action list (task, owner, deadline, status)
   - Meeting dashboard (participation, topics, duration, sentiment)

3. **Apply Facilitator vs Copilot Rule** — When relevant:
   - Facilitator: visible to all participants, acts in meeting context
   - Copilot: private to the user, personal assistant in meeting
   - Different licensing, behavior, visibility and privacy models

4. **Apply Data Storage & Retention Rule** — Always explain:
   - Where transcripts, recordings, recap, notes and tasks are stored
   - How retention policies affect these artifacts
   - How compliance policies impact access, deletion and discovery
   - Which data is used by recap, AI notes and tasks
   - Storage locations: OneDrive, SharePoint, Exchange

5. **Deliver response** using Conference Agent Framework:
   - Inputs → Processing → Outputs
   - Licensing requirements
   - Policy configuration
   - Privacy and compliance considerations

## Key Rules

- Never treat transcript, recap, recording, notes and tasks as equivalent
- Always specify where each artifact is stored
- Apply Licensing Truth Rule for every capability
- Consider compliance and privacy for all meeting data
- Prefer native Teams capabilities before suggesting custom solutions
