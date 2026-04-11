---
concept: Outer Automorphism Group
slug: outer-automorphism-group
category: group-theory
subcategory: group-actions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Group Actions"
chapter_number: 4
pdf_page: 139
section: "4.4 Automorphisms"
extraction_confidence: high
aliases:
  - "Out(G)"
prerequisites:
  - automorphism-group
  - inner-automorphism
  - quotient-group
extends:
  - automorphism-group
related:
  - inner-automorphism
contrasts_with:
  - inner-automorphism
answers_questions:
  - "What is the outer automorphism group?"
  - "When does a group have outer automorphisms?"
---

# Quick Definition
The outer automorphism group of G is Out(G) = Aut(G)/Inn(G), the quotient of the automorphism group by the inner automorphism group. An automorphism is "outer" if it is not conjugation by any element.

# Core Definition
The group Aut(G)/Inn(G) is called the outer automorphism group of G (Exercise 1, Dummit & Foote, p. 139). By Proposition 17(4), Aut(S_n) = Inn(S_n) for n != 6, so Out(S_n) = 1 for n != 6. For n = 6, |Aut(S_6) : Inn(S_6)| = 2, so Out(S_6) = Z_2.

# Prerequisites
- **Automorphism group** — Out(G) is a quotient of Aut(G)
- **Inner automorphism** — Inn(G) is the normal subgroup being quotiented out
- **Quotient group** — Out(G) is a quotient group

# Key Properties
1. Out(G) = Aut(G) / Inn(G)
2. Out(G) = 1 iff every automorphism is inner
3. Out(S_n) = 1 for n != 6
4. Out(S_6) = Z_2

# Relationships
## Builds Upon
- **Automorphism group** and **Inner automorphism**
## Contrasts With
- **Inner automorphism** — Elements of Inn(G) are the "trivial" automorphisms

# Source Reference
Chapter 4, Section 4.4, Exercise 1, p. 139. Proposition 17(4).

# Verification Notes
- Definition source: From Exercise 1, p. 139
- Confidence: HIGH
- Uncertainties: None
