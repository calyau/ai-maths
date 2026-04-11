---
concept: Orbit
slug: orbit
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
  - "G-orbit"
prerequisites:
  - group-action
  - equivalence-relation
extends:
  - group-action
related:
  - stabilizer
  - orbit-stabilizer-theorem
  - transitive-action
  - conjugacy-class
contrasts_with: []
answers_questions:
  - "What is the orbit of an element under a group action?"
  - "How do orbits partition the set being acted on?"
---

# Quick Definition
The orbit of an element a in A under the action of G is the set {g . a | g in G} of all images of a under group elements. Orbits partition A into disjoint equivalence classes.

# Core Definition
Let G be a group acting on the nonempty set A. The equivalence class {g . a | g in G} is called the orbit of G containing a (Dummit & Foote, p. 114). By Proposition 2 (p. 114), the relation a ~ b iff a = g . b for some g in G is an equivalence relation on A, and the number of elements in the orbit containing a equals |G : G_a|, the index of the stabilizer of a.

# Prerequisites
- **Group action** — Orbits are defined relative to an action
- **Equivalence relation** — The orbit relation is an equivalence relation

# Key Properties
1. Orbits partition A into disjoint equivalence classes
2. The number of elements in the orbit of a is |G : G_a| (Proposition 2)
3. Two elements are in the same orbit iff one can be mapped to the other by some group element
4. If G is finite, each orbit size divides |G|
5. The sum of all orbit sizes equals |A|

# Construction / Recognition
## To Find the Orbit of a:
1. Apply every element of G to a
2. Collect all distinct results: {g . a | g in G}

# Context & Application
The partition of A into orbits is fundamental to counting arguments in group theory. The class equation arises from orbits of the conjugation action. Cycle decompositions in symmetric groups correspond to orbits of cyclic subgroups.

# Examples
**Example 1** (p. 115): D_8 acts transitively on the four vertices of a square (one orbit).

**Example 2** (p. 115): D_8 acts transitively on the set of two pairs of opposite vertices (one orbit).

**Example 3** (p. 115): If G acts trivially on A, each orbit is a singleton {a}.

**Example 4** (p. 117): The orbits of <sigma> on {1,...,n} are the sets of numbers appearing in the individual cycles of sigma's cycle decomposition.

# Relationships
## Builds Upon
- **Group action** — Orbits are the equivalence classes of an action
## Enables
- **Orbit-stabilizer theorem** — Relates orbit size to stabilizer index
- **Class equation** — Counts elements via orbit sizes under conjugation
- **Transitive action** — Defined as having exactly one orbit
## Related
- **Conjugacy class** — Orbit under the conjugation action

# Common Errors
- **Error**: Assuming orbits always have the same size
  **Correction**: Different orbits can have different sizes (each divides |G| when G is finite)

# Common Confusions
- **Confusion**: Conflating orbit size with group order
  **Clarification**: The orbit size equals the index of the stabilizer, which divides |G| but may be much smaller

# Source Reference
Chapter 4: Group Actions, Section 4.1, pages 114-118. Proposition 2 and surrounding examples.

# Verification Notes
- Definition source: Direct from p. 114
- Confidence: HIGH — explicit definition
- Uncertainties: None
