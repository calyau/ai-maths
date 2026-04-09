---
# === CORE IDENTIFICATION ===
concept: Application
slug: application

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
  - "function application"
  - "Pi elimination"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pi-type
  - mathematical-object
extends: []
related:
  - lambda-abstraction
  - function-type
contrasts_with:
  - sigma-elimination

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I apply a function (Pi elimination)?"
---

# Quick Definition

Application is the operation of applying a function b of Pi type (Pi x in A)B(x) to an argument a of type A, yielding an object b(a) of type B(a).

# Core Definition

Martin-Lof writes: "we may apply an object b of type (Pi x in A)B(x) to an object of type A, thereby getting an object of type B(a)." The notation "b(a_1, ..., a_n) will be preferred to b(a_1)...(a_n)." (Section 1.3)

The computation rule for application of a lambda abstraction is: (lambda x)b[x](a) = b[a], where b[a] denotes the result of substituting a for x in b[x]. (Section 1.3)

# Prerequisites

- **pi-type**: Application operates on objects of Pi type.
- **mathematical-object**: Both the function and argument must be mathematical objects of appropriate types.

# Key Properties

1. Application is the elimination rule for Pi types.
2. If b in (Pi x in A)B(x) and a in A, then b(a) in B(a).
3. The result type B(a) depends on the specific argument a -- this is the dependent aspect.
4. Multi-argument application b(a_1, ..., a_n) is preferred notation over iterated application.
5. The beta-reduction rule (lambda x)b[x](a) = b[a] governs computation of applied lambda abstractions.

# Construction / Recognition

## To Construct/Create:
1. Have a function b of type (Pi x in A)B(x).
2. Have an argument a of type A.
3. Form the application b(a), which has type B(a).

## To Identify/Recognize:
1. Application is denoted b(a) or b(a_1, ..., a_n).
2. It occurs whenever a function is given an argument.

# Context & Application

Application is the fundamental means of using (eliminating) functions in the theory. Together with lambda abstraction, it completes the introduction-elimination pair for Pi types. The dependent typing of application -- where b(a) has type B(a) depending on a -- is what gives dependent type theory its expressive power.

# Examples

From Section 1.3: If b is of type (Pi x in A)B(x) and a is of type A, then b(a) is of type B(a).

From Section 1.3: The computation rule: (lambda x)b[x](a) = b[a].

From Section 1.4: The inverse function has type (Pi z in R)(z != 0 -> R); applying it to a real number c yields a function of type (c != 0 -> R), and further applying to a proof p of c != 0 yields c^{-1} in R.

# Relationships

## Builds Upon
- pi-type: Application is the elimination rule for Pi types.

## Enables
- All computation in the theory proceeds through application (combined with other eliminators).

## Related
- lambda-abstraction: The introduction form dual to application.

## Contrasts With
- sigma-elimination: Application eliminates Pi types; E(c,d) and projections eliminate Sigma types.

# Common Errors

- **Error**: Applying a function to an argument of the wrong type.
  **Correction**: If b in (Pi x in A)B(x), the argument must be of type A. The result type B(a) depends on the specific argument.

# Common Confusions

- **Confusion**: Thinking application always yields results of a fixed type.
  **Clarification**: In the dependent case, b(a) has type B(a) which varies with a. Only in the non-dependent case (function type A -> B) is the result type fixed.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 1.3: Cartesian product of a family of types.

# Verification Notes

Confidence: high. Application is explicitly described in Section 1.3 with notation and the computation rule stated directly.
