---
# === CORE IDENTIFICATION ===
concept: Function Type
slug: function-type

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
section: "1.3"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "A -> B"
  - "arrow type"
  - "non-dependent function type"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type
  - pi-type
extends:
  - pi-type
related:
  - lambda-abstraction
  - application
  - implication
contrasts_with:
  - pi-type
  - cartesian-product-of-two-types

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the function type A -> B?"
  - "What distinguishes the function type A -> B from the Pi type?"
  - "How does implication relate to the function type?"
---

# Quick Definition

The function type A -> B is the type of functions from A to B; it is the special case of the Pi type (Pi x in A)B(x) where B does not depend on x.

# Core Definition

Martin-Lof writes: "If B(a) is defined to be one and the same type B for every object a of type A, then (Pi x in A)B(x) will be abbreviated A -> B. It is the type of functions from A to B." (Section 1.3)

Associativity convention: "Parentheses are associated to the right so that A_1 -> ... -> A_{n-1} -> A_n abbreviates A_1 -> (... (A_{n-1} -> A_n)...)." (Section 1.3)

Logical reading: "When A and B both represent propositions, A -> B represents the implication A supset B." (Section 1.3)

# Prerequisites

- **type**: Both A and B must be types.
- **pi-type**: The function type is defined as a special case of the Pi type.

# Key Properties

1. A -> B is the non-dependent special case of (Pi x in A)B(x).
2. Objects of A -> B are functions that take any a in A to some element of B (the same B for all a).
3. Parentheses associate to the right: A -> B -> C means A -> (B -> C).
4. When A and B represent propositions, A -> B represents implication A supset B.
5. A proof of A supset B is a function taking proofs of A to proofs of B.

# Construction / Recognition

## To Construct/Create:
1. Have two types A and B.
2. Form A -> B.
3. To construct an object of A -> B, use lambda abstraction: (lambda x)b[x] where b[x] in B for all x in A.

## To Identify/Recognize:
1. The arrow notation A -> B.
2. When the codomain does not depend on the argument.
3. It is a special case of the Pi type.

# Context & Application

The function type is the most familiar special case of the Pi type and corresponds to the standard notion of a function space in mathematics. It is also the type-theoretic representation of logical implication. Many examples in the paper use function types, such as N -> N (number-theoretic functions) and N -> Q (sequences of rationals).

# Examples

From Section 1.1: N -> N is the type of number-theoretic functions. "N -> N is a type not because we know particular number theoretic functions like the primitive recursive ones but because we think we understand the notion of number theoretic function *in general*."

From Section 1.3: "A proof of A supset B is a function which takes an arbitrary proof of A into a proof of B." Thus A -> B represents the implication A supset B.

# Relationships

## Builds Upon
- pi-type: A -> B is (Pi x in A)B when B is constant.

## Enables
- implication: A -> B represents implication when A and B are propositions.

## Related
- lambda-abstraction: Functions of type A -> B are constructed by lambda abstraction.
- application: Functions of type A -> B are used by application.

## Contrasts With
- pi-type: The Pi type allows the codomain to depend on the argument; A -> B does not.
- cartesian-product-of-two-types: A x B is a product of two types (pairs); A -> B is a function space.

# Common Errors

- **Error**: Using A -> B when the codomain actually depends on the argument.
  **Correction**: If the result type varies with the input, use the full Pi type (Pi x in A)B(x), not A -> B.

# Common Confusions

- **Confusion**: Thinking A -> B and (Pi x in A)B(x) are always different things.
  **Clarification**: A -> B is literally an abbreviation for (Pi x in A)B when B does not depend on x. They are the same type in that case.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 1.3: Cartesian product of a family of types.

# Verification Notes

Confidence: high. The function type is explicitly defined as an abbreviation of the Pi type in Section 1.3, with the logical reading stated directly.
