---
# === CORE IDENTIFICATION ===
concept: Associated Graded Algebra
slug: graded-algebra

# === CLASSIFICATION ===
category: enveloping-algebras
subcategory: pbw-theorem
tier: advanced

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 53
section: "4.9 Poincare-Birkhoff-Witt theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Gr Ug"
  - "associated graded"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - filtered-algebra
extends: []
related:
  - pbw-theorem
  - universal-enveloping-algebra
contrasts_with:
  - filtered-algebra

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the associated graded algebra of the universal enveloping algebra?"
---

# Quick Definition

The associated graded algebra $\mathrm{Gr}\, U\mathfrak{g} = \bigoplus_p (F^p U\mathfrak{g}) / F^{p-1} U\mathfrak{g}$ is a commutative algebra obtained from the filtration. By the PBW theorem, $\mathrm{Gr}\, U\mathfrak{g} \cong S\mathfrak{g}$.

# Core Definition

**Corollary 4.59** (Kirillov, p. 53): The associated graded algebra $\mathrm{Gr}\, U\mathfrak{g} = \bigoplus_p (F^p U\mathfrak{g}) / F^{p-1} U\mathfrak{g}$ is commutative.

**Theorem 4.61** (p. 54): $\mathrm{Gr}\, U\mathfrak{g} \cong S\mathfrak{g}$ naturally, via $a_1 \cdots a_p \mapsto a_1 \cdots a_p \mod F^{p-1}$.

# Prerequisites

- **Filtered algebra** — The associated graded is constructed from the filtration

# Key Properties

1. Commutative (even though $U\mathfrak{g}$ is not)
2. Isomorphic to the symmetric algebra $S\mathfrak{g} \cong K[x_1, \ldots, x_n]$
3. The isomorphism is the content of the PBW theorem

# Relationships

## Builds Upon
- **Filtered algebra** — The associated graded is derived from the filtration

## Related
- **PBW theorem** — Establishes $\mathrm{Gr}\, U\mathfrak{g} \cong S\mathfrak{g}$

## Contrasts With
- **Filtered algebra** — The filtration is on $U\mathfrak{g}$; the graded algebra is a simpler derived object

# Source Reference

Chapter 4, Section 4.9, Corollary 4.59, Theorem 4.61, pp. 53-54.

# Verification Notes

- Definition source: Direct from Corollary 4.59 and Theorem 4.61
- Confidence rationale: Explicit statements
- Uncertainties: None
- Cross-reference status: Verified
