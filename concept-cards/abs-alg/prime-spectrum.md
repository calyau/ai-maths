---
concept: Prime Spectrum
slug: prime-spectrum
category: algebraic-geometry
subcategory: scheme-theory
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Commutative Rings and Algebraic Geometry"
chapter_number: 15
pdf_page: 735
section: "15.5 The Prime Spectrum of a Ring"
extraction_confidence: high
aliases:
  - "Spec R"
  - "spectrum"
  - "maximal spectrum"
  - "mSpec R"
prerequisites:
  - prime-ideal
  - zariski-topology
  - localization
extends: []
related:
  - affine-variety
  - structure-sheaf
contrasts_with: []
answers_questions:
  - "What is the prime spectrum of a ring?"
  - "How does localization relate to the prime spectrum?"
---

# Quick Definition
The prime spectrum Spec R is the set of all prime ideals of R, equipped with the Zariski topology. It generalizes affine algebraic sets to arbitrary commutative rings.

# Core Definition
The **spectrum** or **prime spectrum** of R, denoted Spec R, is the set of all prime ideals of R (Definition, p. 736). The **maximal spectrum** mSpec R is the subset of maximal ideals. For f ∈ R, the "value" of f at P ∈ Spec R is f̄ ∈ R/P. The Zariski topology on Spec R has closed sets Z(I) = {P ∈ Spec R | I ⊆ P}. By Proposition 54, Z and I define inverse bijections between Zariski closed subsets and radical ideals.

# Prerequisites
- **prime-ideal** — Points of Spec R are prime ideals
- **zariski-topology** — The topology on Spec R
- **localization** — The stalk at P is R_P

# Key Properties
1. Closed points = maximal ideals; generic points = minimal primes
2. Spec R is irreducible iff R/nilrad(R) is a domain
3. Ring homomorphisms R → S induce continuous maps Spec S → Spec R
4. For k[V] over algebraically closed k: mSpec k[V] ↔ points of V, Spec k[V] ↔ subvarieties

# Examples
**Example** (p. 736): Spec Z = {(0), (2), (3), (5), (7),...}. The point (0) is dense (generic).

**Example** (p. 737): Spec Z[x] has four types of points: (0), (p), (f), and (p,g).

# Relationships
## Builds Upon
- **zariski-topology** — The topology on Spec R
- **localization** — The stalk at P is the local ring R_P

## Enables
- **structure-sheaf** — Functions on Spec R are captured by a sheaf of rings

# Source Reference
Chapter 15, Section 15.5, Definitions and Propositions 53-54, pages 735-740.

# Verification Notes
- Confidence: HIGH — explicit definitions with detailed examples
