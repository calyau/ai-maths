---
# === CORE IDENTIFICATION ===
concept: Conjugate-Linear Part of an Operator
slug: conjugate-linear-part

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
  - "bar{A}_s"
  - "Theorem B.4"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - jordan-decomposition
extends:
  - jordan-decomposition
related:
  - jordan-decomposition-of-ad
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the conjugate-linear part of an operator?"
  - "How can the operator with conjugate eigenvalues be expressed as a polynomial in ad A?"
---

# Quick Definition
Given operator $A$ with semisimple part $A_s$ having eigenvalues $\lambda_i$, the conjugate-linear part $\bar{A}_s$ is the operator with the same eigenspaces but complex conjugate eigenvalues $\bar{\lambda}_i$. It can be expressed as a polynomial in $\mathrm{ad}\, A$.

# Core Definition
**Theorem B.4** (Kirillov, p. 121): Let $A$ be an operator $V \to V$. Define $\bar{A}_s$ to be the operator which has the same eigenspaces as $A_s$ but complex conjugate eigenvalues: if $A_s v = \lambda v$, then $\bar{A}_s v = \bar{\lambda} v$. Then $\bar{A}_s$ can be written in the form $\bar{A}_s = Q(\mathrm{ad}\, A)$ for some polynomial $Q \in t\mathbb{C}[t]$.

# Prerequisites
- **Jordan decomposition** -- $A_s$ is the semisimple part of $A$

# Key Properties
1. $\bar{A}_s$ has the same eigenspaces as $A_s$
2. Eigenvalues of $\bar{A}_s$ are complex conjugates of those of $A_s$
3. $\bar{A}_s$ is a polynomial in $\mathrm{ad}\, A$ (with no constant term)
4. Used in proving existence of compact real forms of semisimple Lie algebras

# Context & Application
This result is used in the proof that every complex semisimple Lie algebra has a compact real form. The ability to conjugate eigenvalues while staying within the Lie algebra (via the polynomial expression in $\mathrm{ad}\, A$) is the technical key.

# Examples
**Example** (p. 121): If $A_s = \mathrm{diag}(\lambda_1, \ldots, \lambda_n)$ in some basis, then $\bar{A}_s = \mathrm{diag}(\bar{\lambda}_1, \ldots, \bar{\lambda}_n)$ in the same basis.

# Relationships
## Builds Upon
- **Jordan decomposition** -- uses $A_s$

## Related
- **Jordan decomposition of adjoint** -- similar technique of expressing derived operators as polynomials in $\mathrm{ad}\, A$

# Source Reference
Appendix B, Theorem B.4, p. 121.

# Verification Notes
- Definition source: Direct from Theorem B.4
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
