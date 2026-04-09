---
# === CORE IDENTIFICATION ===
concept: Such-That Type
slug: such-that-type

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
  - "subset type"
  - "refinement type"
  - "such that"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sigma-type
  - proof-object
extends:
  - sigma-type
related:
  - existential-quantification
  - pairing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the disjoint union (Sigma type) of a family of types?"
---

# Quick Definition

The "such that" type uses the Sigma type to represent the type of all objects a of type A such that B(a) holds, by pairing each object with a proof of the condition.

# Core Definition

Martin-Lof writes: "A third function of (Sigma x in A)B(x) is to represent the type of all objects a of type A such that B(a), because, from the intuitionistic point of view, to give an object a of type A such that B(a) is to give a together with a proof b of the proposition B(a)." (Section 1.4)

He adds: "This interpretation of the notion of such that is implicitly used by Bishop 1967 and discussed by Kreisel 1968. However, its explicit formulation requires us to consider proofs as mathematical objects." (Section 1.4)

# Prerequisites

- **sigma-type**: The "such that" type is an interpretation of the Sigma type.
- **proof-object**: The interpretation requires treating proofs as first-class mathematical objects that appear as components of pairs.

# Key Properties

1. {a in A | B(a)} is represented as (Sigma x in A)B(x).
2. An object of the "such that" type is a pair (a, b) with a in A and b a proof of B(a).
3. This interpretation requires proofs to be mathematical objects (they are part of the data).
4. The proof component b is not mere metadata -- computations may depend on it.

# Construction / Recognition

## To Construct/Create:
1. Choose an object a of type A.
2. Prove that B(a) holds by constructing a proof b.
3. Form the pair (a, b).

## To Identify/Recognize:
1. Whenever a type is described as "the type of all X such that P(X)," it is a Sigma type in this interpretation.
2. The proof of the condition is bundled with the object as a pair.

# Context & Application

The "such that" interpretation is distinctive to Martin-Lof's theory and is essential for formalizing mathematical definitions where objects come with conditions. It requires the conceptual commitment to treating proofs as data. This is particularly visible in the definition of real numbers and in functions whose definitions depend on proof arguments.

# Examples

From Section 1.4: The type R of real numbers is (Sigma x in N -> Q)(Pi m in N)(Pi n in N)(|x_{m+n} - x_m| <= 2^{-m}). "Thus, a real number is a pair (a,b) where a is a sequence of rational numbers and b is a proof that a satisfies the Cauchy condition."

From Section 1.4: The inverse function has type (Pi z in R)(z != 0 -> R) because "the definition of the inverse c^{-1} of a non zero real number c depends effectively on the proof that c != 0."

From Section 1.4: Ordinal subtraction has type (Pi x in O)(Pi y in O)(x < y -> O) because the definition depends on the proof of x < y.

# Relationships

## Builds Upon
- sigma-type: The "such that" type is a specific reading of Sigma.
- proof-object: Requires proofs to be mathematical objects.

## Enables
- Formalization of mathematical definitions with conditions (e.g., real numbers, non-zero reals).

## Related
- existential-quantification: The "such that" and "there exists" readings of Sigma are closely linked but emphasize different aspects (object-with-condition vs. witness-and-evidence).

## Contrasts With
- No direct contrasts within this extraction scope.

# Common Errors

- **Error**: Thinking the proof component can be discarded after construction.
  **Correction**: The proof is part of the object and computations may depend on it. The inverse function example shows this explicitly.

# Common Confusions

- **Confusion**: Thinking "such that" types are the same as subset types where proofs are irrelevant.
  **Clarification**: In Martin-Lof's theory, the proof is part of the data. Two objects (a, b) and (a, b') with different proofs b != b' are distinct objects, even though they have the same first component.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 1.4: Disjoint union of a family of types.

# Verification Notes

Confidence: high. The "such that" interpretation is explicitly described in Section 1.4 with the real number example and the requirement that proofs be mathematical objects stated directly.
