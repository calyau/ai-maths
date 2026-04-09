---
# === CORE IDENTIFICATION ===
concept: Algebraic Number
slug: algebraic-number

# === CLASSIFICATION ===
category: field-theory
subcategory: field-extensions
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Fields"
chapter_number: 21
pdf_page: 274
section: "21.1 Extension Fields"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - algebraic-element
extends:
  - algebraic-element
related:
  - transcendental-number
  - algebraic-closure
contrasts_with:
  - transcendental-number

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an algebraic number?"
---

# Quick Definition

A complex number that is algebraic over $\mathbb{Q}$ is called an algebraic number. The set of all algebraic numbers forms a field.

# Core Definition

A complex number that is algebraic over $\mathbb{Q}$ is an **algebraic number**. A **transcendental number** is an element of $\mathbb{C}$ that is transcendental over $\mathbb{Q}$ (Judson, p. 276).

The set of all algebraic numbers forms a field (Corollary 21.24).

# Prerequisites

- **Algebraic element** — An algebraic number is an algebraic element over $\mathbb{Q}$

# Key Properties

1. The algebraic numbers form a field (Corollary 21.24)
2. The algebraic numbers are countable (while $\mathbb{R}$ and $\mathbb{C}$ are uncountable)
3. Almost all real numbers are transcendental
4. $\sqrt{2}$, $i$, $\sqrt{2 + \sqrt{3}}$ are algebraic numbers

# Examples

**Example 1** (p. 276): $\sqrt{2}$ is algebraic (root of $x^2 - 2$).

**Example 2** (p. 276): $\pi$ and $e$ are transcendental numbers.

# Relationships

## Builds Upon
- **Algebraic element** — Specialized to base field $\mathbb{Q}$

## Contrasts With
- **Transcendental number** — A complex number not algebraic over $\mathbb{Q}$

## Related
- **Algebraic closure** — The algebraic numbers form the algebraic closure of $\mathbb{Q}$ in $\mathbb{C}$

# Source Reference

Chapter 21: Fields, Section 21.1, page 276. See Corollary 21.24.

# Verification Notes

- Definition source: Direct from p. 276
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
