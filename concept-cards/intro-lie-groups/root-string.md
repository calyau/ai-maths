---
# === CORE IDENTIFICATION ===
concept: Root String
slug: root-string

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
pdf_page: 88
section: "7.3. Root decomposition and root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "alpha-string through beta"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root
  - sl2-subalgebra-of-root
extends: []
related:
  - structure-theorem-roots
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a root string?"
  - "How does the sl(2) representation theory determine root strings?"
---

# Quick Definition

The $\alpha$-string through $\beta$ is the set of roots of the form $\beta + k\alpha$ ($k \in \mathbb{Z}$). By Theorem 7.21(6), the subspace $\bigoplus_k \mathfrak{g}_{\beta+k\alpha}$ is an irreducible representation of $\mathfrak{sl}(2, \mathbb{C})_\alpha$, so the string is an unbroken sequence of roots.

# Core Definition

**Theorem 7.21, part (6)** (Kirillov, p. 88): For roots $\alpha, \beta$ with $\beta \neq \pm\alpha$, the subspace

$$V = \bigoplus_{k \in \mathbb{Z}} \mathfrak{g}_{\beta + k\alpha}$$

is an irreducible representation of $\mathfrak{sl}(2, \mathbb{C})_\alpha$.

# Prerequisites

- **Root** — The string consists of roots
- **sl(2) subalgebra of a root** — The string is an $\mathfrak{sl}(2)$ representation

# Key Properties

1. The string is unbroken: if $\beta + k_1\alpha$ and $\beta + k_2\alpha$ are roots with $k_1 < k_2$, then $\beta + k\alpha$ is a root for all $k_1 \leq k \leq k_2$
2. The weights are $\langle h_\alpha, \beta + k\alpha \rangle = \langle h_\alpha, \beta \rangle + 2k$
3. The string has length $\langle h_\alpha, \beta \rangle + 1$ (as an $\mathfrak{sl}(2)$ representation dimension)
4. Irreducibility follows from $\dim \mathfrak{g}_{\beta+k\alpha} = 1$ (Theorem 7.21, part 2)

# Context & Application

Root strings are the combinatorial manifestation of $\mathfrak{sl}(2)$ representation theory applied to the root system. They determine the structure constants of the Lie algebra and constrain which sums of roots can be roots.

# Examples

**Example**: In $\mathfrak{sl}(3, \mathbb{C})$ with $\alpha = e_1 - e_2$, $\beta = e_2 - e_3$: the $\alpha$-string through $\beta$ is $\{e_2 - e_3, e_1 - e_3\}$ (i.e., $\beta$ and $\beta + \alpha$).

# Relationships

## Builds Upon
- **sl(2) subalgebra** — The string is an irreducible representation

## Related
- **Structure theorem for roots** — Part (6) of Theorem 7.21

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.3, page 88. Theorem 7.21(6).

# Verification Notes

- Definition source: Direct from Theorem 7.21(6)
- Confidence rationale: Explicit theorem part
- Uncertainties: None
- Cross-reference status: Verified
