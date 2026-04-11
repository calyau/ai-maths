---
concept: Second Sylow Theorem
slug: second-sylow-theorem
category: group-theory
subcategory: group-actions
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Group Actions"
chapter_number: 4
pdf_page: 142
section: "4.5 Sylow's Theorem"
extraction_confidence: high
aliases:
  - "Sylow conjugacy theorem"
  - "Sylow II"
prerequisites:
  - first-sylow-theorem
  - sylow-p-subgroup
  - conjugation
extends:
  - first-sylow-theorem
related:
  - third-sylow-theorem
  - normal-subgroup
contrasts_with: []
answers_questions:
  - "Are all Sylow p-subgroups conjugate?"
  - "How do I apply the Sylow theorems to analyze group structure?"
---

# Quick Definition
Any two Sylow p-subgroups of a finite group G are conjugate in G. Moreover, any p-subgroup of G is contained in some Sylow p-subgroup.

# Core Definition
Theorem 18(2): If P is a Sylow p-subgroup of G and Q is any p-subgroup of G, then there exists g in G such that Q <= gPg^{-1}, i.e., Q is contained in some conjugate of P. In particular, any two Sylow p-subgroups of G are conjugate in G (Dummit & Foote, p. 142). The proof uses Q acting by conjugation on the set of conjugates of P, with orbit-stabilizer calculations.

# Prerequisites
- **First Sylow theorem** — Existence of Sylow p-subgroups
- **Sylow p-subgroup** — The objects being shown conjugate
- **Conjugation** — The relation between different Sylow p-subgroups

# Key Properties
1. Any two Sylow p-subgroups are conjugate: if P, Q in Syl_p(G), then Q = gPg^{-1} for some g
2. Any p-subgroup is contained in some Sylow p-subgroup
3. All Sylow p-subgroups are isomorphic (since conjugate subgroups are isomorphic)
4. A Sylow p-subgroup is normal iff it is the unique Sylow p-subgroup (n_p = 1)

# Context & Application
The conjugacy of Sylow subgroups is crucial for classification arguments. If n_p = 1, the unique Sylow p-subgroup must be normal (since conjugation cannot move it). This is the most common way to produce normal subgroups in finite groups.

# Examples
**Example 1** (p. 146): The three Sylow 2-subgroups of S_3 are <(1 2)>, <(2 3)>, <(1 3)>, all conjugate to each other.

**Example 2**: In A_4, the unique Sylow 2-subgroup V_4 is normal since it's the only one.

# Relationships
## Builds Upon
- **First Sylow theorem** — Requires existence first
## Enables
- **Normal Sylow subgroup detection** — If n_p = 1, P is normal
## Related
- **Conjugation** — Sylow subgroups are related by conjugation

# Common Errors
- **Error**: Concluding that since Sylow subgroups are conjugate, they must be nontrivially so
  **Correction**: When n_p = 1, the unique Sylow p-subgroup is conjugate only to itself (trivially)

# Source Reference
Chapter 4: Group Actions, Section 4.5, Theorem 18(2), pages 142-145.

# Verification Notes
- Definition source: Direct from Theorem 18(2), p. 142
- Confidence: HIGH — stated and proved
- Uncertainties: None
