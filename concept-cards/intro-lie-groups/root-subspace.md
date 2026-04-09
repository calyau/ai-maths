---
# === CORE IDENTIFICATION ===
concept: Root Subspace
slug: root-subspace

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
pdf_page: 85
section: "7.3. Root decomposition and root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "root space"
  - "g_alpha"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root
  - root-decomposition
extends: []
related:
  - killing-form
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a root subspace?"
  - "What are the properties of root subspaces?"
---

# Quick Definition

The root subspace $\mathfrak{g}_\alpha$ for a root $\alpha$ is the one-dimensional eigenspace $\mathfrak{g}_\alpha = \{x \in \mathfrak{g} \mid [h, x] = \langle \alpha, h \rangle x \text{ for all } h \in \mathfrak{h}\}$. Each root subspace is one-dimensional and pairs non-degenerately with $\mathfrak{g}_{-\alpha}$ via the Killing form.

# Core Definition

From **Theorem 7.16** (Kirillov, p. 85):

$$\mathfrak{g}_\alpha = \{x \mid [h, x] = \langle \alpha, h \rangle x \text{ for all } h \in \mathfrak{h}\}.$$

**Theorem 7.21** (p. 87): Each root subspace is one-dimensional: $\dim \mathfrak{g}_\alpha = 1$.

# Prerequisites

- **Root** — The root $\alpha$ indexes the subspace
- **Root decomposition** — The subspace is part of the decomposition

# Key Properties

1. $\dim \mathfrak{g}_\alpha = 1$ for all $\alpha \in R$
2. $[\mathfrak{g}_\alpha, \mathfrak{g}_\beta] \subset \mathfrak{g}_{\alpha+\beta}$
3. The Killing form pairs $\mathfrak{g}_\alpha \otimes \mathfrak{g}_{-\alpha} \to \mathbb{C}$ non-degenerately
4. $\mathfrak{g}_\alpha \perp \mathfrak{g}_\beta$ whenever $\alpha + \beta \neq 0$
5. If $\alpha + \beta$ is a root, then $[\mathfrak{g}_\alpha, \mathfrak{g}_\beta] = \mathfrak{g}_{\alpha+\beta}$ (Theorem 7.21, part 7)

# Examples

**Example 7.17** (p. 86): $\mathfrak{g}_{e_i - e_j} = \mathbb{C} E_{ij}$ in $\mathfrak{sl}(n, \mathbb{C})$.

# Relationships

## Builds Upon
- **Root** — Indexed by roots

## Related
- **Killing form** — Provides the pairing between $\mathfrak{g}_\alpha$ and $\mathfrak{g}_{-\alpha}$

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.3, pages 85-88. Theorems 7.16, 7.21.

# Verification Notes

- Definition source: Direct from Theorem 7.16
- Confidence rationale: Explicitly defined, one-dimensionality proved
- Uncertainties: None
- Cross-reference status: Verified
