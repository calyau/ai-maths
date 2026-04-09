---
# === CORE IDENTIFICATION ===
concept: sl(2) Subalgebra Associated to a Root
slug: sl2-subalgebra-of-root

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
pdf_page: 87
section: "7.3. Root decomposition and root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "sl(2,C)_alpha"
  - "root sl(2) triple"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - coroot-of-lie-algebra
  - root-subspace
extends: []
related:
  - root-string
  - structure-theorem-roots
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does each root define an sl(2) subalgebra?"
  - "Why is the sl(2) subalgebra associated to a root important?"
---

# Quick Definition

For each root $\alpha$, choosing $e \in \mathfrak{g}_\alpha$, $f \in \mathfrak{g}_{-\alpha}$ with $(e, f) = \frac{2}{(\alpha, \alpha)}$ and $h_\alpha = \frac{2H_\alpha}{(\alpha, \alpha)}$ gives elements satisfying $[e, f] = h_\alpha$, $[h_\alpha, e] = 2e$, $[h_\alpha, f] = -2f$ — the relations of $\mathfrak{sl}(2, \mathbb{C})$.

# Core Definition

**Lemma 7.19** (Kirillov, p. 87): Let $e \in \mathfrak{g}_\alpha$, $f \in \mathfrak{g}_{-\alpha}$ with $(e, f) = \frac{2}{(\alpha, \alpha)}$, and $h_\alpha = \frac{2H_\alpha}{(\alpha, \alpha)}$. Then $\langle h_\alpha, \alpha \rangle = 2$ and $e, f, h_\alpha$ satisfy the relations of $\mathfrak{sl}(2, \mathbb{C})$. The resulting subalgebra is denoted $\mathfrak{sl}(2, \mathbb{C})_\alpha$.

# Prerequisites

- **Coroot of Lie algebra** — $h_\alpha$ is the coroot element
- **Root subspace** — $e \in \mathfrak{g}_\alpha$, $f \in \mathfrak{g}_{-\alpha}$

# Key Properties

1. $[h_\alpha, e] = 2e$, $[h_\alpha, f] = -2f$, $[e, f] = h_\alpha$
2. $\mathfrak{g}$ decomposes as a representation of each $\mathfrak{sl}(2, \mathbb{C})_\alpha$
3. The weights of $\mathfrak{g}_\beta$ under $\mathfrak{sl}(2, \mathbb{C})_\alpha$ are $\langle h_\alpha, \beta \rangle$, which are integers
4. $V = \mathbb{C}h_\alpha \oplus \bigoplus_{k \neq 0} \mathfrak{g}_{k\alpha}$ is an irreducible representation of $\mathfrak{sl}(2, \mathbb{C})_\alpha$ (Lemma 7.20)

# Context & Application

The $\mathfrak{sl}(2)$ subalgebras are the most powerful tool for studying the root structure. By considering $\mathfrak{g}$ as a representation of $\mathfrak{sl}(2, \mathbb{C})_\alpha$, one can apply the complete classification of $\mathfrak{sl}(2)$ representations (Chapter 5) to deduce integrality of $\langle h_\alpha, \beta \rangle$, one-dimensionality of root spaces, and the root string structure.

# Examples

**Example**: In $\mathfrak{sl}(3, \mathbb{C})$ with root $\alpha = e_1 - e_2$: $e = E_{12}$, $f = E_{21}$, $h_\alpha = E_{11} - E_{22}$.

# Relationships

## Builds Upon
- **Coroot of Lie algebra** — The element $h_\alpha$
- **Root subspace** — Sources of $e$ and $f$

## Enables
- **Structure theorem for roots** — Proves integrality, one-dimensionality, reflection invariance
- **Root string** — The decomposition of $\bigoplus_k \mathfrak{g}_{\beta + k\alpha}$ as $\mathfrak{sl}(2)$ representation

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.3, pages 87-88. Lemma 7.19, Lemma 7.20.

# Verification Notes

- Definition source: Direct from Lemma 7.19
- Confidence rationale: Explicitly constructed with verification
- Uncertainties: None
- Cross-reference status: Verified
