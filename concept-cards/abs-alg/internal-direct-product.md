---
concept: Internal Direct Product
slug: internal-direct-product
category: group-theory
subcategory: direct-semidirect-products
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Direct and Semidirect Products and Abelian Groups"
chapter_number: 5
pdf_page: 178
section: "5.4 Recognizing Direct Products"
extraction_confidence: high
aliases: []
prerequisites:
  - direct-product
  - normal-subgroup
extends:
  - direct-product
related:
  - recognizing-direct-products
  - semidirect-product
contrasts_with:
  - direct-product
answers_questions:
  - "When is a group isomorphic to the direct product of its subgroups?"
  - "What is the difference between internal and external direct products?"
---

# Quick Definition
If G has normal subgroups H and K with H intersect K = 1, then HK is called the internal direct product of H and K, and HK is isomorphic to H x K (the external direct product).

# Core Definition
Theorem 9: Suppose G is a group with subgroups H and K such that (1) H and K are normal in G, and (2) H intersect K = 1. Then HK is isomorphic to H x K (Dummit & Foote, p. 179). The proof shows every element of H commutes with every element of K, then constructs the isomorphism hk -> (h, k). The distinction from external direct product is purely notational: elements are written hk vs. ordered pairs (h, k).

# Prerequisites
- **Direct product** — The internal version is isomorphic to the external
- **Normal subgroup** — Both factors must be normal

# Key Properties
1. H and K must both be normal in G
2. H intersect K = 1
3. Every element of H commutes with every element of K
4. Each element of HK is uniquely expressible as hk
5. HK is isomorphic to H x K

# Examples
**Example 1** (p. 181): D_{4n} is isomorphic to D_{2n} x Z_2 when n is odd, taking H = <s, r^2> and K = <r^n>.

**Example 2** (p. 176): A finite abelian group is the internal direct product of its Sylow subgroups.

# Relationships
## Builds Upon
- **Direct product** — Internal and external are isomorphic
## Related
- **Semidirect product** — Generalizes by relaxing normality of one factor
## Contrasts With
- **Direct product** — Internal writes elements as hk; external as (h,k)

# Source Reference
Chapter 5, Section 5.4, Theorem 9, page 179.

# Verification Notes
- Definition source: Direct from Theorem 9, p. 179
- Confidence: HIGH
- Uncertainties: None
