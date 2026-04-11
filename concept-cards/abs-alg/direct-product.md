---
concept: Direct Product
slug: direct-product
category: group-theory
subcategory: direct-semidirect-products
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Direct and Semidirect Products and Abelian Groups"
chapter_number: 5
pdf_page: 152
section: "5.1 Direct Products"
extraction_confidence: high
aliases:
  - "external direct product"
  - "cartesian product of groups"
prerequisites:
  - group
  - normal-subgroup
extends:
  - group
related:
  - internal-direct-product
  - semidirect-product
  - fundamental-theorem-finitely-generated-abelian-groups
contrasts_with:
  - semidirect-product
answers_questions:
  - "What is a direct product of groups?"
  - "What distinguishes a direct product from a semidirect product?"
---

# Quick Definition
The direct product G_1 x G_2 x ... x G_n is the set of n-tuples (g_1, g_2, ..., g_n) with componentwise multiplication. Its order is the product of the orders of the factors.

# Core Definition
The direct product G_1 x G_2 x ... x G_n of groups G_1, ..., G_n is the set of n-tuples (g_1, ..., g_n) where g_i in G_i, with operation defined componentwise: (g_1,...,g_n)(h_1,...,h_n) = (g_1h_1,...,g_nh_n) (Dummit & Foote, p. 156). By Proposition 1, this is a group of order |G_1| * |G_2| * ... * |G_n|. By Proposition 2, each G_i embeds as a normal subgroup, elements from different factors commute, and there are projection homomorphisms onto each factor.

# Prerequisites
- **Group** — The factors are groups
- **Normal subgroup** — Each factor embeds as a normal subgroup

# Key Properties
1. |G_1 x ... x G_n| = |G_1| * ... * |G_n|
2. Each G_i embeds as a normal subgroup of the direct product
3. Elements from different factors commute (Proposition 2(3))
4. |(x_1...x_n)| = lcm(|x_1|, ..., |x_n|) (Example 1, p. 160)
5. Z_m x Z_n is isomorphic to Z_{mn} iff gcd(m,n) = 1 (Proposition 6)
6. Z(G_1 x ... x G_n) = Z(G_1) x ... x Z(G_n)

# Examples
**Example 1** (p. 157): R x R x ... x R (n factors) is Euclidean n-space R^n.

**Example 2** (p. 160): Z_p x Z_p x ... x Z_p (n factors) is the elementary abelian group of order p^n.

# Relationships
## Builds Upon
- **Group** — Direct products construct larger groups from smaller ones
## Enables
- **Fundamental theorem of finitely generated abelian groups** — Abelian groups decompose as direct products
- **Internal direct product** — When the product is recognized inside a group
## Contrasts With
- **Semidirect product** — Generalizes direct product by allowing non-normal factors

# Common Confusions
- **Confusion**: Assuming Z_m x Z_n is always cyclic
  **Clarification**: Z_m x Z_n is cyclic (isomorphic to Z_{mn}) only when gcd(m,n) = 1

# Source Reference
Chapter 5: Direct and Semidirect Products, Section 5.1, pages 156-167.

# Verification Notes
- Definition source: Direct from p. 156
- Confidence: HIGH — explicit definition
- Uncertainties: None
