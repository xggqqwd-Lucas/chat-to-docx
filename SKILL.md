---
name: chat-to-docx
description: 将 AI 聊天记录或 Markdown 转成保留结构且含 Word 原生可编辑 OMML 公式的 DOCX，解决 ChatGPT 公式复制到 Word 乱码、LaTeX 源码残留和公式图片无法编辑的问题。 Convert AI chat transcripts and Markdown to Word DOCX with editable OMML equations.
---

# Chat to DOCX｜聊天记录转 Word

接收用户提供的聊天文本或 Markdown，默认完整保留原文和结构，转换公式后交付 DOCX。不能用公式截图、原样 LaTeX 字符串或仅生成文件代替可编辑公式。无需登录聊天平台。

优先使用宿主 documents 技能的创建、渲染与逐页检查流程。该技能不可用时使用等效工具，明确说明尚未验证的项目。依赖和使用示例见 [README.md](README.md)。

## 内容选择

- 默认按原顺序完整转换所有消息，保留说话者标签、消息边界、标题层级、列表、表格、代码块和链接，不摘要、不删减。
- 只有用户明确要求提取最新版时，选择最后一个完整草稿，再按时间顺序应用后续明确修改。不得合并互相矛盾的草稿。
- 保留用户确定的标题、术语和措辞。更新既有 DOCX 前先检查其正文、样式、表格、页面设置和批注；遵循用户指定的替换或追加范围。
- 提取与清理细节见 [references/extraction-and-cleanup.md](references/extraction-and-cleanup.md)。

## 文档与公式

1. 使用 python-docx 或等效工具建立真实 Word 标题、列表、表格和代码段落。源码使用 UTF-8，并明确设置中西文字体。
2. 识别代码块之外的 `$...$`、`$$...$$`、`\(...\)`、`\[...\]`。代码里的公式字符串原样作为代码保留。
3. 构建或转换为 Presentation MathML，再用 Microsoft Office 的 MML2OMML.XSL 转为 OMML。辅助脚本见 [scripts/mathml_to_omml.py](scripts/mathml_to_omml.py)，流程见 [references/equation-workflow.md](references/equation-workflow.md)。此脚本不直接解析所有 Markdown 或 LaTeX。
4. 行内公式用 m:oMath 放在正文段落中；独立公式放在单独居中的段落中。保留分数、上下标、矩阵、分段函数、积分、求和与对齐推导。
5. 不将公式降级为图片或原始 LaTeX。复杂语法必须核对；无可靠转换器时报告缺失依赖，不宣称已完成。
6. 聊天引用标记仅在真实来源已知时规范化；不得编造引用。明显乱码仅在上下文可确定时修复，不确定的内容保留并询问。

## 验证与交付

先保存工作副本，检查 DOCX 内部 word/document.xml 的 m:oMath 数量，再渲染并逐页检查公式、字体、裁切、表格和分页。结构审计不能替代视觉检查或数学正确性核对。

```bash
python scripts/audit_docx.py final.docx --expect-equations 3 --json
```

验收：没有意外 Unicode 替换字符、动态聊天引用残留或正文中的未转换公式；公式数量符合源内容；标题和正文完整；所有页面经实际检查。源代码块中的合法 LaTeX 例子不应被误删。

如果 Word/WPS 文件被占用，不结束进程或丢弃未保存工作。先构建验证副本；只有用户明确要求更新原路径时才安全连接活动应用、按完整路径匹配文档并更新。无法安全写入时交付独立副本。应用重新保存后重新验证。

交付用户要求的 DOCX；未完成的公式转换或视觉检查必须明确报告。
