---
concept: Automorphism
slug: automorphism
category: group-theory
subcategory: group-actions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Group Actions"
chapter_number: 4
pdf_page: 133
section: "4.4 Automorphisms"
extraction_confidence: high
aliases:
  - "group automorphism"
prerequisites:
  - isomorphism
  - group
extends:
  - isomorphism
related:
  - inner-automorphism
  - automorphism-group
  - characteristic-subgroup
contrasts_with:
  - inner-automorphism
answers_questions:
  - "What is an automorphism of a group?"
  - "How does the automorphism group of a cyclic group relate to Euler's function?"
---

# Quick Definition
An automorphism of a group G is an isomorphism from G onto itself. The set of all automorphisms forms a group under composition, denoted Aut(G).

# Core Definition
Let G be a group. An isomorphism from G onto itself is called an automorphism of G. The set of all automorphisms of G is denoted by Aut(G) (Dummit & Foote, p. 133). Since automorphisms are permutations of the set G, Aut(G) is a subgroup of S_G. By Proposition 16, Aut(Z_n) is isomorphic to (Z/nZ)^x, an abelian group of order phi(n).

# Prerequisites
- **Isomorphism** — An automorphism is an isomorphism from G to itself
- **Group** — The object being mapped to itself

# Key Properties
1. Aut(G) is a group under composition
2. Aut(G) is a subgroup of S_G (automorphisms are permutations of G)
3. Aut(Z_n) is isomorphic to (Z/nZ)^x, of order phi(n) (Proposition 16)
4. Automorphisms preserve subgroup structure, element orders, etc.
5. G/Z(G) is isomorphic to a subgroup of Aut(G) (Corollary 15)

# Examples
**Example 1** (p. 136): If G = Z_2, then Aut(G) = 1 (the unique nonidentity element must map to itself).

**Example 2** (p. 138): Aut(V_4) is isomorphic to GL_2(F_2) is isomorphic to S_3, of order 6.

**Example 3** (p. 137): Aut(S_n) = Inn(S_n) is isomorphic to S_n for all n != 6. For n = 6, |Aut(S_6) : Inn(S_6)| = 2.

# Relationships
## Builds Upon
- **Isomorphism** — Automorphisms are self-isomorphisms
## Enables
- **Automorphism group** — The group of all automorphisms
- **Inner automorphism** — Conjugation gives automorphisms
- **Characteristic subgroup** — Subgroups invariant under all automorphisms
- **Semidirect product** — Defined using homomorphisms into Aut(H)

# Source Reference
Chapter 4: Group Actions, Section 4.4, pages 133-141.

# Verification Notes
- Definition source: Direct from p. 133
- Confidence: HIGH — explicit definition
- Uncertainties: None
