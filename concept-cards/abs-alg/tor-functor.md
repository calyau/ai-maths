---
concept: Tor Functor
slug: tor-functor
category: homological-algebra
subcategory: derived-functors
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Homological Algebra and Group Cohomology"
chapter_number: 17
pdf_page: 789
section: "17.1 Introduction to Homological Algebra"
extraction_confidence: high
aliases:
  - "Tor^n"
  - "Tor groups"
prerequisites:
  - projective-resolution
  - tensor-product
extends: []
related:
  - ext-functor
contrasts_with:
  - ext-functor
answers_questions:
  - "What is the Tor functor?"
---

# Quick Definition
Tor^R_n(A,D) is the n-th homology group obtained by tensoring a projective resolution of A with D. Tor_0 = A ⊗_R D, and higher Tor groups measure failure of tensoring to be exact.

# Core Definition
For R-modules A and D, take a projective resolution of A and tensor with D to get the chain complex ··· → P_1 ⊗ D → P_0 ⊗ D → 0. Then **Tor^R_n(A,D)** is the n-th homology of this complex (p. 789). Tor_0(A,D) ≅ A ⊗_R D. A is flat iff Tor_1(A,D) = 0 for all D.

# Prerequisites
- **projective-resolution** — Used to compute Tor
- **tensor-product** — Tor is derived from tensoring

# Key Properties
1. Tor_0(A,D) ≅ A ⊗_R D
2. Independent of projective resolution
3. A is flat iff Tor_1(A,D) = 0 for all D
4. Short exact sequences give long exact sequences in Tor

# Examples
**Example** (p. 789): Tor^Z_1(Z/mZ, D) ≅ {d ∈ D | md = 0} and Tor^Z_n(Z/mZ, D) = 0 for n ≥ 2.

# Relationships
## Contrasts With
- **ext-functor** — Ext is derived from Hom; Tor from tensor product

# Source Reference
Chapter 17, Section 17.1, pages 789-791.

# Verification Notes
- Confidence: HIGH — parallel treatment to Ext
