---
# === CORE IDENTIFICATION ===
concept: Conjugate Elements
slug: conjugate-elements

# === CLASSIFICATION ===
category: galois-theory
subcategory: field-automorphisms
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Galois Theory"
chapter_number: 23
pdf_page: 307
section: "23.1 Field Automorphisms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "conjugate over F"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - algebraic-element
  - minimal-polynomial
extends: []
related:
  - galois-group
  - field-automorphism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are conjugate elements in a field extension?"
---

# Quick Definition

Two elements $\alpha, \beta$ in an extension field $E$ of $F$ are conjugate over $F$ if they share the same minimal polynomial over $F$.

# Core Definition

Let $E$ be an algebraic extension of a field $F$. Two elements $\alpha, \beta \in E$ are **conjugate** over $F$ if they have the same minimal polynomial (Judson, p. 308).

If $\alpha$ and $\beta$ are conjugate over $F$, there exists an isomorphism $\sigma: F(\alpha) \to F(\beta)$ that is the identity on $F$ (Proposition 23.6).

# Prerequisites

- **Algebraic element** — Conjugate elements must be algebraic
- **Minimal polynomial** — Conjugacy is defined via the minimal polynomial

# Key Properties

1. Conjugate elements are roots of the same irreducible polynomial over $F$
2. Galois group automorphisms map elements to their conjugates (Proposition 23.5)
3. If $\alpha$ and $\beta$ are conjugate, then $F(\alpha) \cong F(\beta)$ (Proposition 23.6)

# Examples

**Example 1** (p. 308): In $\mathbb{Q}(\sqrt{2})$, the elements $\sqrt{2}$ and $-\sqrt{2}$ are conjugate over $\mathbb{Q}$ since both are roots of $x^2 - 2$.

**Example 2**: The four roots of $x^4 - 2$ (namely $\sqrt[4]{2}, -\sqrt[4]{2}, i\sqrt[4]{2}, -i\sqrt[4]{2}$) are all conjugate over $\mathbb{Q}$.

# Relationships

## Builds Upon
- **Minimal polynomial** — Conjugacy means having the same minimal polynomial

## Related
- **Galois group** — Automorphisms permute conjugate elements
- **Field automorphism** — Maps elements to their conjugates

# Source Reference

Chapter 23: Galois Theory, Section 23.1, page 308. See Propositions 23.5, 23.6.

# Verification Notes

- Definition source: Direct from p. 308
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
