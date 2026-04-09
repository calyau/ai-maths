---
# === CORE IDENTIFICATION ===
concept: Lambda Abstraction
slug: lambda-abstraction

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
section: "1.3"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "explicit definition"
  - "Pi introduction"
  - "function introduction"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type
  - mathematical-object
  - pi-type
extends: []
related:
  - application
  - function-type
contrasts_with:
  - pairing

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I construct a function (lambda abstraction)?"
---

# Quick Definition

Lambda abstraction (lambda x)b[x] is the mechanism for introducing functions: given a term b[x] of type B(x) built from a variable x of type A, (lambda x)b[x] is an object of Pi type (Pi x in A)B(x).

# Core Definition

Martin-Lof writes: "Functions may be introduced by *explicit definition*. That is, if we, starting from a variable x that denotes an arbitrary object of type A, build up a term b[x] that denotes an object of type B(x), then we may define a function denoted (lambda x)b[x] of type (Pi x in A)B(x) by means of the schema (lambda x)b[x](a) = b[a]." (Section 1.3)

Here b[a] denotes the result of substituting the object a of type A for the variable x in the term b[x].

# Prerequisites

- **type**: The domain type A and the family of codomain types B(x) must be understood.
- **mathematical-object**: The variable x and the term b[x] denote mathematical objects.
- **pi-type**: Lambda abstraction produces objects of Pi type.

# Key Properties

1. Lambda abstraction is the introduction rule for Pi types.
2. The defining equation (lambda x)b[x](a) = b[a] is the beta-reduction rule.
3. The variable x ranges over all objects of type A.
4. The body b[x] must be a well-typed term of type B(x) for arbitrary x in A.
5. Martin-Lof calls this "explicit definition" of functions.

# Construction / Recognition

## To Construct/Create:
1. Start with a variable x of type A.
2. Build a term b[x] of type B(x) using x.
3. Form the lambda abstraction (lambda x)b[x], which has type (Pi x in A)B(x).

## To Identify/Recognize:
1. Lambda abstractions are denoted (lambda x)b[x].
2. They are the canonical way to introduce functions.
3. They come with a computation rule: applying (lambda x)b[x] to a yields b[a].

# Context & Application

Lambda abstraction is the sole mechanism presented in the paper for constructing functions (objects of Pi type). Together with application, it forms the introduction-elimination pair for the Pi type. The computation rule (lambda x)b[x](a) = b[a] is the fundamental reduction rule that drives computation in the theory.

# Examples

From Section 1.3: If b[x] is a term of type B(x) for x of type A, then (lambda x)b[x] is a function of type (Pi x in A)B(x), and (lambda x)b[x](a) = b[a] for any a in A.

From Section 1.4: The empty function (lambda x)R_0(x) of type (Pi x in N_0)C(x) is constructed by lambda abstraction over the empty type (mentioned in Section 1.6 but using the same mechanism).

# Relationships

## Builds Upon
- pi-type: Lambda abstraction produces objects of Pi type.

## Enables
- Any function definition in the theory relies on lambda abstraction.

## Related
- application: The elimination form that is dual to lambda abstraction.
- function-type: In the non-dependent case, lambda abstraction produces objects of A -> B.

## Contrasts With
- pairing: Pairing (a, b) is the introduction form for Sigma types, while lambda abstraction is the introduction form for Pi types.

# Common Errors

- **Error**: Forgetting that the body b[x] must be well-typed for an arbitrary x of type A.
  **Correction**: The term b[x] must denote an object of type B(x) for any x in A, not just for specific values.

# Common Confusions

- **Confusion**: Treating lambda abstraction as merely notation rather than a type-theoretic operation.
  **Clarification**: Lambda abstraction is the introduction rule for Pi types. It is not just notation but has a specific typing rule and computation rule (beta-reduction).

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 1.3: Cartesian product of a family of types.

# Verification Notes

Confidence: high. Lambda abstraction is explicitly defined in Section 1.3 with the defining schema and its synonym "explicit definition" stated directly.
