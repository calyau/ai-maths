---
concept: Ext Functor
slug: ext-functor
category: homological-algebra
subcategory: derived-functors
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Homological Algebra and Group Cohomology"
chapter_number: 17
pdf_page: 781
section: "17.1 Introduction to Homological Algebra"
extraction_confidence: high
aliases:
  - "Ext^n"
  - "Ext groups"
prerequisites:
  - projective-resolution
  - homology-group
extends: []
related:
  - tor-functor
  - group-cohomology
contrasts_with:
  - tor-functor
answers_questions:
  - "What is the Ext functor?"
---

# Quick Definition
Ext^n_R(A,D) is the n-th cohomology group obtained by applying Hom_R(_,D) to a projective resolution of A. Ext^0 = Hom, and the higher Ext groups measure the failure of Hom to be exact.

# Core Definition
For R-modules A and D, take a projective resolution ··· → P_1 → P_0 → A → 0. Apply Hom_R(_,D) to get the cochain complex 0 → Hom(P_0,D) → Hom(P_1,D) → ···. Then **Ext^n_R(A,D)** = ker d_{n+1}/image d_n (Definition, p. 781). By Theorem 6, this is independent of the choice of resolution.

# Prerequisites
- **projective-resolution** — Used to compute Ext
- **homology-group** — Ext groups are cohomology groups

# Key Properties
1. Ext^0_R(A,D) ≅ Hom_R(A,D) (Proposition 3)
2. Independent of choice of projective resolution (Theorem 6)
3. Can also be computed from injective resolutions of D (Theorem 8)
4. A short exact sequence gives a long exact sequence in Ext
5. A is projective iff Ext^1_R(A,D) = 0 for all D (Corollary 9)

# Examples
**Example** (p. 782): Ext^0_Z(Z/mZ, D) ≅ {d ∈ D | md = 0}, Ext^1_Z(Z/mZ, D) ≅ D/mD, and Ext^n_Z(Z/mZ, D) = 0 for n ≥ 2.

# Relationships
## Contrasts With
- **tor-functor** — Tor is the derived functor of tensor product; Ext is derived from Hom

## Enables
- **group-cohomology** — H^n(G,A) is a special case of Ext

# Source Reference
Chapter 17, Section 17.1, Definition, Propositions 3-5, Theorems 6-8, pages 781-788.

# Verification Notes
- Confidence: HIGH — thorough treatment with examples and independence proof
