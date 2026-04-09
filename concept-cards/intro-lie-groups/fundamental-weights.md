---
# === CORE IDENTIFICATION ===
concept: Fundamental Weights
slug: fundamental-weights

# === CLASSIFICATION ===
category: root-systems
subcategory: lattices
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 97
section: "8.5. Weight and root lattices"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$\\omega_i$"
  - "fundamental dominant weights"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simple-roots
  - coroot
extends: []
related:
  - weight-lattice
  - positive-weyl-chamber
contrasts_with:
  - simple-roots

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are fundamental weights?"
  - "How are fundamental weights related to simple roots?"
---

# Quick Definition
The fundamental weights $\omega_1,\ldots,\omega_r$ are the basis of $E$ dual to the simple coroots: $\langle\omega_i,\alpha_j^\vee\rangle = \delta_{ij}$. They form a $\mathbb{Z}$-basis of the weight lattice $P$.

# Core Definition
The fundamental weights $\omega_i \in E$ are defined by (equation 8.14, p. 97):

$$\langle\omega_i, \alpha_j^\vee\rangle = \delta_{ij}$$

They form a basis of $E$ and satisfy $P = \bigoplus_i \mathbb{Z}\omega_i$.

# Prerequisites
- **simple-roots** -- the simple coroots appear in the defining condition
- **coroot** -- the pairing $\langle\omega_i,\alpha_j^\vee\rangle$ uses coroots

# Key Properties
1. $\langle\omega_i, \alpha_j^\vee\rangle = \delta_{ij}$ (the defining property)
2. $\omega_1,\ldots,\omega_r$ form a basis of $E$
3. $P = \bigoplus \mathbb{Z}\omega_i$
4. Each $\omega_i$ lies on the boundary of the positive Weyl chamber (it is orthogonal to all simple roots except $\alpha_i$)
5. The half-sum of positive roots satisfies $\langle\rho,\alpha_i^\vee\rangle = 1$ (Lemma 8.36), so $\rho = \sum \omega_i$

# Construction / Recognition
1. Given simple roots $\alpha_1,\ldots,\alpha_r$ and their coroots $\alpha_i^\vee$
2. Solve the system $\langle\omega_i,\alpha_j^\vee\rangle = \delta_{ij}$ for $\omega_i$
3. This amounts to expressing $\omega_i$ in terms of simple roots using the inverse of the Cartan matrix

# Context & Application
Fundamental weights are the natural coordinates for the weight lattice. In representation theory, the highest weight of an irreducible representation is a non-negative integer combination of fundamental weights: $\lambda = \sum m_i\omega_i$ with $m_i \geq 0$. The representation with highest weight $\omega_i$ is called the $i$-th fundamental representation.

# Examples
**Example 8.20** (p. 97): For $A_1$, $\omega = \alpha/2$ since $\langle\omega,\alpha^\vee\rangle = 1$ and $\langle\alpha,\alpha^\vee\rangle = 2$.

**Example 8.21** (p. 97): For $A_2$, the fundamental weights $\omega_1, \omega_2$ are shown in Figure 8.3.

# Relationships
## Builds Upon
- **simple-roots** -- fundamental weights are dual to simple coroots

## Enables
- **weight-lattice** -- $P = \bigoplus\mathbb{Z}\omega_i$

## Related
- **positive-weyl-chamber** -- defined by $\langle\lambda,\alpha_i^\vee\rangle > 0$; fundamental weights lie on its walls

## Contrasts With
- **simple-roots** -- provide a basis for $Q$, while fundamental weights provide a basis for $P$

# Common Errors
- **Error**: Confusing fundamental weights with simple roots
  **Correction**: In general $\omega_i \neq \alpha_i$; they are dual bases for different lattices

# Common Confusions
- **Confusion**: Thinking $\omega_i$ are always roots
  **Clarification**: Fundamental weights need not be roots; for $A_1$, $\omega = \alpha/2 \notin R$

# Source Reference
Chapter 8: Root Systems, Section 8.5, page 97. Equation (8.14).

# Verification Notes
- Definition source: Direct from equation (8.14)
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
- Cross-reference status: Verified
