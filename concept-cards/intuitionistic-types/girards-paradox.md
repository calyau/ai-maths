---
# === CORE IDENTIFICATION ===
concept: Girard's Paradox
slug: girards-paradox

# === CLASSIFICATION ===
category: paradoxes
tier: advanced

# === PROVENANCE ===
source: "An Intuitionistic Theory of Types"
source_slug: intuitionistic-types
authors: "Per Martin-Löf"
chapter: "Informal Explanations of the Basic Concepts"
chapter_number: 1
pdf_page: null
section: "1.9. Girard's paradox"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "type-theoretic Burali-Forti paradox"
  - "paradox of the type of all types"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - universe
  - reflection-principle
  - small-type-vs-large-type
  - natural-numbers
  - pi-type
  - sigma-type
  - function-type
  - ordering-without-infinite-descending-chains
related:
  - empty-type
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Girard's paradox relate to the assumption V in V?"
  - "What must I know before understanding Girard's paradox?"
---

# Quick Definition
Girard's paradox shows that the assumption V in V (the universe is an element of itself, i.e., the type of all types is itself a type) leads to a contradiction. It is a type-theoretic analogue of the Burali-Forti paradox from set theory.

# Core Definition
Martin-Lof states: "Suppose that we think of V not as the type of small types but as the type of all types whatsoever. Then, being a type, namely, the type of types, V is itself an object of type V, in short, V in V and a type is the same as an object of type V. The following paradox which is a modification of the one discovered by Girard 1972 (which, in turn, resembles the Burali-Forti paradox) shows that the idea of the type of all types whatsoever is inconsistent." (Section 1.9)

# Prerequisites
- **Universe**: Must understand V and its role as a type of types.
- **Reflection principle**: Must understand the closure conditions on V.
- **Small type vs large type**: The paradox arises from collapsing this distinction.
- **Natural numbers**: Used in defining "no infinite descending chains."
- **Pi type, Sigma type, function type**: Used in constructing the orderings.
- **Ordering without infinite descending chains**: The key technical device in the paradox construction.

# Key Properties
1. The paradox assumes V in V (the type of all types contains itself).
2. It constructs U, the type of all orderings without infinite descending chains.
3. U itself, with a natural ordering <_U, forms an ordering without infinite descending chains.
4. Therefore (U, <_U, p_U, q_U) is in U -- it is an element of itself.
5. Every element of U is strictly less than (U, <_U, p_U, q_U) -- it is maximal.
6. But then (U, <_U, p_U, q_U) <_U (U, <_U, p_U, q_U), contradicting irreflexivity.

# Construction / Recognition
## To Construct/Create:
1. Assume V in V.
2. Define an ordering without infinite descending chains as (A, <) where < is transitive and has no infinite descending chain.
3. Form U = (Sigma A in V)(Sigma < in A -> A -> V)(P(A,<) x Q(A,<)), the type of all such orderings.
4. Define <_U: one ordering is less than another if there is an order-preserving map with a dominating element.
5. Show <_U is transitive (by composing maps) and has no infinite descending chains (by transferring a chain to A_0).
6. Conclude (U, <_U, p_U, q_U) in U (since U in V by assumption).
7. Show every (A, <, p, q) in U satisfies (A, <, p, q) <_U (U, <_U, p_U, q_U) by the segment embedding.
8. In particular, (U, <_U, p_U, q_U) <_U (U, <_U, p_U, q_U), contradicting irreflexivity.

## To Identify/Recognize:
1. Any argument that derives a contradiction from V in V or "the type of all types."
2. The characteristic structure: constructing a maximal element that must be strictly less than itself.

# Context & Application
Girard's paradox is the fundamental reason why Martin-Lof's type theory stratifies types into small and large. It shows that naive type-in-type is inconsistent, just as Russell's paradox shows naive set comprehension is inconsistent. The paradox was discovered by Girard (1972) and resembles the Burali-Forti paradox (the ordinal of all ordinals cannot exist). Martin-Lof's presentation is a "modification" of Girard's original.

This paradox has far-reaching consequences: it means the "category of all categories" cannot be formed within the theory, and any type theory must have some form of universe stratification to remain consistent.

# Examples
The paradox itself is the primary example. The key steps from the source:

The ordering <_U on U is defined by: (A, <_A, p_A, q_A) <_U (B, <_B, p_B, q_B) holds when there exists an order-preserving map f from A to B and an element b of B dominating the range of f.

The maximal element is shown by taking f(a) = (A_a, <_a, p_a, q_a) (the segment determined by a), which is order-preserving, with (A, <, p, q) itself as the dominating element.

# Relationships
## Builds Upon
- **universe**: The paradox concerns V in V.
- **small-type-vs-large-type**: Collapsing this distinction causes the paradox.
- **ordering-without-infinite-descending-chains**: The technical device used in the proof.
## Enables
- Justification of the small/large type distinction.
- Motivation for universe hierarchies in later type theories.
## Related
- **empty-type**: The contradiction derived is bottom (an object of N_0), showing the system is inconsistent.

# Common Errors
- **Error**: Thinking the paradox shows type theory itself is inconsistent.
  **Correction**: The paradox only arises from the assumption V in V. Martin-Lof's theory avoids it by maintaining the small/large distinction.

- **Error**: Conflating Girard's paradox with Russell's paradox.
  **Correction**: Girard's paradox resembles the Burali-Forti paradox (about ordinals), not Russell's paradox (about self-membership of sets). The mechanism is different: it uses orderings and maximality, not direct self-reference.

# Common Confusions
- **Confusion**: Thinking V in V is merely technically inconvenient rather than contradictory.
  **Clarification**: V in V is provably contradictory. Girard's paradox derives an outright contradiction (an object of N_0), not merely an undesirable consequence.

# Source Reference
Martin-Lof, P. (1972). "An Intuitionistic Theory of Types," Section 1.9.

# Verification Notes
Extracted from Section 1.9. The full proof structure is faithfully represented. High confidence.
