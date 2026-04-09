---
# === CORE IDENTIFICATION ===
concept: Pairing (Sigma Introduction)
slug: pairing

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
  - "Sigma introduction"
  - "pair formation"
  - "dependent pair"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sigma-type
  - mathematical-object
extends: []
related:
  - sigma-elimination
  - sigma-elimination
  - existential-quantification
contrasts_with:
  - lambda-abstraction

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I form a pair (Sigma introduction)?"
---

# Quick Definition

Pairing (a, b) is the introduction form for Sigma types: given a in A and b in B(a), the pair (a, b) is an object of type (Sigma x in A)B(x).

# Core Definition

From Section 1.4: The Sigma type "(Sigma x in A)B(x) ... is the type of pairs (a,b) where a and b are objects of type A and B(a), respectively."

For existential propositions: "we prove [the existential] by exhibiting a pair (a,b) where a is an object of type A and b a proof of the proposition B(a)." (Section 1.4)

# Prerequisites

- **sigma-type**: Pairing produces objects of Sigma type.
- **mathematical-object**: Both components of the pair must be mathematical objects of appropriate types.

# Key Properties

1. The pair (a, b) is the canonical introduction form for Sigma types.
2. The first component a determines the type B(a) of the second component b.
3. When the Sigma type represents an existential proposition, the first component is the witness and the second is the proof.
4. When the Sigma type represents a "such that" type, the first component is the object and the second is the proof of the condition.

# Construction / Recognition

## To Construct/Create:
1. Choose an object a of type A (the first component / witness).
2. Construct an object b of type B(a) (the second component / proof).
3. Form the pair (a, b), which has type (Sigma x in A)B(x).

## To Identify/Recognize:
1. Notation: (a, b).
2. Appears whenever an object of a Sigma type is constructed.
3. In logical contexts, appears as the proof of an existential statement.

# Context & Application

Pairing is the way to introduce objects of Sigma type, just as lambda abstraction introduces objects of Pi type. In logical terms, pairing corresponds to proving an existential statement by providing a witness and a proof. In the "such that" interpretation, pairing bundles an object with evidence that it satisfies a condition.

# Examples

From Section 1.4: A real number is a pair (a, b) where a in N -> Q is a sequence of rationals and b is a proof that a satisfies the Cauchy condition.

From Section 1.4: A proof of (exists x in A)B(x) is a pair (a, b) where a in A is the witness and b in B(a) is the proof.

# Relationships

## Builds Upon
- sigma-type: Pairing is the introduction form for Sigma types.

## Enables
- Objects of Sigma type exist because they can be formed by pairing.

## Related
- sigma-elimination: The E operator eliminates pairs.
- left-and-right-projection: Projections p and q extract components from pairs.
- existential-quantification: Pairing proves existential propositions.

## Contrasts With
- lambda-abstraction: Lambda abstraction is Pi introduction; pairing is Sigma introduction. Lambda produces functions; pairing produces pairs.

# Common Errors

- **Error**: Forming (a, b) where b has type B(a') for a' != a.
  **Correction**: The second component b must have type B(a) -- the type determined by the actual first component a.

# Common Confusions

- **Confusion**: Thinking a pair is just a tuple with no typing constraint between components.
  **Clarification**: In a dependent pair, the type of b depends on a. This dependency is the defining feature of dependent pairs versus ordinary (non-dependent) pairs.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 1.4: Disjoint union of a family of types.

# Verification Notes

Confidence: high. Pairing is explicitly described as the way to form objects of Sigma type throughout Section 1.4, with concrete examples.
