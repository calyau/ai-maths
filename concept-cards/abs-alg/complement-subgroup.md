---
concept: Complement of a Subgroup
slug: complement-subgroup
category: group-theory
subcategory: direct-semidirect-products
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Direct and Semidirect Products and Abelian Groups"
chapter_number: 5
pdf_page: 191
section: "5.5 Semidirect Products"
extraction_confidence: high
aliases:
  - "complement"
  - "complementary subgroup"
prerequisites:
  - subgroup
  - normal-subgroup
  - semidirect-product
extends: []
related:
  - semidirect-product
  - split-extension
  - internal-direct-product
contrasts_with: []
answers_questions:
  - "What is a complement for a subgroup?"
  - "When does a normal subgroup have a complement?"
---

# Quick Definition
A subgroup K of G is a complement for the subgroup H if G = HK and H intersect K = 1. If H is normal and has a complement K, then G is a semidirect product of H and K.

# Core Definition
Let H be a subgroup of the group G. A subgroup K of G is called a complement for H in G if G = HK and H intersect K = 1 (Dummit & Foote, p. 191). By Theorem 12, if H is normal and K is a complement, then G is isomorphic to the semidirect product H x_phi K. Not every normal subgroup has a complement; for example, the unique subgroup of order 2 in Z_4 has no complement.

# Prerequisites
- **Subgroup** — Both H and K must be subgroups
- **Normal subgroup** — For semidirect product recognition, H must be normal
- **Semidirect product** — Complement existence gives semidirect product structure

# Key Properties
1. G = HK (every element can be written as a product hk)
2. H intersect K = 1
3. If H is normal and K is a complement, then G = H x K (semidirect product)
4. Not every normal subgroup has a complement
5. A complement for a normal subgroup is sometimes called a splitting

# Examples
**Example 1**: In S_3, <(1 2 3)> is normal and <(1 2)> is a complement. So S_3 = Z_3 x Z_2.

**Example 2**: In Z_4, the subgroup {0, 2} has no complement (Z_4 is not a semidirect product).

# Relationships
## Enables
- **Semidirect product** — H normal with complement K gives G = H x K
- **Split extension** — An extension that splits has a complement

# Source Reference
Chapter 5, Section 5.5, page 191. Theorem 12.

# Verification Notes
- Definition source: Direct from p. 191
- Confidence: HIGH
- Uncertainties: None
