---
# === CORE IDENTIFICATION ===
concept: Splitting Field
slug: splitting-field

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
  - extension-field
  - kronecker-theorem
extends:
  - extension-field
related:
  - algebraic-closure
  - galois-group
  - normal-extension
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a splitting field?"
  - "How do splitting fields relate to Galois theory?"
  - "Is a splitting field unique?"
---

# Quick Definition

A splitting field of a polynomial $p(x) \in F[x]$ is the smallest extension field $E$ of $F$ over which $p(x)$ factors completely into linear factors. It is unique up to isomorphism.

# Core Definition

Let $F$ be a field and $p(x) = a_0 + a_1x + \cdots + a_nx^n$ be a nonconstant polynomial in $F[x]$. An extension field $E$ of $F$ is a **splitting field** of $p(x)$ if there exist elements $\alpha_1, \ldots, \alpha_n$ in $E$ such that $E = F(\alpha_1, \ldots, \alpha_n)$ and

$$p(x) = (x - \alpha_1)(x - \alpha_2) \cdots (x - \alpha_n)$$

(Judson, p. 282). A polynomial $p(x) \in F[x]$ **splits** in $E$ if it is the product of linear factors in $E[x]$.

# Prerequisites

- **Extension field** — A splitting field is a specific type of extension
- **Kronecker's Theorem** — Guarantees roots exist in some extension, enabling iterative construction

# Key Properties

1. A splitting field always exists (Theorem 21.31)
2. A splitting field is unique up to isomorphism (Corollary 21.36)
3. $[E:F] \leq n!$ where $n = \deg p(x)$
4. A splitting field is the smallest field over which $p(x)$ factors completely
5. Splitting fields are normal extensions (Theorem 23.19)

# Construction / Recognition

## To Construct:
1. Start with $p(x) \in F[x]$
2. Find a root $\alpha_1$ in some extension (using Kronecker's Theorem)
3. Factor: $p(x) = (x - \alpha_1)q(x)$ in $F(\alpha_1)[x]$
4. Repeat for $q(x)$ until all roots are found
5. $E = F(\alpha_1, \ldots, \alpha_n)$ is the splitting field

## To Recognize:
1. Verify $p(x)$ factors into linear factors over $E$
2. Verify $E$ is generated over $F$ by the roots of $p(x)$ (no unnecessary elements)

# Context & Application

Splitting fields are the natural domains for studying the roots of polynomials. They are central to Galois theory: the Galois group of a polynomial is defined as $G(E/F)$ where $E$ is the splitting field. The uniqueness of splitting fields (up to isomorphism) means the Galois group is well-defined.

# Examples

**Example 1** (p. 282): The splitting field of $x^4 + 2x^2 - 8$ over $\mathbb{Q}$ is $\mathbb{Q}(\sqrt{2}, i)$, since $x^4 + 2x^2 - 8 = (x^2 - 2)(x^2 + 4)$.

**Example 2** (p. 282): The splitting field of $x^3 - 3$ over $\mathbb{Q}$ is not $\mathbb{Q}(\sqrt[3]{3})$, because the complex cube roots are not in this field. The full splitting field requires adjoining a primitive cube root of unity as well.

# Relationships

## Builds Upon
- **Extension field** — Splitting fields are extensions
- **Kronecker's Theorem** — Provides the existence of roots needed for construction

## Enables
- **Galois group** — Defined using the splitting field
- **Normal extension** — Splitting fields of separable polynomials are normal
- **Fundamental Theorem of Galois Theory** — Applies to splitting fields of separable polynomials

## Related
- **Algebraic closure** — Contains all splitting fields

# Common Errors

- **Error**: Assuming the splitting field of $x^3 - a$ is always $F(\sqrt[3]{a})$
  **Correction**: The splitting field must contain all roots, including complex ones; for $x^3 - 3$ over $\mathbb{Q}$, one needs $\mathbb{Q}(\sqrt[3]{3}, \omega)$ where $\omega$ is a primitive cube root of unity

# Common Confusions

- **Confusion**: Thinking the splitting field depends on the order in which roots are adjoined
  **Clarification**: The splitting field is unique up to isomorphism regardless of construction order (Corollary 21.36)

# Source Reference

Chapter 21: Fields, Section 21.2 "Splitting Fields," pages 282–284. See Theorem 21.31, Corollary 21.36.

# Verification Notes

- Definition source: Direct from p. 282
- Confidence: HIGH — explicit definition with uniqueness theorem
- Cross-reference status: Verified
- Uncertainties: None
