---
# === CORE IDENTIFICATION ===
concept: Jordan Decomposition
slug: jordan-decomposition

# === CLASSIFICATION ===
category: lie-algebras
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix B - Jordan Decomposition"
chapter_number: null
pdf_page: 120
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Jordan-Chevalley decomposition"
  - "additive Jordan decomposition"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semisimple-operator
  - nilpotent-operator
  - generalized-eigenspace
extends: []
related:
  - jordan-decomposition-of-ad
  - cartan-subalgebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Jordan decomposition of a linear operator?"
  - "Why is the Jordan decomposition important for Lie algebra structure theory?"
---

# Quick Definition
The Jordan decomposition writes any linear operator $A$ uniquely as a sum $A = A_s + A_n$ of a semisimple (diagonalizable) part and a nilpotent part that commute with each other. Both parts are polynomials in $A$.

# Core Definition
**Theorem B.2** (Kirillov, p. 120-121): Any linear operator $A$ can be uniquely written as a sum of commuting semisimple and nilpotent operators:

$$A = A_s + A_n, \quad A_s A_n = A_n A_s, \quad A_n \text{ nilpotent}, \quad A_s \text{ semisimple}$$

Moreover, $A_s, A_n$ can be written as polynomials of $A$: $A_s = p(A)$, $A_n = A - p(A)$ for some polynomial $p \in \mathbb{C}[t]$ depending on $A$.

# Prerequisites
- **Semisimple operator** -- $A_s$ is the semisimple part
- **Nilpotent operator** -- $A_n$ is the nilpotent part
- **Generalized eigenspace** -- used in the construction

# Key Properties
1. **Existence**: Construct $A_s$ by defining $A_s|_{V_{(\lambda)}} = \lambda \cdot \mathrm{id}$ on each generalized eigenspace
2. **Uniqueness**: If $A = A_s' + A_n'$ is another such decomposition, then $A_s = A_s'$ and $A_n = A_n'$
3. **Polynomial property**: $A_s = p(A)$ and $A_n = A - p(A)$ for some polynomial $p$
4. Both $A_s$ and $A_n$ commute with any operator that commutes with $A$
5. In a suitable basis, $A_s$ is diagonal and $A_n$ is strictly upper-triangular (p. 121)

# Construction / Recognition
1. Decompose $V = \bigoplus V_{(\lambda)}$ into generalized eigenspaces
2. Define $A_s|_{V_{(\lambda)}} = \lambda \cdot \mathrm{id}$
3. Define $A_n = A - A_s$
4. Verify: $A_s$ is diagonal on each generalized eigenspace, $A_n = A - A_s$ is nilpotent on each

# Context & Application
The Jordan decomposition is used in Section 6.6 to analyze the structure of semisimple Lie algebras. The decomposition of the adjoint representation into semisimple and nilpotent parts leads to the Cartan subalgebra (spanned by the semisimple elements). Theorem B.3 extends the Jordan decomposition to the adjoint action on $\mathrm{End}(V)$.

# Examples
**Example** (p. 120-121): For $A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$, we have $A_s = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$ and $A_n = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.

# Relationships
## Builds Upon
- **Semisimple operator** -- the diagonalizable part
- **Nilpotent operator** -- the nilpotent part
- **Generalized eigenspace** -- the construction tool

## Enables
- **Jordan decomposition of adjoint** -- Theorem B.3
- **Cartan subalgebra** -- via the semisimple part of adjoint action

# Common Errors
- **Error**: Forgetting the commutativity condition $A_s A_n = A_n A_s$
  **Correction**: The decomposition requires that the parts commute; this is what makes it unique

# Common Confusions
- **Confusion**: Confusing with Jordan normal form
  **Clarification**: Jordan decomposition is $A = A_s + A_n$; Jordan normal form puts $A$ in a specific block-diagonal form. They are related but distinct.

# Source Reference
Appendix B: Jordan Decomposition, Theorem B.2, pp. 120-121.

# Verification Notes
- Definition source: Direct from Theorem B.2
- Confidence rationale: Full theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
