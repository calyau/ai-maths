---
concept: Inner Automorphism
slug: inner-automorphism
category: group-theory
subcategory: group-actions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Group Actions"
chapter_number: 4
pdf_page: 136
section: "4.4 Automorphisms"
extraction_confidence: high
aliases:
  - "conjugation automorphism"
prerequisites:
  - automorphism
  - conjugation
  - center
extends:
  - automorphism
related:
  - automorphism-group
  - outer-automorphism-group
  - normal-subgroup
contrasts_with:
  - outer-automorphism-group
answers_questions:
  - "What is an inner automorphism?"
  - "How does Inn(G) relate to G/Z(G)?"
---

# Quick Definition
Conjugation by a fixed element g in G defines an automorphism of G called an inner automorphism. The group of all inner automorphisms, Inn(G), is isomorphic to G/Z(G) and is a normal subgroup of Aut(G).

# Core Definition
Let G be a group and let g in G. Conjugation by g, defined by phi_g(x) = gxg^{-1}, is called an inner automorphism of G. The subgroup of Aut(G) consisting of all inner automorphisms is denoted by Inn(G) (Dummit & Foote, p. 136). By Corollary 15, Inn(G) is isomorphic to G/Z(G), and Inn(G) is a normal subgroup of Aut(G).

# Prerequisites
- **Automorphism** — Inner automorphisms are specific automorphisms
- **Conjugation** — The defining operation
- **Center** — The kernel of the map g -> phi_g

# Key Properties
1. phi_g(x) = gxg^{-1} defines an automorphism of G
2. Inn(G) is isomorphic to G/Z(G) (Corollary 15)
3. Inn(G) is a normal subgroup of Aut(G) (Exercise 1, p. 139)
4. G is abelian iff Inn(G) = {id}
5. sigma phi_g sigma^{-1} = phi_{sigma(g)} for any sigma in Aut(G) (Exercise 1)

# Examples
**Example 1** (p. 136): Inn(Q_8) is isomorphic to V_4 since Z(Q_8) = <-1>.

**Example 2** (p. 137): Inn(S_n) is isomorphic to S_n for n >= 3 since Z(S_n) = 1.

# Relationships
## Builds Upon
- **Automorphism** — Inner automorphisms are a special type
## Enables
- **Outer automorphism group** — Defined as Aut(G)/Inn(G)
## Related
- **Normal subgroup** — A subgroup is normal iff it is invariant under all inner automorphisms

# Common Confusions
- **Confusion**: Thinking every automorphism is inner
  **Clarification**: For n != 6, Aut(S_n) = Inn(S_n), but Aut(S_6) has outer automorphisms

# Source Reference
Chapter 4: Group Actions, Section 4.4, page 136. Corollary 15, page 136.

# Verification Notes
- Definition source: Direct from p. 136
- Confidence: HIGH — explicit definition
- Uncertainties: None
