---
# === CORE IDENTIFICATION ===
concept: Basis of a Simple Algebraic Extension
slug: simple-extension-basis

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
  - simple-extension
  - minimal-polynomial
  - basis
extends: []
related:
  - degree-of-field-extension
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a basis for a simple algebraic extension?"
  - "How do I do arithmetic in F(alpha)?"
---

# Quick Definition

If $\alpha$ is algebraic over $F$ with minimal polynomial of degree $n$, then $\{1, \alpha, \alpha^2, \ldots, \alpha^{n-1}\}$ is a basis for $F(\alpha)$ over $F$. Every element has a unique expression as $b_0 + b_1\alpha + \cdots + b_{n-1}\alpha^{n-1}$.

# Core Definition

**Theorem 21.13.** Let $E = F(\alpha)$ be a simple extension of $F$, where $\alpha \in E$ is algebraic over $F$ with degree $n$. Then every element $\beta \in E$ can be expressed uniquely in the form

$$\beta = b_0 + b_1\alpha + \cdots + b_{n-1}\alpha^{n-1}$$

for $b_i \in F$ (Judson, p. 277).

# Prerequisites

- **Simple extension** — The extension is $F(\alpha)$
- **Minimal polynomial** — Its degree determines the basis size
- **Basis** — The theorem provides a basis for the extension

# Key Properties

1. The basis has exactly $n$ elements where $n = \deg p(x)$
2. Every element has a unique representation (linear combination)
3. Higher powers $\alpha^m$ for $m \geq n$ can be reduced using $p(\alpha) = 0$
4. This provides a concrete algorithm for arithmetic in $F(\alpha)$

# Construction / Recognition

## To Compute in $F(\alpha)$:
1. Find the minimal polynomial $p(\alpha) = 0$
2. Express $\alpha^n$ in terms of lower powers using $p(\alpha) = 0$
3. Reduce all products to polynomials of degree $< n$ in $\alpha$

# Examples

**Example 1** (p. 278): In $\mathbb{R}(\alpha)$ where $\alpha^2 + 1 = 0$ (i.e., $\alpha = i$): basis is $\{1, \alpha\}$, every element is $a + b\alpha = a + bi$.

**Example 2** (p. 275): In $\mathbb{Z}_2(\alpha)$ where $\alpha^2 + \alpha + 1 = 0$: basis is $\{1, \alpha\}$, elements are $0, 1, \alpha, 1 + \alpha$.

# Relationships

## Builds Upon
- **Simple extension** — The basis is for $F(\alpha)$
- **Minimal polynomial** — Determines the basis size

## Related
- **Degree of field extension** — $[F(\alpha):F] = n$ equals the number of basis elements

# Source Reference

Chapter 21: Fields, Section 21.1, pages 277–278. Theorem 21.13.

# Verification Notes

- Definition source: Direct from Theorem 21.13, p. 277
- Confidence: HIGH — explicit theorem with proof and examples
- Cross-reference status: Verified
- Uncertainties: None
