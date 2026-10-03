# chat-to-docx

[English](#english) | [简体中文](#简体中文)

## English

**Turn AI chat transcripts into Word documents with editable equations.**

Ever copied a formula from ChatGPT into Word, only to get raw LaTeX, broken fractions, or missing subscripts? Pasting equations as images makes even a small edit tedious. Tables and headings often need rebuilding too.

chat-to-docx converts Markdown chat records into DOCX, stores equations as native Word OMML, and preserves headings, lists, tables, and code blocks. It is useful for research derivations, course notes, and technical documentation.

### Usage

Download this repository into your agent's skills directory as `chat-to-docx`. The default Codex location is `~/.codex/skills/chat-to-docx/`.

Attach a Markdown file or paste the chat text, then ask:

```text
Use $chat-to-docx to convert this chat transcript into Word.
Preserve message order, headings, tables, lists, and code blocks.
Use editable OMML for inline and display equations.
```

The default is a full transcript conversion. Request "extract the latest draft only" when that is what you need.

### Match a reference document

Attach a reference Word document before or together with the transcript. The agent reads its formatting, summarizes the fonts, sizes, line spacing, indentation, page setup, headings, tables, and equation numbering, then uses that profile for the export. A reference supplied earlier stays active for later conversions. Without a reference, it uses an A4 layout with 11 pt body text and 1.25 line spacing.

```text
Use this DOCX as the formatting reference. Summarize its main formatting,
then convert the attached chat transcript using the same layout and editable OMML equations.
```

### Equations and layout

- Recognizes `$...$`, `$$...$$`, `\(...\)`, and `\[...\]` outside code blocks.
- Keeps inline equations in their sentences and display equations in separate paragraphs.
- Preserves fractions, scripts, integrals, sums, matrices, and cases.
- Uses native Word headings, lists, and tables.
- Checks `m:oMath` objects in the DOCX and inspects rendered pages.

The equations can be modified in the Word equation editor.

### Environment

This is an AI agent skill with conversion and audit helpers.

```bash
python -m pip install -r requirements.txt
```

Document assembly uses `python-docx`. The equation helper uses `lxml` and a local Office `MML2OMML.XSL` stylesheet to transform Presentation MathML into OMML. Source parsing and assembly are handled by the agent workflow. Obtain the Microsoft stylesheet from your local Office installation; it is not bundled here.

Use the host's `documents` skill or a local document renderer for page inspection. Check complex equations and rendering in your target office application.

```bash
python scripts/mathml_to_omml.py --self-test
python scripts/audit_docx.py final.docx --expect-equations 5 --json
```

### Example

[Signal processing and deep learning](examples/chat-with-equations.md) covers the discrete Fourier transform, continuous wavelet transform, input normalization, and cross-entropy loss. It includes five equations, a table, and a code block.

### Files

| File | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | Agent instructions |
| [Equation workflow](references/equation-workflow.md) | MathML to OMML |
| [Formatting profile](references/formatting-profile.md) | Reference formatting and export defaults |
| [Content extraction](references/extraction-and-cleanup.md) | Chat selection and Markdown cleanup |
| [mathml_to_omml.py](scripts/mathml_to_omml.py) | Equation conversion helper |
| [audit_docx.py](scripts/audit_docx.py) | Equation count and artifact checks |

---

## 简体中文

**把 AI 聊天记录转换成 Word，让公式保持可编辑。**

有没有遇到过：ChatGPT 里排版清楚的公式，复制到 Word 后变成一串 LaTeX 源码；分数、上下标和矩阵需要重新输入；公式粘成图片，想改一个变量也得重做？

chat-to-docx 将 Markdown 聊天记录整理为 DOCX，用 Word 原生 OMML 保存数学公式，同时保留标题、列表、表格和代码块。适合科研推导、课程笔记和技术文档整理。

AI chat and Markdown to Word DOCX with editable OMML equations.

## 使用

将仓库下载到支持 Agent Skills 的工具的技能目录，文件夹名为 `chat-to-docx`。Codex 默认目录为 `~/.codex/skills/chat-to-docx/`。

发送 Markdown 文件或粘贴聊天文本，然后使用：

```text
使用 $chat-to-docx，将这份聊天记录转换为 Word。
保留原文顺序、标题、表格、列表和代码块。
行内公式和独立公式使用可编辑的 OMML 格式。
```

默认完整转换。只需要最终正文时，可以指定“仅提取最新版”。

## 沿用参考文件格式

可以先发送一份参考 Word 文件，再发送聊天记录，也可以同时提供。技能会读取文件内容与版式，概述字体、字号、行距、缩进、页面设置、标题、表格和公式编号方式，然后按提取的格式生成 Word。之前提供的参考文件会继续用于后续转换；没有参考文件时，使用 A4、正文 11 pt、1.25 倍行距的默认版式。

```text
请将这份 DOCX 作为格式参考，先总结主要格式，
再按同样的版式把聊天记录转换为 Word，公式使用可编辑 OMML。
```

## 公式和排版

- 识别代码块之外的 `$...$`、`$$...$$`、`\(...\)` 和 `\[...\]`。
- 行内公式与正文同行，独立公式单独排版。
- 保留分数、上下标、积分、求和、矩阵和分段函数的数学结构。
- 使用 Word 标题、列表和表格，保留消息顺序与代码内容。
- 检查 DOCX 中的 `m:oMath` 公式对象，并渲染检查页面。

生成的公式可以在 Word 公式编辑器中继续修改。

## 环境

这是供 AI agent 使用的技能，附有公式转换与文档检查脚本。

```bash
python -m pip install -r requirements.txt
```

正文使用 `python-docx`；公式通过 `lxml` 和本机 Office 的 `MML2OMML.XSL` 将 Presentation MathML 转换为 OMML。脚本接收 MathML，Markdown 与 LaTeX 的解析由 agent 工作流处理。微软样式表需要从本机 Office 获取，仓库不包含该文件。

渲染可使用宿主的 `documents` 技能或本地文档工具。复杂公式和其他办公软件的显示效果应在目标环境中检查。

```bash
python scripts/mathml_to_omml.py --self-test
python scripts/audit_docx.py final.docx --expect-equations 5 --json
```

## 示例

[信号处理与深度学习](examples/chat-with-equations.md) 展示离散傅里叶变换、连续小波变换、输入归一化和交叉熵损失，包含 5 个公式，以及表格和代码块。

## 文件

| 文件 | 用途 |
|---|---|
| [SKILL.md](SKILL.md) | 技能入口 |
| [公式流程](references/equation-workflow.md) | MathML 到 OMML |
| [格式提取](references/formatting-profile.md) | 参考文件分析与默认版式 |
| [内容整理](references/extraction-and-cleanup.md) | 聊天提取与 Markdown 处理 |
| [mathml_to_omml.py](scripts/mathml_to_omml.py) | 公式转换辅助脚本 |
| [audit_docx.py](scripts/audit_docx.py) | 公式数量和文字残留检查 |


Related terms / 相关关键词: ChatGPT to Word · AI chat export · Markdown to DOCX · LaTeX to Word · editable equations · OMML · Agent Skills · AI 聊天记录转 Word · 公式复制乱码。
