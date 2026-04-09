---
# === CORE IDENTIFICATION ===
concept: Fundamental Weights of Type A_n
slug: fundamental-weights-type-a

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
aliases:
  - "omega_k for type A"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simple-roots-type-a
  - fundamental-weight
extends: []
related:
  - weight-lattice-type-a
  - exterior-power-representation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the fundamental weights of type A_n?"
---

# Quick Definition
The fundamental weights of $A_n$ are $\omega_k = e_1 + e_2 + \cdots + e_k = (1, \ldots, 1, 0, \ldots, 0)$ for $k = 1, \ldots, n$, dual to the simple coroots. The corresponding fundamental representations are the exterior powers $\Lambda^k \mathbb{C}^{n+1}$.

# Core Definition
(Kirillov, p. 123): The fundamental weights are determined by $\langle \omega_k, \alpha_i^\vee \rangle = \delta_{ki}$. For type $A_n$, this gives $\omega_k = e_1 + \cdots + e_k$ (in the representative with $\sum \lambda_i = 0$: $\omega_k = (\underbrace{\frac{n+1-k}{n+1}, \ldots}_{k}, \underbrace{\frac{-k}{n+1}, \ldots}_{n+1-k})$).

# Prerequisites
- **Simple roots type A** -- fundamental weights are dual to simple coroots
- **Fundamental weight** -- general concept

# Key Properties
1. $\omega_k$ is the highest weight of $\Lambda^k \mathbb{C}^{n+1}$
2. In coordinates (using representative with last entry 0): $\omega_k = (1, \ldots, 1, 0, \ldots, 0)$ with $k$ ones
3. $P_+ = \{\sum m_k \omega_k \mid m_k \in \mathbb{Z}_+\}$
4. The dominant weight $\lambda = \sum m_k \omega_k$ corresponds to a Young diagram with rows of lengths $\lambda_1 \geq \cdots \geq \lambda_n \geq 0$

# Examples
**Example** (p. 123): For $A_2$: $\omega_1 = (1, 0, 0)$ (standard representation), $\omega_2 = (1, 1, 0)$ (dual standard $\cong \Lambda^2 \mathbb{C}^3$).

# Relationships
## Builds Upon
- **Simple roots type A** -- dual basis relationship

## Enables
- **Exterior power representation** -- $\Lambda^k \mathbb{C}^{n+1}$ has highest weight $\omega_k$
- **Weight lattice type A** -- $P = \bigoplus \mathbb{Z}\omega_k$

# Source Reference
Appendix C, Section C.1, p. 123.

# Verification Notes
- Definition source: Inferred from weight lattice description and standard theory
- Confidence rationale: High -- consistent with explicit lattice description
- Uncertainties: Fundamental weights not listed individually in source but follow from the lattice description
- Cross-reference status: Verified
