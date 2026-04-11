---
concept: Permutation Representation
slug: permutation-representation
category: group-theory
subcategory: group-actions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Group Actions"
chapter_number: 4
pdf_page: 112
section: "4.1 Group Actions and Permutation Representations"
extraction_confidence: high
aliases: []
prerequisites:
  - group-action
  - homomorphism
  - symmetric-group
extends:
  - homomorphism
related:
  - faithful-action
  - cayleys-theorem
  - left-regular-representation
contrasts_with: []
answers_questions:
  - "What is a permutation representation of a group?"
  - "How does a permutation representation relate to a group action?"
---

# Quick Definition
A permutation representation of a group G is any homomorphism phi: G -> S_A for some nonempty set A. Every group action on A gives rise to a permutation representation, and conversely.

# Core Definition
If G is a group, a permutation representation of G is any homomorphism of G into the symmetric group S_A for some nonempty set A (Dummit & Foote, p. 113). By Proposition 1, there is a bijection between actions of G on A and homomorphisms G -> S_A. A given action affords or induces the associated permutation representation. When A is finite with n elements, we may view permutations as elements of S_n by fixing a labeling.

# Prerequisites
- **Group action** — Permutation representations arise from actions
- **Homomorphism** — A permutation representation IS a homomorphism
- **Symmetric group** — The codomain of the representation

# Key Properties
1. A permutation representation is a homomorphism phi: G -> S_A
2. There is a bijection between actions on A and homomorphisms into S_A
3. The kernel of the representation equals the kernel of the action
4. Faithful actions correspond to injective representations
5. For finite A with n elements, this is a homomorphism G -> S_n

# Context & Application
Permutation representations translate abstract group actions into concrete permutations. They are analogous to matrix representations of linear transformations. The left regular representation is the permutation representation from G acting on itself by left multiplication.

# Examples
**Example 1** (p. 112): S_n acting on {1,...,n} gives the identity map S_n -> S_n as its permutation representation.

**Example 2** (p. 112): D_8 acting on four vertices gives sigma_r = (1 2 3 4) and sigma_s = (2 4).

# Relationships
## Builds Upon
- **Homomorphism** — A permutation representation is a homomorphism
## Enables
- **Cayleys theorem** — Uses the left regular permutation representation
## Related
- **Left regular representation** — The permutation representation from left multiplication

# Source Reference
Chapter 4: Group Actions, Section 4.1, pages 112-113.

# Verification Notes
- Definition source: Direct from p. 113
- Confidence: HIGH — explicit definition
- Uncertainties: None
