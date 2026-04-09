---
# === CORE IDENTIFICATION ===
concept: Splitting Field Uniqueness
slug: splitting-field-uniqueness

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
section: "21.2 Splitting Fields"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - splitting-field
extends: []
related:
  - galois-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Is the splitting field of a polynomial unique?"
---

# Quick Definition

The splitting field of a polynomial $p(x) \in F[x]$ is unique up to isomorphism. Any two splitting fields of the same polynomial over the same base field are isomorphic via an isomorphism fixing $F$.

# Core Definition

**Corollary 21.36.** Let $p(x)$ be a polynomial in $F[x]$. Then there exists a splitting field $K$ of $p(x)$ that is unique up to isomorphism (Judson, p. 284).

This follows from Theorem 21.34, which shows that any isomorphism $\phi: E \to F$ extends to an isomorphism between the splitting fields of corresponding polynomials.

# Prerequisites

- **Splitting field** — The theorem concerns splitting fields

# Key Properties

1. Existence: a splitting field always exists (Theorem 21.31)
2. Uniqueness: any two splitting fields are isomorphic (Corollary 21.36)
3. The isomorphism can be chosen to fix the base field
4. This makes the Galois group well-defined

# Context & Application

Uniqueness of splitting fields is crucial because it ensures the Galois group of a polynomial is well-defined (independent of which splitting field is chosen).

# Examples

**Example 1**: Both $\mathbb{Q}(\sqrt{2})$ and $\mathbb{Q}(-\sqrt{2})$ are splitting fields of $x^2 - 2$ over $\mathbb{Q}$; they are the same field.

# Relationships

## Builds Upon
- **Splitting field** — Establishes uniqueness

## Enables
- **Galois group** — Well-definedness depends on splitting field uniqueness

# Source Reference

Chapter 21: Fields, Section 21.2, page 284. Theorem 21.34, Corollary 21.36.

# Verification Notes

- Definition source: Direct from Corollary 21.36, p. 284
- Confidence: HIGH — explicit corollary
- Cross-reference status: Verified
- Uncertainties: None
