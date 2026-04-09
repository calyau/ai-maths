---
# === CORE IDENTIFICATION ===
concept: Finite Field Existence and Uniqueness
slug: finite-field-existence-and-uniqueness

# === CLASSIFICATION ===
category: field-theory
subcategory: finite-fields
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Finite Fields"
chapter_number: 22
pdf_page: 292
section: "22.1 Structure of a Finite Field"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - finite-field
  - splitting-field
  - freshmans-dream
extends: []
related:
  - separable-polynomial
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do we know finite fields of every prime-power order exist?"
  - "Are finite fields of the same order isomorphic?"
---

# Quick Definition

For every prime $p$ and positive integer $n$, there exists a unique (up to isomorphism) finite field with $p^n$ elements. It is the splitting field of $x^{p^n} - x$ over $\mathbb{Z}_p$.

# Core Definition

**Theorem 22.6.** For every prime $p$ and every positive integer $n$, there exists a finite field $F$ with $p^n$ elements. Furthermore, any field of order $p^n$ is isomorphic to the splitting field of $x^{p^n} - x$ over $\mathbb{Z}_p$ (Judson, p. 294).

# Prerequisites

- **Finite field** — The theorem characterizes all finite fields
- **Splitting field** — The construction uses splitting fields
- **Freshman's Dream** — Used to show the roots form a subfield

# Key Properties

1. The polynomial $x^{p^n} - x$ has exactly $p^n$ distinct roots (separable since $f'(x) = -1$)
2. The roots of $x^{p^n} - x$ form a subfield (closed under $+, \times, -, /$ by Freshman's Dream)
3. Any two fields of order $p^n$ are isomorphic (uniqueness of splitting fields)
4. Subfields have order $p^m$ where $m \mid n$, and conversely (Theorem 22.7)

# Context & Application

This theorem completely classifies finite fields: they are parameterized by pairs $(p, n)$ with $p$ prime and $n \geq 1$. The classification is remarkably clean — there is exactly one field of each prime-power order, up to isomorphism.

# Examples

**Example 1** (p. 294): The lattice of subfields of $GF(p^{24})$ reflects the divisors of 24.

**Example 2**: $GF(8)$ is the unique field with 8 elements; it is the splitting field of $x^8 - x$ over $\mathbb{Z}_2$.

# Relationships

## Builds Upon
- **Splitting field** — Construction as splitting field of $x^{p^n} - x$
- **Freshman's Dream** — Proves roots form a field

# Source Reference

Chapter 22: Finite Fields, Section 22.1, pages 294–295. Theorem 22.6, Theorem 22.7.

# Verification Notes

- Definition source: Direct from Theorem 22.6, p. 294
- Confidence: HIGH — explicit theorem with proof
- Cross-reference status: Verified
- Uncertainties: None
