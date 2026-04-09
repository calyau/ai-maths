---
# === CORE IDENTIFICATION ===
concept: Weight Set
slug: weight-set

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
pdf_page: 110
section: "9.1 Weight decomposition"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "P(V)"
  - "set of weights"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - weight-of-representation
  - weight-space
extends: []
related:
  - weight-decomposition-theorem
  - integral-weight
  - weight-lattice
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the weight set P(V)?"
  - "How do I determine which weights appear in a representation?"
---

# Quick Definition
The weight set $P(V)$ of a representation $V$ is the set of all $\lambda \in \mathfrak{h}^*$ that occur as weights, i.e., for which the weight space $V[\lambda]$ is non-zero.

# Core Definition
**Definition 9.1** (Kirillov, p. 110): The set of all weights of $V$ is denoted $P(V)$:

$$P(V) = \{ \lambda \in \mathfrak{h}^* \mid V[\lambda] \neq 0 \}.$$

# Prerequisites
- **Weight of a representation** -- elements of $P(V)$ are weights
- **Weight space** -- $\lambda \in P(V)$ iff $V[\lambda] \neq 0$

# Key Properties
1. $P(V)$ is a finite set for any finite-dimensional representation $V$
2. $P(V) \subset P$ (the weight lattice) for any finite-dimensional representation (Theorem 9.2)
3. For a highest-weight module with highest weight $\lambda$: $P(V) \subset \lambda - Q_+$ where $Q_+ = \{\sum n_i \alpha_i, n_i \in \mathbb{Z}_+\}$ (Theorem 9.10)
4. $P(V)$ is invariant under the Weyl group for finite-dimensional $V$

# Construction / Recognition
1. Compute the weight decomposition of $V$
2. Collect all $\lambda$ for which $V[\lambda] \neq 0$
3. For highest-weight modules, the weights lie below the highest weight in the partial order defined by the positive roots

# Context & Application
The weight set encodes the "spectrum" of a representation with respect to the Cartan subalgebra. Two representations are isomorphic if and only if they have the same weight sets with the same multiplicities (for completely reducible representations). The weight set, together with multiplicities, is captured by the formal character of the representation.

# Examples
**Example** (p. 110): For the adjoint representation of $\mathfrak{g}$, the weight set is $P(\mathfrak{g}) = R \cup \{0\}$, where $R$ is the root system.

**Example** (p. 112): For the Verma module $M_\lambda$, the weight set is $P(M_\lambda) = \lambda - Q_+$ (Theorem 9.9).

# Relationships
## Builds Upon
- **Weight of a representation** -- $P(V)$ collects all weights
- **Weight space** -- non-vanishing weight spaces determine $P(V)$

## Enables
- **Character** -- the formal character records weights with multiplicities
- **Highest weight representation** -- classified by the maximal element of $P(V)$

## Related
- **Weight lattice** -- $P(V) \subset P$ for finite-dimensional representations
- **Root lattice** -- weights differ by elements of the root lattice

# Common Errors
- **Error**: Forgetting that $P(V)$ records only which weights appear, not their multiplicities
  **Correction**: The weight set is a set, not a multiset; multiplicities are recorded separately as $\dim V[\lambda]$

# Common Confusions
- **Confusion**: Confusing the weight set $P(V)$ with the weight lattice $P$
  **Clarification**: $P$ is the lattice of all integral weights; $P(V)$ is the finite subset of weights actually appearing in $V$

# Source Reference
Chapter 9: Representations of Semisimple Lie Algebras, Section 9.1, Definition 9.1 and equations (9.1)-(9.2), p. 110.

# Verification Notes
- Definition source: Direct from equation (9.2)
- Confidence rationale: Explicit definition with notation
- Uncertainties: None
- Cross-reference status: Verified
