---
concept: Derived Series
slug: derived-series
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
  - "commutator series"
prerequisites:
  - commutator-subgroup
  - characteristic-subgroup
extends:
  - commutator-subgroup
related:
  - solvable-group
  - lower-central-series
contrasts_with:
  - lower-central-series
answers_questions:
  - "What is the derived series of a group?"
  - "How does the derived series characterize solvability?"
---

# Quick Definition
The derived series of G is G^{(0)} = G, G^{(1)} = G' = [G,G], G^{(i+1)} = [G^{(i)}, G^{(i)}]. A group is solvable iff the derived series reaches the identity.

# Core Definition
For any group G define G^{(0)} = G, G^{(1)} = [G, G], and G^{(i+1)} = [G^{(i)}, G^{(i)}] for all i >= 1. This series is called the derived or commutator series of G (Dummit & Foote, p. 201). Each G^{(i)} is characteristic in G. G^{(i)} <= G^i (lower central series) for all i. The derived series is the series of shortest length with abelian successive quotients.

# Prerequisites
- **Commutator subgroup** — G^{(1)} = G'
- **Characteristic subgroup** — Each term is characteristic

# Key Properties
1. G^{(i)} is characteristic in G for all i
2. G^{(i+1)} = [G^{(i)}, G^{(i)}]
3. G^{(i)} <= G^i (contained in lower central series terms)
4. G is solvable iff G^{(n)} = 1 for some n (Theorem 9)
5. The series consists of characteristic subgroups of G (not just normal in the next term)

# Examples
**Example 1** (p. 202): For S_3: G^{(0)} = S_3, G^{(1)} = A_3, G^{(2)} = [A_3, A_3] = 1. So S_3 is solvable of length 2.

**Example 2**: For A_5: G^{(1)} = A_5 (since A_5 is perfect), so G^{(n)} = A_5 for all n. Not solvable.

# Relationships
## Builds Upon
- **Commutator subgroup** — Each term is a commutator subgroup
## Enables
- **Solvable group** — Characterized by derived series reaching 1
## Contrasts With
- **Lower central series** — Uses [G, G^i] instead of [G^{(i)}, G^{(i)}]; G^{(i)} <= G^i

# Source Reference
Chapter 6, Section 6.1, pages 201-202.

# Verification Notes
- Definition source: Direct from p. 201
- Confidence: HIGH
- Uncertainties: None
