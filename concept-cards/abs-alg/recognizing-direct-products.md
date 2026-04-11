---
concept: Recognizing Direct Products
slug: recognizing-direct-products
category: group-theory
subcategory: direct-semidirect-products
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Direct and Semidirect Products and Abelian Groups"
chapter_number: 5
pdf_page: 174
section: "5.4 Recognizing Direct Products"
extraction_confidence: high
aliases:
  - "direct product recognition theorem"
prerequisites:
  - direct-product
  - internal-direct-product
  - normal-subgroup
extends:
  - internal-direct-product
related:
  - semidirect-product
contrasts_with: []
answers_questions:
  - "How do I tell if a group is a direct product of its subgroups?"
  - "What conditions must subgroups satisfy to form a direct product?"
---

# Quick Definition
A group G is the (internal) direct product of normal subgroups H and K when: (1) H and K are both normal in G, and (2) H intersect K = 1. Then HK is isomorphic to H x K, with elements of H commuting with elements of K.

# Core Definition
Theorem 9: Suppose G is a group with subgroups H and K such that (1) H and K are normal in G, and (2) H intersect K = 1. Then HK is isomorphic to H x K (Dummit & Foote, p. 179). The proof shows every element of H commutes with every element of K (since h^{-1}k^{-1}hk lies in both H and K, hence equals 1), and constructs the isomorphism hk -> (h,k).

# Prerequisites
- **Direct product** — The external product being recognized internally
- **Internal direct product** — The concept being identified
- **Normal subgroup** — Both factors must be normal

# Key Properties
1. Both H and K must be normal (not just one)
2. H intersect K = 1
3. Elements of different factors commute: hk = kh
4. Each element of HK is uniquely expressible as hk
5. For semidirect products, only ONE factor needs to be normal

# Examples
**Example 1** (p. 181): D_{4n} = D_{2n} x Z_2 when n is odd.

**Example 2** (p. 176): A finite abelian group is the direct product of its Sylow subgroups.

# Relationships
## Builds Upon
- **Internal direct product**
## Related
- **Semidirect product** — Generalization where only H needs to be normal

# Common Errors
- **Error**: Trying to recognize a direct product when only one subgroup is normal
  **Correction**: Both must be normal for a direct product; if only H is normal, you may have a semidirect product

# Source Reference
Chapter 5, Section 5.4, Theorem 9, page 179.

# Verification Notes
- Definition source: Direct from Theorem 9, p. 179
- Confidence: HIGH
- Uncertainties: None
