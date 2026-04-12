---
concept: Unitary Group
slug: unitary-group
category: linear-groups
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Groups"
chapter_number: 9
pdf_page: 264
section: "9.1 The Classical Groups"
extraction_confidence: high
aliases: ["U_n"]
prerequisites: [hermitian-form, unitary-matrix]
extends: [general-linear-group]
related: [special-unitary-group-su2]
contrasts_with: [orthogonal-group]
answers_questions: ["What is the unitary group?"]
---
# Quick Definition
The unitary group U_n is the group of complex n x n matrices P satisfying P*P = I. It preserves the standard Hermitian form on C^n.
# Core Definition
U_n = {P in GL_n(C) | P*P = I} (Artin, (9.1.3), p. 264). A change of basis by a unitary matrix preserves the standard Hermitian product X*Y. U_1 is the unit circle in C (the complex numbers of absolute value 1).
# Prerequisites
- **Hermitian form** — U_n preserves the standard Hermitian form
- **Unitary matrix** — The elements of U_n
# Key Properties
1. P*P = I
2. |det P| = 1
3. Preserves the Hermitian form: (PX)*(PY) = X*Y
4. U_1 is the circle group (complex numbers of absolute value 1)
5. Lie algebra = skew-Hermitian matrices (A* = -A)
6. Every finite subgroup of GL_n is conjugate to a subgroup of U_n (Theorem 10.3.8(d))
# Context & Application
U_n is the symmetry group of the Hermitian form on C^n. It plays a central role in quantum mechanics, representation theory, and harmonic analysis. The fundamental result that every finite subgroup of GL_n is conjugate to a subgroup of U_n (Corollary 10.3.8(d)) underpins representation theory.
# Examples
**Example 1** (p. 264): U_1 = {p in C* | |p| = 1}, the unit circle group.
# Relationships
## Builds Upon
- **Hermitian form** — U_n preserves it
## Enables
- **Special unitary group SU_2** — SU_n = U_n intersect SL_n
## Contrasts With
- **Orthogonal group** — Real analogue; uses P^t P = I
# Source Reference
Chapter 9: Linear Groups, Section 9.1, page 264.
# Verification Notes
- Definition source: Direct from (9.1.3)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
