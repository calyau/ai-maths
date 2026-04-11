---
concept: Automorphism Group
slug: automorphism-group
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
  - "Aut(G)"
prerequisites:
  - automorphism
  - group
extends:
  - automorphism
related:
  - inner-automorphism
  - outer-automorphism-group
  - semidirect-product
contrasts_with: []
answers_questions:
  - "What is the automorphism group of a group?"
  - "How is Aut(Z_n) determined?"
---

# Quick Definition
The automorphism group Aut(G) is the group of all automorphisms of G under composition. It is a subgroup of S_G. Key examples: Aut(Z_n) is isomorphic to (Z/nZ)^x of order phi(n), and Aut(Z_p x Z_p) is isomorphic to GL_2(F_p).

# Core Definition
The set of all automorphisms of G is denoted by Aut(G) and forms a group under composition, the automorphism group of G (Dummit & Foote, p. 133). Since automorphisms are permutations of G, Aut(G) <= S_G. By Proposition 16, Aut(Z_n) is isomorphic to (Z/nZ)^x, abelian of order phi(n). By Proposition 17(3), Aut(Z_p x Z_p) is isomorphic to GL_2(F_p). Inn(G) is a normal subgroup of Aut(G), with Aut(G)/Inn(G) the outer automorphism group.

# Prerequisites
- **Automorphism** — Elements of Aut(G)
- **Group** — Aut(G) is itself a group

# Key Properties
1. Aut(G) is a group under composition
2. Aut(G) <= S_G
3. Inn(G) is a normal subgroup of Aut(G)
4. Aut(Z_n) is isomorphic to (Z/nZ)^x, of order phi(n)
5. Aut(Z_p x Z_p) = GL_2(F_p), of order p(p-1)^2(p+1)
6. Aut(S_n) = Inn(S_n) = S_n for n != 6; |Aut(S_6) : Inn(S_6)| = 2
7. G/Z(G) embeds in Aut(G) via inner automorphisms (Corollary 15)

# Examples
**Example 1** (p. 136): Aut(Z_2) = 1. Aut(V_4) = S_3.

**Example 2** (p. 137): Aut(D_8) = D_8. Aut(Q_8) = S_4.

# Relationships
## Builds Upon
- **Automorphism** — Aut(G) collects all automorphisms
## Enables
- **Semidirect product** — Defined via homomorphisms K -> Aut(H)
- **Outer automorphism group** — Aut(G)/Inn(G)

# Source Reference
Chapter 4, Section 4.4, pages 133-141.

# Verification Notes
- Definition source: Direct from p. 133
- Confidence: HIGH
- Uncertainties: None
