---
# === CORE IDENTIFICATION ===
concept: Type
slug: type

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
section: "1.1"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "kind"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - mathematical-object
  - proposition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a type in Martin-Lof's intuitionistic theory?"
  - "What must I know before understanding dependent types?"
---

# Quick Definition

A type is defined by prescribing what we have to do in order to construct an object of that type. It is the fundamental classifying notion in Martin-Lof's theory.

# Core Definition

Martin-Lof writes: "A type is defined by prescribing what we have to do in order to construct an object of that type." He adds: "Put differently, a type is welldefined if we understand (or grasp to use a word favoured by Kreisel 1970) what it means to be an object of that type." (Section 1.1)

This is described as "almost verbatim the definition of the notion of set given by Bishop 1967" and as "a simpler and at the same time more general formulation of Russell's 1903 *doctrine of types*, according to which a type is the range of significance of a propositional function." (Section 1.1)

# Prerequisites

Foundational concept -- no prerequisites within this source.

# Key Properties

1. A type is defined intensionally, by its construction rules, not by enumerating its objects.
2. Understanding a type requires understanding what it means to be an arbitrary object of that type, not knowing all its objects individually.
3. It is not required that we can generate all objects of a given type.
4. Every propositional function has a type as its domain.
5. Each proposition can be represented by a type (the type of its proofs).

# Construction / Recognition

## To Construct/Create:
1. Prescribe what counts as an object of the type being defined.
2. The prescription must be clear enough that we understand what it means to be an arbitrary object of that type.

## To Identify/Recognize:
1. A type is present whenever there is a well-defined notion of what counts as its objects.
2. Check that the construction criteria are specified (not merely an extensional collection).

# Context & Application

The notion of type is the central organizing concept of the entire theory. All other constructions -- Pi types, Sigma types, function types, natural numbers -- are specific types defined by their particular construction rules. The identification of propositions with types (Section 1.2) is one of the paper's most important ideas.

# Examples

From Section 1.1: "N -> N is a type not because we know particular number theoretic functions like the primitive recursive ones but because we think we understand the notion of number theoretic function *in general*."

From Section 1.2: When a type A represents a proposition, a in A may be read as "a is a proof of the proposition A."

# Relationships

## Builds Upon
- No prerequisites within this source.

## Enables
- mathematical-object: Objects are defined relative to types.
- proposition: Propositions are identified with certain types.
- pi-type: The Pi type is a specific type-forming operation.
- sigma-type: The Sigma type is a specific type-forming operation.
- function-type: The function type A -> B is a specific type.

## Related
- proof-object: When a type represents a proposition, its objects are proofs.

## Contrasts With
- No direct contrasts within this extraction scope.

# Common Errors

- **Error**: Thinking a type must be defined by listing all its elements (extensional definition).
  **Correction**: A type is defined by prescribing how to construct its objects. We need not enumerate or generate all objects.

# Common Confusions

- **Confusion**: Equating Martin-Lof's "type" with a set in ZFC set theory.
  **Clarification**: A type here is an intensional notion defined by construction rules, not an extensional collection. The notation a in A means "a is an object of type A," not set membership.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 1.1: Mathematical objects and their types.

# Verification Notes

Confidence: high. The concept is explicitly defined in Section 1.1 with clear quotable text. The relationship to Bishop's notion of set and Russell's doctrine of types is stated directly.
