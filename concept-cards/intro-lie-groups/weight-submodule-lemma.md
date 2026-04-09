---
# === CORE IDENTIFICATION ===
concept: Weight Decomposition Preservation Lemma
slug: weight-submodule-lemma

# === CLASSIFICATION ===
category: representations
subcategory: highest-weight-theory
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Semisimple Lie Algebras"
chapter_number: 9
pdf_page: 113
section: "9.2 Highest-weight representations and Verma modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Lemma 9.11"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - weight-decomposition-theorem
extends: []
related:
  - verma-module
  - irreducible-highest-weight-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Do submodules and quotients of weight modules also have weight decompositions?"
---

# Quick Definition
If an $\mathfrak{h}$-module $M$ admits a weight decomposition with finite-dimensional weight spaces, then any submodule and any quotient of $M$ also admits a weight decomposition.

# Core Definition
**Lemma 9.11** (Kirillov, p. 113): Let $\mathfrak{h}$ be a commutative finite-dimensional Lie algebra and $M$ a module over $\mathfrak{h}$ (not necessarily finite-dimensional) which admits weight decomposition with finite-dimensional weight spaces. Then any submodule and quotient of $M$ also admits a weight decomposition.

# Prerequisites
- **Weight decomposition theorem** -- the property being preserved

# Key Properties
1. Applies to infinite-dimensional modules (important for Verma modules)
2. Requires finite-dimensionality of individual weight spaces, not of $M$ itself
3. The proof uses the existence of separating polynomials in $U\mathfrak{h} = S\mathfrak{h}$ (Exercise 9.1)

# Context & Application
This lemma is essential for the theory of Verma modules and their quotients. Since Verma modules have weight decompositions, this ensures that all their submodules and quotients (including $L_\lambda$) do as well. Without this, the weight-theoretic analysis of representations would not extend from Verma modules to their quotients.

# Examples
**Example** (p. 113): Applied in the proof of Theorem 9.10 to show that quotients of Verma modules admit weight decompositions.

# Relationships
## Builds Upon
- **Weight decomposition theorem** -- the property being generalized

## Enables
- **Irreducible highest-weight module** -- inherits weight decomposition from $M_\lambda$
- **Submodule analysis** -- submodules of Verma modules have weight decompositions

# Source Reference
Chapter 9, Section 9.2, Lemma 9.11, p. 113. Proof outlined in Exercise 9.1.

# Verification Notes
- Definition source: Direct from Lemma 9.11
- Confidence rationale: Explicit lemma statement
- Uncertainties: None
- Cross-reference status: Verified
