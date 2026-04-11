---
concept: Artinian Ring
slug: artinian-ring
category: commutative-algebra
subcategory: chain-conditions
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Artinian Rings, Discrete Valuation Rings, and Dedekind Domains"
chapter_number: 16
pdf_page: 750
section: "16.1 Artinian Rings"
extraction_confidence: high
aliases:
  - "ring satisfying D.C.C."
  - "descending chain condition"
prerequisites:
  - noetherian-ring
  - ring
extends: []
related:
  - krull-dimension
contrasts_with:
  - noetherian-ring
answers_questions:
  - "What is an Artinian ring?"
  - "What distinguishes an Artinian ring from a Noetherian ring?"
---

# Quick Definition
A commutative ring is Artinian if it satisfies the descending chain condition (D.C.C.) on ideals: every decreasing chain of ideals eventually stabilizes.

# Core Definition
A commutative ring R is **Artinian** if there is no infinite decreasing chain of ideals. A commutative ring is Artinian if and only if it is Noetherian and has Krull dimension 0 (i.e., every prime ideal is maximal). In particular, every commutative Artinian ring is Noetherian, but not conversely (Z is Noetherian but not Artinian).

# Prerequisites
- **noetherian-ring** — Every Artinian ring is Noetherian
- **ring** — Artinian is a property of commutative rings

# Key Properties
1. D.C.C. on ideals implies A.C.C. (i.e., Artinian implies Noetherian) for commutative rings
2. Artinian iff Noetherian with Krull dimension 0
3. Every prime ideal in an Artinian ring is maximal
4. Artinian rings have finitely many maximal ideals
5. An Artinian ring is a finite direct product of Artinian local rings

# Examples
**Example**: k[x]/(f(x)) for any nonzero f is Artinian (finite dimensional over k).

**Example**: Z is Noetherian but not Artinian: (2) ⊃ (4) ⊃ (8) ⊃ ··· is an infinite descending chain.

# Relationships
## Contrasts With
- **noetherian-ring** — Noetherian = A.C.C.; Artinian = D.C.C. Artinian ⟹ Noetherian but not conversely.

# Source Reference
Chapter 16, Section 16.1, pages 750-756.

# Verification Notes
- Confidence: HIGH — fundamental definitions and equivalences stated
