---
# === CORE IDENTIFICATION ===
concept: Dominant Integral Weight
slug: dominant-integral-weight

# === CLASSIFICATION ===
category: representations
subcategory: highest-weight-theory
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Semisimple Lie Algebras"
chapter_number: 9
pdf_page: 114
section: "9.3 Classification of irreducible finite-dimensional representations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "dominant weight"
  - "element of P_+"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - integral-weight
  - weight-lattice
  - positive-roots
  - coroot
extends:
  - integral-weight
related:
  - finite-dimensional-criterion
  - irreducible-highest-weight-module
  - positive-weyl-chamber
  - fundamental-weight
contrasts_with:
  - integral-weight

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a dominant integral weight?"
  - "How do I classify irreducible representations using highest weights?"
---

# Quick Definition
A dominant integral weight is an element $\lambda \in \mathfrak{h}^*$ satisfying $\langle \lambda, \alpha^\vee \rangle \in \mathbb{Z}_+$ for all positive roots $\alpha \in R_+$. The set of dominant integral weights $P_+$ parametrizes the irreducible finite-dimensional representations of $\mathfrak{g}$.

# Core Definition
**Definition 9.16** (Kirillov, p. 114): A weight $\lambda \in \mathfrak{h}^*$ is called *dominant integral* if

$$\langle \lambda, \alpha^\vee \rangle \in \mathbb{Z}_+ \quad \text{for all } \alpha \in R_+.$$

The set of all integral dominant weights is denoted $P_+$. Note that it suffices to check this for simple roots: $\langle \lambda, \alpha_i^\vee \rangle \in \mathbb{Z}_+$ for all $\alpha_i \in \Pi$ (equation (9.8)).

# Prerequisites
- **Integral weight** -- dominant integral weights form a subset of the weight lattice
- **Weight lattice** -- $P_+ \subset P$
- **Positive roots** -- the dominance condition involves $R_+$
- **Coroot** -- the condition is stated via coroot pairings

# Key Properties
1. $P_+ \subset P$ (dominant integral weights are integral)
2. Checking against simple roots suffices: $\langle \lambda, \alpha_i^\vee \rangle \in \mathbb{Z}_+$ for $\alpha_i \in \Pi$ (equation (9.8))
3. $P_+$ is in bijection with irreducible finite-dimensional representations (Corollary 9.18)
4. In the fundamental weight basis $\lambda = \sum m_i \omega_i$, dominance means $m_i \in \mathbb{Z}_+$ for all $i$
5. $P_+$ is the intersection of the weight lattice with the closed positive Weyl chamber

# Construction / Recognition
## To check if $\lambda$ is dominant integral
1. Express $\lambda$ in the fundamental weight basis: $\lambda = \sum m_i \omega_i$
2. Check that all $m_i$ are non-negative integers
3. Equivalently, compute $\langle \lambda, \alpha_i^\vee \rangle$ for each simple root and verify $\geq 0$ and $\in \mathbb{Z}$

# Context & Application
The dominant integral weights are the "labels" for irreducible finite-dimensional representations. **Theorem 9.17** states: $L_\lambda$ is finite-dimensional if and only if $\lambda \in P_+$. Combined with Corollary 9.18, this gives a complete classification: the irreducible finite-dimensional representations are $\{L_\lambda \mid \lambda \in P_+\}$, pairwise non-isomorphic.

# Examples
**Example** (p. 114): For $\mathfrak{sl}(2, \mathbb{C})$, $P_+ = \mathbb{Z}_+ = \{0, 1, 2, \ldots\}$, and $L_n$ is the $(n+1)$-dimensional irreducible.

**Example** (p. 123): For $A_n = \mathfrak{sl}(n+1, \mathbb{C})$, $P_+ = \{(\lambda_1, \ldots, \lambda_n, 0) \mid \lambda_i \in \mathbb{Z}, \lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_n \geq 0\}$.

# Relationships
## Builds Upon
- **Integral weight** -- adds the dominance (non-negativity) condition

## Enables
- **Finite-dimensional criterion** -- $L_\lambda$ finite-dimensional iff $\lambda \in P_+$
- **Classification of irreducible representations** -- $P_+$ indexes them

## Contrasts With
- **Integral weight** -- integral weights satisfy $\langle \lambda, \alpha^\vee \rangle \in \mathbb{Z}$; dominant integral additionally requires $\geq 0$

# Common Errors
- **Error**: Forgetting the integrality condition and only checking dominance ($\geq 0$)
  **Correction**: Both integrality ($\in \mathbb{Z}$) and dominance ($\geq 0$) are required

# Common Confusions
- **Confusion**: Confusing $P_+$ (dominant integral weights) with $C_+$ (positive Weyl chamber)
  **Clarification**: $C_+$ is an open cone; $P_+ = P \cap \overline{C_+}$ is a discrete set (lattice points in the closed chamber)

# Source Reference
Chapter 9, Section 9.3, Definition 9.16, equations (9.7)-(9.8), p. 114.

# Verification Notes
- Definition source: Direct from Definition 9.16
- Confidence rationale: Explicit definition with clear notation
- Uncertainties: None
- Cross-reference status: Verified
