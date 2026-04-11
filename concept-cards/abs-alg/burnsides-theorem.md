---
concept: "Burnside's Theorem (p^a q^b)"
slug: burnsides-theorem
category: representation-theory
subcategory: applications
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Examples and Applications of Character Theory"
chapter_number: 19
pdf_page: 892
section: "19.2 Theorems of Burnside and Hall"
extraction_confidence: high
aliases:
  - "Burnside p^a q^b theorem"
prerequisites:
  - character
  - orthogonality-relations
extends: []
related:
  - halls-theorem
contrasts_with: []
answers_questions:
  - "What is Burnside's theorem about groups of order p^a q^b?"
---

# Quick Definition
Every group of order p^a q^b (p, q prime) is solvable. This is proved using character theory — one of the earliest applications of representation theory to pure group theory.

# Core Definition
**Burnside's Theorem** (p. 892): If G is a finite group with |G| = p^a q^b for primes p, q, then G is solvable. The proof uses the fact that an irreducible character of degree not divisible by a prime p must take the value 0 on some element of a Sylow p-subgroup.

# Prerequisites
- **character** — The proof is character-theoretic
- **orthogonality-relations** — Used in the proof

# Key Properties
1. No simple group has order p^a q^b (for a,b ≥ 1)
2. Proved using representation theory (no purely group-theoretic proof was known for decades)
3. A remarkable application showing representation theory can prove results about groups

# Relationships
## Related
- **halls-theorem** — Another application of character theory to group structure

# Source Reference
Chapter 19, Section 19.2, Burnside's Theorem, pages 892-895.

# Verification Notes
- Confidence: HIGH — named theorem with character-theoretic proof
