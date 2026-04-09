---
# === CORE IDENTIFICATION ===
concept: Mathematical Object
slug: mathematical-object

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
  - "construction"
  - "object"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - type
  - proposition
  - proof-object
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a mathematical object (construction)?"
  - "What must I know before understanding dependent types?"
---

# Quick Definition

A mathematical object (or construction) is the fundamental entity in Martin-Lof's type theory; every mathematical object is always given together with its type.

# Core Definition

Martin-Lof writes: "We shall think of *mathematical objects* or *constructions*. Every mathematical object is of a certain kind or *type*. Better, a mathematical object is always given together with its type, that is, it is not just an object, it is an object of a certain type." (Section 1.1)

The notation a in A expresses that a is an object of type A. When A represents a proposition, a in A may alternatively be read as "a is a proof of the proposition A" (Section 1.2).

# Prerequisites

Foundational concept -- no prerequisites within this source. General mathematical maturity is assumed.

# Key Properties

1. Every mathematical object is always paired with a type; there are no untyped objects.
2. The term "construction" is used synonymously, reflecting the intuitionistic emphasis on constructive evidence.
3. Objects are the inhabitants of types; a type is defined by prescribing how to construct its objects.

# Construction / Recognition

## To Construct/Create:
1. Identify or define a type A by prescribing what counts as an object of that type.
2. Carry out the prescribed construction to produce an object a of type A.

## To Identify/Recognize:
1. An entity is a mathematical object only relative to some type -- check that a type is specified.
2. Verify that the entity satisfies the criteria that define objects of that type.

# Context & Application

Mathematical objects are the basic building blocks of Martin-Lof's entire type-theoretic framework. Every further concept (functions, pairs, proofs) is an instance of a mathematical object of some type. The insistence that objects are always given with their types distinguishes this framework from untyped formalisms and reflects Russell's doctrine of types in a simplified and generalized form.

# Examples

From Section 1.1: The notation a in A expresses that a is an object of type A. For instance, a number-theoretic function is an object of type N -> N.

From Section 1.4: A real number is a pair (a, b) where a is a sequence of rational numbers and b is a proof that a satisfies the Cauchy condition -- both a and b are mathematical objects of their respective types.

# Relationships

## Builds Upon
- No prerequisites within this source.

## Enables
- type: Objects are the inhabitants that give types their meaning.
- proof-object: Proofs are mathematical objects when propositions are identified with types.

## Related
- proposition: When a type represents a proposition, its objects are proofs.

## Contrasts With
- No direct contrasts within the scope of this extraction.

# Common Errors

- **Error**: Thinking of a mathematical object as existing independently of any type.
  **Correction**: In Martin-Lof's framework, an object is always given together with its type. "a" alone is incomplete; "a in A" is the proper form.

# Common Confusions

- **Confusion**: Conflating "mathematical object" with set-theoretic elements.
  **Clarification**: Here, a in A means "a is an object of type A," not set membership. Types are defined by construction rules, not by extensional membership criteria.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 1.1: Mathematical objects and their types.

# Verification Notes

Confidence: high. The concept is explicitly defined and named in Section 1.1 with a direct quotation. The synonymy with "construction" is stated in the same sentence.
