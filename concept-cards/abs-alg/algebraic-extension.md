---
concept: Algebraic Extension
slug: algebraic-extension
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
aliases: []
prerequisites:
  - field-extension
  - minimal-polynomial-field
extends: []
related:
  - transcendental-extension
  - algebraic-element
  - algebraic-closure
contrasts_with:
  - transcendental-extension
answers_questions:
  - "What is an algebraic extension?"
  - "What is an algebraic element?"
---

# Quick Definition
An element $\alpha \in K$ is algebraic over F if it is a root of some nonzero polynomial in F[x]. The extension K/F is algebraic if every element of K is algebraic over F. Every finite extension is algebraic.

# Core Definition
An element $\alpha$ of an extension field K of F is algebraic over F if $\alpha$ is a root of some nonzero polynomial $f(x) \in F[x]$; otherwise $\alpha$ is transcendental over F. The extension K/F is algebraic if every element of K is algebraic over F. Key results: (1) $\alpha$ is algebraic over F iff $[F(\alpha):F]$ is finite, and then $[F(\alpha):F] = \deg m_\alpha(x)$ where $m_\alpha$ is the minimal polynomial; (2) every finite extension is algebraic; (3) if $\alpha$ is algebraic over F of degree n, then $F(\alpha) = F[\alpha] \cong F[x]/(m_\alpha(x))$ (Dummit & Foote, pp. 522-529).

# Prerequisites
- **field-extension** — Algebraic extensions are a type of field extension
- **minimal-polynomial-field** — Every algebraic element has a minimal polynomial

# Key Properties
1. $\alpha$ algebraic over F $\iff$ $[F(\alpha):F] < \infty$
2. Finite extensions are algebraic (converse false in general)
3. If $\alpha$ has degree n over F, then $\{1, \alpha, \ldots, \alpha^{n-1}\}$ is a basis for $F(\alpha)$ over F
4. Algebraic extensions of algebraic extensions are algebraic
5. The set of elements in K algebraic over F forms a subfield

# Relationships
## Builds Upon
- **field-extension**, **minimal-polynomial-field**

## Enables
- **splitting-field** — Splitting fields are algebraic extensions
- **algebraic-closure** — Maximal algebraic extension

## Contrasts With
- **transcendental-extension** — Contains transcendental elements

# Source Reference
Chapter 13, Section 13.2, pp. 522-529.

# Verification Notes
- Confidence: HIGH — extensive development
