---
concept: Upper Central Series
slug: upper-central-series
category: group-theory
subcategory: further-topics
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Further Topics in Group Theory"
chapter_number: 6
pdf_page: 192
section: "6.1 p-Groups, Nilpotent Groups, and Solvable Groups"
extraction_confidence: high
aliases:
  - "ascending central series"
prerequisites:
  - center
  - quotient-group
  - normal-subgroup
extends:
  - center
related:
  - nilpotent-group
  - lower-central-series
contrasts_with:
  - lower-central-series
  - derived-series
answers_questions:
  - "What is the upper central series of a group?"
  - "How does the upper central series relate to nilpotency?"
---

# Quick Definition
The upper central series of G is the ascending chain Z_0(G) = 1 <= Z_1(G) = Z(G) <= Z_2(G) <= ..., where Z_{i+1}(G)/Z_i(G) = Z(G/Z_i(G)). A group is nilpotent iff this series reaches G.

# Core Definition
For any group G, define inductively: Z_0(G) = 1, Z_1(G) = Z(G), and Z_{i+1}(G) is the subgroup of G containing Z_i(G) such that Z_{i+1}(G)/Z_i(G) = Z(G/Z_i(G)). The chain Z_0(G) <= Z_1(G) <= Z_2(G) <= ... is called the upper central series of G (Dummit & Foote, p. 192). Each Z_i(G) is a characteristic subgroup of G. G is nilpotent iff Z_c(G) = G for some c.

# Prerequisites
- **Center** — Z_1(G) = Z(G) starts the series
- **Quotient group** — Each step uses the center of a quotient
- **Normal subgroup** — Each term is normal (in fact characteristic) in G

# Key Properties
1. Z_i(G) is characteristic in G for all i
2. Z_0 = 1, Z_1 = Z(G)
3. Z_{i+1}/Z_i = Z(G/Z_i)
4. G is nilpotent iff Z_c(G) = G for some c
5. The series is ascending ("upper" indicates Z_i <= Z_{i+1})
6. For non-nilpotent groups, the series stabilizes at a proper subgroup

# Examples
**Example 1** (p. 194): For D_8: Z_0 = 1, Z_1 = <r^2>, Z_2 = D_8. So D_8 is nilpotent of class 2.

**Example 2** (p. 194): For S_3: Z_n(S_3) = 1 for all n, so S_3 is not nilpotent.

# Relationships
## Builds Upon
- **Center** — First nontrivial term is the center
## Enables
- **Nilpotent group** — Defined by the upper central series reaching G
## Contrasts With
- **Lower central series** — Descends from G; agrees in length for nilpotent groups
- **Derived series** — Uses commutators differently

# Source Reference
Chapter 6, Section 6.1, page 192.

# Verification Notes
- Definition source: Direct from p. 192
- Confidence: HIGH
- Uncertainties: None
