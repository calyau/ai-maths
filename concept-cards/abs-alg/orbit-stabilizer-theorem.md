---
concept: Orbit-Stabilizer Theorem
slug: orbit-stabilizer-theorem
category: group-theory
subcategory: group-actions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Group Actions"
chapter_number: 4
pdf_page: 114
section: "4.1 Group Actions and Permutation Representations"
extraction_confidence: high
aliases:
  - "orbit-counting theorem"
prerequisites:
  - group-action
  - orbit
  - stabilizer
  - coset
  - lagranges-theorem
extends:
  - lagranges-theorem
related:
  - class-equation
  - sylow-theorems
contrasts_with: []
answers_questions:
  - "How does the size of an orbit relate to the stabilizer?"
  - "What is the orbit-stabilizer theorem?"
---

# Quick Definition
For a group G acting on a set A, the number of elements in the orbit containing a equals the index of the stabilizer of a in G: |orbit of a| = |G : G_a|. When G is finite, this gives |orbit of a| = |G| / |G_a|.

# Core Definition
Let G be a group acting on the nonempty set A. For each a in A, the number of elements in the equivalence class (orbit) containing a is |G : G_a|, the index of the stabilizer of a (Proposition 2, Dummit & Foote, p. 114). The proof exhibits an explicit bijection between the orbit of a and the set of left cosets of G_a: the map g . a -> gG_a is a well-defined bijection.

# Prerequisites
- **Group action** — The theorem applies to group actions
- **Orbit** — One side of the equation
- **Stabilizer** — The other side of the equation
- **Coset** — The proof uses a bijection with left cosets
- **Lagrange's theorem** — In finite groups, |G : G_a| = |G|/|G_a|

# Key Properties
1. |orbit of a| = |G : G_a| = |G| / |G_a| (for finite G)
2. Each orbit size divides |G| when G is finite
3. g . a = h . a if and only if h^{-1}g is in G_a (if and only if gG_a = hG_a)
4. The bijection is explicit: g . a maps to the coset gG_a

# Construction / Recognition
## To Apply the Theorem:
1. Identify the group G, the set A, and the action
2. Pick an element a in A
3. Compute the stabilizer G_a
4. The orbit size equals |G| / |G_a|

# Context & Application
This theorem is the workhorse behind counting arguments in group theory. It is used to derive the class equation, to count conjugacy classes, and is fundamental to the proof of Sylow's Theorem.

# Examples
**Example 1** (p. 115): S_n acts on {1,...,n}. The stabilizer of i is isomorphic to S_{n-1}, so the orbit of i has |S_n|/|S_{n-1}| = n elements (confirming the action is transitive).

**Example 2** (p. 115): D_8 acts on four vertices. The stabilizer of any vertex has order 2, so the orbit has 8/2 = 4 elements (all four vertices).

# Relationships
## Builds Upon
- **Lagrange's theorem** — Orbit size divides |G| via index of stabilizer
## Enables
- **Class equation** — Derived by summing orbit sizes under conjugation
- **Sylow theorems** — Proof uses orbit-stabilizer calculations

# Common Errors
- **Error**: Writing |orbit| = |G_a| instead of |G|/|G_a|
  **Correction**: The orbit size equals the INDEX of the stabilizer, not the order of the stabilizer

# Common Confusions
- **Confusion**: Thinking the theorem requires G to be finite
  **Clarification**: The theorem holds for infinite groups too, with |orbit| = |G : G_a| as an index of subgroups

# Source Reference
Chapter 4: Group Actions, Section 4.1, Proposition 2, page 114.

# Verification Notes
- Definition source: Direct from Proposition 2, p. 114
- Confidence: HIGH — stated and proved as a proposition
- Uncertainties: None
