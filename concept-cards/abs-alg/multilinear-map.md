---
concept: Multilinear Map
slug: multilinear-map
category: module-theory
subcategory: tensor-products
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Module Theory"
chapter_number: 10
pdf_page: 384
section: "10.4 Tensor Products of Modules"
extraction_confidence: high
aliases:
  - "n-multilinear map"
  - "n-multilinear function"
prerequisites:
  - left-module
extends:
  - bilinear-map
related:
  - tensor-product
  - alternating-map
  - determinant
contrasts_with: []
answers_questions:
  - "What is a multilinear map?"
---

# Quick Definition
A map $\varphi: M_1 \times \cdots \times M_n \to L$ is n-multilinear over R if it is R-linear in each variable when the others are held fixed.

# Core Definition
Let R be a commutative ring with 1 and let $M_1, \ldots, M_n$ and L be R-modules. A map $\varphi: M_1 \times \cdots \times M_n \to L$ is called n-multilinear over R if for each i, $\varphi(m_1, \ldots, rm_i + r'm_i', \ldots, m_n) = r\varphi(\ldots, m_i, \ldots) + r'\varphi(\ldots, m_i', \ldots)$. Multilinear maps factor uniquely through the n-fold tensor product $M_1 \otimes \cdots \otimes M_n$ (Dummit & Foote, p. 384, Corollary 16).

# Prerequisites
- **left-module** — Multilinear maps act on modules

# Key Properties
1. Multilinear maps correspond to R-module homomorphisms from $M_1 \otimes \cdots \otimes M_n$
2. When n = 2, this is bilinear; when n = 3, trilinear
3. The n-fold tensor product is the universal object for multilinear maps

# Relationships
## Builds Upon
- **bilinear-map** — The n = 2 case

## Enables
- **determinant** — The determinant is an alternating multilinear form
- **tensor-algebra**, **symmetric-algebra**, **exterior-algebra**

# Source Reference
Chapter 10, Section 10.4, pp. 384-385 and Chapter 11, Section 11.4.

# Verification Notes
- Confidence: HIGH — explicit definition
