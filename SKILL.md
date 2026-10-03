---
name: chat-to-docx
description: Convert AI chat transcripts and Markdown into Word DOCX with editable native OMML equations, preserving headings, lists, tables, code blocks, and message order. Use for ChatGPT-to-Word exports, Markdown-to-DOCX conversion, and equation-rich chat records.
---

# Chat to DOCX

Convert user-supplied chat text or Markdown into a structured Word document with editable equations. See [README.md](README.md) for installation and dependencies.

Use the host's `documents` skill when available for document creation, rendering, and page inspection. Otherwise use equivalent local tools.

## Content selection

- Convert the complete supplied transcript in source order by default. Preserve speaker labels, message boundaries, headings, lists, tables, links, and code blocks.
- Extract the latest draft only when requested. Select the last complete draft and apply subsequent explicit corrections in order.
- Preserve finalized headings and terminology. Inspect an existing DOCX before changing its content, styles, tables, sections, or comments.
- Follow [references/extraction-and-cleanup.md](references/extraction-and-cleanup.md) for source cleanup.

## Document assembly

1. Build native Word headings, lists, and tables with `python-docx` or an equivalent tool. Keep source text in UTF-8 and set fonts for the source languages.
2. Recognize `$...$`, `$$...$$`, `\(...\)`, and `\[...\]` outside code blocks. Preserve formula strings inside code as code.
3. Convert mathematical expressions to Presentation MathML, then transform them into OMML using the local Office `MML2OMML.XSL` stylesheet. See [references/equation-workflow.md](references/equation-workflow.md) and [scripts/mathml_to_omml.py](scripts/mathml_to_omml.py).
4. Place inline `m:oMath` objects within prose paragraphs and display equations in separate centered paragraphs. Preserve fractions, scripts, integrals, sums, matrices, cases, and aligned derivations.
5. Normalize chat citation markers when their original sources are available. Repair encoding damage only when the intended text is clear from context.

## Verification

Save a working copy and check the native equation count:

```bash
python scripts/audit_docx.py final.docx --expect-equations 5 --json
```

Compare formulas and text against the source, then render and inspect every page for missing glyphs, clipped content, equation layout, tables, and pagination. Review audit findings in context: a literal LaTeX example in a preserved code block is valid source content.

A completed document should contain the expected `m:oMath` objects, all requested content, and no accidental chat artifacts or unconverted formulas in prose. Report any incomplete conversion or rendering check with the delivered file.

## Open documents

For a locked Word or WPS file, first build and verify a separate copy. Update the active document only when the user requested that path, matching its full path and preserving unsaved work. If the application cannot be updated safely, deliver the separate copy. Recheck a document after the application saves it.
