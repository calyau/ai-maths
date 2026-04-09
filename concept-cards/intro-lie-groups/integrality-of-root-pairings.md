---
# === CORE IDENTIFICATION ===
concept: Integrality of Root Pairings
slug: integrality-of-root-pairings

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
  - "integer pairing condition"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root
  - sl2-subalgebra-of-root
extends: []
related:
  - cartan-matrix
  - structure-theorem-roots
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why are the numbers <h_alpha, beta> integers?"
---

# Quick Definition

For any two roots $\alpha, \beta$, the number $\langle h_\alpha, \beta \rangle = \frac{2(\alpha, \beta)}{(\alpha, \alpha)}$ is an integer. This integrality condition follows from the fact that roots are weights of $\mathfrak{sl}(2)$ representations, which have integer weights.

# Core Definition

**Theorem 7.21, part (3)** (Kirillov, p. 87): For any two roots $\alpha, \beta$,

$$\langle h_\alpha, \beta \rangle = \frac{2(\alpha, \beta)}{(\alpha, \alpha)} \in \mathbb{Z}.$$

# Prerequisites

- **Root** — The pairing is between roots
- **sl(2) subalgebra of a root** — Provides the representation-theoretic proof

# Key Properties

1. The proof: elements of $\mathfrak{g}_\beta$ have weight $\langle h_\alpha, \beta \rangle$ under $\mathfrak{sl}(2, \mathbb{C})_\alpha$, and weights of finite-dimensional $\mathfrak{sl}(2)$ representations are integers (Theorem 5.7)
2. These integers are the entries of the Cartan matrix
3. Constrains the geometry: $\frac{2(\alpha,\beta)}{(\alpha,\alpha)} \cdot \frac{2(\beta,\alpha)}{(\beta,\beta)} = 4\cos^2\theta \in \{0, 1, 2, 3, 4\}$

# Context & Application

Integrality is the fundamental arithmetic constraint on root systems. It forces roots to lie in a lattice-like structure and restricts the possible angles between roots to a finite set, ultimately leading to the classification via Dynkin diagrams.

# Relationships

## Builds Upon
- **sl(2) subalgebra** — Weights of $\mathfrak{sl}(2)$ reps are integers

## Enables
- **Cartan matrix** — Entries are these integer pairings
- **Root system classification** — Constrained by integrality

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.3, page 87. Theorem 7.21(3).

# Verification Notes

- Definition source: Direct from Theorem 7.21(3)
- Confidence rationale: Explicit theorem part with clear proof
- Uncertainties: None
- Cross-reference status: Verified
