---
concept: Nilpotent Group
slug: nilpotent-group
category: group-theory
subcategory: further-topics
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Further Topics in Group Theory"
chapter_number: 6
pdf_page: 188
section: "6.1 p-Groups, Nilpotent Groups, and Solvable Groups"
extraction_confidence: high
aliases:
  - "nilpotent"
prerequisites:
  - p-group
  - center
  - normal-subgroup
  - upper-central-series
extends:
  - p-group
related:
  - solvable-group
  - upper-central-series
  - lower-central-series
  - sylow-p-subgroup
contrasts_with:
  - solvable-group
answers_questions:
  - "What is a nilpotent group?"
  - "What are the equivalent characterizations of finite nilpotent groups?"
---

# Quick Definition
A group G is nilpotent if its upper central series reaches G: Z_c(G) = G for some c. Equivalently (for finite groups): every Sylow subgroup is normal, or G is the direct product of its Sylow subgroups, or every proper subgroup is properly contained in its normalizer.

# Core Definition
A group G is called nilpotent if Z_c(G) = G for some c in Z. The smallest such c is called the nilpotence class of G (Dummit & Foote, p. 193). Theorem 3 gives equivalent characterizations for finite groups: (1) G is nilpotent; (2) every proper subgroup is a proper subgroup of its normalizer; (3) every Sylow subgroup is normal; (4) G is the direct product of its Sylow subgroups. The hierarchy is: cyclic < abelian < nilpotent < solvable < all groups.

# Prerequisites
- **p-group** — Every p-group is nilpotent (Proposition 2)
- **Center** — The upper central series uses iterated centers
- **Normal subgroup** — Nilpotent groups have many normal subgroups
- **Upper central series** — Defines nilpotency

# Key Properties
1. Every p-group is nilpotent of class at most a-1 where |P| = p^a (Proposition 2)
2. Abelian groups are nilpotent of class 1 (if nontrivial)
3. Finite nilpotent iff every Sylow subgroup is normal (Theorem 3)
4. Finite nilpotent iff direct product of Sylow subgroups (Theorem 3)
5. Finite nilpotent iff every proper subgroup is properly contained in its normalizer
6. Every maximal subgroup of a nilpotent group is normal (Proposition 7)
7. Subgroups and quotients of nilpotent groups are nilpotent

# Examples
**Example 1** (p. 194): D_8 and Q_8 are nilpotent of class 2. More generally, D_{2^n} is nilpotent of class n-1.

**Example 2** (p. 197): D_{2n} is nilpotent iff n is a power of 2.

**Example 3**: S_3 is NOT nilpotent (its Sylow 2-subgroups are not normal).

# Relationships
## Builds Upon
- **p-group** — p-groups are the prototypical nilpotent groups
## Enables
- **Understanding group structure** — Nilpotent groups are well-behaved
## Related
- **Upper central series** — Defines nilpotency
- **Lower central series** — Alternative characterization via G^n = 1
## Contrasts With
- **Solvable group** — All nilpotent groups are solvable, but not conversely (S_3 is solvable but not nilpotent)

# Common Confusions
- **Confusion**: Thinking nilpotent and solvable are the same
  **Clarification**: Every nilpotent group is solvable, but S_3 is solvable and not nilpotent

# Source Reference
Chapter 6, Section 6.1, pages 188-201. Theorem 3 on p. 196.

# Verification Notes
- Definition source: Direct from p. 193
- Confidence: HIGH — explicit definition with equivalent characterizations
- Uncertainties: None
