---
# === CORE IDENTIFICATION ===
concept: Cohomology Vanishing for Semisimple Algebras
slug: cohomology-vanishing

# === CLASSIFICATION ===
category: structure-theory
subcategory: complete-reducibility
tier: advanced

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 79
section: "6.9. Complete reducibility of representations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Whitehead's lemma"
  - "H^1(g,V) = 0"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semisimple-lie-algebra
  - casimir-element
  - complete-reducibility
extends: []
related:
  - levi-decomposition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why does Lie algebra cohomology vanish for semisimple algebras?"
---

# Quick Definition

For a semisimple Lie algebra $\mathfrak{g}$ and any finite-dimensional representation $V$, $H^1(\mathfrak{g}, V) = \operatorname{Ext}^1(\mathbb{C}, V) = 0$. This is equivalent to complete reducibility and is the key vanishing result of the theory.

# Core Definition

**Lemma 6.59** (Kirillov, p. 80): $H^1(\mathfrak{g}, V) = 0$ for any representation $V$ of a semisimple Lie algebra $\mathfrak{g}$.

More generally, $H^i(\mathfrak{g}, V) = 0$ for all $i > 0$ and all non-trivial irreducible $V$ (Remark, p. 81).

# Prerequisites

- **Semisimple Lie algebra** — The vanishing holds for semisimple algebras
- **Casimir element** — Used to prove the irreducible case
- **Complete reducibility** — Equivalent formulation

# Key Properties

1. $H^1(\mathfrak{g}, V) = 0$ for irreducible $V$: trivial case by nilpotency argument, non-trivial by Casimir eigenvalue separation
2. General case by long exact sequence and induction on dimension
3. $H^2(\mathfrak{g}, \mathbb{C}) = 0$ gives the Levi decomposition
4. $H^i(\mathfrak{g}, \mathbb{C})$ can be nonzero — it equals topological cohomology of the compact form

# Context & Application

The vanishing of $H^1$ is the homological algebra formulation of complete reducibility. The vanishing of $H^2$ implies the Levi theorem. These are the first instances of the powerful interaction between Lie algebra cohomology and structure theory.

# Examples

**Remark 6.60** (p. 81): For connected, simply-connected compact $G$ with $\mathfrak{g} = \operatorname{Lie}(G)$: $H^i(\mathfrak{g}, \mathbb{R}) = H^i(G, \mathbb{R})$ (de Rham cohomology).

# Relationships

## Builds Upon
- **Casimir element** — Separates eigenvalues in the proof

## Enables
- **Complete reducibility** — Equivalent formulation
- **Levi decomposition** — $H^2 = 0$ implies existence

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.9, pages 79-81. Lemma 6.58, Lemma 6.59, Remark 6.60.

# Verification Notes

- Definition source: Direct from Lemmas 6.58, 6.59
- Confidence rationale: Explicit lemmas with proofs
- Uncertainties: Higher cohomology vanishing stated without proof
- Cross-reference status: Verified
