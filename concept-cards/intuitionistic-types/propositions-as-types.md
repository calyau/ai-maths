---
# === CORE IDENTIFICATION ===
concept: Propositions-as-Types / Curry-Howard Correspondence
slug: propositions-as-types

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
  - "Curry-Howard correspondence"
  - "Curry-Howard isomorphism"
  - "formulae-as-types"
  - "proofs-as-programs"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type
  - proposition
  - proof-object
extends: []
related:
  - mathematical-object
  - pi-type
  - sigma-type
  - function-type
  - implication
  - universal-quantification
  - existential-quantification
  - conjunction
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the Curry-Howard correspondence relate propositions to types?"
  - "What is a proposition in the propositions-as-types framework?"
  - "What is a proof in the propositions-as-types framework?"
---

# Quick Definition

The propositions-as-types correspondence identifies each proposition with the type of its proofs, so that logical connectives correspond to type-forming operations and proofs correspond to constructions.

# Core Definition

Martin-Lof writes: "we can represent each proposition by a certain type, namely, the type of proofs of that proposition." He attributes the formal discovery to Curry and Feys 1958 (analogy between formulae and types) and Howard 1969 (extension to quantifiers): "On the formal level, the analogy between formulae and types was discovered by Curry and Feys 1958 and further extended by Howard 1969 to whom I am indebted for explaining it to me." (Section 1.2)

The correspondence is realized concretely throughout Sections 1.3 and 1.4:

| Logical notion | Type-theoretic notion |
|---|---|
| Implication A supset B | Function type A -> B |
| Universal quantification (forall x in A)B(x) | Pi type (Pi x in A)B(x) |
| Existential quantification (exists x in A)B(x) | Sigma type (Sigma x in A)B(x) |
| Conjunction A & B | Cartesian product A x B |

# Prerequisites

- **type**: The right-hand side of the correspondence.
- **proposition**: The left-hand side of the correspondence.
- **proof-object**: Proofs are the objects inhabiting the types that represent propositions.

# Key Properties

1. The correspondence is not merely formal but conceptually motivated by the intuitionistic explanations of the logical operations.
2. It unifies logic and type theory into a single framework rather than relating two separate systems.
3. It extends from propositional logic (Curry-Feys) to predicate logic with quantifiers (Howard).
4. Proofs carry computational content: a proof of an implication is a function, a proof of an existential is a pair.

# Construction / Recognition

## To Construct/Create:
1. Given a logical statement, identify which logical connectives it uses.
2. Replace each connective with the corresponding type former (implication -> function type, universal -> Pi, existential -> Sigma, conjunction -> product).
3. A proof of the statement is then an object of the resulting type.

## To Identify/Recognize:
1. Whenever a type is given a logical reading, the propositions-as-types correspondence is at work.
2. Whenever a in A is read both as "a is an object of type A" and "a is a proof of proposition A."

# Context & Application

The propositions-as-types correspondence is the conceptual backbone of Martin-Lof's paper. It justifies the entire approach of formalizing intuitionistic mathematics within a theory of types rather than within a separate logical calculus. It also underpins the computational interpretation of proofs that has been influential in programming language theory and proof assistants.

# Examples

From Section 1.3: "A proof of (forall x in A)B(x) is a function which to an arbitrary object a of type A assigns a proof of B(a)." Here universal quantification corresponds to the Pi type and a proof corresponds to a dependent function.

From Section 1.3: "A proof of A supset B is a function which takes an arbitrary proof of A into a proof of B." Here implication corresponds to the function type A -> B.

From Section 1.4: "we prove [an existential] by exhibiting a pair (a,b) where a is an object of type A and b a proof of the proposition B(a)." Here existential quantification corresponds to the Sigma type and a proof is a dependent pair.

# Relationships

## Builds Upon
- type, proposition, proof-object

## Enables
- All logical interpretations of type formers: implication, universal-quantification, existential-quantification, conjunction.

## Related
- pi-type, sigma-type, function-type: The type-theoretic side of specific correspondences.

## Contrasts With
- No direct contrasts within this extraction scope.

# Common Errors

- **Error**: Thinking the correspondence is merely a notational convention or encoding trick.
  **Correction**: Martin-Lof treats it as a genuine identification: propositions *are* types. The logical and computational content are one and the same.

# Common Confusions

- **Confusion**: Thinking the Curry-Howard correspondence applies only to propositional logic.
  **Clarification**: Howard 1969 extended it to predicate logic (quantifiers), and Martin-Lof's theory realizes this extension with dependent types (Pi and Sigma).

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 1.2: Propositions and proofs, with concrete instances in Sections 1.3 and 1.4.

# Verification Notes

Confidence: high. The correspondence is explicitly described in Section 1.2 with attribution to Curry-Feys and Howard, and concretely realized throughout Sections 1.3-1.4.
