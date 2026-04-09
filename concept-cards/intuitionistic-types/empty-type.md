---
# === CORE IDENTIFICATION ===
concept: Empty Type
slug: empty-type

# === CLASSIFICATION ===
category: type-formers
tier: foundational

# === PROVENANCE ===
source: "An Intuitionistic Theory of Types"
source_slug: intuitionistic-types
authors: "Per Martin-Löf"
chapter: "Informal Explanations of the Basic Concepts"
chapter_number: 1
pdf_page: null
section: "1.6. Finite types"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "N_0"
  - "bottom"
  - "falsehood"
  - "absurdity"
  - "void type"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type
  - finite-type
  - proposition
related:
  - unit-type
contrasts_with:
  - unit-type

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the empty type (N_0)?"
  - "What distinguishes N_0 (falsehood) from N_1 (truth)?"
---

# Quick Definition
The empty type N_0 is the finite type with zero objects. It represents the logical constant falsehood (bottom). Since it has no objects, there are no proofs of falsehood.

# Core Definition
Martin-Lof states: "In particular, N_0 is the empty type which also represents the logical constant falsehood, and the function (lambda x)R_0(x) of type (Pi x in N_0)C(x) is the empty function." (Section 1.6)

# Prerequisites
- **Type**: Must understand what a type is.
- **Finite type**: N_0 is the special case of N_n with n = 0.
- **Proposition**: Understanding the logical reading of N_0 as falsehood requires the propositions-as-types correspondence.

# Key Properties
1. N_0 has no canonical objects whatsoever.
2. N_0 represents the logical constant falsehood (bottom).
3. The empty function (lambda x)R_0(x) has type (Pi x in N_0)C(x) for any type family C -- this is ex falso quodlibet.
4. Since N_0 has no objects, R_0 has no computation rules (there are no cases to handle).

# Construction / Recognition
## To Construct/Create:
1. N_0 cannot be constructed -- it has no objects. That is the whole point: falsehood has no proof.

## To Identify/Recognize:
1. A type with no canonical elements.
2. Logically, the proposition that can never be proved.
3. Any function from N_0 to any type exists (vacuously) -- ex falso quodlibet.

# Context & Application
The empty type plays the role of falsehood in the propositions-as-types correspondence. The principle of ex falso quodlibet (from falsehood, anything follows) is captured by the fact that for any type family C, there exists a function of type (Pi x in N_0)C(x) -- the empty function. Negation of a proposition A is defined as A -> N_0 (a function from A to falsehood).

# Examples
- The empty function (lambda x)R_0(x) of type (Pi x in N_0)C(x) is the type-theoretic rendering of ex falso quodlibet.
- Negation: not-A is defined as A -> N_0, meaning a proof of not-A is a function transforming any proof of A into an object of the empty type (which is impossible, so A must have no proofs).

# Relationships
## Builds Upon
- **finite-type**: N_0 is the n = 0 case of N_n.
## Enables
- Negation: not-A = A -> N_0.
- Ex falso quodlibet: from N_0, anything follows.
## Contrasts With
- **unit-type**: N_1 has exactly one object and represents truth; N_0 has no objects and represents falsehood.

# Common Errors
- **Error**: Thinking N_0 contains zero as an object.
  **Correction**: N_0 is the type with zero objects -- it is empty. The subscript 0 indicates the count of elements, not an element.

# Common Confusions
- **Confusion**: Conflating the empty type N_0 with the natural number 0.
  **Clarification**: N_0 is a type (with no elements); 0 is an object of the type N of natural numbers. They are entirely different things.

# Source Reference
Martin-Lof, P. (1972). "An Intuitionistic Theory of Types," Section 1.6.

# Verification Notes
Extracted directly from Section 1.6. High confidence.
