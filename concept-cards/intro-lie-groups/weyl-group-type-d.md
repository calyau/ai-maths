---
# === CORE IDENTIFICATION ===
concept: Weyl Group of Type D_n
slug: weyl-group-type-d

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
  - weyl-group
extends: []
related: []
contrasts_with:
  - weyl-group-type-b

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Weyl group of type D_n?"
---

# Quick Definition
The Weyl group of $D_n$ consists of all permutations and an even number of sign changes of coordinates. It has order $2^{n-1} n!$, which is half the order of the $B_n$ Weyl group.

# Core Definition
(Kirillov, p. 128): $W = \{\text{permutations and even number of sign changes}\}$. Simple reflections: $s_i = (i \;\; i+1)$ for $i = 1, \ldots, n-1$; $s_n: (\lambda_1, \ldots, \lambda_{n-1}, \lambda_n) \mapsto (\lambda_1, \ldots, -\lambda_n, -\lambda_{n-1})$.

# Prerequisites
- **Root system type D** -- reflections in roots generate $W$
- **Weyl group** -- general concept

# Key Properties
1. $|W| = 2^{n-1} n!$ (half of $|W(B_n)| = 2^n n!$)
2. Only an even number of sign changes are allowed (vs. any number for $B_n$)
3. $s_n$ simultaneously flips the signs of the last two coordinates
4. $W(D_n)$ is an index-2 subgroup of $W(B_n)$

# Context & Application
The restriction to even sign changes reflects the geometry of $\mathrm{SO}(2n)$: the two connected components of $\mathrm{O}(2n)$ give rise to the constraint that an even number of coordinates must change sign.

# Relationships
## Contrasts With
- **Weyl group type B** -- $B_n$ allows any number of sign changes; $D_n$ requires an even number. $W(D_n)$ has index 2 in $W(B_n)$.

# Source Reference
Appendix C, Section C.4, p. 128.

# Verification Notes
- Definition source: Direct from p. 128
- Confidence rationale: Explicit
- Uncertainties: None
- Cross-reference status: Verified
