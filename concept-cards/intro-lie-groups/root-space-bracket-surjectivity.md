---
# === CORE IDENTIFICATION ===
concept: Root Space Bracket Surjectivity
slug: root-space-bracket-surjectivity

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-subspace
  - root-string
extends: []
related:
  - structure-theorem-roots
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When does the bracket of root spaces equal the next root space?"
---

# Quick Definition

If $\alpha$, $\beta$, and $\alpha + \beta$ are all roots, then $[\mathfrak{g}_\alpha, \mathfrak{g}_\beta] = \mathfrak{g}_{\alpha+\beta}$. The bracket is surjective onto the sum root space, not just contained in it.

# Core Definition

**Theorem 7.21, part (7)** (Kirillov, p. 88): If $\alpha, \beta$ are roots such that $\alpha + \beta$ is also a root, then $[\mathfrak{g}_\alpha, \mathfrak{g}_\beta] = \mathfrak{g}_{\alpha+\beta}$.

# Prerequisites

- **Root subspace** — The bracket is between root subspaces
- **Root string** — Uses the irreducible $\mathfrak{sl}(2)$ representation on the root string

# Key Properties

1. We already know $[\mathfrak{g}_\alpha, \mathfrak{g}_\beta] \subset \mathfrak{g}_{\alpha+\beta}$
2. Since $\dim \mathfrak{g}_{\alpha+\beta} = 1$, surjectivity means $[\mathfrak{g}_\alpha, \mathfrak{g}_\beta] \neq 0$
3. Follows from $\mathfrak{sl}(2)$ theory: in an irreducible representation, $e$ acts non-trivially on non-highest-weight vectors

# Context & Application

This property ensures the Lie algebra is "generated" by the root spaces in a strong sense: the bracket structure is completely determined by the root system.

# Relationships

## Builds Upon
- **Root string** — Uses irreducibility of root strings

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.3, page 88. Theorem 7.21(7).

# Verification Notes

- Definition source: Direct from Theorem 7.21(7)
- Confidence rationale: Explicit theorem part
- Uncertainties: None
- Cross-reference status: Verified
