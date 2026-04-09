---
# === CORE IDENTIFICATION ===
concept: Finite Type
slug: finite-type

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
  - "N_n"
  - "enumeration type"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type
related:
  - empty-type
  - unit-type
  - disjoint-union-of-two-types
  - natural-numbers
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the disjoint union A + B of two types?"
---

# Quick Definition
For each nonnegative integer n, the finite type N_n is the type with precisely n objects: 1, 2, ..., n. The two fundamental cases are N_0 (the empty type) and N_1 (the unit type); all others can be built from N_1 using disjoint union.

# Core Definition
Martin-Lof defines: "For each nonnegative integer n we introduce a type N_n with precisely the n objects 1, 2, ..., n. Actually, it would suffice to introduce N_0 and N_1 because, for n greater than one, we can define N_n to be the union of N_1 with itself n times." (Section 1.6)

The eliminator R_n is defined by: "R_n(1, c_1, ..., c_n) = c_1, ..., R_n(n, c_1, ..., c_n) = c_n." (Section 1.6)

# Prerequisites
- **Type**: Must understand what a type is.

# Key Properties
1. N_n has exactly n canonical objects: 1, 2, ..., n.
2. N_0 and N_1 are primitive; N_n for n > 1 is definable as N_1 + N_1 + ... + N_1 (n times).
3. The eliminator R_n selects among n given values based on which element of N_n is provided.
4. R_n supports dependent elimination: the result type C(x) can depend on x in N_n.

# Construction / Recognition
## To Construct/Create:
1. Choose one of the n canonical elements: 1, 2, ..., n.

## To Identify/Recognize:
1. A type with a fixed, finite number of canonical elements.
2. Functions out of it are defined by exhaustive enumeration of cases.

# Context & Application
Finite types provide the type-theoretic counterparts of finite sets. The special cases N_0 and N_1 represent the logical constants falsehood and truth, respectively. The general N_n provides enumeration types. The observation that N_n for n > 1 reduces to iterated sums of N_1 shows that + and N_1 together generate all finite types.

# Examples
- N_0 = empty type (no objects), represents falsehood.
- N_1 = unit type (one object: 1), represents truth.
- N_2 = N_1 + N_1, the boolean type with two elements.

# Relationships
## Builds Upon
- **type**: Each N_n is a type.
## Enables
- **empty-type**: N_0 is the empty type.
- **unit-type**: N_1 is the unit type.
## Related
- **disjoint-union-of-two-types**: N_n for n > 1 is built from iterated disjoint unions of N_1.
- **natural-numbers**: N is the infinite analogue of the finite types.

# Common Errors
- **Error**: Assuming the finite types are indexed starting from 0.
  **Correction**: The objects of N_n are 1, 2, ..., n (starting from 1), not 0, 1, ..., n-1.

# Common Confusions
- **Confusion**: Thinking N_n requires n to be a term in the type theory.
  **Clarification**: Here n is a meta-level nonnegative integer. Each N_n is a specific type with a fixed number of elements.

# Source Reference
Martin-Lof, P. (1972). "An Intuitionistic Theory of Types," Section 1.6.

# Verification Notes
Extracted directly from Section 1.6. High confidence.
