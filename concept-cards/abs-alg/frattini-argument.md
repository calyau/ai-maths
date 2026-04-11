---
concept: "Frattini's Argument"
slug: frattini-argument
category: group-theory
subcategory: further-topics
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Further Topics in Group Theory"
chapter_number: 6
pdf_page: 198
section: "6.1 p-Groups, Nilpotent Groups, and Solvable Groups"
extraction_confidence: high
aliases:
  - "Frattini argument"
  - "Frattini lemma"
prerequisites:
  - normal-subgroup
  - sylow-p-subgroup
  - second-sylow-theorem
  - normalizer
extends:
  - second-sylow-theorem
related:
  - nilpotent-group
contrasts_with: []
answers_questions:
  - "What is Frattini's argument?"
  - "How does it relate Sylow subgroups to normalizers?"
---

# Quick Definition
If H is a normal subgroup of a finite group G and P is a Sylow p-subgroup of H, then G = H * N_G(P) and |G : H| divides |N_G(P)|.

# Core Definition
Proposition 6 (Frattini's Argument): Let G be a finite group, let H be a normal subgroup of G and let P be a Sylow p-subgroup of H. Then G = H * N_G(P) and |G : H| divides |N_G(P)| (Dummit & Foote, p. 198). The proof uses the Sylow conjugacy theorem: for any g in G, P^g is also a Sylow p-subgroup of H (since H is normal), so P^g = P^x for some x in H, giving gx^{-1} in N_G(P).

# Prerequisites
- **Normal subgroup** — H must be normal in G
- **Sylow p-subgroup** — P must be Sylow in H
- **Second Sylow theorem** — Conjugacy of Sylow subgroups is used
- **Normalizer** — N_G(P) appears in the conclusion

# Key Properties
1. G = H * N_G(P)
2. |G : H| divides |N_G(P)|
3. Applies to any Sylow p-subgroup of a normal subgroup
4. Used to prove: nilpotent iff every maximal subgroup is normal
5. Used extensively in studying solvable groups and groups of medium order

# Context & Application
Frattini's argument is a fundamental technique for studying finite groups. It is used to prove that finite nilpotent groups have normal Sylow subgroups, and it appears throughout the classification arguments in Section 6.2.

# Relationships
## Builds Upon
- **Second Sylow theorem** — Uses conjugacy of Sylow subgroups
## Enables
- **Nilpotent group characterization** — Every maximal subgroup is normal

# Source Reference
Chapter 6, Section 6.1, Proposition 6, page 198.

# Verification Notes
- Definition source: Direct from Proposition 6, p. 198
- Confidence: HIGH
- Uncertainties: None
