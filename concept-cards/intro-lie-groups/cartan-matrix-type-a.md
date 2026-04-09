---
# === CORE IDENTIFICATION ===
concept: Cartan Matrix of Type A_n
slug: cartan-matrix-type-a

# === CLASSIFICATION ===
category: classification
subcategory: type-a
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 123
section: "C.1 A_n = sl(n+1,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simple-roots-type-a
  - cartan-matrix
extends: []
related:
  - dynkin-diagram-type-a
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Cartan matrix of type A_n?"
---

# Quick Definition
The Cartan matrix of $A_n$ is the $n \times n$ tridiagonal matrix with 2 on the diagonal and $-1$ on the super- and sub-diagonals.

# Core Definition
(Kirillov, p. 123): The Cartan matrix is $A_{ij} = \langle \alpha_i, \alpha_j^\vee \rangle$:

$$A = \begin{pmatrix} 2 & -1 & & \\ -1 & 2 & -1 & \\ & -1 & 2 & \ddots \\ & & \ddots & \ddots & -1 \\ & & & -1 & 2 \end{pmatrix}$$

# Prerequisites
- **Simple roots type A** -- entries are computed from simple root pairings
- **Cartan matrix** -- general concept

# Key Properties
1. Symmetric matrix (since $A_n$ is simply laced)
2. Determinant $= n + 1$ (equals $|P/Q|$)
3. Positive definite
4. $A_{ii} = 2$, $A_{i,i+1} = A_{i+1,i} = -1$, all other entries 0

# Examples
**Example** (p. 123): For $A_2$: $A = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$.

# Relationships
## Related
- **Dynkin diagram type A** -- encodes the same information graphically

# Source Reference
Appendix C, Section C.1, p. 123.

# Verification Notes
- Definition source: Direct from p. 123
- Confidence rationale: Explicit matrix given
- Uncertainties: None
- Cross-reference status: Verified
