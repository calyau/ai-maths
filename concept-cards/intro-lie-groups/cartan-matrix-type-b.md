---
# === CORE IDENTIFICATION ===
concept: Cartan Matrix of Type B_n
slug: cartan-matrix-type-b

# === CLASSIFICATION ===
category: classification
subcategory: type-b
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 125
section: "C.2 B_n = so(2n+1,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simple-roots-type-b
  - cartan-matrix
extends: []
related:
  - dynkin-diagram-type-b
contrasts_with:
  - cartan-matrix-type-c

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Cartan matrix of type B_n?"
---

# Quick Definition
The Cartan matrix of $B_n$ is tridiagonal with 2 on the diagonal and $-1$ on most off-diagonals, except the $(n-1, n)$ entry is $-1$ and the $(n, n-1)$ entry is $-2$, reflecting the different root lengths.

# Core Definition
(Kirillov, p. 125):

$$A = \begin{pmatrix} 2 & -1 & & \\ -1 & 2 & -1 & \\ & \ddots & \ddots & \ddots \\ & & -1 & 2 & -1 \\ & & & -2 & 2 \end{pmatrix}$$

# Prerequisites
- **Simple roots type B** -- entries computed from simple root pairings
- **Cartan matrix** -- general concept

# Key Properties
1. Not symmetric: $a_{n-1,n} = -1$ but $a_{n,n-1} = -2$
2. The asymmetry reflects the two root lengths
3. $\det A = 2$ (equals $|P/Q|$)

# Examples
**Example** (p. 125): For $B_2$: $A = \begin{pmatrix} 2 & -1 \\ -2 & 2 \end{pmatrix}$.

# Relationships
## Contrasts With
- **Cartan matrix type C** -- has $a_{n-1,n} = -2$ and $a_{n,n-1} = -1$ (swapped)

# Source Reference
Appendix C, Section C.2, p. 125.

# Verification Notes
- Definition source: Direct from p. 125
- Confidence rationale: Explicit matrix
- Uncertainties: None
- Cross-reference status: Verified
