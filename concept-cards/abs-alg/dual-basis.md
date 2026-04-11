---
concept: Dual Basis
slug: dual-basis
category: linear-algebra
subcategory: dual-spaces
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Vector Spaces"
chapter_number: 11
pdf_page: 425
section: "11.3 Dual Vector Spaces"
extraction_confidence: high
aliases: []
prerequisites:
  - dual-space
  - basis
extends: []
related:
  - transpose
contrasts_with: []
answers_questions:
  - "What is a dual basis?"
---

# Quick Definition
If $\mathcal{B} = \{v_1, \ldots, v_n\}$ is a basis of V, the dual basis $\{v_1^*, \ldots, v_n^*\}$ of $V^*$ is defined by $v_i^*(v_j) = \delta_{ij}$ (1 if $i=j$, 0 otherwise).

# Core Definition
Let $\mathcal{B} = \{v_1, \ldots, v_n\}$ be a basis of the finite dimensional space V. Define $v_i^* \in V^*$ by $v_i^*(v_j) = 1$ if $i = j$ and $v_i^*(v_j) = 0$ if $i \neq j$. Then $\{v_1^*, \ldots, v_n^*\}$ is a basis of $V^*$ called the dual basis to $\mathcal{B}$ (Dummit & Foote, Proposition 18, p. 425).

# Prerequisites
- **dual-space** — The dual basis lives in $V^*$
- **basis** — Defined relative to a basis of V

# Key Properties
1. The dual basis is indeed a basis of $V^*$
2. Every linear functional can be written uniquely as a linear combination of the dual basis
3. The matrix of $\varphi^*$ with respect to dual bases is the transpose of the matrix of $\varphi$

# Relationships
## Builds Upon
- **dual-space**, **basis**

## Related
- **transpose** — Transpose arises from dual bases

# Source Reference
Chapter 11, Section 11.3, Proposition 18, p. 425.

# Verification Notes
- Confidence: HIGH — explicit construction and proposition
