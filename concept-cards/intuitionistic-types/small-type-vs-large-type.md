---
# === CORE IDENTIFICATION ===
concept: Small Type vs Large Type
slug: small-type-vs-large-type

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
  - "small/large distinction"
  - "type stratification"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type
  - universe
  - reflection-principle
related:
  - girards-paradox
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a small type vs. a large type?"
  - "What distinguishes small types from large types?"
---

# Quick Definition
A small type is a type that is an object of the universe V. A large type is one that is not in V -- notably V itself and any type derived from V. The universe V is the type of small types.

# Core Definition
Martin-Lof states: "Borrowing terminology from category theory, a type which is an object of V is said to be small whereas V itself and all types which are derived from it are large. Thus the universe V is the type of small types." (Section 1.8)

# Prerequisites
- **Type**: Must understand what types are.
- **Universe**: The small/large distinction is defined relative to V.
- **Reflection principle**: Determines which types are small (those constructible under V's closure conditions).

# Key Properties
1. Small types are exactly the objects of V: N_n, N, and anything built from them using +, Pi, Sigma.
2. Large types include V itself and types formed using V (e.g., V -> V, (Pi x in V)B(x)).
3. The distinction is essential for consistency: collapsing it (V in V) leads to Girard's paradox.
4. The theory with this distinction is adequate for formalizing basic category theory.
5. The "category of all categories" cannot be formed, as it would require V in V.

# Construction / Recognition
## To Construct/Create:
1. Small types: build from N_n and N using +, Pi, Sigma (all within V).
2. Large types: form types that involve V itself as a component.

## To Identify/Recognize:
1. Ask: is this type an object of V? If yes, it is small. If no (especially if it involves V), it is large.
2. V itself is the paradigmatic large type.

# Context & Application
The small/large distinction is Martin-Lof's solution to the size issues that plague naive type theory (and set theory). It is analogous to the set/class distinction in set theory or the small/large category distinction in category theory. Martin-Lof explicitly notes that "the present theory, despite its limited proof theoretical strength, is adequate for the formulation of the basic notions and constructions of category theory" precisely because of this stratification. However, "it does not legitimatize the construction of the category of all categories whatsoever which in view of Girard's paradox seems highly dubious" (Section 1.8).

# Examples
- Small types: N, N_0, N_1, N -> N, (Pi x in N)(N -> N), N + N.
- Large types: V, V -> N, (Pi x in V)B(x), (Sigma x in V)B(x).

# Relationships
## Builds Upon
- **universe**: The distinction is defined by membership in V.
- **reflection-principle**: Determines the boundary between small and large.
## Enables
- Consistent type theory (avoiding Girard's paradox).
- Formalization of category theory with proper size distinctions.
## Related
- **girards-paradox**: Demonstrates why the distinction is necessary.

# Common Errors
- **Error**: Thinking every type is small (i.e., an object of V).
  **Correction**: V and types derived from V are large. Not every type is in V.

- **Error**: Thinking the small/large distinction is merely conventional.
  **Correction**: It is foundationally necessary. Girard's paradox shows that collapsing it leads to inconsistency.

# Common Confusions
- **Confusion**: Confusing the small/large distinction with set-theoretic notions of size (cardinality).
  **Clarification**: "Small" here means "belonging to V," not "having few elements." N is small (it is in V) despite being infinite. V is large not because of its size but because it cannot be an object of itself.

# Source Reference
Martin-Lof, P. (1972). "An Intuitionistic Theory of Types," Section 1.8.

# Verification Notes
Extracted directly from Section 1.8. Key quote preserved. High confidence.
