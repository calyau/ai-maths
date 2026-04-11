---
concept: Free Group
slug: free-group
category: group-theory
subcategory: further-topics
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Further Topics in Group Theory"
chapter_number: 6
pdf_page: 215
section: "6.3 A Word on Free Groups"
extraction_confidence: high
aliases:
  - "free group on a set"
prerequisites:
  - group
  - homomorphism
  - symmetric-group
extends:
  - group
related:
  - presentation
  - generators-and-relations
  - free-abelian-group
contrasts_with:
  - free-abelian-group
answers_questions:
  - "What is a free group?"
  - "What is the universal property of free groups?"
---

# Quick Definition
The free group F(S) on a set S is the group of reduced words in the elements of S and their inverses, with concatenation (followed by reduction) as the operation. There are no relations among the generators beyond the group axioms.

# Core Definition
F(S) is the set of reduced words on S with binary operation defined by concatenation and cancellation (Theorem 16, Dummit & Foote, p. 218). Universal property (Theorem 17): given any set map phi: S -> G to a group G, there is a unique group homomorphism Phi: F(S) -> G extending phi. A group F is free if F = F(S) for some set S; S is a set of free generators and |S| is the rank. If |S| > 1, F(S) is non-abelian (Exercise 2). Every nonidentity element has infinite order (Exercise 4). Subgroups of free groups are free (Schreier's Theorem).

# Prerequisites
- **Group** — Free groups are groups
- **Homomorphism** — The universal property involves homomorphisms
- **Symmetric group** — Used in proving associativity

# Key Properties
1. Universal property: any set map S -> G extends uniquely to a homomorphism F(S) -> G
2. F(S) is unique up to unique isomorphism (Corollary 18)
3. If |S| > 1, F(S) is non-abelian
4. Every nonidentity element has infinite order
5. Subgroups of free groups are free (Schreier's Theorem)
6. Every group is a quotient of a free group

# Construction / Recognition
## To Construct F(S):
1. Form all reduced words in elements of S and S^{-1}
2. A word is reduced if no s is adjacent to s^{-1}
3. Multiply by concatenating and canceling adjacent inverse pairs

# Context & Application
Free groups are foundational for presentations of groups. Every group G can be written as F(S)/N for some normal subgroup N of a free group. The universal property makes free groups the "most general" groups on a given set of generators. Free objects appear across algebra: free abelian groups, free modules, polynomial algebras.

# Examples
**Example 1** (p. 219): F({a}) = <a> is isomorphic to Z (the infinite cyclic group).

**Example 2** (p. 221): Z x Z = <a, b | [a,b] = 1> is NOT free on {a,b}; it's the free abelian group of rank 2.

# Relationships
## Enables
- **Presentation** — Groups are presented as quotients of free groups
- **Generators and relations** — Formalized via free groups
## Contrasts With
- **Free abelian group** — Free abelian group on S has the additional relation [s,t] = 1 for all s, t in S

# Common Confusions
- **Confusion**: Thinking free groups are always abelian
  **Clarification**: Free groups on more than one generator are non-abelian; the free abelian group is a different construction

# Source Reference
Chapter 6, Section 6.3, pages 215-224. Theorems 16-19.

# Verification Notes
- Definition source: Direct from pp. 218-219
- Confidence: HIGH — explicit construction and proof
- Uncertainties: None
