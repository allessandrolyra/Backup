---
name: copilot-m365-guidance
description: Guide usage of Copilot in PowerPoint, Designer, Slide Master, templates and M365 features.
---

**Language:** Use `{communication_language}` for all output.

# Copilot & Microsoft 365 PowerPoint Guidance

Guide users on leveraging Microsoft 365 features, Copilot in PowerPoint, Designer, Slide Master, templates, and integrations to maximize productivity and quality.

## Activation

When the user asks about PowerPoint features, Copilot, or M365 tools, identify the topic and provide comprehensive guidance.

### Copilot in PowerPoint

**What Copilot Can Do:**
- Create a presentation from a prompt describing the topic
- Create a presentation from a Word document or PDF
- Add slides based on text prompts
- Summarize the presentation
- Organize the presentation structure
- Generate speaker notes
- Suggest design improvements

**How to Use Effectively:**

1. **Creating from Prompt:**
   - Provide clear, specific instructions (topic, audience, slide count, style)
   - Better prompt: "Create a 10-slide executive presentation about Q3 sales results for the board of directors, focusing on revenue growth, market expansion, and strategic priorities"
   - Worse prompt: "Make a presentation about sales"

2. **Creating from Document:**
   - Upload a Word document or PDF
   - Copilot extracts key content and structures slides
   - Always review and refine — Copilot may miss nuance or create verbose slides
   - Best results: well-structured source documents with clear headings

3. **Adding/Editing Slides:**
   - "Add a slide about market competition with a comparison table"
   - "Rewrite this slide to be more concise"
   - "Add speaker notes for slides 3-7"

**Copilot Limitations (Critical to Communicate):**
- Requires Microsoft 365 Copilot license (paid add-on)
- Quality depends heavily on prompt quality and source document structure
- May generate generic or verbose content — human review always required
- Does not access real-time external data unless connected
- Design suggestions are basic — manual refinement usually needed
- Cannot perfectly replicate complex corporate templates
- Output language quality varies — verify terminology and tone

### Designer / Design Suggestions

**What Designer Does:**
- Automatically suggests layout improvements for the current slide
- Recommends icon, image, and layout combinations
- Applies professional design patterns to your content

**How to Use:**
1. Enter content on a slide (text, images)
2. Designer panel opens automatically (or via Design tab → Designer)
3. Browse suggested layouts and click to apply
4. Works best with 1-3 bullet points and/or one image

**Designer Limitations:**
- Requires Microsoft 365 subscription (not available in all plans)
- Must be online and connected
- Suggestions are based on generic patterns, not your brand guidelines
- Does not work well with complex, multi-element slides
- Requires content on the slide first — cannot design from empty slides
- Quality varies by content type and complexity

### Slide Master & Layouts

**When to Use Slide Master:**
- Establishing consistent branding across all slides
- Defining reusable layouts for the organization
- Setting default fonts, colors, logos, and footer elements
- Creating organizational templates

**Key Operations:**
1. **Access:** View tab → Slide Master
2. **Master slide** (top) — Changes here affect ALL layouts
3. **Layout slides** — Individual templates for different content types
4. **Placeholders** — Define where titles, content, images, footers go
5. **Close Master View** when done to return to normal editing

**Best Practices:**
- Set brand fonts and colors at the Master level
- Create 5-8 purpose-specific layouts (title, content, two-column, chart, image, section divider, closing)
- Place logo and footer on the Master — it inherits to all layouts
- Use placeholders, not free-form text boxes, for consistent positioning
- Test all layouts with real content before distributing

### Templates

**Organizational Templates:**
- Stored in SharePoint or OneDrive for Business (with M365)
- Accessible via File → New → Organization or Shared tabs
- Ensure IT/design team maintains the template library
- Templates should include all standard layouts via Slide Master

**Creating a Custom Template (.potx):**
1. Design the Slide Master with all layouts
2. Set theme colors and fonts
3. Add placeholder content
4. Save as PowerPoint Template (.potx)
5. Distribute via SharePoint, OneDrive, or network share

### Word to PowerPoint Integration

**Native Feature:**
1. Open Word document with heading structure (Heading 1, Heading 2, etc.)
2. In Word: File → Export → Export to PowerPoint
3. Select a design theme
4. PowerPoint generates slides based on heading structure

**Tips for Best Results:**
- Structure the Word document with clear heading hierarchy
- Heading 1 → New slide titles
- Heading 2 → Bullet points or subheadings
- Keep paragraphs concise — long text blocks become dense slides
- Review and refine the generated presentation

**Limitations:**
- Requires Microsoft 365 web (not available in desktop app natively for all versions)
- Results are a starting point — always needs manual refinement
- Complex formatting, tables, and images may not transfer cleanly

### Excel to PowerPoint Integration

**Linking Charts:**
1. Create chart in Excel
2. Copy chart
3. In PowerPoint: Paste Special → Paste Link (keeps live connection to Excel data)
4. Chart updates when Excel data changes (with link maintenance)

**Embedding Data:**
1. Copy Excel range or chart
2. In PowerPoint: Paste (embeds static copy)
3. Double-click embedded object to edit in Excel interface within PowerPoint

**Best Practices:**
- Linked charts: use when data updates frequently
- Embedded charts: use when presentation must be self-contained
- Always simplify charts for presentation context (fewer data points, larger labels)
- Never paste full spreadsheets — summarize for the audience

### Feature Availability Matrix

| Feature | PowerPoint Desktop | PowerPoint Web | Requires M365 | Requires Copilot License |
|---------|-------------------|----------------|---------------|--------------------------|
| Slide Master | Yes | Limited | No | No |
| Designer | Yes | Yes | Yes | No |
| Copilot | Yes | Yes | Yes | Yes |
| Word Export to PPT | No | Yes | Yes | No |
| Linked Excel Charts | Yes | Limited | No | No |
| Org Templates (SharePoint) | Yes | Yes | Yes | No |
| Accessibility Checker | Yes | Yes | No | No |
| Recording/Rehearse | Yes | Limited | No | No |

Always verify the user's specific environment and licensing before recommending features that require subscriptions or add-ons.
