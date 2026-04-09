---
# === CORE IDENTIFICATION ===
concept: Disjoint Union of Two Types
slug: disjoint-union-of-two-types

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
section: "1.5. Disjoint union of two types"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "sum type"
  - "coproduct type"
  - "A + B"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type
  - proposition
extends:
  - sigma-type
related:
  - canonical-injections
  - definition-by-cases
  - disjunction
contrasts_with:
  - pi-type

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the disjoint union A + B of two types?"
---

# Quick Definition
If A and B are types, their disjoint union A + B is the type whose objects are either i(a) with a of type A or j(b) with b of type B, where i and j are the canonical injections.

# Core Definition
Martin-Lof defines: "If A and B are types, so is the disjoint union A + B which is the type of objects of the form i(a) with a of type A or j(b) with b of type B. Here i and j denote the canonical injections." (Section 1.5)

# Prerequisites
- **Type**: One must understand what a type is and how types are defined by prescribing how to construct their objects.
- **Proposition**: The logical reading of A + B as disjunction requires understanding the propositions-as-types correspondence.

# Key Properties
1. Every object of A + B is either of the form i(a) for some a in A, or j(b) for some b in B.
2. The injections i and j are tagged, making the union disjoint even when A and B are the same type.
3. When A and B represent propositions, A + B represents their disjunction A v B.

# Construction / Recognition
## To Construct/Create:
1. Start with two types A and B.
2. Apply i to an object a of type A to get i(a) in A + B.
3. Or apply j to an object b of type B to get j(b) in A + B.

## To Identify/Recognize:
1. Check whether a type is described as a tagged union of two component types.
2. Look for canonical injections i and j tagging elements from each side.

# Context & Application
The disjoint union A + B is the binary coproduct in the type-theoretic setting. It provides the computational content behind disjunction: to prove A v B, one must either prove A (and inject via i) or prove B (and inject via j). Functions out of A + B are defined by cases using the D operator.

# Examples
Martin-Lof notes that finite types N_n for n > 1 can be defined as the union of N_1 with itself n times, showing how A + B serves as a basic building block for finite types (Section 1.6).

# Relationships
## Builds Upon
- **type**: A + B requires A and B to be types.
## Enables
- **definition-by-cases**: The D operator eliminates A + B by case analysis.
- **disjunction**: A + B represents A v B when A and B are propositions.
- **finite-type**: N_n for n > 1 is built from iterated sums of N_1.
## Related
- **canonical-injections**: i and j are the introduction forms for A + B.
## Contrasts With
- **cartesian-product-of-a-family-of-types**: Pi types represent universal quantification / functions; A + B represents disjunction / choice.
- **disjoint-union-of-a-family-of-types**: Sigma types are dependent pairs; A + B is a non-dependent tagged union.

# Common Errors
- **Error**: Confusing A + B with the set-theoretic union A U B.
  **Correction**: A + B is a *disjoint* (tagged) union. Even if A = B, the two copies are distinguished by the tags i and j.

# Common Confusions
- **Confusion**: Thinking A + B is the same as (Sigma x in A)B(x).
  **Clarification**: The Sigma type is a dependent pair type. A + B is a binary coproduct with tagged injections, not a dependent construction.

# Source Reference
Martin-Lof, P. (1972). "An Intuitionistic Theory of Types," Section 1.5.

# Verification Notes
Extracted directly from Section 1.5. All notation and definitions match the source. High confidence.
