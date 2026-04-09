---
# === CORE IDENTIFICATION ===
concept: Proposition
slug: proposition

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
  - "proposition as type"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type
  - mathematical-object
extends: []
related:
  - proof-object
  - propositions-as-types
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a proposition in the propositions-as-types framework?"
  - "How does the Curry-Howard correspondence relate propositions to types?"
---

# Quick Definition

A proposition is defined by prescribing how we are allowed to prove it. In Martin-Lof's framework, each proposition is identified with the type of its proofs.

# Core Definition

Martin-Lof writes: "A *proposition* is defined by prescribing how we are allowed to prove it." He then explains: "it will not be necessary to introduce the notion of proposition as a separate notion because we can represent each proposition by a certain type, namely, the type of proofs of that proposition." (Section 1.2)

The justification is that "the proofs of a proposition must form a type" because intuitionistic explanations of the logical operations require it. For example, "a proof of A supset B is a function which to an arbitrary proof of A assigns a proof of B. And, if every function is to have a type as its domain, this requires that the proofs of the proposition A must form a type." (Section 1.2)

# Prerequisites

- **type**: A proposition is identified with a type, so the notion of type must be understood first.
- **mathematical-object**: Proofs of propositions are mathematical objects inhabiting the corresponding type.

# Key Properties

1. A proposition is not a separate primitive notion; it is identified with a type.
2. The type representing a proposition is the type of its proofs.
3. When A represents a proposition, a in A can be read as "a is a proof of the proposition A."
4. The identification is forced by the intuitionistic explanation of logical operations together with the doctrine of types.

# Construction / Recognition

## To Construct/Create:
1. Prescribe how the proposition may be proved (its proof conditions).
2. The collection of all such proofs forms a type, which represents the proposition.

## To Identify/Recognize:
1. A proposition is any type viewed under its logical interpretation.
2. When working with logical connectives (implication, quantification, etc.), the types involved represent propositions.

# Context & Application

The identification of propositions with types is the conceptual foundation of the propositions-as-types correspondence (Curry-Howard correspondence) that pervades the entire paper. It means that logical reasoning and type-theoretic construction are two views of the same activity. This identification enables the systematic translation between logical connectives and type-forming operations (implication/function type, universal quantification/Pi type, existential quantification/Sigma type, conjunction/product type).

# Examples

From Section 1.2: "971 is a non prime number" is a proposition which we prove by exhibiting two natural numbers greater than one and a computation showing their product equals 971.

From Section 1.2: The intuitionistic notion of implication requires that proofs of A form a type, since a proof of A supset B is a function from proofs of A to proofs of B, and every function must have a type as its domain.

# Relationships

## Builds Upon
- type: A proposition is identified with a type.
- mathematical-object: Proofs are mathematical objects.

## Enables
- proof-object: The notion of proof-as-object follows from propositions-as-types.
- propositions-as-types: This identification is the core of the Curry-Howard correspondence.

## Related
- implication: Implication A supset B is represented by the function type A -> B.
- universal-quantification: Universal quantification is represented by the Pi type.
- existential-quantification: Existential quantification is represented by the Sigma type.
- conjunction: Conjunction A & B is represented by the product A x B.

## Contrasts With
- No direct contrasts within this extraction scope.

# Common Errors

- **Error**: Treating propositions as separate entities from types and then trying to relate them externally.
  **Correction**: In Martin-Lof's framework, a proposition simply *is* a type (the type of its proofs). There is no separate category of propositions.

# Common Confusions

- **Confusion**: Thinking that the proposition/type identification is merely an analogy or encoding.
  **Clarification**: Martin-Lof treats the identification literally: "I shall sometimes simply identify a proposition with the type that represents it." It is not a translation between two separate systems but a single unified framework.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 1.2: Propositions and proofs.

# Verification Notes

Confidence: high. The concept is explicitly defined in Section 1.2 with direct quotations. The identification with types is stated unambiguously.
