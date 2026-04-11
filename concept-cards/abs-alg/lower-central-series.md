---
concept: Lower Central Series
slug: lower-central-series
category: group-theory
subcategory: further-topics
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Further Topics in Group Theory"
chapter_number: 6
pdf_page: 200
section: "6.1 p-Groups, Nilpotent Groups, and Solvable Groups"
extraction_confidence: high
aliases:
  - "descending central series"
prerequisites:
  - commutator-subgroup
  - characteristic-subgroup
extends:
  - commutator-subgroup
related:
  - upper-central-series
  - nilpotent-group
  - derived-series
contrasts_with:
  - upper-central-series
  - derived-series
answers_questions:
  - "What is the lower central series of a group?"
  - "How does the lower central series relate to nilpotency?"
---

# Quick Definition
The lower central series is G^0 = G >= G^1 = [G,G] >= G^2 = [G, G^1] >= ..., where G^{i+1} = [G, G^i]. A group is nilpotent iff G^n = 1 for some n.

# Core Definition
For any group G, define G^0 = G, G^1 = [G, G], and G^{i+1} = [G, G^i]. The chain G^0 >= G^1 >= G^2 >= ... is called the lower central series of G (Dummit & Foote, p. 200). Each G^i is characteristic in G. By Theorem 8, G is nilpotent of class c iff c is the smallest nonnegative integer with G^c = 1.

# Prerequisites
- **Commutator subgroup** — G^1 = [G,G] = G'
- **Characteristic subgroup** — Each G^i is characteristic in G

# Key Properties
1. G^i is characteristic in G for all i
2. G^0 = G, G^1 = G' = [G,G]
3. G^{i+1} = [G, G^i]
4. G is nilpotent iff G^n = 1 for some n (Theorem 8)
5. G^{(i)} <= G^i (derived series terms are contained in lower central series terms)
6. For non-nilpotent groups, the series stabilizes at a nontrivial subgroup

# Examples
**Example 1** (p. 201): For S_3: G^1 = A_3, G^2 = [S_3, A_3] = A_3, so the series stabilizes at A_3. Since G^n = A_3 != 1 for all n, S_3 is not nilpotent.

# Relationships
## Builds Upon
- **Commutator subgroup** — First step is the commutator subgroup
## Enables
- **Nilpotent group** — Alternative characterization via lower central series
## Contrasts With
- **Upper central series** — Ascending vs. descending
- **Derived series** — Uses [G^{(i)}, G^{(i)}] instead of [G, G^i]

# Common Confusions
- **Confusion**: Confusing G^i (lower central series) with G^{(i)} (derived series)
  **Clarification**: G^{i+1} = [G, G^i] uses the whole group G; G^{(i+1)} = [G^{(i)}, G^{(i)}] uses G^{(i)} with itself. We have G^{(i)} <= G^i, and equality holds for i = 0, 1 but not generally.

# Source Reference
Chapter 6, Section 6.1, pages 200-201.

# Verification Notes
- Definition source: Direct from p. 200
- Confidence: HIGH
- Uncertainties: None
