---
# === CORE IDENTIFICATION ===
concept: Reflection Principle
slug: reflection-principle

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
  - "universe closure"
  - "type-theoretic reflection"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - universe
  - type
related:
  - small-type-vs-large-type
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the reflection principle relate to the universe V?"
---

# Quick Definition
The reflection principle states that the universe V is closed under all the basic type-forming operations: whatever can be done with types in general can be done within V. Concretely, V contains all finite types and N, and is closed under +, Pi, and Sigma.

# Core Definition
Martin-Lof states the principle as: "the reflection principle which roughly speaking says that whatever we are used to doing with types can be done inside the universe V. More precisely, this means that V is closed under the following inductive clauses. N_0, N_1, ... and N are objects of type V. If A and B are objects of type V, then so is A + B. If A is an object of type V and B is a function which to an arbitrary object of type A assigns an object of type V, then (Pi x in A)B(x) and (Sigma x in A)B(x) are objects of type V." (Section 1.8)

Critically: "the reflection principle does not justify the axiom that V is an object of type V" (Section 1.8).

# Prerequisites
- **Universe**: The reflection principle describes the closure properties of V.
- **Type**: Must understand type-forming operations to understand what V is closed under.

# Key Properties
1. V reflects the type-forming operations: everything constructible from types is constructible within V.
2. The reflection principle is stated as inductive closure conditions on V.
3. V is NOT required to be the least type satisfying these conditions (no induction principle over V).
4. The principle explicitly excludes V in V.
5. V is kept open: the reflection principle can be extended with new type formers.

# Construction / Recognition
## To Construct/Create:
1. The reflection principle is not something one constructs; it describes which types belong to V.
2. To show a type is in V, demonstrate it can be built from the base types (N_n, N) using the operations (+, Pi, Sigma) that V is closed under.

## To Identify/Recognize:
1. An assertion that V is closed under specified type-forming operations.
2. The informal slogan: "whatever we do with types can be done inside V."

# Context & Application
Martin-Lof compares his reflection principle to the set-theoretic reflection principle used by Kreisel (1965) and Feferman (1969) for formalizing category theory. Both serve similar purposes -- overcoming limitations of finite types and enabling the formalization of category theory -- but operate in fundamentally different formal settings. The openness of V (not requiring it to be the least closed type) is deliberate: it allows future extensions with new type formers like ordinals O or wellfounded trees W(A).

# Examples
The reflection principle enables:
1. Defining equality on N by recursion into V (since top and bottom are in V).
2. Defining transfinite type families like F(0) = N, F(s(n)) = F(n) -> N (since N is in V and V is closed under ->).

# Relationships
## Builds Upon
- **universe**: The reflection principle characterizes V.
## Enables
- **small-type-vs-large-type**: The distinction arises from what is in V vs what is not.
- Type-valued recursion.
## Related
- **girards-paradox**: Shows why the reflection principle must exclude V in V.

# Common Errors
- **Error**: Thinking the reflection principle says V is in V.
  **Correction**: The reflection principle explicitly does NOT include V in V. Martin-Lof states: "V would so to say have to have been there already before we introduced it."

# Common Confusions
- **Confusion**: Confusing the type-theoretic reflection principle with the set-theoretic one.
  **Clarification**: Martin-Lof's reflection principle says V is closed under type formers. The set-theoretic reflection principle (Kreisel/Feferman) says properties of V_omega reflect into some V_kappa. They serve analogous purposes but are formally different.

# Source Reference
Martin-Lof, P. (1972). "An Intuitionistic Theory of Types," Section 1.8.

# Verification Notes
Extracted directly from Section 1.8. Key quotes preserved. High confidence.
