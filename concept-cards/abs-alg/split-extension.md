---
concept: Split Extension
slug: split-extension
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
extraction_confidence: medium
aliases:
  - "split short exact sequence"
prerequisites:
  - semidirect-product
  - complement-subgroup
  - normal-subgroup
extends:
  - semidirect-product
related:
  - direct-product
contrasts_with: []
answers_questions:
  - "What is a split extension?"
  - "When is a group extension split?"
---

# Quick Definition
A group G is a split extension of H by K if H is normal in G and K is a complement for H (G = HK, H intersect K = 1). Equivalently, G is a semidirect product of H and K. Not all extensions split: Z_4 is an extension of Z_2 by Z_2 that does not split.

# Core Definition
By Theorem 12 (Dummit & Foote, p. 191), if G has a normal subgroup H with complement K (G = HK, H intersect K = 1), then G is isomorphic to the semidirect product H x K. Such a group is called a split extension. The criterion for recognizing a semidirect product is the existence of a complement for a proper normal subgroup.

# Prerequisites
- **Semidirect product** — A split extension IS a semidirect product
- **Complement subgroup** — The complement provides the "splitting"
- **Normal subgroup** — H must be normal

# Key Properties
1. G = HK with H normal and H intersect K = 1
2. G is isomorphic to H x_phi K where phi is conjugation
3. Not every extension splits (Z_4 is a non-split extension of Z_2 by Z_2)
4. Direct products are split extensions where phi is trivial

# Relationships
## Builds Upon
- **Semidirect product** — Split extensions are semidirect products
## Related
- **Direct product** — A direct product is a split extension with trivial action

# Source Reference
Chapter 5, Section 5.5, Theorem 12, page 191.

# Verification Notes
- Definition source: Synthesized from Theorem 12 and surrounding discussion
- Confidence: MEDIUM — the term "split extension" is used implicitly rather than formally defined
- Uncertainties: The source uses the term informally
