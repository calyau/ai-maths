---
concept: Transcendental Extension
slug: transcendental-extension
category: galois-theory
subcategory: transcendental
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Galois Theory"
chapter_number: 14
pdf_page: 645
section: "14.9 Transcendental Extensions"
extraction_confidence: high
aliases:
  - "transcendental element"
  - "transcendence degree"
  - "purely transcendental extension"
prerequisites:
  - field-extension
  - algebraic-extension
extends: []
related:
  - algebraic-closure
contrasts_with:
  - algebraic-extension
answers_questions:
  - "What is a transcendental extension?"
---

# Quick Definition
An element $\alpha \in K$ is transcendental over F if it is not a root of any nonzero polynomial in F[x]. A purely transcendental extension is $F(x_1, \ldots, x_n)$ (rational functions). The transcendence degree is the size of a maximal algebraically independent subset.

# Core Definition
An element $\alpha$ of an extension K/F is transcendental over F if $\alpha$ is not algebraic over F, i.e., $f(\alpha) \neq 0$ for all nonzero $f(x) \in F[x]$. Then $F(\alpha) \cong F(x)$, the field of rational functions. A transcendence basis of K/F is a maximal algebraically independent subset S of K over F. The transcendence degree of K/F is $|S|$ (well-defined). K/F is purely transcendental if $K = F(S)$ for a transcendence basis S (Dummit & Foote, pp. 645-650).

# Prerequisites
- **field-extension** — Transcendental extensions are a type of extension
- **algebraic-extension** — Defined by contrast with algebraic

# Key Properties
1. $\alpha$ transcendental $\Rightarrow$ $F(\alpha) \cong F(x)$ (rational function field)
2. $[F(\alpha):F] = \infty$ when $\alpha$ is transcendental
3. $\pi$ and $e$ are transcendental over $\mathbb{Q}$
4. Transcendence degree is well-defined (analogous to vector space dimension)
5. $\text{tr.deg}(\mathbb{C}/\mathbb{Q})$ is uncountable

# Relationships
## Builds Upon
- **field-extension**, **algebraic-extension**

## Contrasts With
- **algebraic-extension** — Algebraic elements satisfy polynomials; transcendental ones don't

# Source Reference
Chapter 14, Section 14.9, pp. 645-650.

# Verification Notes
- Confidence: HIGH — explicit definitions
