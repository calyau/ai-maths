---
# === CORE IDENTIFICATION ===
concept: Pi-Elimination Rule
slug: pi-elimination-rule

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
section: "2.3.4"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "application"
  - "Pi-elimination"
  - "function application"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variable
  - type-formation-rules
  - pi-type
  - pi-introduction-rule
extends:
  - application
related:
  - function-type
contrasts_with:
  - pi-introduction-rule

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I apply a function (Pi elimination)?"
  - "What distinguishes introduction rules from elimination rules?"
---

# Quick Definition

The Pi-elimination rule (rule 2.3.4) states that applying a term b of Pi type (Pi x in A)B[x] to an argument a of type A yields a term b(a) of type B[a].

# Core Definition

Martin-Lof writes in Section 2.3.4: "If a and b are terms of types A and (Pi x in A)B[x], respectively, then b(a) is a term of type B[a]."

The Gentzen-style schema is:

```
  b in (Pi x in A)B[x]    a in A
  ─────────────────────────────────
  b(a) in B[a]
```

The result type B[a] is obtained by substituting the argument a for x in the dependent type B[x]. This is the key feature of dependent function application: the output type depends on the input value.

# Prerequisites

- variable: The rule substitutes a term for a variable in the result type.
- type-formation-rules: The Pi type (Pi x in A)B[x] must be well-formed.
- cartesian-product-of-a-family-of-types: The informal explanation from Chapter 1.
- pi-introduction-rule: Typically the function b was constructed by lambda-abstraction.

# Key Properties

1. This is the sole elimination rule for Pi types.
2. The result type B[a] depends on the argument a -- this is the hallmark of dependent types.
3. When B does not depend on x, the result type is simply B regardless of the argument, recovering ordinary function application.
4. The corresponding contraction rule is: (lambda x)b[x](a) contr b[a] -- applying a lambda-abstraction substitutes the argument for the bound variable.

# Construction / Recognition

## To Apply a Function:
1. Confirm that b is a term of type (Pi x in A)B[x].
2. Confirm that a is a term of type A (the domain).
3. Form b(a); this is a term of type B[a].

## To Recognize:
A term of the form f(t) is an application and was produced by Pi-elimination.

# Context & Application

Pi-elimination formalizes function application. In the propositions-as-types reading, it corresponds to universal instantiation: from a proof b of (forall x in A)B(x) and a term a in A, one obtains a proof b(a) of B(a). The dependent character means the proposition proved depends on the specific witness a.

The contraction (lambda x)b[x](a) contr b[a] is the computational content: applying a function to an argument computes by substitution (beta-reduction).

# Examples

If f is a term of type N -> N (a non-dependent function) and n is a term of type N, then f(n) is a term of type N.

If b is a term of type (Pi x in A)B[x] and a is a term of type A, then b(a) is a term of type B[a]. For instance, if B[x] is the type "x is even," then b(a) is a proof that a is even.

# Relationships

## Builds Upon
- pi-introduction-rule: Typically the function was constructed by lambda-abstraction.
- cartesian-product-of-a-family-of-types: Application operates on Pi types.

## Enables
- Computation via the contraction rule: (lambda x)b[x](a) contr b[a].

## Related
- application: The informal counterpart from Chapter 1.
- function-type: The non-dependent special case.

## Contrasts With
- pi-introduction-rule: Introduction builds functions; elimination applies them.

# Common Errors

- **Error**: Applying a term of Pi type to an argument of the wrong type.
  **Correction**: The argument a must be a term of type A, the domain of the Pi type.

- **Error**: Forgetting that the result type depends on the argument.
  **Correction**: The result of b(a) has type B[a], not B. The substitution of a for x in B[x] is essential.

# Common Confusions

- **Confusion**: Thinking application "evaluates" or "reduces" the function.
  **Clarification**: Application is a rule of term formation; it produces a new term b(a). Reduction (contraction) is a separate operation that applies when b has the form (lambda x)c[x].

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 2.3.4: Pi-elimination or application.

# Verification Notes

Confidence: high. Rule 2.3.4 is explicitly stated with its Gentzen schema.
