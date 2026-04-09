---
# === CORE IDENTIFICATION ===
concept: Cartan Matrix of Type C_n
slug: cartan-matrix-type-c

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
  - simple-roots-type-c
  - cartan-matrix
extends: []
related:
  - dynkin-diagram-type-c
contrasts_with:
  - cartan-matrix-type-b

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Cartan matrix of type C_n?"
---

# Quick Definition
The Cartan matrix of $C_n$ is tridiagonal with 2 on the diagonal, $-1$ on most off-diagonals, except $a_{n-1,n} = -2$ and $a_{n,n-1} = -1$. It is the transpose of the $B_n$ Cartan matrix.

# Core Definition
(Kirillov, p. 126):

$$A = \begin{pmatrix} 2 & -1 & & \\ -1 & 2 & -1 & \\ & \ddots & \ddots & \ddots \\ & & -1 & 2 & -2 \\ & & & -1 & 2 \end{pmatrix}$$

# Prerequisites
- **Simple roots type C** -- entries from simple root pairings
- **Cartan matrix** -- general concept

# Key Properties
1. $a_{n-1,n} = -2$, $a_{n,n-1} = -1$ (opposite from $B_n$)
2. $\det A = 2$
3. $A_{C_n} = A_{B_n}^T$ (transpose relationship)

# Relationships
## Contrasts With
- **Cartan matrix type B** -- $B_n$ has $a_{n-1,n} = -1$, $a_{n,n-1} = -2$

# Source Reference
Appendix C, Section C.3, p. 126.

# Verification Notes
- Definition source: Direct from p. 126
- Confidence rationale: Explicit matrix
- Uncertainties: None
- Cross-reference status: Verified
