---
# === CORE IDENTIFICATION ===
concept: Solvability Lemma for Trace Condition
slug: cartan-criterion-solvability-lemma

# === CLASSIFICATION ===
category: structure-theory
subcategory: bilinear-forms
tier: advanced

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 75
section: "6.6. Killing form and Cartan criterion"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Lemma 6.39"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - jordan-decomposition-operators
  - engel-theorem
extends: []
related:
  - cartan-criterion-solvability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the trace condition on commutators imply solvability?"
---

# Quick Definition

If $\mathfrak{g} \subset \mathfrak{gl}(V)$ satisfies $\operatorname{tr}(xy) = 0$ for all $x \in [\mathfrak{g}, \mathfrak{g}]$ and $y \in \mathfrak{g}$, then $\mathfrak{g}$ is solvable. This is the key lemma in the proof of the Cartan criterion.

# Core Definition

**Lemma 6.39** (Kirillov, p. 75): Let $V$ be a complex vector space and $\mathfrak{g} \subset \mathfrak{gl}(V)$ a Lie subalgebra such that $\operatorname{tr}(xy) = 0$ for any $x \in [\mathfrak{g}, \mathfrak{g}]$, $y \in \mathfrak{g}$. Then $\mathfrak{g}$ is solvable.

# Prerequisites

- **Jordan decomposition (operators)** — Uses the conjugate semisimple part $\bar{A}_s$
- **Engel theorem** — Used to conclude nilpotency of $[\mathfrak{g}, \mathfrak{g}]$

# Key Properties

1. The proof shows every $x \in [\mathfrak{g}, \mathfrak{g}]$ has all eigenvalues zero
2. Uses $\operatorname{tr}(x \bar{x}_s) = \sum |\lambda_i|^2 = 0$ where $\bar{x}_s$ is the conjugate semisimple part
3. The conjugate semisimple part satisfies $\operatorname{ad} \bar{x}_s = Q(\operatorname{ad} x)$, so $[\bar{x}_s, z_i] \in [\mathfrak{g}, \mathfrak{g}]$
4. Engel's theorem then gives nilpotency of $[\mathfrak{g}, \mathfrak{g}]$, hence solvability

# Context & Application

This lemma is the technical heart of the Cartan criterion proof. The clever use of the conjugate semisimple part $\bar{x}_s$ (which has complex conjugate eigenvalues) allows extracting $\sum |\lambda_i|^2 = 0$ from the trace condition.

# Relationships

## Enables
- **Cartan criterion (solvability)** — Applied to $\operatorname{ad} \mathfrak{g} \subset \mathfrak{gl}(\mathfrak{g})$

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.6, page 75. Lemma 6.39.

# Verification Notes

- Definition source: Direct from Lemma 6.39
- Confidence rationale: Explicit lemma with detailed proof
- Uncertainties: None
- Cross-reference status: Verified
