---
concept: Separable Extension
slug: separable-extension
category: field-theory
subcategory: separability
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Field Theory"
chapter_number: 13
pdf_page: 547
section: "13.5 Separable and Inseparable Extensions"
extraction_confidence: high
aliases:
  - "separable polynomial"
prerequisites:
  - algebraic-extension
  - splitting-field
extends: []
related:
  - inseparable-extension
  - perfect-field
  - galois-extension
contrasts_with:
  - inseparable-extension
answers_questions:
  - "What is a separable extension?"
  - "What distinguishes a normal extension from a separable extension?"
---

# Quick Definition
A polynomial is separable if it has no repeated roots (in its splitting field). An algebraic extension K/F is separable if the minimal polynomial of every element of K over F is separable. Over fields of characteristic 0, every extension is separable.

# Core Definition
A polynomial $f(x) \in F[x]$ is separable if it has no repeated roots in its splitting field, equivalently if $\gcd(f, f') = 1$ where $f'$ is the formal derivative. An irreducible polynomial is inseparable iff $f'(x) = 0$, which can only happen in characteristic p > 0. An algebraic element $\alpha$ is separable over F if its minimal polynomial is separable. K/F is a separable extension if every element of K is separable over F (Dummit & Foote, pp. 547-554).

# Prerequisites
- **algebraic-extension** — Separability is defined for algebraic extensions
- **splitting-field** — Repeated roots are detected in the splitting field

# Key Properties
1. In characteristic 0, every irreducible polynomial is separable
2. In characteristic p, an irreducible polynomial is inseparable iff it is a polynomial in $x^p$
3. A field F is perfect if every irreducible polynomial over F is separable (char 0, or char p with $F = F^p$)
4. $\mathbb{Q}$ and all finite fields are perfect
5. An algebraic extension of a perfect field is separable
6. K/F is Galois iff it is both separable and normal

# Relationships
## Builds Upon
- **algebraic-extension**, **splitting-field**

## Enables
- **galois-extension** — Galois = separable + normal

## Related
- **perfect-field** — Fields where all extensions are separable

## Contrasts With
- **inseparable-extension** — Contains elements whose minimal polynomials have repeated roots

# Common Confusions
- **Confusion**: Thinking inseparable extensions are common. **Clarification**: They only occur in characteristic p and only for non-perfect fields. In characteristic 0 (e.g., over $\mathbb{Q}$), everything is separable.

# Source Reference
Chapter 13, Section 13.5, pp. 547-554.

# Verification Notes
- Confidence: HIGH — explicit definitions with clear characterizations
