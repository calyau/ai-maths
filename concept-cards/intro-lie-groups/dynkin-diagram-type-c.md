---
# === CORE IDENTIFICATION ===
concept: Dynkin Diagram of Type C_n
slug: dynkin-diagram-type-c

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
  - dynkin-diagram
extends: []
related:
  - cartan-matrix-type-c
contrasts_with:
  - dynkin-diagram-type-b

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Dynkin diagram of type C_n?"
  - "What distinguishes the root systems of types A, B, C, D?"
---

# Quick Definition
The Dynkin diagram of $C_n$ is a chain of $n$ nodes where the last edge is a double edge with an arrow pointing from the short root to the long root: $\circ - \circ - \cdots - \circ \Leftarrow \circ$. The arrow direction is opposite to that of $B_n$.

# Core Definition
(Kirillov, p. 126): The Dynkin diagram has $n$ nodes, with single edges between $\alpha_1, \ldots, \alpha_{n-1}$ and a double edge with arrow pointing toward the long root ($\Leftarrow$, from $\alpha_n$ to $\alpha_{n-1}$).

# Prerequisites
- **Simple roots type C** -- nodes correspond to simple roots
- **Dynkin diagram** -- general concept

# Key Properties
1. The double bond arrow points from short to long root (opposite direction from $B_n$)
2. Cartan matrix has $a_{n-1,n} = -2$ and $a_{n,n-1} = -1$ (opposite from $B_n$)

# Relationships
## Contrasts With
- **Dynkin diagram type B** -- arrow points in opposite direction on the double bond

# Source Reference
Appendix C, Section C.3, p. 126.

# Verification Notes
- Definition source: Direct from p. 126
- Confidence rationale: Standard diagram
- Uncertainties: None
- Cross-reference status: Verified
