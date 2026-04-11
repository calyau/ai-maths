---
concept: "Hall's Theorem"
slug: halls-theorem
category: representation-theory
subcategory: applications
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Examples and Applications of Character Theory"
chapter_number: 19
pdf_page: 896
section: "19.2 Theorems of Burnside and Hall"
extraction_confidence: high
aliases:
  - "Hall subgroups"
prerequisites:
  - group
  - character
extends: []
related:
  - burnsides-theorem
contrasts_with: []
answers_questions:
  - "What is Hall's theorem on solvable groups?"
---

# Quick Definition
A finite group G is solvable if and only if for every divisor d of |G| with gcd(d, |G|/d) = 1, G has a subgroup of order d (a Hall subgroup). This generalizes Sylow's theorem to solvable groups.

# Core Definition
**Hall's Theorem** (p. 896): A finite group G is solvable if and only if G has a Hall π-subgroup for every set of primes π. Moreover, any two Hall π-subgroups are conjugate, and any π-subgroup is contained in a Hall π-subgroup. This is a strong generalization of Sylow's theorems to solvable groups.

# Prerequisites
- **group** — Applies to finite groups
- **character** — Character theory provides tools for the proof

# Source Reference
Chapter 19, Section 19.2, Hall's Theorem, pages 896-900.

# Verification Notes
- Confidence: HIGH — stated theorem
