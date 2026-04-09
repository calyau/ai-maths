---
# === CORE IDENTIFICATION ===
concept: Simple Roots of Type D_n
slug: simple-roots-type-d

# === CLASSIFICATION ===
category: classification
subcategory: type-d
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 128
section: "C.4 D_n = so(2n,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-system-type-d
  - simple-roots
extends: []
related:
  - dynkin-diagram-type-d
  - cartan-matrix-type-d
contrasts_with:
  - simple-roots-type-b

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the simple roots of type D_n?"
---

# Quick Definition
The simple roots of $D_n$ are $\alpha_i = e_i - e_{i+1}$ for $i = 1, \ldots, n-1$ and $\alpha_n = e_{n-1} + e_n$. The last simple root is $e_{n-1} + e_n$ (not $e_n$ or $2e_n$), giving the characteristic fork in the Dynkin diagram.

# Core Definition
(Kirillov, p. 128):

$$\Pi = \{\alpha_1, \ldots, \alpha_n\}, \quad \alpha_1 = e_1 - e_2, \ldots, \alpha_{n-1} = e_{n-1} - e_n, \quad \alpha_n = e_{n-1} + e_n$$

# Prerequisites
- **Root system type D** -- the roots being organized
- **Simple roots** -- general concept

# Key Properties
1. All simple roots have equal length (simply laced)
2. $\alpha_{n-1}$ and $\alpha_n$ are both connected to $\alpha_{n-2}$ but not to each other
3. $(\alpha_{n-2}, \alpha_n) = -1$ (they share the $e_{n-1}$ component)
4. $(\alpha_{n-1}, \alpha_n) = 0$ (orthogonal -- the fork)
5. The fork structure distinguishes $D_n$ from all other classical types

# Relationships
## Enables
- **Dynkin diagram type D** -- the fork arises from $\alpha_{n-1}$ and $\alpha_n$ being orthogonal but both adjacent to $\alpha_{n-2}$

## Contrasts With
- **Simple roots type B** -- $B_n$ has $\alpha_n = e_n$ (short root, no fork)

# Source Reference
Appendix C, Section C.4, p. 128.

# Verification Notes
- Definition source: Direct from p. 128
- Confidence rationale: Explicit list
- Uncertainties: None
- Cross-reference status: Verified
