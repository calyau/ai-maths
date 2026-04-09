---
# === CORE IDENTIFICATION ===
concept: Exterior Power Representation
slug: exterior-power-representation

# === CLASSIFICATION ===
category: representations
subcategory: highest-weight-theory
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Semisimple Lie Algebras"
chapter_number: 9
pdf_page: 116
section: "9.6 Representations of sl(n,C)"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "Lambda^k V"
  - "exterior powers"
  - "alternating power"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - representations-of-sln
  - standard-representation-type-a
extends: []
related:
  - fundamental-weights-type-a
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are exterior powers and how do they give representations?"
  - "What are the fundamental representations of sl(n,C)?"
---

# Quick Definition
The $k$-th exterior power $\Lambda^k V$ of a representation $V$ is a representation where the Lie algebra acts by the Leibniz rule. For $\mathfrak{sl}(n+1, \mathbb{C})$, the representations $\Lambda^k \mathbb{C}^{n+1}$ ($k = 1, \ldots, n$) are the fundamental representations corresponding to the fundamental weights $\omega_k$.

# Core Definition
(Kirillov, Section 9.6, p. 116): The exterior powers of the standard representation give the fundamental representations of $\mathfrak{sl}(n+1, \mathbb{C})$. For $V = \mathbb{C}^{n+1}$, the representation $\Lambda^k V$ has dimension $\binom{n+1}{k}$ and highest weight $\omega_k = e_1 + \cdots + e_k$.

# Prerequisites
- **Representations of sl(n,C)** -- exterior powers are key building blocks
- **Standard representation type A** -- the representation being wedged

# Key Properties
1. $\dim \Lambda^k \mathbb{C}^{n+1} = \binom{n+1}{k}$
2. $\Lambda^k V$ is irreducible with highest weight $\omega_k$ (the $k$-th fundamental weight)
3. $\Lambda^{n+1} \mathbb{C}^{n+1} \cong \mathbb{C}$ is the trivial representation (determinant)
4. $\Lambda^k V \cong (\Lambda^{n+1-k} V)^*$ as $\mathfrak{sl}(n+1, \mathbb{C})$-modules
5. The action is: $x \cdot (v_1 \wedge \cdots \wedge v_k) = \sum_i v_1 \wedge \cdots \wedge xv_i \wedge \cdots \wedge v_k$

# Context & Application
Exterior powers provide the most explicit construction of the fundamental representations of $\mathfrak{sl}(n+1, \mathbb{C})$. Every irreducible representation can be obtained from tensor products of these fundamental representations (and then projecting to irreducible components). This connects the abstract highest-weight theory to concrete linear algebra constructions.

# Examples
**Example**: For $\mathfrak{sl}(3, \mathbb{C})$: $\Lambda^1 \mathbb{C}^3 = \mathbb{C}^3$ (standard, $\omega_1$), $\Lambda^2 \mathbb{C}^3 \cong (\mathbb{C}^3)^*$ (dual standard, $\omega_2$).

# Relationships
## Builds Upon
- **Standard representation** -- the base representation being wedged

## Enables
- **Fundamental representations of type A** -- exterior powers realize them
- **General irreducible representations** -- via Schur functors

# Source Reference
Chapter 9, Section 9.6, p. 116.

# Verification Notes
- Definition source: Synthesized from section context; section content truncated
- Confidence rationale: Medium -- standard result consistent with source
- Uncertainties: Exact presentation in source not verified due to truncation
- Cross-reference status: Verified
