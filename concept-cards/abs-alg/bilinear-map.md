---
concept: Bilinear Map
slug: bilinear-map
category: module-theory
subcategory: tensor-products
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Module Theory"
chapter_number: 10
pdf_page: 377
section: "10.4 Tensor Products of Modules"
extraction_confidence: high
aliases:
  - "R-bilinear map"
  - "balanced map"
  - "R-balanced map"
  - "middle linear map"
prerequisites:
  - left-module
extends: []
related:
  - tensor-product
  - multilinear-map
contrasts_with: []
answers_questions:
  - "What is a bilinear map?"
  - "What is an R-balanced map?"
---

# Quick Definition
An R-bilinear map $\varphi: M \times N \to L$ is a map that is R-linear in each variable separately. An R-balanced map satisfies $\varphi(mr, n) = \varphi(m, rn)$ and is additive in each variable.

# Core Definition
Let R be a commutative ring with 1 and let M, N, L be R-modules. A map $\varphi: M \times N \to L$ is R-bilinear if it is R-linear in each factor: $\varphi(r_1 m_1 + r_2 m_2, n) = r_1\varphi(m_1, n) + r_2\varphi(m_2, n)$ and $\varphi(m, r_1 n_1 + r_2 n_2) = r_1\varphi(m, n_1) + r_2\varphi(m, n_2)$. More generally, if M is a right R-module and N is a left R-module, a map $\varphi: M \times N \to L$ is R-balanced if it is additive in each variable and $\varphi(mr, n) = \varphi(m, rn)$ (Dummit & Foote, pp. 370, 377).

# Prerequisites
- **left-module** — Bilinear maps are defined on modules

# Key Properties
1. Bilinear maps from $M \times N$ correspond bijectively to R-module homomorphisms from $M \otimes_R N$
2. Every R-bilinear map is R-balanced (when R is commutative)
3. The tensor product is the universal object for balanced/bilinear maps

# Context & Application
Bilinear maps motivate the construction of the tensor product. The universal property of the tensor product converts bilinear maps to linear maps.

# Examples
**Example** (p. 395): The dot product on $\mathbb{R}^n$ is a bilinear form.

# Relationships
## Enables
- **tensor-product** — Universalizes bilinear maps

## Related
- **multilinear-map** — Generalization to n variables

# Source Reference
Chapter 10, Section 10.4, pp. 370, 377-378. See also Corollary 12.

# Verification Notes
- Confidence: HIGH — explicit definitions
