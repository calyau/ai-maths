---
# === CORE IDENTIFICATION ===
concept: Centralizer
slug: centralizer

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: intermediate

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
  - "C(h)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-algebra
extends: []
related:
  - cartan-subalgebra
  - toroidal-subalgebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the centralizer of a subalgebra?"
  - "How does the centralizer relate to the Cartan subalgebra?"
---

# Quick Definition

The centralizer $C(\mathfrak{h}) = \{x \in \mathfrak{g} \mid [x, h] = 0 \text{ for all } h \in \mathfrak{h}\}$ is the set of elements commuting with all of $\mathfrak{h}$. A Cartan subalgebra is defined by the condition $C(\mathfrak{h}) = \mathfrak{h}$.

# Core Definition

For a subalgebra $\mathfrak{h} \subset \mathfrak{g}$ (Kirillov, p. 84):

$$C(\mathfrak{h}) = \{x \in \mathfrak{g} \mid [x, h] = 0 \text{ for all } h \in \mathfrak{h}\}.$$

In the eigenspace decomposition $\mathfrak{g} = \bigoplus \mathfrak{g}_\alpha$, $C(\mathfrak{h}) = \mathfrak{g}_0$.

# Prerequisites

- **Lie algebra** — The centralizer is defined in any Lie algebra

# Key Properties

1. $C(\mathfrak{h})$ is always a subalgebra containing $\mathfrak{h}$ (when $\mathfrak{h}$ is commutative)
2. For a toroidal $\mathfrak{h}$: $C(\mathfrak{h}) = \mathfrak{g}_0$ in the eigenspace decomposition
3. Killing form restricted to $C(\mathfrak{h})$ is non-degenerate (by Theorem 7.7)
4. $C(\mathfrak{h})$ is reductive (by Cartan criterion argument, Step 2 of Theorem 7.11)

# Context & Application

The centralizer condition $C(\mathfrak{h}) = \mathfrak{h}$ is the defining property of Cartan subalgebras. The four-step proof of Theorem 7.11 shows that for maximal toroidal subalgebras, $C(\mathfrak{h})$ must be commutative, consist of semisimple elements, and hence equal $\mathfrak{h}$.

# Relationships

## Enables
- **Cartan subalgebra** — Defined by $C(\mathfrak{h}) = \mathfrak{h}$

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.2, page 84. Definition 7.8, Theorem 7.11.

# Verification Notes

- Definition source: Used in Definition 7.8
- Confidence rationale: Standard concept, explicitly used
- Uncertainties: None
- Cross-reference status: Verified
