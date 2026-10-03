# chat-to-docx｜AI 聊天记录转 Word，让公式真正可编辑

**有没有遇见这样的烦恼？**

AI 生成的推导，聊天窗口里看起来很漂亮，一复制到 Word，公式却乱码了：分数变成 LaTeX 源码，上下标丢了，矩阵散了，或者整段公式变成无法修改的图片。几十个公式只能重新输入，标题、列表和表格也要重新排。

**chat-to-docx 是一个 Agent Skill：将你提供的 Markdown 聊天记录转换为 Word DOCX，并将数学公式转换成 Word 原生可编辑的 OMML 公式。**

> AI chat / Markdown → Word DOCX with editable OMML equations. Preserve headings, lists, tables, code blocks and source order.

## 为谁准备？

- 写论文、整理推导和技术说明的科研人员。
- 想把 ChatGPT、Claude、DeepSeek、Gemini 的回答保存成 Word 的用户。
- 需要真正可编辑公式，而不是公式截图的学生和老师。
- 希望 Markdown 的标题、表格、代码块和多轮消息完整保留的用户。

## 怎么用？

将仓库下载到支持 Agent Skills 的工具的技能目录，文件夹命名为 chat-to-docx。Codex 通常使用 ~/.codex/skills/chat-to-docx/；其他工具以自身文档为准。

```text
使用 $chat-to-docx，把我提供的聊天记录完整转换为 Word。
保留原文顺序、标题、列表、表格和代码块。
所有行内和独立公式转换为可编辑 OMML，不要生成公式图片。
检查公式对象与页面排版，交付 DOCX。
```

默认完整转换，不擅自摘要或删减。只想要最后一版正文时，请明确要求“仅提取最新版”。

## 为什么强调 OMML？

OMML 是 Office Math Markup Language，是 Word 原生数学公式结构。你应能点击公式并在 Word 公式编辑器内修改。DOCX 内部应存在 m:oMath 对象；成功生成文件并不等于公式转换成功。

支持识别代码块之外的美元符号与反斜杠括号公式。分数、上下标、矩阵、分段函数和对齐推导必须核对。复杂 LaTeX 命令的支持程度取决于转换引擎。

## 依赖和边界

这是 AI agent 的工作流技能，不是一键转换任意 Markdown 的完整软件。正文构建使用 python-docx；公式 helper 使用 lxml，将 Presentation MathML 经 Microsoft Office 的 MML2OMML.XSL 转为 OMML。仓库不分发微软样式表。现有 helper 不直接解析所有 Markdown 或 LaTeX。

优先结合宿主 documents 技能进行渲染与逐页检查；无该技能时需要等效流程。WPS、LibreOffice 显示效果可能不同，需在实际软件中验证。结构审计也不能证明数学推导正确。

## 文件导航

- [技能入口](SKILL.md)
- [聊天提取与清理](references/extraction-and-cleanup.md)
- [公式转换流程](references/equation-workflow.md)
- [MathML → OMML helper](scripts/mathml_to_omml.py)
- [DOCX 审计工具](scripts/audit_docx.py)
- [带公式的聊天输入示例](examples/chat-with-equations.md)

## English discovery summary

chat-to-docx is an Agent Skill for converting user-supplied AI chat transcripts and Markdown into Microsoft Word DOCX documents with editable Office Math Markup Language (OMML) equations. It targets ChatGPT-to-Word, Claude-to-Word, DeepSeek-to-Word and Markdown-to-DOCX workflows, preserving document structure and checking native equation objects. A capable agent and local conversion/rendering dependencies are required.

Search terms: AI 聊天记录转 Word、ChatGPT 公式复制 Word 乱码、Markdown 转 DOCX、LaTeX 转 Word 可编辑公式、OMML、MathML to OMML、editable Word equations、ChatGPT export Word、Claude skill、Codex skill、Agent Skills。

公开文档和关键词有助于搜索理解，但无法保证搜索引擎或任何 LLM 的收录时间和排名。
