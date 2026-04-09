---
# === CORE IDENTIFICATION ===
concept: Object Constant
slug: object-constant

# === CLASSIFICATION ===
category: formal-system
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "An Intuitionistic Theory of Types"
source_slug: intuitionistic-types
authors: "Per Martin-Lof"
chapter: "Formalization of an Intuitionistic Theory of Types"
chapter_number: 2
pdf_page: 9
section: "2.3.2"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "constant"
  - "individual constant"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type
extends: []
related:
  - type-formation-rules
  - variable
  - mathematical-object
contrasts_with:
  - variable

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

An object constant is a primitive term symbol with a fixed closed type, corresponding to individual constants, function symbols, or axioms in first order logic.

# Core Definition

Martin-Lof writes in Section 2.3.2: "If a is an *object constant* of type A, then a is a term of type A. The type of an object constant must always be closed. The object constants correspond, on the one hand, to the individual constants and function symbols in ordinary first order predicate logic and, on the other hand, to the axioms of a first order theory."

# Prerequisites

- type: Object constants are typed; their types must be closed.

# Key Properties

1. An object constant is a primitive (unanalyzed) term of a specified type.
2. The type of an object constant must be closed -- it cannot depend on any variables.
3. Object constants serve two roles: they represent (a) individual constants and function symbols, and (b) axioms of a theory.
4. Object constants are distinct from variables: variables have types that may depend on other variables; object constants always have closed types.

# Construction / Recognition

## To Introduce an Object Constant:
1. Declare a symbol a.
2. Specify a closed type A.
3. Then a is an object constant of type A, and hence a term of type A.

## To Recognize:
An object constant is a primitive symbol that is neither a variable nor a compound expression built by introduction/elimination rules.

# Context & Application

Object constants are the mechanism by which specific mathematical theories are embedded into the type-theoretic framework. For example, to formalize arithmetic, one might introduce 0 as an object constant of type N (though in Martin-Lof's presentation, 0 is introduced by the N-introduction rule instead). To formalize a first order theory with axioms, each axiom is represented as an object constant whose type is the corresponding proposition.

# Examples

In a theory of groups: a constant e of type G (the identity element), or a constant op of type G -> G -> G (the group operation), would be object constants.

An axiom such as "for all x, e * x = x" would be an object constant of the corresponding proposition-type.

# Relationships

## Builds Upon
- type: Every object constant has a closed type.

## Enables
- Embedding of first order theories into type theory (Chapter 3).

## Related
- type-constant: Type constants are the type-level analogue; object constants are the term-level analogue.
- variable: Both are atomic terms, but with different roles and restrictions.
- mathematical-object: Object constants denote specific mathematical objects.

## Contrasts With
- variable: Variables may have open types and can be bound; object constants have closed types and cannot be bound.

# Common Errors

- **Error**: Declaring an object constant with a type that depends on variables.
  **Correction**: The type of an object constant must always be closed (depend on no variables).

# Common Confusions

- **Confusion**: Confusing object constants with defined terms.
  **Clarification**: Object constants are primitive; they have no definition or reduction rule. Defined terms (like lambda-abstractions) are built from the term formation rules.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 2.3.2: Constants.

# Verification Notes

Confidence: high. Rule 2.3.2 is explicitly stated.
