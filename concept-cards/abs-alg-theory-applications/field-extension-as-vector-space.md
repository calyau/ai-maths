---
# === CORE IDENTIFICATION ===
concept: Field Extension as Vector Space
slug: field-extension-as-vector-space

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
  - extension-field
  - vector-space
extends: []
related:
  - degree-of-field-extension
  - basis
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can a field extension be viewed as a vector space?"
  - "Why is linear algebra useful in field theory?"
---

# Quick Definition

Every field extension $E/F$ can be viewed as a vector space over $F$, where elements of $E$ are vectors, elements of $F$ are scalars, and the dimension is $[E:F]$.

# Core Definition

Let $E$ be a field extension of $F$. If we regard $E$ as a vector space over $F$, then the elements in $E$ are vectors, the elements in $F$ are scalars, addition in $E$ is vector addition, and multiplication of an element of $E$ by an element of $F$ is scalar multiplication. This view is "especially fruitful if a field extension $E$ of $F$ is a finite dimensional vector space over $F$" (Judson, p. 278).

For $E = F(\alpha)$ with $\alpha$ algebraic of degree $n$, the set $\{1, \alpha, \alpha^2, \ldots, \alpha^{n-1}\}$ is a basis (Theorem 21.13).

# Prerequisites

- **Extension field** — The extension provides the vector space
- **Vector space** — The structure being applied

# Key Properties

1. $[E:F]$ is the dimension of $E$ as a vector space over $F$
2. For $F(\alpha)$ with $\alpha$ algebraic of degree $n$: basis is $\{1, \alpha, \ldots, \alpha^{n-1}\}$
3. The tower law $[K:F] = [K:E][E:F]$ is a statement about dimensions
4. This perspective allows linear algebra techniques to solve field theory problems

# Context & Application

This viewpoint is the crucial bridge between Chapters 20 and 21. Linear algebra tools — dimension, independence, basis — become available for studying field extensions. The degree $[E:F]$ then controls divisibility, impossibility of constructions, and the size of Galois groups.

# Examples

**Example 1** (p. 278): $\mathbb{C}$ as a vector space over $\mathbb{R}$ has basis $\{1, i\}$ and dimension 2.

**Example 2** (p. 280): $\mathbb{Q}(\sqrt{3}, \sqrt{5})$ as a vector space over $\mathbb{Q}$ has basis $\{1, \sqrt{3}, \sqrt{5}, \sqrt{15}\}$ and dimension 4.

# Relationships

## Builds Upon
- **Extension field** — The extension is the vector space
- **Vector space** — The abstract structure being applied

## Related
- **Degree of field extension** — $[E:F]$ is the dimension
- **Basis** — $\{1, \alpha, \ldots, \alpha^{n-1}\}$ for simple algebraic extensions

# Source Reference

Chapter 21: Fields, Section 21.1, page 278.

# Verification Notes

- Definition source: Direct from p. 278
- Confidence: HIGH — explicit discussion
- Cross-reference status: Verified
- Uncertainties: None
