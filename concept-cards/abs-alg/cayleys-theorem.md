---
concept: "Cayley's Theorem"
slug: cayleys-theorem
category: group-theory
subcategory: group-actions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Group Actions"
chapter_number: 4
pdf_page: 120
section: "4.2 Groups Acting on Themselves by Left Multiplication"
extraction_confidence: high
aliases:
  - "Cayley theorem"
prerequisites:
  - group-action
  - permutation-representation
  - symmetric-group
  - isomorphism
extends:
  - permutation-representation
related:
  - left-regular-representation
  - permutation-group
contrasts_with: []
answers_questions:
  - "Is every group isomorphic to a group of permutations?"
  - "How does Cayley's theorem connect abstract groups to permutation groups?"
---

# Quick Definition
Every group is isomorphic to a subgroup of some symmetric group. Specifically, if G has order n, then G is isomorphic to a subgroup of S_n.

# Core Definition
Corollary 4 (Cayley's Theorem): Every group is isomorphic to a subgroup of some symmetric group. If G is a group of order n, then G is isomorphic to a subgroup of S_n (Dummit & Foote, p. 120). The proof takes H = 1 in Theorem 3 to obtain a homomorphism G -> S_G with trivial kernel, so G embeds in S_G.

# Prerequisites
- **Group action** — The proof uses G acting on itself by left multiplication
- **Permutation representation** — The left regular representation provides the embedding
- **Symmetric group** — G embeds as a subgroup of S_n
- **Isomorphism** — G is isomorphic to its image in S_n

# Key Properties
1. Every group embeds in a symmetric group
2. A group of order n embeds in S_n
3. The embedding comes from the left regular representation
4. The theorem proves historical and axiomatic definitions of groups are equivalent
5. G is isomorphic to a SUBGROUP of S_n, not necessarily the full S_n

# Construction / Recognition
## To Realize the Embedding:
1. Label the elements of G as g_1, ..., g_n
2. For each g in G, define sigma_g(i) = j where g * g_i = g_j
3. The map g -> sigma_g is an injective homomorphism G -> S_n

# Context & Application
Cayley's Theorem shows that studying abstract groups is equivalent to studying permutation groups (subgroups of symmetric groups). Historically, finite groups were first studied as subgroups of S_n. The modern axiomatic approach is "coordinate free" — we are not restricted to any particular symmetric group. The theorem, while theoretically important, is not computationally practical since studying G requires working in the much larger group S_n.

# Examples
**Example 1** (p. 119): The Klein 4-group V = {1, a, b, c} embeds in S_4 via the left regular representation: a -> (1 2)(3 4), b -> (1 3)(2 4), c -> (1 4)(2 3).

# Relationships
## Builds Upon
- **Permutation representation** — Uses the left regular representation
## Enables
- **Permutation group** — Every group is a permutation group
## Related
- **Left regular representation** — The specific representation used in the proof

# Common Errors
- **Error**: Stating that G IS S_n rather than a subgroup of S_n
  **Correction**: G is isomorphic to a subgroup; for example, V_4 embeds in S_4 but is not all of S_4

# Common Confusions
- **Confusion**: Thinking Cayley's theorem gives a practical way to study groups
  **Clarification**: Working in S_n is usually impractical since |S_n| = n! is much larger than |G| = n

# Source Reference
Chapter 4: Group Actions, Section 4.2, Corollary 4, page 120.

# Verification Notes
- Definition source: Direct from Corollary 4, p. 120
- Confidence: HIGH — stated and proved as a corollary
- Uncertainties: None
