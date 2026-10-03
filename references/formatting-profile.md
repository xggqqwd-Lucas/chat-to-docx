# Reference document formatting

## Select a profile

Use a supplied reference file as the formatting source, including one supplied before the chat transcript. Read enough of its content to distinguish body text, heading levels, captions, lists, tables, code, and equation paragraphs. A formatting reference does not become transcript content. Keep it unchanged.

For an existing document edit, preserve its formatting unless the user selects another reference. Explicit user settings override the reference; use defaults only for roles or settings that the reference does not establish.

## Inspect and summarize

For DOCX, inspect sections, styles, paragraph properties, runs, tables, numbering, headers, footers, and math properties with python-docx and OOXML. Resolve direct formatting over paragraph/character styles, their basedOn chains, document defaults, and theme fonts. A missing direct property means inherited or unspecified, not zero.

Capture a reusable profile in working notes, with representative paragraph or style evidence:

| Role | Settings |
|---|---|
| Page | Size, orientation, margins, header/footer distances, columns, section changes |
| Body | Latin and East Asian fonts, size in pt, alignment, first-line/hanging indent, line spacing and its rule, space before/after, pagination controls |
| Headings | Role and level, font, size, weight, spacing, alignment, numbering, keep-with-next |
| Lists | Marker/number format, nesting, indent and hanging indent, spacing |
| Tables | Widths, alignment, borders, cell margins, header font/shading, row behavior |
| Equations | Inline/display placement, math font, spacing, numbering and alignment mechanism |
| Captions/code | Font, size, alignment, spacing, indentation |

Distinguish multiple line spacing from exact/at-least point spacing. Report explicit units; DOCX twips are 1/20 pt. Inspect w:rFonts for ascii/hAnsi/eastAsia and math settings separately. Include headers, footers, and page-number style when relevant without copying their unrelated text.

Summarize the main settings in the user's language before conversion. This is a brief format summary, not an approval gate. If the user asks only for analysis, return the summary and retain the profile for the later conversion.

Choose the dominant consistent formatting within each content role, not the most common run across the entire file. Record intentional section differences. If visually equivalent headings use different internal styles, map them to consistent native Heading styles. Identify incidental inconsistencies and state the normalization chosen; ask only when competing patterns materially affect the result.

For PDF or images, inspect visible typography and geometry and label inferred values as estimates. Do not claim exact line-spacing or font metadata from a screenshot.

## Apply the profile

Create a clean document using the extracted settings, or use a working copy of the reference as a template when this preserves required styles and section layout. Remove sample body content and unrelated headers, comments, and metadata from a new export. Preserve the reference itself.

Map source headings and content roles to the profile. Set Latin and East Asian fonts explicitly; apply paragraph spacing and indentation through styles where possible. Preserve bold/italic semantic emphasis. Use native OMML regardless of the reference's equation representation.

For numbered equations, reproduce the reference's layout, including tab stops or borderless tables. If it uses three columns, keep their relative widths within the available text width, center the equation, and right-align its number. Keep numbering only when present in the source or requested by the user.

Verify representative effective properties against the profile and render all pages. Check font substitution, equation clipping under exact line spacing, long tables, and page breaks. Adjust an individual equation row's height or spacing when required to show the full formula, and report material deviations.

## Default profile

Use this profile for new exports without a reference; choose installed font substitutes when necessary and mention a material substitution.

- A4 portrait; 2.54 cm margins; header/footer distances 1.27 cm.
- Body: Times New Roman for Latin text, SimSun for Chinese; 11 pt, justified, 1.25 multiple line spacing, 0 pt before and 6 pt after; no first-line indent.
- Heading 1/2/3: 16/14/12 pt, bold, left aligned; 12 pt before and 6 pt after; keep with next. Use the body language fonts.
- Lists: body font and spacing; native numbering, 0.63 cm increments per level with a 0.32 cm hanging indent.
- Tables: 10 pt text, single spacing, no first-line indent, fit to text width, repeating header row, simple borders.
- Math: Cambria Math; inline equations remain in prose; display equations centered with at least single spacing and 6 pt before/after. No automatic equation numbering.
- Captions: 10 pt, centered, single spacing, 6 pt before/after. Code: Consolas 9 pt, left aligned, single spacing, preserve whitespace.

These are export defaults, not a journal template. Preserve source hierarchy and content when selecting styles.
