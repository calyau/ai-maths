---
# === CORE IDENTIFICATION ===
concept: Proof Object
slug: proof-object

# === CLASSIFICATION ===
category: foundations
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "An Intuitionistic Theory of Types"
source_slug: intuitionistic-types
authors: "Per Martin-Lof"
chapter: "Informal Explanations of the Basic Concepts"
chapter_number: 1
pdf_page: 0
section: "1.2"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "proof"
  - "proof as object"
  - "evidence"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type
  - mathematical-object
  - proposition
extends: []
related:
  - propositions-as-types
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a proof in the propositions-as-types framework?"
  - "How does the Curry-Howard correspondence relate propositions to types?"
---

# Quick Definition

A proof is a mathematical object inhabiting the type that represents a proposition. To prove a proposition A is to construct an object of type A.

# Core Definition

When a type A represents a proposition, "a in A may be read alternatively: a is a proof of the proposition A." (Section 1.2)

Proofs are full-fledged mathematical objects. Martin-Lof emphasizes this in Section 1.4: "its explicit formulation requires us to consider proofs as mathematical objects." The example of the inverse function shows that "the definition of the inverse c^{-1} of a non zero real number c depends effectively on the proof that c != 0." (Section 1.4)

# Prerequisites

- **type**: Proofs inhabit types; the type is the proposition being proved.
- **mathematical-object**: Proofs are mathematical objects in the full sense.
- **proposition**: A proof is always a proof *of* some proposition (i.e., an inhabitant of some type-qua-proposition).

# Key Properties

1. A proof is not a meta-level argument but a first-class mathematical object.
2. Proofs can be arguments to functions and components of pairs.
3. Computations can depend on proofs -- proofs carry computational content.
4. The type of a proof object is the proposition it proves.

# Construction / Recognition

## To Construct/Create:
1. Identify the proposition A to be proved (equivalently, the type A to be inhabited).
2. Construct an object of type A according to the rules defining that type.
3. The resulting object a is a proof of A.

## To Identify/Recognize:
1. Any object a in A, where A is viewed as a proposition, is a proof of A.
2. Proofs are recognized by their computational content and the type they inhabit.

# Context & Application

The treatment of proofs as mathematical objects is essential to Martin-Lof's framework and has deep consequences. It means that proofs are not merely certificates of truth but carry computational content that can be used in further constructions. This is particularly visible in the "such that" interpretation of Sigma types and in examples where function definitions depend on proof arguments.

# Examples

From Section 1.4: A real number is defined as a pair (a, b) where a is a sequence of rational numbers and b is a proof that a satisfies the Cauchy condition. Here b is a proof treated as a mathematical object and paired with a.

From Section 1.4: The inverse function on reals is not of type R -> R but of type (Pi z in R)(z != 0 -> R), because "the definition of the inverse c^{-1} of a non zero real number c depends effectively on the proof that c != 0."

# Relationships

## Builds Upon
- type: A proof inhabits a type.
- mathematical-object: Proofs are mathematical objects.
- proposition: A proof is a proof of a proposition.

## Enables
- sigma-type: Sigma types can pair data with proofs (the "such that" interpretation).
- existential-quantification: A proof of an existential is a pair (witness, proof).

## Related
- propositions-as-types: The dual reading of a in A as "a is a proof of A."

## Contrasts With
- No direct contrasts within this extraction scope.

# Common Errors

- **Error**: Treating proofs as irrelevant or erasable metadata.
  **Correction**: In Martin-Lof's theory, proofs are computational objects. The definition of the inverse function, for example, depends effectively on the proof argument.

# Common Confusions

- **Confusion**: Thinking "proof" means a sequence of logical deduction steps (as in Hilbert-style proof theory).
  **Clarification**: Here a proof is a mathematical object (a term, a function, a pair, etc.) that inhabits the type representing the proposition. It is a construction, not a derivation tree.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Sections 1.2 and 1.4.

# Verification Notes

Confidence: high. The concept is explicitly discussed in Sections 1.2 and 1.4, with direct quotations. The examples from Section 1.4 (real numbers, inverse function) strongly illustrate the point.
