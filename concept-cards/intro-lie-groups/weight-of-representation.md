---
# === CORE IDENTIFICATION ===
concept: Weight of a Representation
slug: weight-of-representation

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
  - weight
  - "weight of V"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - representation-of-lie-algebra
  - cartan-subalgebra
extends: []
related:
  - weight-space
  - weight-set
  - weight-decomposition-theorem
  - integral-weight
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a weight of a representation of a semisimple Lie algebra?"
  - "How do I classify irreducible representations using highest weights?"
  - "What must I know before studying representations of semisimple Lie algebras?"
---

# Quick Definition
A weight of a representation $V$ of a semisimple Lie algebra $\mathfrak{g}$ is an element $\lambda \in \mathfrak{h}^*$ such that the corresponding weight space $V[\lambda]$ is non-zero. Weights generalize the notion of eigenvalues for the simultaneous action of the Cartan subalgebra.

# Core Definition
**Definition 9.1** (Kirillov, p. 110): Let $V$ be a representation of $\mathfrak{g}$. A vector $v \in V$ is called a *vector of weight* $\lambda \in \mathfrak{h}^*$ if, for any $h \in \mathfrak{h}$, one has $hv = \langle \lambda, h \rangle v$. If $V[\lambda] \neq 0$, then $\lambda$ is called a *weight* of $V$.

# Prerequisites
- **Representation of a Lie algebra** -- weights are defined for representations
- **Cartan subalgebra** -- weights are elements of $\mathfrak{h}^*$, the dual of the Cartan subalgebra

# Key Properties
1. Vectors of different weights are linearly independent (standard linear algebra)
2. The set of weights $P(V)$ is finite for any finite-dimensional representation
3. All weights of a finite-dimensional representation are integral: $P(V) \subset P$ (Theorem 9.2)
4. Weights are simultaneous eigenvalues for all elements of $\mathfrak{h}$

# Construction / Recognition
## To identify weights of a representation
1. Fix a Cartan subalgebra $\mathfrak{h} \subset \mathfrak{g}$
2. Simultaneously diagonalize the action of all $h \in \mathfrak{h}$ on $V$
3. Each simultaneous eigenvalue is a linear functional $\lambda \in \mathfrak{h}^*$
4. If the corresponding eigenspace is non-zero, $\lambda$ is a weight of $V$

# Context & Application
Weights are the fundamental tool for analyzing representations of semisimple Lie algebras. Just as representations of $\mathfrak{sl}(2, \mathbb{C})$ are classified by their eigenvalues for $h$, representations of general semisimple Lie algebras are analyzed via their weights. The weight decomposition is the starting point for the classification of irreducible representations via highest weights.

# Examples
**Example** (p. 110): For the adjoint representation, the weights are exactly the roots $R$ together with zero (with multiplicity equal to the rank).

**Example** (p. 110, cf. Section 5.1): For $\mathfrak{g} = \mathfrak{sl}(2, \mathbb{C})$, weights reduce to eigenvalues of $h$, recovering the theory from Section 5.1.

# Relationships
## Builds Upon
- **Cartan subalgebra** -- weights live in $\mathfrak{h}^*$
- **Representation of a Lie algebra** -- weights are defined for representations

## Enables
- **Weight space** -- the eigenspace for a given weight
- **Weight decomposition theorem** -- every finite-dimensional representation decomposes by weights
- **Highest weight representation** -- distinguished by a maximal weight

## Related
- **Root** -- roots are the weights of the adjoint representation
- **Integral weight** -- all weights of finite-dimensional representations are integral

# Common Errors
- **Error**: Confusing weights (elements of $\mathfrak{h}^*$) with roots (weights of the adjoint representation)
  **Correction**: Roots are a special case of weights; an arbitrary representation has weights that need not be roots

# Common Confusions
- **Confusion**: Thinking weights depend on the choice of basis for $V$
  **Clarification**: Weights depend only on the choice of Cartan subalgebra $\mathfrak{h}$, not on any basis for $V$

# Source Reference
Chapter 9: Representations of Semisimple Lie Algebras, Section 9.1 "Weight decomposition," Definition 9.1, p. 110.

# Verification Notes
- Definition source: Direct from Definition 9.1
- Confidence rationale: Explicit definition with clear terminology in source
- Uncertainties: None
- Cross-reference status: Connects to weight-space, weight-set, integral-weight (all planned)
