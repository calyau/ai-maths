---
# === CORE IDENTIFICATION ===
concept: Cartan Subalgebra
slug: cartan-subalgebra

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Complex Semisimple Lie Algebras"
chapter_number: 7
pdf_page: 84
section: "7.2. Cartan subalgebra"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "CSA"
  - "maximal torus (Lie algebra)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - toroidal-subalgebra
  - semisimple-lie-algebra
extends:
  - toroidal-subalgebra
related:
  - root-decomposition
  - rank-of-lie-algebra
  - cartan-conjugacy
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Cartan subalgebra?"
  - "How does the Cartan subalgebra determine the root decomposition?"
---

# Quick Definition

A Cartan subalgebra $\mathfrak{h} \subset \mathfrak{g}$ of a semisimple Lie algebra is a toroidal subalgebra that equals its own centralizer: $C(\mathfrak{h}) = \mathfrak{h}$. It is the maximal commutative subalgebra of semisimple elements, and its dimension is the rank of $\mathfrak{g}$.

# Core Definition

**Definition 7.8** (Kirillov, p. 84): Let $\mathfrak{g}$ be a semisimple Lie algebra. A Cartan subalgebra $\mathfrak{h} \subset \mathfrak{g}$ is a toroidal subalgebra which coincides with its centralizer: $C(\mathfrak{h}) = \{x \mid [x, h] = 0 \text{ for all } h \in \mathfrak{h}\} = \mathfrak{h}$.

**Remark 7.9**: This definition is specific to semisimple Lie algebras; the general definition differs.

# Prerequisites

- **Toroidal subalgebra** — A Cartan subalgebra is a special toroidal subalgebra
- **Semisimple Lie algebra** — The definition requires semisimplicity

# Key Properties

1. Every maximal toroidal subalgebra is a Cartan subalgebra (Theorem 7.11)
2. Cartan subalgebras exist in every complex semisimple Lie algebra (Corollary 7.12)
3. Any two Cartan subalgebras are conjugate under $\operatorname{Ad} G$ (Theorem 7.13)
4. All Cartan subalgebras have the same dimension = rank of $\mathfrak{g}$ (Corollary 7.14)
5. The condition $C(\mathfrak{h}) = \mathfrak{h}$ means $\mathfrak{g}_0 = \mathfrak{h}$ in the eigenspace decomposition

# Construction / Recognition

## To Construct:
1. Find a semisimple element $h_1$
2. Extend to a maximal commuting set of semisimple elements
3. The resulting toroidal subalgebra is automatically Cartan (Theorem 7.11)

## To Verify:
1. Check $\mathfrak{h}$ is commutative and all elements are semisimple
2. Verify $C(\mathfrak{h}) = \mathfrak{h}$

# Context & Application

The Cartan subalgebra is the cornerstone of the structure theory of semisimple Lie algebras. It determines the root decomposition, which in turn determines the algebra up to isomorphism. The conjugacy theorem ensures the root system is independent of the choice of Cartan subalgebra.

# Examples

**Example 7.10** (p. 84): For $\mathfrak{g} = \mathfrak{sl}(n, \mathbb{C})$, $\mathfrak{h} = \{\text{diagonal matrices with trace } 0\}$ is a Cartan subalgebra. It is commutative, every element is semisimple, and choosing $h$ with distinct eigenvalues shows $C(\mathfrak{h}) = \mathfrak{h}$.

**Example 7.15** (p. 85): $\operatorname{rank}(\mathfrak{sl}(n, \mathbb{C})) = n - 1$.

# Relationships

## Builds Upon
- **Toroidal subalgebra** — A Cartan subalgebra is a maximal toroidal subalgebra

## Enables
- **Root decomposition** — $\mathfrak{g} = \mathfrak{h} \oplus \bigoplus_{\alpha \in R} \mathfrak{g}_\alpha$
- **Rank of Lie algebra** — $\operatorname{rank}(\mathfrak{g}) = \dim \mathfrak{h}$
- **Root system** — The set of nonzero weights for $\operatorname{ad} \mathfrak{h}$

## Related
- **Cartan conjugacy** — Any two Cartan subalgebras are conjugate

# Common Errors

- **Error**: Using this definition for non-semisimple algebras
  **Correction**: For general algebras, a different definition is used (self-normalizing nilpotent subalgebra)

# Common Confusions

- **Confusion**: Thinking the Cartan subalgebra is unique
  **Clarification**: It is unique only up to conjugation; there are many Cartan subalgebras, but they are all equivalent under $\operatorname{Ad} G$

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.2, pages 84-85. Definition 7.8, Example 7.10, Theorem 7.11, Theorem 7.13, Corollary 7.14.

# Verification Notes

- Definition source: Direct from Definition 7.8
- Confidence rationale: Central definition with existence and conjugacy theorems
- Uncertainties: None
- Cross-reference status: Verified
