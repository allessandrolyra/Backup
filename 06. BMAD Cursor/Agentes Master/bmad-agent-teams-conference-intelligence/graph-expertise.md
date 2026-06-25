# Microsoft Graph Expertise

## Purpose

Deep Microsoft Graph expertise focused on Meeting APIs, transcripts, recordings, call records, permissions, webhooks and change notifications for Teams conference intelligence.

## Process

1. **Identify Graph need** — Ask the user:
   - What data do you need? (transcripts, recordings, call records, meeting metadata, attendance, chat messages)
   - Is it real-time or batch? (webhooks/change notifications vs. scheduled polling)
   - Is it delegated (user context) or application (daemon/service)?
   - What is the consumption pattern? (one-time extraction, continuous monitoring, event-driven processing)

2. **Provide Graph API guidance**:

   ### Online Meetings API
   - Create, update, retrieve online meetings
   - `POST /users/{id}/onlineMeetings`
   - `GET /users/{id}/onlineMeetings/{id}`
   - Permissions: `OnlineMeetings.ReadWrite`, `OnlineMeetings.Read.All`

   ### Meeting Transcripts API
   - Retrieve meeting transcripts
   - `GET /users/{id}/onlineMeetings/{id}/transcripts`
   - `GET /users/{id}/onlineMeetings/{id}/transcripts/{id}/content`
   - Permissions: `OnlineMeetingTranscript.Read.All`
   - Content format: text/vtt, application/vnd.openxmlformats-officedocument.wordprocessingml.document

   ### Meeting Recordings API
   - Retrieve meeting recordings
   - `GET /users/{id}/onlineMeetings/{id}/recordings`
   - `GET /users/{id}/onlineMeetings/{id}/recordings/{id}/content`
   - Permissions: `OnlineMeetingRecording.Read.All`

   ### Call Records API
   - Retrieve call records and sessions
   - `GET /communications/callRecords/{id}`
   - `GET /communications/callRecords/{id}/sessions`
   - Permissions: `CallRecords.Read.All`

   ### Change Notifications (Webhooks)
   - Subscribe to meeting events
   - `POST /subscriptions` with resource paths for meetings, call records
   - Notification types: created, updated, deleted
   - Lifecycle notifications for subscription management
   - Encryption for notification content

   ### Attendance Reports
   - `GET /users/{id}/onlineMeetings/{id}/attendanceReports`
   - Participant details, join/leave times, duration

3. **Apply Graph Access Rule** — For each API:
   - Required permissions (delegated and application)
   - Admin consent requirements
   - Security impact assessment
   - Metered API identification and cost implications
   - Rate limiting and throttling (429 handling)
   - Pagination (nextLink, deltaLink)
   - Batch requests for efficiency

4. **Provide implementation patterns**:
   - Authentication: MSAL, certificate-based, managed identity
   - SDK: Microsoft Graph SDK (.NET, JavaScript, Python)
   - Direct HTTP: when SDK doesn't cover the scenario
   - Retry logic: exponential backoff for 429/503
   - Delta queries for incremental sync

5. **Deliver** with:
   - Exact API endpoints
   - Permission matrix
   - Request/response examples
   - Error handling patterns
   - Rate limit considerations
   - Security recommendations

## Key Rules

- Never assume access to transcripts or recordings without proper permissions and consent
- Always distinguish delegated vs application permissions
- Always flag metered APIs that may incur additional cost
- Provide exact permission scope names, not generic descriptions
- Include pagination handling for list operations
- Include error handling for common failure scenarios (404, 403, 429)
- Reference official Graph documentation for each endpoint
