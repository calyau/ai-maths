---
# === CORE IDENTIFICATION ===
concept: Universe
slug: universe

# === CLASSIFICATION ===
category: foundations
tier: intermediate

# === PROVENANCE ===
source: "An Intuitionistic Theory of Types"
source_slug: intuitionistic-types
authors: "Per Martin-Löf"
chapter: "Informal Explanations of the Basic Concepts"
chapter_number: 1
pdf_page: null
section: "1.8. Reflection principle"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "V"
  - "type of small types"
  - "type universe"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type
  - natural-numbers
  - disjoint-union-of-two-types
  - pi-type
  - sigma-type
  - finite-type
related:
  - reflection-principle
  - small-type-vs-large-type
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a universe (V) in type theory?"
---

# Quick Definition
The universe V is a type whose objects are types -- specifically, the small types. It allows types to be treated as mathematical objects, enabling definitions by recursion that return types.

# Core Definition
Martin-Lof introduces: "a type V which will be called a universe and whose objects are to be types, together with the reflection principle which roughly speaking says that whatever we are used to doing with types can be done inside the universe V." (Section 1.8)

The closure conditions are: "N_0, N_1, ... and N are objects of type V. If A and B are objects of type V, then so is A + B. If A is an object of type V and B is a function which to an arbitrary object of type A assigns an object of type V, then (Pi x in A)B(x) and (Sigma x in A)B(x) are objects of type V." (Section 1.8)

# Prerequisites
- **Type**: Must understand what types are before understanding a type of types.
- **Natural numbers, finite types, disjoint union, Pi type, Sigma type**: These are the type formers that V is closed under.

# Key Properties
1. V is a type whose objects are themselves types (the small types).
2. V is closed under all the basic type-forming operations: N_n, N, +, Pi, Sigma.
3. V itself is NOT an object of V -- this is essential to avoid Girard's paradox.
4. V is intentionally kept open: new type formers can be added to extend the closure conditions.
5. The principle of transfinite induction over V is not assumed, to maintain this openness.

# Construction / Recognition
## To Construct/Create:
1. N_0, N_1, ..., N are in V (base cases).
2. If A, B are in V, then A + B is in V.
3. If A is in V and B maps objects of A to objects of V, then (Pi x in A)B(x) and (Sigma x in A)B(x) are in V.

## To Identify/Recognize:
1. A type that collects types as its objects.
2. The type that enables type-valued recursion and type-level computation.

# Context & Application
The universe V is motivated by concrete needs. Martin-Lof gives two examples: (1) defining equality E on natural numbers by recursion, which requires top and bottom to be objects of some type V so that E can be defined by recursion returning types; (2) defining transfinite type families like (Pi x in N)F(x) where F(0) = N and F(s(n)) = F(n) -> N, which requires N and A -> B to be objects of V. Without V, these definitions are impossible because the recursion operator R can only produce objects of a fixed type, not types themselves.

# Examples
Equality on natural numbers (Section 1.8):
- E(0,0) = top, E(s(m),0) = bottom, E(0,s(n)) = bottom, E(s(m),s(n)) = E(m,n).
This requires top and bottom to be objects of V so that E can be defined by recursion on N.

Transfinite type family (Section 1.8):
- F(0) = N, F(s(n)) = F(n) -> N.
This requires N in V and closure under ->.

# Relationships
## Builds Upon
- **type**: V is a type.
- All basic type formers: V is closed under them.
## Enables
- **reflection-principle**: The closure conditions on V are the reflection principle.
- **small-type-vs-large-type**: V introduces the small/large distinction.
- Type-valued recursion and computation.
## Related
- **girards-paradox**: Assuming V in V leads to contradiction.

# Common Errors
- **Error**: Assuming V is in V (i.e., that V is a small type).
  **Correction**: V is explicitly NOT an object of V. This restriction is essential to avoid Girard's paradox.

# Common Confusions
- **Confusion**: Thinking V is a set-theoretic universe like V_kappa in ZFC.
  **Clarification**: V in Martin-Lof's theory is a type whose objects are types, governed by the reflection principle. It is structurally different from cumulative set-theoretic universes, though the terminology is borrowed from set theory.

# Source Reference
Martin-Lof, P. (1972). "An Intuitionistic Theory of Types," Section 1.8.

# Verification Notes
Extracted directly from Section 1.8. All closure conditions quoted from source. High confidence.
