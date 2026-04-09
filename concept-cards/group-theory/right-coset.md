---
# === CORE IDENTIFICATION ===
concept: Right Coset
slug: right-coset

# === CLASSIFICATION ===
category: subgroup-theory
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 17
section: "Cosets"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subgroup
extends: []
related:
  - left-coset
  - normal-subgroup
contrasts_with:
  - left-coset

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a right coset?"
  - "How do left and right cosets relate?"
---

# Quick Definition

For a subgroup $H$ of $G$ and $a \in G$, the right coset is $Ha = \{ha \mid h \in H\}$. There is a natural bijection between the set of left cosets and the set of right cosets.

# Core Definition

"The sets of the form $Ha$ are called the **right cosets** of $H$ in $G$." (Milne, p. 17)

The map $S \mapsto S^{-1}$ (where $S^{-1} = \{g^{-1} \mid g \in S\}$) gives a bijection $aH \leftrightarrow Ha^{-1}$ between left and right cosets. (1.29)

# Prerequisites

- **Subgroup** — Right cosets are defined relative to a subgroup

# Key Properties

1. $(aH)^{-1} = Ha^{-1}$ and $(Ha)^{-1} = a^{-1}H$ (1.29)
2. The number of left cosets equals the number of right cosets
3. In general, a left coset is *not* a right coset (1.29)
4. $aH = Ha$ for all $a$ if and only if $H$ is normal

# Construction / Recognition

Right cosets are computed as $Ha = \{ha \mid h \in H\}$ by right-multiplying.

# Context & Application

Right cosets are dual to left cosets. The coincidence of left and right cosets characterizes normal subgroups, which is essential for forming quotient groups.

# Examples

**Example 1** (p. 18): In $D_n$ with $H = \{e, s\}$ (not normal for $n \ge 3$): $rH = \{r, rs\}$ but $Hr = \{r, sr\} = \{r, r^{n-1}s\}$, so $rH \neq Hr$.

# Relationships

## Builds Upon
- **subgroup** — right cosets are defined relative to a subgroup

## Related
- **left-coset** — dual notion
- **normal-subgroup** — $H$ is normal iff left and right cosets coincide

## Contrasts With
- **left-coset** — $aH$ vs $Ha$; they coincide iff $H \trianglelefteq G$

# Common Errors

- **Error**: Assuming left and right cosets always coincide
  **Correction**: They coincide only when $H$ is normal

# Source Reference

Chapter 1, p. 17, Remark 1.29.

# Verification Notes

- Definition source: Direct from p. 17
- Confidence: HIGH — explicit definition
- Uncertainties: None
