---
name: cn-grant-proposal
description: Use when writing, structuring, improving, or reviewing a Chinese-language research fund application (基金申请书/标书) — 国家社科基金, 北京市社会科学基金, 教育部人文社科, 国家自然科学基金 and similar — especially in economics (应用经济/理论经济/管理). Covers 选题与标题, 课题说明/选题依据/研究内容/创新之处/预期成果/参考文献/研究基础, the persuasion and language craft reviewers reward, and the red lines that get proposals rejected. Distinct from the English AER/econ skills (which target English journals): this skill governs Chinese grant prose and the 活页/申请书 format.
---

# 中文经济学基金申请书写作 (CN Grant Proposal)

## Overview

A Chinese fund application is won or lost on **(1) 选题与标题, (2) 创新与价值, (3) 综述与可行性 — and the language that carries them.** Reviewers skim under time pressure: the form exists to let a reviewer grasp *what you do, why it matters, and whether you can pull it off* within three minutes. This skill encodes the techniques distilled from 18 winning economics 社科 proposals (2007–2022) and申报经验 guides.

**The full handbook lives in [playbook.md](playbook.md) — read it before writing or revising any substantive section.** It is organized by dimension (选题与标题 / 结构与各部分模板 / 语言与修辞 / 创新 / 价值 / 综述 / 方案可行性 / 红线 / 句式金句库 / 提交前自检清单). What follows is the operating procedure and the non-negotiables.

## When to use
- Drafting or rewriting any section of a Chinese 申请书/活页 (especially economics).
- Improving language organization, structure, or persuasiveness of an existing draft.
- A pre-submission review of a Chinese grant proposal.

For English-journal economics writing use the `aer-*` / `econ-craft` / `journal-fit` skills instead — the surface rules differ (Chinese grant prose uses 加粗, 顿号、分号；, hierarchical 一/（一）/1./（1）, and policy-aligned framing, none of which apply to AER prose).

## Operating procedure
1. **Read [playbook.md](playbook.md) in full.** Then load the official 申报说明 + 课题指南 for the specific fund (limits on 字数, 成果形式, 经费, eligibility, format) — compliance is a gate, not a style choice.
2. **Title first.** Spend real effort here; the title's keywords must map one-to-one onto 综述每段 / 研究内容各点 / 创新各点. Prefer `[视角/方法] + [研究对象] + [机制/治理/对策/测度]`, optionally 主标题（钩子概念）+ 副标题（呼应指南条目）.
3. **Draft in the official section order**, copying each 提纲 prompt then answering it. Budget the space ≈ 现状意义 1 : 内容创新 2 : 成果文献 1.
4. **Apply the language craft** (playbook §三): topic sentence first in every paragraph; hierarchical numbering; 加粗 only the 创新/闪光句 (≤ ~500 字 total); 机制语言 not 关系语言; 数字 not 形容词; delete 空话; define any coined term before use.
5. **Make 创新 mirror the 综述空白** one-for-one, written as testable propositions, never as "填补空白/国内领先".
6. **Run the 提交前自检清单 (playbook §十)** before declaring done.

## Non-negotiable red lines (auto-reject risks)
- Never claim "填补空白 / 国内独创 / 国际领先 / 国内一流" — high-frequency rejection cause. Show a sharp 特色 instead.
- 活页 must be fully anonymous: no 姓名/单位/成果名称/发表时间/负责人.
- Respect every stated limit (字数, 成果形式, 经费上限, 年龄, 份数). Zero错别字; proofread字字.
- 前期成果 must be real and relevant; do not over-state to the point the project looks already finished.

## Project setup (upper-level setting)
For a new grant-application project under `Work\基金申请\`:
- Keep `参考标书与范本\` (winning samples) and read the economics ones for the target program before drafting.
- Maintain the build pipeline used in `Work\基金申请\北社科\`: edit `_work\sectionN.md` → `pandoc -f markdown-smart` → `python _work\build.py` (rebuilds the 论证/研究基础 cells with 宋体12pt / 固定行距21磅 / 首行缩进200 / preserved 加粗 / images / OMML equations) → `python _work\fix_budget.py` → Word COM export to PDF for a visual + 字数 check (`ComputeStatistics(0)` = the Word 字数 that matches the platform's "字" count).
- Always work on a copy; never overwrite a delivered 提交稿.
