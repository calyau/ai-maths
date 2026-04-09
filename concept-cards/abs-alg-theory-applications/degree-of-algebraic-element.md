---
# === CORE IDENTIFICATION ===
concept: Degree of an Algebraic Element
slug: degree-of-algebraic-element

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
  - minimal-polynomial
  - algebraic-element
extends: []
related:
  - degree-of-field-extension
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the degree of an algebraic element over a field?"
---

# Quick Definition

The degree of an algebraic element $\alpha$ over $F$ is the degree of its minimal polynomial over $F$. It equals $[F(\alpha):F]$, the dimension of the simple extension as a vector space.

# Core Definition

The degree of the minimal polynomial $p(x)$ of an algebraic element $\alpha$ over $F$ is called the **degree of $\alpha$ over $F$** (Judson, p. 277). By Theorem 21.13, $[F(\alpha):F] = \deg p(x)$.

# Prerequisites

- **Minimal polynomial** — The degree of $\alpha$ equals the degree of its minimal polynomial
- **Algebraic element** — Only algebraic elements have a degree

# Key Properties

1. $\deg \alpha = \deg p(x) = [F(\alpha):F]$
2. $\{1, \alpha, \ldots, \alpha^{n-1}\}$ is a basis for $F(\alpha)$ over $F$ where $n = \deg \alpha$
3. If $\beta \in F(\alpha)$ has minimal polynomial $q(x)$, then $\deg q(x) \mid \deg p(x)$ (Corollary 21.19)

# Examples

**Example 1** (p. 277): $\sqrt{2}$ has degree 2 over $\mathbb{Q}$ (minimal polynomial $x^2 - 2$).

**Example 2** (p. 277): $\sqrt{2 + \sqrt{3}}$ has degree 4 over $\mathbb{Q}$ (minimal polynomial $x^4 - 4x^2 + 1$).

# Relationships

## Builds Upon
- **Minimal polynomial** — Degree of element = degree of minimal polynomial

## Related
- **Degree of field extension** — $[F(\alpha):F] = \deg \alpha$

# Source Reference

Chapter 21: Fields, Section 21.1, pages 277–278.

# Verification Notes

- Definition source: Direct from p. 277
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
