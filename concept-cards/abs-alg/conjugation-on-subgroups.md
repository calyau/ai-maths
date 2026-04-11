---
concept: Conjugation Action on Subgroups
slug: conjugation-on-subgroups
category: group-theory
subcategory: group-actions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Group Actions"
chapter_number: 4
pdf_page: 126
section: "4.3 Groups Acting on Themselves by Conjugation"
extraction_confidence: high
aliases:
  - "conjugate subgroups"
prerequisites:
  - conjugation-action
  - normalizer
  - subgroup
extends:
  - conjugation-action
related:
  - sylow-p-subgroup
  - normal-subgroup
contrasts_with: []
answers_questions:
  - "When are two subgroups conjugate?"
  - "How does the normalizer relate to conjugation of subgroups?"
---

# Quick Definition
G acts on its set of subsets (and subgroups) by conjugation: g . S = gSg^{-1}. Two subsets S and T are conjugate if T = gSg^{-1} for some g. The stabilizer of S is its normalizer N_G(S). The number of conjugates of S equals |G : N_G(S)|.

# Core Definition
Two subsets S and T of G are said to be conjugate in G if there is some g in G such that T = gSg^{-1} (Dummit & Foote, p. 126). The stabilizer of S under this action is the normalizer N_G(S) = {g in G | gSg^{-1} = S}. By Proposition 6, the number of conjugates of S equals |G : N_G(S)|. Conjugate subgroups have the same order and are isomorphic (Corollary 14).

# Prerequisites
- **Conjugation action** — This extends conjugation to subsets
- **Normalizer** — The stabilizer is the normalizer
- **Subgroup** — Conjugation preserves the subgroup property

# Key Properties
1. Conjugate subgroups are isomorphic (Corollary 14)
2. Number of conjugates of S = |G : N_G(S)| (Proposition 6)
3. S is normal in G iff it has exactly one conjugate (itself)
4. All Sylow p-subgroups are conjugate (Second Sylow Theorem)
5. A subgroup is normal iff it equals all its conjugates

# Relationships
## Builds Upon
- **Conjugation action** — Extension to subsets
## Related
- **Sylow p-subgroup** — All Sylow p-subgroups form a single conjugacy class
- **Normal subgroup** — Normal iff invariant under all conjugations

# Source Reference
Chapter 4, Section 4.3, pages 126-127.

# Verification Notes
- Definition source: Direct from p. 126
- Confidence: HIGH
- Uncertainties: None
