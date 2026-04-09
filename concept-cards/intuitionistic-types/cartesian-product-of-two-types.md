---
# === CORE IDENTIFICATION ===
concept: Cartesian Product of Two Types
slug: cartesian-product-of-two-types

# === CLASSIFICATION ===
category: type-formers
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "An Intuitionistic Theory of Types"
source_slug: intuitionistic-types
authors: "Per Martin-Lof"
chapter: "Informal Explanations of the Basic Concepts"
chapter_number: 1
pdf_page: 0
section: "1.4"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "A x B"
  - "binary product"
  - "product type"
  - "pair type"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sigma-type
extends:
  - sigma-type
related:
  - conjunction
  - pairing
contrasts_with:
  - function-type

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does conjunction relate to the Cartesian product?"
---

# Quick Definition

The Cartesian product A x B is the type of pairs (a, b) with a in A and b in B; it is the non-dependent special case of the Sigma type (Sigma x in A)B(x) where B does not depend on x.

# Core Definition

Martin-Lof writes: "In the special case when B(a) is defined to be one and the same type B for every object a of type A, (Sigma x in A)B(x) is abbreviated [A x B]. It is the *cartesian product* of the two types A and B." (Section 1.4)

Logical reading: "If A and B both represent propositions, then A x B represents their conjunction A & B." (Section 1.4)

# Prerequisites

- **sigma-type**: A x B is defined as a special case of the Sigma type.

# Key Properties

1. A x B is (Sigma x in A)B where B is constant (does not depend on x).
2. Objects of A x B are pairs (a, b) with a in A and b in B.
3. When A and B represent propositions, A x B represents conjunction A & B.
4. The projections p and q have simple (non-dependent) types: A x B -> A and A x B -> B.

# Construction / Recognition

## To Construct/Create:
1. Have an object a of type A and an object b of type B.
2. Form the pair (a, b) of type A x B.

## To Identify/Recognize:
1. Notation: A x B.
2. The type of pairs where neither component's type depends on the other.
3. Special case of Sigma type with constant family.

# Context & Application

The Cartesian product of two types is the familiar notion of ordered pairs. It is the non-dependent specialization of the Sigma type, just as the function type A -> B is the non-dependent specialization of the Pi type. Under the propositions-as-types reading, it represents logical conjunction.

# Examples

From Section 1.4: If A and B are propositions, A x B represents A & B, proved by exhibiting a pair (a, b) where a proves A and b proves B.

From Section 1.4 (Girard's paradox context): P(A, <) x Q(A, <) is used to conjoin the transitivity and well-foundedness properties of an ordering.

# Relationships

## Builds Upon
- sigma-type: A x B is the non-dependent special case of (Sigma x in A)B(x).

## Enables
- conjunction: A x B represents A & B under the propositions-as-types reading.

## Related
- pairing: Objects of A x B are formed by pairing.

## Contrasts With
- function-type: A -> B (functions from A to B) vs. A x B (pairs of elements from A and B). A -> B is non-dependent Pi; A x B is non-dependent Sigma.

# Common Errors

- **Error**: Confusing the Cartesian product A x B (non-dependent Sigma) with the "Cartesian product of a family of types" (Pi type).
  **Correction**: Despite sharing the name "Cartesian product," A x B is a special case of Sigma, while "Cartesian product of a family" is the Pi type. The terminology follows set-theoretic convention where a product of a family of sets is Pi and a product of two sets is pairs.

# Common Confusions

- **Confusion**: Thinking A x B is a separate primitive type former.
  **Clarification**: A x B is defined as an abbreviation for (Sigma x in A)B where B is constant. It is not a new type former but a notation for a special case.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 1.4: Disjoint union of a family of types.

# Verification Notes

Confidence: high. The Cartesian product of two types is explicitly defined as an abbreviation of the Sigma type in Section 1.4, with the logical reading stated directly.
