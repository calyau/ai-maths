---
# === CORE IDENTIFICATION ===
concept: Pi-Introduction Rule
slug: pi-introduction-rule

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
section: "2.3.3"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "lambda-abstraction"
  - "Pi-introduction"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variable
  - type-formation-rules
  - pi-type
extends:
  - lambda-abstraction
related:
  - pi-elimination-rule
  - function-type
contrasts_with:
  - pi-elimination-rule

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I construct a function (lambda abstraction)?"
  - "What distinguishes introduction rules from elimination rules?"
---

# Quick Definition

The Pi-introduction rule (rule 2.3.3) states that lambda-abstraction (lambda x)b[x] produces a term of the Pi type (Pi x in A)B[x], given that b[x] is a term of type B[x] for variable x of type A.

# Core Definition

Martin-Lof writes in Section 2.3.3: "If x is a variable of type A and b[x] is a term of type B[x], then (lambda x)b[x] is a term of type (Pi x in A)B[x]."

The Gentzen-style schema is:

```
  x in A
  b[x] in B[x]
  ─────────────────────────────
  (lambda x)b[x] in (Pi x in A)B[x]
```

The variable x is bound by the lambda; all free occurrences of x in b[x] become bound in (lambda x)b[x]. The notational convention from Section 2.1 ensures that the variable restrictions are satisfied: no free variable in b[x] or B[x] has a type depending on x (other than those explicitly exhibited).

# Prerequisites

- variable: The rule binds a variable x of type A.
- type-formation-rules: The Pi type (Pi x in A)B[x] must be well-formed (rule 2.2.2).
- cartesian-product-of-a-family-of-types: The informal explanation of Pi types from Chapter 1.

# Key Properties

1. This is the sole introduction rule for Pi types -- the only way to construct a term of a Pi type from scratch.
2. Lambda-abstraction binds the variable x, turning a term b[x] that depends on x into a function (lambda x)b[x] that takes an argument.
3. When B does not depend on x, the Pi type degenerates to the function type A -> B, and lambda-abstraction produces an ordinary (non-dependent) function.
4. The corresponding contraction rule is: (lambda x)b[x](a) contr b[a] -- applying a lambda-abstraction to an argument substitutes the argument for the bound variable.

# Construction / Recognition

## To Construct a Function:
1. Declare a variable x of type A.
2. Construct a term b[x] of type B[x], possibly using x.
3. Form (lambda x)b[x]; this is a term of type (Pi x in A)B[x].

## To Recognize:
A term of the form (lambda x)e is a lambda-abstraction and was introduced by Pi-introduction.

# Context & Application

Pi-introduction formalizes the informal notion of function construction described in Section 1.5: "a function from A to the family of types B(x), x in A, is defined by prescribing how the value b(a) depends on the argument a in A." The formal rule makes this precise: one specifies b[x] for an arbitrary x of type A, then abstracts over x.

In the propositions-as-types reading, Pi-introduction corresponds to the rule of universal generalization: to prove (forall x in A)B(x), assume x in A and derive a proof b[x] of B(x), then (lambda x)b[x] is the proof.

# Examples

If x is a variable of type N and b[x] = s(x) is a term of type N, then (lambda x)s(x) is a term of type N -> N (the successor function).

If x is a variable of type A and b[x] = x is a term of type A, then (lambda x)x is a term of type A -> A (the identity function).

# Relationships

## Builds Upon
- variable: The rule binds a variable.
- cartesian-product-of-a-family-of-types: The Pi type is the target type.

## Enables
- pi-elimination-rule: Functions produced by Pi-introduction are consumed by Pi-elimination (application).

## Related
- lambda-abstraction: The informal counterpart from Chapter 1.
- function-type: The non-dependent special case A -> B.

## Contrasts With
- pi-elimination-rule: Introduction constructs functions; elimination applies them.

# Common Errors

- **Error**: Forgetting that the variable x in (lambda x)b[x] must be of a declared type A.
  **Correction**: Lambda-abstraction always involves a typed variable; the type A determines the domain of the resulting function.

- **Error**: Attempting to abstract over a variable that violates the variable restrictions.
  **Correction**: Ensure no free variable in b[x] or B[x] has a type depending on x (beyond the variables explicitly parameterized).

# Common Confusions

- **Confusion**: Confusing (lambda x)b[x] as a "definition" rather than a term.
  **Clarification**: (lambda x)b[x] is a term of a specific type -- it is a first-class mathematical object, not merely a notational device.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 2.3.3: Pi-introduction or lambda-abstraction.

# Verification Notes

Confidence: high. Rule 2.3.3 is explicitly stated and the corresponding Gentzen schema is given later in Section 2.3.
