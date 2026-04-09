---
# === CORE IDENTIFICATION ===
concept: Universal Quantification (as Pi Type)
slug: universal-quantification

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
section: "1.3"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "for all"
  - "(forall x in A)B(x)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pi-type
  - proposition
  - propositions-as-types
extends: []
related:
  - implication
  - existential-quantification
contrasts_with:
  - existential-quantification

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does universal quantification relate to the Pi type?"
---

# Quick Definition

Universal quantification (forall x in A)B(x) is represented by the Pi type (Pi x in A)B(x); a proof of the universal proposition is a function assigning to each object of type A a proof of B(a).

# Core Definition

Martin-Lof writes: "When B(a) represents a proposition for every object a of type A, (Pi x in A)B(x) represents the universal proposition (forall x in A)B(x). A proof of (forall x in A)B(x) is a function which to an arbitrary object a of type A assigns a proof of B(a)." (Section 1.3)

# Prerequisites

- **pi-type**: Universal quantification is the logical reading of the Pi type.
- **proposition**: B(a) must represent a proposition for each a in A.
- **propositions-as-types**: The identification of propositions with types underlies this correspondence.

# Key Properties

1. (forall x in A)B(x) is represented by (Pi x in A)B(x).
2. A proof is a dependent function: for each a in A, it produces a proof of B(a).
3. This is the dependent generalization of implication (which is the special case where B does not depend on x).

# Construction / Recognition

## To Construct/Create:
1. For each a in A, construct a proof of B(a).
2. This construction, as a function of a, is a lambda abstraction (lambda x)b[x] of type (Pi x in A)B(x).

## To Identify/Recognize:
1. A universally quantified proposition (forall x in A)B(x) is present whenever a Pi type is given a logical reading.
2. The quantifier ranges over a type A, not over an untyped domain.

# Context & Application

The representation of universal quantification as the Pi type is a central instance of the propositions-as-types correspondence. It shows how dependent types extend the Curry-Howard correspondence from propositional logic (where implication corresponds to function types) to predicate logic (where universal quantification corresponds to Pi types).

# Examples

From Section 1.3: "A proof of (forall x in A)B(x) is a function which to an arbitrary object a of type A assigns a proof of B(a)."

From Section 1.4: The Cauchy condition for real numbers involves nested universal quantification: (Pi m in N)(Pi n in N)(|x_{m+n} - x_m| <= 2^{-m}).

# Relationships

## Builds Upon
- pi-type: Universal quantification is the logical reading of the Pi type.

## Enables
- Logical reasoning about all objects of a given type within the type-theoretic framework.

## Related
- implication: Implication is the non-dependent special case (forall over a domain where the conclusion does not depend on the variable).

## Contrasts With
- existential-quantification: Universal quantification (Pi / functions) vs. existential quantification (Sigma / pairs).

# Common Errors

- **Error**: Thinking universal quantification ranges over all objects whatsoever (as in untyped logic).
  **Correction**: In Martin-Lof's theory, quantification is always typed: (forall x in A)B(x) ranges over objects of type A.

# Common Confusions

- **Confusion**: Conflating universal quantification with the non-dependent function type A -> B.
  **Clarification**: A -> B represents implication (where the conclusion B does not depend on the hypothesis). The full universal (forall x in A)B(x) allows B(x) to vary with x.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 1.3: Cartesian product of a family of types.

# Verification Notes

Confidence: high. The correspondence is explicitly stated in Section 1.3 with a direct quotation.
