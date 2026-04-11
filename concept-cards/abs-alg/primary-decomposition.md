---
concept: Primary Decomposition
slug: primary-decomposition
category: commutative-algebra
subcategory: ideal-theory
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Commutative Rings and Algebraic Geometry"
chapter_number: 15
pdf_page: 710
section: "15.2 Radicals and Affine Varieties"
extraction_confidence: high
aliases:
  - "Lasker-Noether decomposition"
  - "minimal primary decomposition"
prerequisites:
  - primary-ideal
  - noetherian-ring
extends: []
related:
  - associated-prime-ideal
contrasts_with: []
answers_questions:
  - "What is primary decomposition in a Noetherian ring?"
---

# Quick Definition
Every proper ideal in a Noetherian ring can be written as a finite intersection of primary ideals. The associated prime ideals in any minimal decomposition are uniquely determined.

# Core Definition
An ideal I has a **primary decomposition** if I = Q_1 ∩ ··· ∩ Q_m where each Q_i is primary. The decomposition is **minimal** if no Q_i contains the intersection of the others, and the associated primes rad Q_i are all distinct (Definition, p. 710). **Theorem 21 (Primary Decomposition Theorem)**: Every proper ideal in a Noetherian ring has a minimal primary decomposition, and the set of associated primes is uniquely determined. The primary components belonging to minimal (isolated) primes are also unique.

# Prerequisites
- **primary-ideal** — The components of the decomposition
- **noetherian-ring** — Ensures existence of decomposition

# Key Properties
1. Existence in Noetherian rings (Theorem 21)
2. Uniqueness of the set of associated primes
3. Primary components of isolated primes are unique
4. Embedded prime components may not be unique
5. rad I = intersection of isolated primes (Corollary 22(2))
6. Generalizes unique factorization: in a UFD, (p_1^{e_1}···p_m^{e_m}) = (p_1)^{e_1} ∩ ··· ∩ (p_m)^{e_m}

# Examples
**Example** (p. 713): (x^2,xy) = (x) ∩ (x,y)^2 = (x) ∩ (x^2,y) gives two minimal primary decompositions in R[x,y], with associated primes (x) (isolated) and (x,y) (embedded).

# Relationships
## Builds Upon
- **primary-ideal** — Components of decomposition are primary

## Enables
- **associated-prime-ideal** — Associated primes provide information about ideal structure

# Source Reference
Chapter 15, Section 15.2, Theorem 21 and Corollary 22, pages 710-713.

# Verification Notes
- Confidence: HIGH — major theorem with uniqueness results
