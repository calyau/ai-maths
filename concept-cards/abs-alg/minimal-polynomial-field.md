---
concept: Minimal Polynomial (Field Extension)
slug: minimal-polynomial-field
category: field-theory
subcategory: algebraic-extensions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Field Theory"
chapter_number: 13
pdf_page: 522
section: "13.2 Algebraic Extensions"
extraction_confidence: high
aliases:
  - "minimal polynomial of an algebraic element"
prerequisites:
  - field-extension
  - irreducible-polynomial
extends: []
related:
  - algebraic-extension
  - degree-of-extension
contrasts_with: []
answers_questions:
  - "What is the minimal polynomial of an algebraic element?"
---

# Quick Definition
The minimal polynomial of an algebraic element $\alpha$ over F is the unique monic irreducible polynomial $m_\alpha(x) \in F[x]$ having $\alpha$ as a root. Its degree equals $[F(\alpha):F]$.

# Core Definition
If $\alpha$ is algebraic over F, the minimal polynomial $m_\alpha(x)$ is the unique monic polynomial of minimal degree in F[x] with $m_\alpha(\alpha) = 0$. It is irreducible and divides every polynomial in F[x] having $\alpha$ as a root. We have $F(\alpha) \cong F[x]/(m_\alpha(x))$ and $[F(\alpha):F] = \deg m_\alpha(x)$ (Dummit & Foote, pp. 522-525).

# Prerequisites
- **field-extension** — Minimal polynomial is relative to a base field
- **irreducible-polynomial** — The minimal polynomial is irreducible

# Key Properties
1. Unique monic irreducible polynomial in F[x] with $\alpha$ as a root
2. Divides every polynomial in F[x] vanishing at $\alpha$
3. $\deg m_\alpha = [F(\alpha):F]$
4. $\{1, \alpha, \ldots, \alpha^{n-1}\}$ is a basis for $F(\alpha)$ over F where $n = \deg m_\alpha$

# Relationships
## Builds Upon
- **field-extension**, **irreducible-polynomial**

## Enables
- **algebraic-extension** — Characterizes algebraic elements

# Source Reference
Chapter 13, Section 13.2, pp. 522-525.

# Verification Notes
- Confidence: HIGH — fundamental definition
