---
concept: Field Extension
slug: field-extension
category: field-theory
subcategory: basic-extensions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Field Theory"
chapter_number: 13
pdf_page: 510
section: "13.1 Basic Theory of Field Extensions"
extraction_confidence: high
aliases:
  - "extension field"
  - "K/F"
prerequisites:
  - field
  - vector-space
extends: []
related:
  - degree-of-extension
  - algebraic-extension
  - transcendental-extension
  - splitting-field
contrasts_with: []
answers_questions:
  - "What is a field extension?"
  - "What must I know before studying Galois theory?"
---

# Quick Definition
A field extension K/F means K is a field containing F as a subfield. K is then a vector space over F, and its dimension $[K:F]$ is the degree of the extension.

# Core Definition
If K is a field containing the subfield F, then K is said to be an extension field (or simply an extension) of F, denoted K/F. The notation K/F means "K over F" (NOT a quotient). The multiplication in K makes K into a vector space over F. The degree $[K:F] = \dim_F K$ is the dimension of K as a vector space over F. The extension is finite if $[K:F]$ is finite, infinite otherwise (Dummit & Foote, pp. 512-513).

# Prerequisites
- **field** — Both F and K are fields
- **vector-space** — K is a vector space over F

# Key Properties
1. $[K:F] = \dim_F K$ (degree = dimension as vector space)
2. Tower law: $[K:F] = [K:L][L:F]$ for intermediate field L
3. Every field contains a prime subfield isomorphic to $\mathbb{Q}$ (char 0) or $\mathbb{F}_p$ (char p)
4. For any irreducible $p(x) \in F[x]$, $K = F[x]/(p(x))$ is an extension of F of degree $\deg p$

# Construction / Recognition
## To Construct:
1. Take an irreducible polynomial $p(x) \in F[x]$
2. Form $K = F[x]/(p(x))$; this is a field containing a copy of F
3. $[K:F] = \deg p(x)$ and $K = F(\theta)$ where $\theta = \bar{x}$, a root of p(x)

# Context & Application
Field extensions are the central objects of study in field theory and Galois theory. The construction $F[x]/(p(x))$ guarantees that every irreducible polynomial has a root in some extension.

# Examples
**Example 1** (p. 515): $\mathbb{C} = \mathbb{R}[x]/(x^2+1) \cong \mathbb{R}(i)$ with $[\mathbb{C}:\mathbb{R}] = 2$.
**Example 2** (p. 516): $\mathbb{Q}(\sqrt{2}) = \{a + b\sqrt{2} \mid a, b \in \mathbb{Q}\}$ with $[\mathbb{Q}(\sqrt{2}):\mathbb{Q}] = 2$.
**Example 3** (p. 516): $\mathbb{Q}(\sqrt[3]{2}) = \{a + b\theta + c\theta^2 \mid a,b,c \in \mathbb{Q}\}$ with $[\mathbb{Q}(\sqrt[3]{2}):\mathbb{Q}] = 3$ where $\theta^3 = 2$.

# Relationships
## Builds Upon
- **field**, **vector-space**

## Enables
- **algebraic-extension** — Extensions where every element satisfies a polynomial
- **splitting-field** — Smallest extension containing all roots of a polynomial
- **galois-extension** — Extensions with enough automorphisms

# Source Reference
Chapter 13, Section 13.1, pp. 510-521.

# Verification Notes
- Confidence: HIGH — foundational definition with extensive examples
