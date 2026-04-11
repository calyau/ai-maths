---
concept: Degree of a Field Extension
slug: degree-of-extension
category: field-theory
subcategory: basic-extensions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Field Theory"
chapter_number: 13
pdf_page: 512
section: "13.1 Basic Theory of Field Extensions"
extraction_confidence: high
aliases:
  - "[K:F]"
  - "relative degree"
  - "index of extension"
prerequisites:
  - field-extension
  - dimension
extends: []
related:
  - tower-law
  - algebraic-extension
contrasts_with: []
answers_questions:
  - "What is the degree of a field extension?"
---

# Quick Definition
The degree $[K:F]$ of a field extension K/F is the dimension of K as a vector space over F. The extension is finite if $[K:F] < \infty$.

# Core Definition
The degree $[K:F]$ of a field extension K/F is defined as $\dim_F K$. The fundamental tower law states: if $F \subseteq L \subseteq K$ are fields, then $[K:F] = [K:L] \cdot [L:F]$, with one side finite iff both factors on the other side are finite (Dummit & Foote, pp. 512-513).

# Prerequisites
- **field-extension** — Degree is defined for field extensions
- **dimension** — Degree equals dimension of K as F-vector space

# Key Properties
1. $[K:F] = 1$ iff $K = F$
2. Tower law: $[K:F] = [K:L][L:F]$
3. If $[K:F]$ is prime, there are no intermediate fields
4. $[F(\alpha):F] = \deg m_\alpha(x)$ where $m_\alpha$ is the minimal polynomial of $\alpha$

# Relationships
## Builds Upon
- **field-extension**, **dimension**

## Enables
- **algebraic-extension** — Finite degree implies algebraic

# Source Reference
Chapter 13, Section 13.1, pp. 512-513.

# Verification Notes
- Confidence: HIGH — explicit definition
