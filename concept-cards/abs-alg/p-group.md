---
concept: p-Group
slug: p-group
category: group-theory
subcategory: group-actions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Group Actions"
chapter_number: 4
pdf_page: 142
section: "4.5 Sylow's Theorem"
extraction_confidence: high
aliases:
  - "p-subgroup"
  - "prime power group"
prerequisites:
  - group
  - order-of-group
  - lagranges-theorem
extends:
  - group
related:
  - sylow-p-subgroup
  - class-equation
  - nilpotent-group
contrasts_with:
  - sylow-p-subgroup
answers_questions:
  - "What is a p-group?"
  - "What are the basic properties of groups of prime power order?"
---

# Quick Definition
A p-group is a group whose order is a power of the prime p, i.e., |G| = p^a for some a >= 1. A p-subgroup of a group G is a subgroup that is itself a p-group.

# Core Definition
Let G be a group and let p be a prime. A group of order p^a for some a >= 1 is called a p-group. Subgroups of G which are p-groups are called p-subgroups (Dummit & Foote, p. 142). By Theorem 8 (p. 127), every p-group has a nontrivial center. By Corollary 9, groups of order p^2 are abelian, isomorphic to either Z_{p^2} or Z_p x Z_p.

# Prerequisites
- **Group** — A p-group is a group with specific order
- **Order of group** — The order must be a prime power
- **Lagrange's theorem** — Every element has p-power order

# Key Properties
1. Every p-group has nontrivial center: Z(P) != 1 (Theorem 8, via class equation)
2. Groups of order p^2 are abelian (Corollary 9)
3. Every element has order a power of p (by Lagrange's theorem)
4. P has normal subgroups of every order p^b dividing |P| (Theorem 6.1)
5. Every maximal subgroup has index p and is normal (Theorem 6.1)
6. Every proper subgroup is properly contained in its normalizer (Theorem 6.1)
7. Every p-group is nilpotent (Proposition 6.2)

# Examples
**Example 1**: Z_p, Z_{p^2}, Z_p x Z_p are p-groups.

**Example 2**: D_8 and Q_8 are 2-groups of order 8.

**Example 3** (p. 127): The class equation for Q_8 is 8 = 2 + 2 + 2 + 2.

# Relationships
## Builds Upon
- **Group** — A p-group is a group with prime-power order
## Enables
- **Sylow p-subgroup** — Maximal p-subgroups of a finite group
- **Nilpotent group** — p-groups are nilpotent
## Contrasts With
- **Sylow p-subgroup** — A p-group is any group of prime-power order; a Sylow p-subgroup is a maximal p-subgroup of a larger group

# Common Confusions
- **Confusion**: Confusing "p-group" with "Sylow p-subgroup"
  **Clarification**: Every Sylow p-subgroup is a p-group, but a p-group need not be a Sylow subgroup of anything. "p-group" refers to the group's own order; "Sylow p-subgroup" refers to its role inside a larger group.

# Source Reference
Chapter 4: Group Actions, Section 4.5, page 142. Properties in Chapter 6, Section 6.1, Theorem 1.

# Verification Notes
- Definition source: Direct from p. 142
- Confidence: HIGH — explicit definition
- Uncertainties: None
