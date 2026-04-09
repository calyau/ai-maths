---
# === CORE IDENTIFICATION ===
concept: Cartesian Product of a Family of Types (Pi Type)
slug: pi-type

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
  - "Pi type"
  - "dependent function type"
  - "dependent product"
  - "cartesian product of a family of types"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type
  - mathematical-object
extends: []
related:
  - lambda-abstraction
  - application
  - function-type
  - universal-quantification
contrasts_with:
  - sigma-type
  - function-type

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Cartesian product (Pi type) of a family of types?"
  - "How does universal quantification relate to the Pi type?"
  - "What distinguishes the Pi type from the Sigma type?"
  - "What distinguishes the function type A -> B from the Pi type?"
  - "What must I know before understanding dependent types?"
---

# Quick Definition

The Pi type (Pi x in A)B(x) is the type of functions that take an arbitrary object a of type A into an object of type B(a), where the result type may depend on the argument.

# Core Definition

Martin-Lof writes: "Suppose now that A is a type and that B is a function, rule or method which to an arbitrary object a of type A assigns a type B(a). Then the cartesian product (Pi x in A)B(x) is a type, namely the type of functions which take an arbitrary object a of type A into an object of type B(a)." (Section 1.3)

Application: "we may apply an object b of type (Pi x in A)B(x) to an object of type A, thereby getting an object of type B(a)." (Section 1.3)

The non-dependent special case: "If B(a) is defined to be one and the same type B for every object a of type A, then (Pi x in A)B(x) will be abbreviated A -> B." (Section 1.3)

# Prerequisites

- **type**: The Pi type is a type, and both A and B(x) must be types.
- **mathematical-object**: Objects of Pi type are functions; the argument and result are mathematical objects.

# Key Properties

1. The result type B(a) may depend on the argument a -- this is what makes it a *dependent* function type.
2. Objects of the Pi type are functions from A to the family B.
3. Application of b in (Pi x in A)B(x) to a in A yields b(a) in B(a).
4. The notation b(a_1, ..., a_n) is preferred to b(a_1)...(a_n).
5. When B does not depend on x, the Pi type reduces to the ordinary function type A -> B.

# Construction / Recognition

## To Construct/Create:
1. Specify a type A (the domain).
2. Specify a type-valued function B that assigns to each a in A a type B(a) (the family of codomains).
3. The Pi type (Pi x in A)B(x) is then formed.
4. To construct an *object* of this type, use lambda abstraction: (lambda x)b[x].

## To Identify/Recognize:
1. A Pi type is present when a type is described as "functions from A to a family B(x) depending on x."
2. Notation: (Pi x in A)B(x).
3. Special case: A -> B when B does not depend on x.

# Context & Application

The Pi type is the first and most fundamental type-forming operation in Martin-Lof's theory. It generalizes the ordinary function type to allow the codomain to depend on the argument. This dependence is the essence of dependent types and is what enables the type-theoretic representation of universal quantification.

# Examples

From Section 1.3: If B(a) represents a proposition for every a in A, then (Pi x in A)B(x) represents the universal proposition (forall x in A)B(x). "A proof of (forall x in A)B(x) is a function which to an arbitrary object a of type A assigns a proof of B(a)."

From Section 1.4: The inverse function on reals has type (Pi z in R)(z != 0 -> R), a Pi type where the inner function type depends on z.

# Relationships

## Builds Upon
- type, mathematical-object

## Enables
- lambda-abstraction: The introduction form for Pi types.
- application: The elimination form for Pi types.
- universal-quantification: The logical reading of the Pi type.
- function-type: The non-dependent special case.

## Related
- implication: When A and B are both propositions and B does not depend on x, A -> B represents A supset B.

## Contrasts With
- sigma-type: Pi type is "for all x, B(x)" (functions); Sigma type is "there exists x, B(x)" (pairs). Pi collects functions over a family; Sigma collects pairs.
- function-type: A -> B is the special case where B does not depend on the argument. The general Pi type allows dependency.

# Common Errors

- **Error**: Confusing the Pi type with the Sigma type because both involve a family B(x) over A.
  **Correction**: The Pi type is the type of *functions* (for each a in A, an element of B(a)). The Sigma type is the type of *pairs* (some a in A together with an element of B(a)).

# Common Confusions

- **Confusion**: Thinking "Cartesian product" here means the same as the binary product A x B.
  **Clarification**: The name "Cartesian product of a family of types" refers to the generalized product over an indexed family {B(a) : a in A}, analogous to the set-theoretic product of a family of sets. The binary product A x B is a special case of the *Sigma* type, not the Pi type.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 1.3: Cartesian product of a family of types.

# Verification Notes

Confidence: high. The Pi type is explicitly defined in Section 1.3 with clear notation and explanation. The non-dependent special case and logical interpretation are stated directly.
