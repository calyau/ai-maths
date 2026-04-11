---
concept: Maximal Subgroup
slug: maximal-subgroup
category: group-theory
subcategory: further-topics
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Further Topics in Group Theory"
chapter_number: 6
pdf_page: 188
section: "6.1 p-Groups, Nilpotent Groups, and Solvable Groups"
extraction_confidence: high
aliases: []
prerequisites:
  - subgroup
  - normal-subgroup
extends:
  - subgroup
related:
  - p-group
  - nilpotent-group
contrasts_with: []
answers_questions:
  - "What is a maximal subgroup?"
  - "What is special about maximal subgroups in p-groups?"
---

# Quick Definition
A maximal subgroup of G is a proper subgroup M such that there are no subgroups H with M < H < G. In p-groups, every maximal subgroup has index p and is normal.

# Core Definition
A maximal subgroup of a group G is a proper subgroup M of G such that there are no subgroups H of G with M < H < G (Dummit & Foote, p. 188). By Theorem 1(5), every maximal subgroup of a p-group has index p and is normal. By Proposition 7, a finite group is nilpotent iff every maximal subgroup is normal. Every proper subgroup of a finite group is contained in some maximal subgroup.

# Prerequisites
- **Subgroup** — Maximal subgroups are subgroups
- **Normal subgroup** — In nilpotent groups, all maximal subgroups are normal

# Key Properties
1. M is proper and no proper subgroup of G properly contains M
2. In p-groups, maximal subgroups have index p and are normal (Theorem 1(5))
3. Finite group is nilpotent iff every maximal subgroup is normal (Proposition 7)
4. Every proper subgroup of a finite group is contained in a maximal subgroup
5. Infinite groups need not have maximal subgroups (e.g., Q under addition)

# Examples
**Example 1**: The maximal subgroups of Z_{p^2} are the single subgroup of order p.

**Example 2** (p. 188): pZ is a maximal subgroup of Z; Q (rationals under addition) has no maximal subgroups.

# Relationships
## Builds Upon
- **Subgroup** — Maximal subgroups are maximal proper subgroups
## Related
- **p-group** — Maximal subgroups of p-groups have index p
- **Nilpotent group** — Characterized by normality of all maximal subgroups

# Source Reference
Chapter 6, Section 6.1, pages 188-189. Theorem 1(5) and Proposition 7.

# Verification Notes
- Definition source: Direct from p. 188
- Confidence: HIGH
- Uncertainties: None
