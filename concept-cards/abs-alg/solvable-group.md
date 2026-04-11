---
concept: Solvable Group
slug: solvable-group
category: group-theory
subcategory: further-topics
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Further Topics in Group Theory"
chapter_number: 6
pdf_page: 201
section: "6.1 p-Groups, Nilpotent Groups, and Solvable Groups"
extraction_confidence: high
aliases:
  - "soluble group"
prerequisites:
  - commutator-subgroup
  - derived-series
  - normal-subgroup
  - quotient-group
extends:
  - nilpotent-group
related:
  - derived-series
  - nilpotent-group
  - simple-group
contrasts_with:
  - nilpotent-group
  - simple-group
answers_questions:
  - "What is a solvable group?"
  - "How does solvability relate to nilpotency?"
---

# Quick Definition
A group G is solvable if it has a chain of subgroups 1 = H_0 <= H_1 <= ... <= H_s = G with each H_i normal in H_{i+1} and each quotient H_{i+1}/H_i abelian. Equivalently, G^{(n)} = 1 for some n, where G^{(i)} is the derived series.

# Core Definition
A solvable group was defined in Section 3.4 as one possessing a series 1 = H_0 <= H_1 <= ... <= H_s = G such that each factor H_{i+1}/H_i is abelian. Theorem 9 gives the equivalent characterization: G is solvable iff G^{(n)} = 1 for some n >= 0, where G^{(0)} = G, G^{(1)} = [G,G], G^{(i+1)} = [G^{(i)}, G^{(i)}] is the derived series (Dummit & Foote, p. 202). The smallest such n is the solvable length. Proposition 10: subgroups and quotients of solvable groups are solvable; extensions of solvable groups by solvable groups are solvable.

# Prerequisites
- **Commutator subgroup** — The derived series uses iterated commutator subgroups
- **Derived series** — Solvability is characterized by the derived series
- **Normal subgroup** — The defining series uses normal subgroups
- **Quotient group** — Successive quotients must be abelian

# Key Properties
1. G is solvable iff G^{(n)} = 1 for some n (Theorem 9)
2. Every nilpotent group is solvable
3. S_n is solvable iff n <= 4 (since A_n is simple for n >= 5)
4. Subgroups of solvable groups are solvable (Proposition 10(1))
5. Quotients of solvable groups are solvable (Proposition 10(2))
6. If N is normal in G with N and G/N both solvable, then G is solvable (Proposition 10(3))
7. Every group of order p^a q^b (p, q primes) is solvable (Burnside's Theorem)
8. Every group of odd order is solvable (Feit-Thompson Theorem)

# Examples
**Example 1**: S_3 is solvable: 1 <= A_3 <= S_3 with A_3/1 = Z_3 and S_3/A_3 = Z_2.

**Example 2**: S_4 is solvable: 1 <= V_4 <= A_4 <= S_4.

**Example 3**: A_5 is NOT solvable (it's simple and non-abelian, so A_5' = A_5 = A_5^{(n)} for all n).

# Relationships
## Builds Upon
- **Nilpotent group** — Every nilpotent group is solvable
## Related
- **Derived series** — Characterizes solvability
## Contrasts With
- **Nilpotent group** — S_3 is solvable but not nilpotent
- **Simple group** — Non-abelian simple groups are not solvable

# Common Confusions
- **Confusion**: Thinking every solvable group is nilpotent
  **Clarification**: S_3 is solvable (derived series terminates) but not nilpotent (upper central series doesn't reach S_3)

# Source Reference
Chapter 6, Section 6.1, pages 201-206. Theorem 9, Proposition 10, Theorem 11.

# Verification Notes
- Definition source: Direct from pp. 201-202
- Confidence: HIGH
- Uncertainties: None
