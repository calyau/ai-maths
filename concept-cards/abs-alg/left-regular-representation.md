---
concept: Left Regular Representation
slug: left-regular-representation
category: group-theory
subcategory: group-actions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Group Actions"
chapter_number: 4
pdf_page: 118
section: "4.2 Groups Acting on Themselves by Left Multiplication"
extraction_confidence: high
aliases: []
prerequisites:
  - group-action
  - permutation-representation
extends:
  - permutation-representation
related:
  - cayleys-theorem
  - faithful-action
  - transitive-action
contrasts_with: []
answers_questions:
  - "What is the left regular representation of a group?"
---

# Quick Definition
The left regular representation of G is the permutation representation pi: G -> S_G obtained from G acting on itself by left multiplication: g . a = ga. This action is always faithful and transitive, yielding the embedding used in Cayley's Theorem.

# Core Definition
The permutation representation afforded by left multiplication on the elements of G (cosets of H = 1) is called the left regular representation of G (Dummit & Foote, p. 120). For each g in G, the permutation sigma_g is defined by sigma_g(i) = j where g * g_i = g_j. This action is faithful (kernel is trivial) and transitive (every element can be moved to any other). The stabilizer of any point is the identity subgroup.

# Prerequisites
- **Group action** — Left multiplication is a group action
- **Permutation representation** — Produces a homomorphism G -> S_n

# Key Properties
1. Always faithful (kernel = 1)
2. Always transitive
3. Stabilizer of every point is {1}
4. Gives an embedding G -> S_n where n = |G|
5. Foundation for Cayley's Theorem

# Examples
**Example 1** (p. 119): V_4 = {1, a, b, c} maps to: a -> (12)(34), b -> (13)(24), c -> (14)(23) in S_4.

# Relationships
## Builds Upon
- **Permutation representation**
## Enables
- **Cayley's theorem** — Uses this representation

# Source Reference
Chapter 4, Section 4.2, pages 118-122.

# Verification Notes
- Definition source: Direct from p. 120
- Confidence: HIGH
- Uncertainties: None
