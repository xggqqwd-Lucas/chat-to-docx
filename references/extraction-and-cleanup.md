# Extraction and cleanup

## Select content

For full-chat conversion, preserve every supplied message in source order, including speaker labels, headings, lists, tables, and code blocks. Do not select just one answer or remove repeated headings belonging to different messages. Interpret Markdown formatting into Word structures; remove delimiter syntax only after preserving the represented content.

### When the user explicitly requests the latest draft

Build a short decision log before editing:

1. Locate the last full manuscript block.
2. Apply later explicit corrections in chronological order.
3. Record frozen titles and phrases.
4. Exclude exploratory outlines and rejected variants.

## Clean chat-only artifacts

Remove or normalize:

- dynamic ChatGPT markers: `cite...`, `navlist...`;
- outer transport-only Markdown fences; preserve actual code-block contents, language labels, and transcript messages;
- duplicated headings only in latest-draft mode when they are extraction artifacts;
- replacement characters (`U+FFFD`, `�`);
- obvious UTF-8/GBK mojibake sequences.

Do not fabricate missing citations. If citation recovery is part of the request, use the dedicated citation-backtrace or citation-repair workflow instead of deleting source semantics.

## Repair terminology conservatively

Encoding corruption may create readable-looking but invalid domain words. Infer a correction only when the surrounding sentence and repeated usage make it unambiguous. Examples include replacing a corrupted form of “色度学” or “色域” only when the technical sentence clearly requires that term. If uncertain, preserve the source in notes and ask the user.

## Normalize equations

Separate each display equation from prose and represent it in structured form. Preserve:

- subscripts and superscripts;
- matrices and cases;
- integrals, sums, limits, and set-builder notation;
- bold vectors and calligraphic sets;
- equation punctuation when grammatically required.

Use ASCII punctuation in prose where renderer compatibility matters, but retain mathematical Unicode inside OMML when supported.

