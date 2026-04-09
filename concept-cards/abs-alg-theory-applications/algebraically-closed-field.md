---
# === CORE IDENTIFICATION ===
concept: Algebraically Closed Field
slug: algebraically-closed-field

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
  - field
  - polynomial
extends: []
related:
  - algebraic-closure
  - fundamental-theorem-of-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an algebraically closed field?"
---

# Quick Definition

A field $F$ is algebraically closed if every nonconstant polynomial in $F[x]$ has a root in $F$, or equivalently, every nonconstant polynomial factors completely into linear factors over $F$.

# Core Definition

A field $F$ is **algebraically closed** if every nonconstant polynomial in $F[x]$ has a root in $F$ (Judson, p. 281). Equivalently, $F$ is algebraically closed if and only if every nonconstant polynomial in $F[x]$ factors into linear factors over $F[x]$ (Theorem 21.25).

# Prerequisites

- **Field** — Algebraic closure is a property of fields
- **Polynomial** — Defined in terms of factoring polynomials

# Key Properties

1. Every nonconstant polynomial splits into linear factors (Theorem 21.25)
2. An algebraically closed field has no proper algebraic extension (Corollary 21.26)
3. $\mathbb{C}$ is algebraically closed (Theorem 21.28, proved in Chapter 23)
4. No finite field is algebraically closed

# Context & Application

Algebraically closed fields are the "complete" fields for polynomial equations. They play a role analogous to the real numbers for analysis — all equations are solvable. The most important example is $\mathbb{C}$.

# Examples

**Example 1** (p. 282): $\mathbb{C}$ is algebraically closed (Fundamental Theorem of Algebra, Theorem 21.28).

**Example 2**: $\mathbb{R}$ is not algebraically closed since $x^2 + 1$ has no root in $\mathbb{R}$.

**Example 3**: $\mathbb{Q}$ is not algebraically closed since $x^2 - 2$ has no root in $\mathbb{Q}$.

# Relationships

## Enables
- **Algebraic closure** — Every algebraic closure is algebraically closed

## Related
- **Fundamental Theorem of Algebra** — States that $\mathbb{C}$ is algebraically closed

# Source Reference

Chapter 21: Fields, Section 21.1, pages 281–282. See Theorems 21.25, 21.27, 21.28.

# Verification Notes

- Definition source: Direct from p. 281
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
