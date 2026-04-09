---
# === CORE IDENTIFICATION ===
concept: Simple Roots of Type C_n
slug: simple-roots-type-c

# === CLASSIFICATION ===
category: classification
subcategory: type-c
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 126
section: "C.3 C_n = sp(n,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-system-type-c
  - simple-roots
extends: []
related:
  - dynkin-diagram-type-c
  - cartan-matrix-type-c
contrasts_with:
  - simple-roots-type-b

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the simple roots of type C_n?"
---

# Quick Definition
The simple roots of $C_n$ are $\alpha_i = e_i - e_{i+1}$ for $i = 1, \ldots, n-1$ and $\alpha_n = 2e_n$. The last simple root $\alpha_n$ is a long root.

# Core Definition
(Kirillov, p. 126):

$$\Pi = \{\alpha_1, \ldots, \alpha_n\}, \quad \alpha_1 = e_1 - e_2, \ldots, \alpha_{n-1} = e_{n-1} - e_n, \quad \alpha_n = 2e_n$$

# Prerequisites
- **Root system type C** -- the roots being organized
- **Simple roots** -- general concept

# Key Properties
1. $\alpha_1, \ldots, \alpha_{n-1}$ are short roots
2. $\alpha_n = 2e_n$ is a long root
3. Compare with $B_n$: there $\alpha_n = e_n$ (short); here $\alpha_n = 2e_n$ (long)

# Relationships
## Contrasts With
- **Simple roots type B** -- $B_n$ has $\alpha_n = e_n$ (short); $C_n$ has $\alpha_n = 2e_n$ (long)

# Source Reference
Appendix C, Section C.3, p. 126.

# Verification Notes
- Definition source: Direct from p. 126
- Confidence rationale: Explicit
- Uncertainties: None
- Cross-reference status: Verified
