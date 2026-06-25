---
name: document-to-deck
description: Transform Word, PDF, TXT or Excel documents into structured, presentation-ready slide decks.
---

**Language:** Use `{communication_language}` for all output.

# Document-to-Deck Transformation

Transform raw documents (Word, PDF, TXT, Excel) into structured, professional presentations. This is never a copy-paste operation — it is a content synthesis, restructuring, and visual adaptation process.

## Activation

When the user provides a document to convert, follow this process:

### Step 1 — Source Analysis

Analyze the provided document and identify:

1. **Document type** — Report, proposal, analysis, manual, research, memo, data export
2. **Content structure** — How is the document organized? Headers, sections, narrative flow
3. **Core message** — What is the central thesis or purpose?
4. **Key data points** — Numbers, metrics, KPIs, comparisons
5. **Decision points** — Actions, recommendations, conclusions
6. **Audience fit** — Does the document's language match the target audience?

Present a brief assessment: "Here's what I found in your document and how I recommend structuring the presentation."

### Step 2 — Content Synthesis

Apply the Content Synthesis Protocol:

1. **Extract** — Identify the central message of each section
2. **Eliminate** — Remove redundancies, filler text, repeated information
3. **Reduce** — Transform paragraphs into presentable bullet points (8-12 words each)
4. **Classify** — Separate facts, data, conclusions, decisions, and actions
5. **Prioritize** — Highlight what truly matters for the audience
6. **Restructure** — Convert information into narrative flow

**Transformation rules:**
- A 1-page document section ≠ 1 slide (content dictates structure, not source pages)
- Long paragraphs → 2-3 key bullet points
- Data tables → Charts, KPI highlights, or summary tables
- Lists of items → Categorized groups with visual hierarchy
- Conclusions buried in text → Highlighted on dedicated slide
- Technical jargon → Audience-appropriate language

### Step 3 — Propose Deck Structure

Based on the synthesis, propose a complete slide outline:

```
Slide 1 — [Title]
Source: Section X of document
Transformation: [What was extracted and how it was adapted]

Slide 2 — [Title]
Source: Sections Y and Z (merged)
Transformation: [What was synthesized]
```

Show the mapping between document sections and proposed slides so the user can validate.

### Step 4 — Generate Slides

For each slide, use the standard format:

```
Slide X — Title
Message: [Core message extracted from document]
Bullets:
- [Synthesized point 1]
- [Synthesized point 2]
- [Synthesized point 3]
Visual Suggestion: [Chart from data, icon, layout]
Objective: [Role in the narrative]
Speaker Notes: [Additional context from the original document]
```

### Step 5 — Handle Data (Excel/Tables)

When the source includes data:

1. **Assess** — Is the data better as a chart, summary table, KPI card, or textual highlight?
2. **Recommend chart type** — Bar, line, pie, waterfall, combo — based on the data story
3. **Simplify** — Never put an entire Excel table on a slide
4. **Highlight** — Call out the key insight from the data as the slide headline
5. **Appendix** — Full data tables go in appendix slides, if needed at all

**Decision matrix for data visualization:**

| Data Type | Best Format |
|-----------|-------------|
| Trend over time | Line chart |
| Comparison between categories | Bar chart |
| Part of a whole | Pie/donut (max 5 segments) |
| Before/after | Side-by-side or waterfall |
| Single metric | KPI card with trend arrow |
| Complex multi-dimension | Summary table (max 5 rows × 5 columns) |

### Step 6 — Quality Validation

Before finalizing, verify:

- [ ] No raw text copied verbatim from source
- [ ] Every slide adds unique value (no redundant slides)
- [ ] Data transformed into visual insights, not raw tables
- [ ] Narrative flows independently from the source document
- [ ] Audience-appropriate language (source jargon removed/adapted)
- [ ] Speaker notes capture important context from the original
- [ ] Source coverage: all critical content represented
