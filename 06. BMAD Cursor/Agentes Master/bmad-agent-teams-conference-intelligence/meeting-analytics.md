# Meeting Analytics

## Purpose

Generate meeting analytics including participation, speech distribution, topics discussed, decisions made, open actions, sentiment analysis, risk identification and meeting trends.

## Process

1. **Identify analytics scope** — Ask the user:
   - What level of analytics? (individual meeting, team, department, organization)
   - What time period? (single meeting, weekly, monthly, quarterly)
   - What metrics matter most? (participation, productivity, decision tracking, compliance)
   - What audience? (team leads, executives, HR, compliance)
   - What data sources? (Teams native, Graph API, custom pipeline)

2. **Define analytics categories**:

   ### Meeting Efficiency Metrics
   - Total meeting time per period
   - Average meeting duration by type
   - Meeting frequency trends
   - Meetings that could have been an email (short, no decisions, no actions)
   - Meeting start/end punctuality

   ### Participation Analytics
   - Per-user participation rate
   - Speech distribution (who talks most/least)
   - Silent participants identification
   - Active vs passive participation
   - Camera on/off patterns (when available)
   - Join/leave time analysis

   ### Content Analytics
   - Topics discussed (extracted from transcript)
   - Topic frequency and trending
   - Decision density per meeting
   - Action item generation rate
   - Follow-up completion rate

   ### Decision & Action Tracking
   - Decisions made per meeting/period
   - Decision implementation status
   - Action items created vs completed
   - Overdue actions
   - Responsibility distribution

   ### Sentiment & Risk
   - General meeting sentiment (positive, neutral, negative)
   - Sentiment trends over time
   - Risk keywords and escalation patterns
   - Conflict indicators
   - Engagement level estimation

   ### Organizational Patterns
   - Cross-team meeting frequency
   - Meeting culture assessment
   - Meeting cost estimation (time × participants × hourly rate)
   - Recurring meeting ROI

3. **Design the analytics pipeline**:

   ### Data Collection
   - Graph API: call records, attendance reports, meeting metadata
   - Transcript processing: NLP for topics, decisions, actions, sentiment
   - Change notifications for real-time event capture

   ### Data Processing
   - Azure OpenAI for NLP analysis
   - Azure Functions for data transformation
   - Azure AI Search for temporal queries

   ### Data Storage
   - Cosmos DB for structured analytics data
   - Azure AI Search for semantic queries
   - Power BI dataset for visualization

   ### Visualization
   - Power BI dashboards
   - Teams Adaptive Cards for inline reports
   - Email digests for periodic summaries
   - SharePoint pages for team dashboards

4. **Deliver** with:
   - Metrics catalog with definitions
   - Data source mapping
   - Processing pipeline architecture
   - Dashboard mockup/specification
   - Licensing requirements
   - Privacy considerations (anonymization, consent)

## Key Rules

- Always consider privacy: participation analytics can be sensitive
- Distinguish what's available natively vs what requires custom processing
- Sentiment analysis requires Azure OpenAI — not available natively in Teams
- Per-user analytics must comply with local labor laws and privacy regulations
- Graph API call records have specific permission and consent requirements
- Meeting cost calculations require HR data integration (or estimated rates)
- Clearly separate real-time analytics from batch/historical analytics
