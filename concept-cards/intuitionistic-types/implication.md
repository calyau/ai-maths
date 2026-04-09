---
# === CORE IDENTIFICATION ===
concept: Implication (as Function Type)
slug: implication

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
section: "1.2, 1.3"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "A supset B"
  - "A implies B"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-type
  - proposition
  - propositions-as-types
extends: []
related:
  - universal-quantification
contrasts_with:
  - conjunction

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does implication relate to the function type?"
---

# Quick Definition

Implication A supset B is represented by the function type A -> B; a proof of A supset B is a function that transforms any proof of A into a proof of B.

# Core Definition

Martin-Lof introduces implication in two places. In Section 1.2: "the intuitionistic notion of implication is explained by saying that a proof of A supset B is a function which to an arbitrary proof of A assigns a proof of B."

In Section 1.3: "When A and B both represent propositions, A -> B represents the implication A supset B. A proof of A supset B is a function which takes an arbitrary proof of A into a proof of B."

# Prerequisites

- **function-type**: Implication is the logical reading of A -> B.
- **proposition**: Both A and B must represent propositions.
- **propositions-as-types**: The identification of propositions with types underlies the correspondence.

# Key Properties

1. A supset B is represented by A -> B.
2. A proof of implication is a function from proofs to proofs.
3. Implication is the non-dependent special case of universal quantification.
4. The function must handle *arbitrary* proofs of A -- it cannot depend on the specific form of the proof.

# Construction / Recognition

## To Construct/Create:
1. Assume a proof x of A (variable of type A).
2. Construct a proof b[x] of B using x.
3. Form (lambda x)b[x] of type A -> B, which is the proof of A supset B.

## To Identify/Recognize:
1. An implication A supset B corresponds to the function type A -> B.
2. A proof of an implication is always a function (lambda abstraction).

# Context & Application

Implication is the most basic logical connective in the propositions-as-types correspondence. Its identification with the function type was part of the original Curry-Feys observation and is the starting point for the entire correspondence. It is also the non-dependent special case of universal quantification viewed as the Pi type.

# Examples

From Section 1.2: "a proof of A supset B is a function which to an arbitrary proof of A assigns a proof of B."

From Section 1.3: When A and B both represent propositions, A -> B represents A supset B.

# Relationships

## Builds Upon
- function-type: Implication is the logical reading of A -> B.

## Enables
- Logical reasoning with hypothetical proofs.

## Related
- universal-quantification: Implication is the non-dependent special case of universal quantification (when B does not depend on x in A).

## Contrasts With
- conjunction: Implication (A -> B, functions) vs. conjunction (A x B, pairs).

# Common Errors

- **Error**: Thinking a proof of A supset B merely establishes a truth-value relationship.
  **Correction**: A proof of A supset B is a function -- a computational object that transforms proofs of A into proofs of B.

# Common Confusions

- **Confusion**: Conflating material implication (classical) with intuitionistic implication.
  **Clarification**: Intuitionistic implication requires a constructive function from proofs of A to proofs of B, not merely the absence of a counterexample (A true and B false).

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Sections 1.2 and 1.3.

# Verification Notes

Confidence: high. Implication is explicitly discussed in Sections 1.2 and 1.3, with the correspondence to function types stated directly in both places.
