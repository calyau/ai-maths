---
# === CORE IDENTIFICATION ===
concept: Unit Type
slug: unit-type

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
  - "N_1"
  - "top"
  - "truth"
  - "trivial type"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type
  - finite-type
  - proposition
related:
  - empty-type
contrasts_with:
  - empty-type

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes N_0 (falsehood) from N_1 (truth)?"
---

# Quick Definition
The unit type N_1 is the finite type with exactly one object (the element 1). It represents the logical constant truth (top), since truth is trivially provable.

# Core Definition
Martin-Lof states: "Similarly, the one element type N_1 is used to represent the logical constant truth." (Section 1.6)

As a special case of the finite types, N_1 has precisely one object: 1. The eliminator R_1 satisfies: R_1(1, c_1) = c_1.

# Prerequisites
- **Type**: Must understand what a type is.
- **Finite type**: N_1 is the special case of N_n with n = 1.
- **Proposition**: Understanding the logical reading of N_1 as truth requires the propositions-as-types correspondence.

# Key Properties
1. N_1 has exactly one canonical object: 1.
2. N_1 represents the logical constant truth (top).
3. Truth is trivially provable: the element 1 is the canonical proof.
4. Any function from a type A to N_1 is trivial (constant), since N_1 has only one element.
5. N_1 serves as a building block: N_n for n > 1 is N_1 + N_1 + ... + N_1.

# Construction / Recognition
## To Construct/Create:
1. The unique object of N_1 is 1.

## To Identify/Recognize:
1. A type with exactly one canonical element.
2. Logically, the proposition that is trivially true.

# Context & Application
The unit type plays the role of truth in the propositions-as-types correspondence. It is used in the definition of equality on natural numbers (Section 1.8), where E(0,0) = top (N_1) and E(s(m),0) = bottom (N_0). Together with N_0, it provides the type-theoretic foundation for boolean-valued operations.

# Examples
From Section 1.8, the equality function on natural numbers is defined by recursion with: E(0,0) = top (i.e., N_1), E(s(m),0) = bottom (i.e., N_0), showing N_1 in use as the type representing a true proposition.

# Relationships
## Builds Upon
- **finite-type**: N_1 is the n = 1 case of N_n.
## Enables
- **finite-type**: All N_n for n > 1 are built from iterated sums of N_1.
- Equality on natural numbers uses N_1 (truth) and N_0 (falsehood).
## Contrasts With
- **empty-type**: N_0 has no objects (falsehood); N_1 has one object (truth).

# Common Errors
- **Error**: Confusing the element 1 of N_1 with the natural number 1 or with the type N_1 itself.
  **Correction**: The element 1 is the unique object of the type N_1. It is distinct from the successor s(0) in N and from the type N_1 itself.

# Common Confusions
- **Confusion**: Thinking N_1 carries information.
  **Clarification**: N_1 carries no information (it has exactly one element). That is precisely why it represents truth: the proof is trivial and unique.

# Source Reference
Martin-Lof, P. (1972). "An Intuitionistic Theory of Types," Section 1.6.

# Verification Notes
Extracted from Section 1.6. High confidence.
