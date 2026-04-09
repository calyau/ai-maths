---
# === CORE IDENTIFICATION ===
concept: Degree of Field Extension
slug: degree-of-field-extension

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
aliases:
  - "[E:F]"
  - "index of extension"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - extension-field
  - dimension
extends: []
related:
  - tower-theorem
  - minimal-polynomial
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the degree of a field extension?"
  - "How does the degree relate to dimension?"
---

# Quick Definition

The degree of a field extension $E$ over $F$, written $[E:F]$, is the dimension of $E$ viewed as a vector space over $F$. If $[E:F]$ is finite, $E$ is called a finite extension.

# Core Definition

If an extension field $E$ of a field $F$ is a finite dimensional vector space over $F$ of dimension $n$, then we say that $E$ is a **finite extension of degree $n$ over $F$**. We write $[E:F] = n$ to indicate the dimension of $E$ over $F$ (Judson, p. 278).

# Prerequisites

- **Extension field** — The degree measures the "size" of an extension
- **Dimension** — The degree is defined as the dimension of the vector space

# Key Properties

1. $[F(\alpha):F] = \deg p(x)$ where $p(x)$ is the minimal polynomial of $\alpha$ (Theorem 21.13)
2. Tower law: $[K:F] = [K:E][E:F]$ for $F \subset E \subset K$ (Theorem 21.17)
3. Every finite extension is algebraic (Theorem 21.15)
4. If $\alpha$ has minimal polynomial of degree $n$ and $\beta \in F(\alpha)$ has minimal polynomial $q(x)$, then $\deg q(x)$ divides $n$ (Corollary 21.19)

# Construction / Recognition

## To Compute:
1. Find a basis for $E$ as a vector space over $F$
2. Count the basis elements
3. This count is $[E:F]$

# Context & Application

The degree of a field extension is the central numerical invariant in field theory. It connects field theory to linear algebra and controls divisibility constraints on subextensions via the tower law. In Galois theory, $[E:F] = |G(E/F)|$ for normal separable extensions.

# Examples

**Example 1** (p. 278): $[\mathbb{C}:\mathbb{R}] = 2$ with basis $\{1, i\}$.

**Example 2** (p. 280): $[\mathbb{Q}(\sqrt{3} + \sqrt{5}):\mathbb{Q}] = 4$ with basis $\{1, \sqrt{3}, \sqrt{5}, \sqrt{15}\}$.

**Example 3** (p. 280): $[\mathbb{Q}(\sqrt[3]{5}, \sqrt{5}i):\mathbb{Q}] = 6$.

# Relationships

## Builds Upon
- **Dimension** — The degree is the dimension of the vector space
- **Extension field** — The degree measures an extension

## Enables
- **Tower theorem** — Multiplicativity of degrees in towers
- **Galois theory** — $|G(E/F)| = [E:F]$ for Galois extensions

## Related
- **Minimal polynomial** — Its degree equals the degree of a simple extension

# Common Errors

- **Error**: Assuming $[E:F]$ equals the number of elements of $E$
  **Correction**: The degree is the dimension of the vector space, not the cardinality; $[\mathbb{C}:\mathbb{R}] = 2$ even though both fields are uncountable

# Source Reference

Chapter 21: Fields, Section 21.1, pages 278–280. See Theorems 21.13, 21.15, 21.17.

# Verification Notes

- Definition source: Direct from p. 278
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
