# Word equation workflow

## Preferred path

1. Express the equation as Presentation MathML.
2. Locate `MML2OMML.XSL`, commonly at:
   `C:\Program Files\Microsoft Office\root\Office16\MML2OMML.XSL`.
3. Transform MathML to OMML with `lxml.etree.XSLT`.
4. Append the generated `m:oMath` node to a centered Word paragraph.
5. Save and inspect `word/document.xml`.

Import helpers from `scripts/mathml_to_omml.py`:

```python
from mathml_to_omml import find_mml2omml, append_display_equation

xsl = find_mml2omml()
append_display_equation(paragraph, mathml_string, xsl_path=xsl)
```

## Fallbacks

- If Microsoft Office's stylesheet is absent, search the installed Office/WPS paths before considering another converter.
- Do not downgrade an equation to an image.
- Do not paste raw LaTeX as visible manuscript text.
- If no reliable converter exists, stop and report the dependency instead of claiming the formula is editable.

## Structural check

An editable equation must appear as `m:oMath` in `word/document.xml`. `m:oMathPara` is a display wrapper and should not be counted as a second equation.

