---
# === CORE IDENTIFICATION ===
concept: Dynkin Diagram of Type B_n
slug: dynkin-diagram-type-b

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
  - dynkin-diagram
extends: []
related:
  - cartan-matrix-type-b
contrasts_with:
  - dynkin-diagram-type-a
  - dynkin-diagram-type-c
  - dynkin-diagram-type-d

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Dynkin diagram of type B_n?"
  - "What distinguishes the root systems of types A, B, C, D?"
---

# Quick Definition
The Dynkin diagram of $B_n$ is a chain of $n$ nodes where the last edge is a double edge with an arrow pointing from the long root to the short root: $\circ - \circ - \cdots - \circ \Rightarrow \circ$. The double bond indicates roots of different lengths.

# Core Definition
(Kirillov, p. 125): The Dynkin diagram has $n$ nodes connected in a line, with single edges between $\alpha_1, \ldots, \alpha_{n-1}$ and a double edge (with arrow $\Rightarrow$ pointing toward the short root $\alpha_n$) between $\alpha_{n-1}$ and $\alpha_n$.

# Prerequisites
- **Simple roots type B** -- the nodes correspond to simple roots
- **Dynkin diagram** -- general concept

# Key Properties
1. $n$ nodes, with a double bond at the right end
2. Arrow on double bond points from long root to short root (toward $\alpha_n$)
3. Corresponds to Cartan matrix entry $a_{n-1,n} = -1$, $a_{n,n-1} = -2$

# Examples
**Example** (p. 125): $B_2$: $\circ \Rightarrow \circ$. $B_3$: $\circ - \circ \Rightarrow \circ$.

# Relationships
## Contrasts With
- **Dynkin diagram type A** -- all single edges
- **Dynkin diagram type C** -- double bond with arrow in opposite direction ($\Leftarrow$)
- **Dynkin diagram type D** -- fork instead of double bond

# Source Reference
Appendix C, Section C.2, p. 125.

# Verification Notes
- Definition source: Direct from p. 125
- Confidence rationale: Standard diagram
- Uncertainties: None
- Cross-reference status: Verified
