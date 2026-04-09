---
# === CORE IDENTIFICATION ===
concept: Irreducible Representation on Root Multiples
slug: irreducible-multiples-representation

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: advanced

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
  - "Lemma 7.20"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sl2-subalgebra-of-root
  - root-subspace
extends: []
related:
  - irreducibility-of-multiples
  - structure-theorem-roots
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why is the space of root multiples an irreducible sl(2) representation?"
---

# Quick Definition

For a root $\alpha$, the subspace $V = \mathbb{C}h_\alpha \oplus \bigoplus_{k \neq 0} \mathfrak{g}_{k\alpha}$ is an irreducible representation of $\mathfrak{sl}(2, \mathbb{C})_\alpha$. This is the key lemma proving that root spaces are one-dimensional and $2\alpha$ is never a root.

# Core Definition

**Lemma 7.20** (Kirillov, p. 87): Let $\alpha$ be a root and $\mathfrak{sl}(2, \mathbb{C})_\alpha$ as in Lemma 7.19. The subspace $V = \mathbb{C}h_\alpha \oplus \bigoplus_{k \in \mathbb{Z}, k \neq 0} \mathfrak{g}_{k\alpha}$ is an irreducible representation of $\mathfrak{sl}(2, \mathbb{C})_\alpha$.

Irreducibility follows from the fact that $V[0] = \mathbb{C}h_\alpha$ is one-dimensional, and by Exercise 5.1, this implies irreducibility.

# Prerequisites

- **sl(2) subalgebra of a root** — $V$ is a representation of this subalgebra
- **Root subspace** — Components of $V$

# Key Properties

1. Weight decomposition: $V[2k] = \mathfrak{g}_{k\alpha}$, $V[0] = \mathbb{C}h_\alpha$
2. Zero weight space is one-dimensional, forcing irreducibility
3. Since $\dim \mathfrak{g}_\alpha = \dim V[2] = 1$ in the irreducible, $\operatorname{ad} e_\alpha\colon \mathfrak{g}_\alpha \to \mathfrak{g}_{2\alpha}$ is zero
4. This means $V$ has highest weight 2: $V = \mathfrak{g}_{-\alpha} \oplus \mathbb{C}h_\alpha \oplus \mathfrak{g}_\alpha$

# Relationships

## Enables
- **Irreducibility of multiples** — Proves $2\alpha$ is never a root
- **One-dimensionality of root spaces** — Follows from irreducible $\mathfrak{sl}(2)$ weight spaces

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.3, page 87. Lemma 7.20.

# Verification Notes

- Definition source: Direct from Lemma 7.20
- Confidence rationale: Explicit lemma with proof
- Uncertainties: None
- Cross-reference status: Verified
