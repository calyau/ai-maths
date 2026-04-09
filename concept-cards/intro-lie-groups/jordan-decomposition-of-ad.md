---
# === CORE IDENTIFICATION ===
concept: Jordan Decomposition of the Adjoint Operator
slug: jordan-decomposition-of-ad

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
pdf_page: 121
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Theorem B.3"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - jordan-decomposition
  - semisimple-operator
extends:
  - jordan-decomposition
related:
  - cartan-subalgebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Jordan decomposition interact with the adjoint representation?"
  - "Why is ad A_s a polynomial in ad A?"
---

# Quick Definition
For a linear operator $A: V \to V$, the Jordan decomposition of the adjoint operator $\mathrm{ad}\, A$ on $\mathrm{End}(V)$ satisfies $(\mathrm{ad}\, A)_s = \mathrm{ad}\, A_s$, and $\mathrm{ad}\, A_s = Q(\mathrm{ad}\, A)$ for some polynomial $Q$ with $Q(0) = 0$.

# Core Definition
**Theorem B.3** (Kirillov, p. 121): Let $A$ be an operator $V \to V$. Define $\mathrm{ad}\, A: \mathrm{End}(V) \to \mathrm{End}(V)$ by $\mathrm{ad}\, A \cdot B = AB - BA$. Then $(\mathrm{ad}\, A)_s = \mathrm{ad}\, A_s$, and $\mathrm{ad}\, A_s$ can be written in the form $\mathrm{ad}\, A_s = Q(\mathrm{ad}\, A)$ for some polynomial $Q \in \mathbb{C}[t]$ such that $Q(0) = 0$.

# Prerequisites
- **Jordan decomposition** -- applied to both $A$ and $\mathrm{ad}\, A$
- **Semisimple operator** -- $A_s$ and $\mathrm{ad}\, A_s$

# Key Properties
1. $(\mathrm{ad}\, A)_s = \mathrm{ad}\, A_s$ -- the semisimple part of ad commutes with taking ad
2. $\mathrm{ad}\, A_s = Q(\mathrm{ad}\, A)$ with $Q(0) = 0$ -- crucial for Lie algebra applications
3. $Q(0) = 0$ ensures that $\mathrm{ad}\, A_s$ preserves any Lie subalgebra that $\mathrm{ad}\, A$ preserves
4. In a basis diagonalizing $A_s$: $\mathrm{ad}\, A_s \cdot E_{ij} = (\lambda_i - \lambda_j)E_{ij}$

# Context & Application
This theorem is the key technical tool used in Section 6.6 to show that the abstract Jordan decomposition is compatible with Lie algebra structure. The condition $Q(0) = 0$ ensures that if $A$ is in a Lie subalgebra $\mathfrak{g} \subset \mathfrak{gl}(V)$, then $A_s$ is also in $\mathfrak{g}$ (since $\mathrm{ad}\, A_s$ maps $\mathfrak{g}$ to $\mathfrak{g}$).

# Examples
**Example** (p. 121): In a basis of eigenvectors of $A_s$ with eigenvalues $\lambda_i$, the adjoint action on matrix units is $\mathrm{ad}\, A_s \cdot E_{ij} = (\lambda_i - \lambda_j)E_{ij}$, which is diagonal.

# Relationships
## Builds Upon
- **Jordan decomposition** -- this extends it to the adjoint action

## Enables
- **Cartan subalgebra construction** -- uses the compatibility of Jordan decomposition with Lie brackets

# Source Reference
Appendix B, Theorem B.3, p. 121.

# Verification Notes
- Definition source: Direct from Theorem B.3
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
