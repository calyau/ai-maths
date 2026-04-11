---
concept: Properties of p-Groups
slug: p-group-properties
category: group-theory
subcategory: further-topics
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Further Topics in Group Theory"
chapter_number: 6
pdf_page: 189
section: "6.1 p-Groups, Nilpotent Groups, and Solvable Groups"
extraction_confidence: high
aliases:
  - "omnibus theorem for p-groups"
prerequisites:
  - p-group
  - class-equation
  - center
  - normal-subgroup
  - maximal-subgroup
extends:
  - p-group
related:
  - nilpotent-group
  - sylow-p-subgroup
contrasts_with: []
answers_questions:
  - "What structural properties must p-groups satisfy?"
  - "Why do p-groups have nontrivial centers?"
---

# Quick Definition
The omnibus theorem (Theorem 6.1) establishes five key properties of p-groups: (1) nontrivial center, (2) nontrivial normal subgroups intersect center nontrivially, (3) normal subgroups of all possible orders exist, (4) proper subgroups are proper subgroups of their normalizers, (5) maximal subgroups have index p and are normal.

# Core Definition
Theorem 1: Let p be a prime and P a group of order p^a, a >= 1. Then (1) Z(P) != 1; (2) if H is nontrivial normal in P then H intersect Z(P) != 1, and normal subgroups of order p lie in Z(P); (3) for each divisor p^b of |H| (H normal in P), H contains a subgroup of order p^b normal in P; (4) if H < P then H < N_P(H); (5) every maximal subgroup has index p and is normal (Dummit & Foote, pp. 189-191).

# Prerequisites
- **p-group** — These are properties of p-groups
- **Class equation** — Central tool in the proofs
- **Center** — Property (1) concerns the center
- **Normal subgroup** — Many properties involve normality
- **Maximal subgroup** — Property (5)

# Key Properties
1. Nontrivial center (proved via class equation; p divides |Z(P)|)
2. Every nontrivial normal subgroup meets the center nontrivially
3. Normal subgroups of every possible p-power order exist
4. Every proper subgroup is properly contained in its normalizer
5. Every maximal subgroup has index p and is normal

# Context & Application
These properties are the starting point for understanding p-groups and are used extensively in Sylow theory applications and classification of groups of specific orders. Property (4) is particularly important: it is one of the equivalent characterizations of nilpotent groups (Theorem 3).

# Relationships
## Builds Upon
- **p-group** — Properties of p-groups
## Enables
- **Nilpotent group** — p-groups are nilpotent because of these properties

# Source Reference
Chapter 6, Section 6.1, Theorem 1, pages 189-191.

# Verification Notes
- Definition source: Direct from Theorem 1, pp. 189-191
- Confidence: HIGH — major theorem, fully proved
- Uncertainties: None
