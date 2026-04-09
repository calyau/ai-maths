---
# === CORE IDENTIFICATION ===
concept: Plus-Elimination Rule
slug: plus-elimination-rule

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
section: "2.3.8"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "definition by cases"
  - "+-elimination"
  - "D operator"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variable
  - type-formation-rules
  - disjoint-union-of-two-types
extends:
  - definition-by-cases
related:
  - plus-introduction-rule
  - canonical-injections
contrasts_with:
  - plus-introduction-rule

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define a function by cases on A + B?"
  - "What distinguishes introduction rules from elimination rules?"
---

# Quick Definition

The +-elimination rule (rule 2.3.8) states that the D operator defines a function by cases on a term c of type A + B, applying one branch to the left injection and another to the right injection.

# Core Definition

Martin-Lof writes in Section 2.3.8: "Let x, y and z be variables of types A, B and A + B, respectively, and let C[z] be a type. Then, if c, d[x] and e[y] are terms of types A + B, C[i(x)] and C[j(y)], respectively, D(c, (lambda x)d[x], (lambda y)e[y]) is a term of type C[c]."

The term D(c, (lambda x)d[x], (lambda y)e[y]) performs case analysis: if c = i(a) (left injection), the result is d[a]; if c = j(b) (right injection), the result is e[b].

The contraction rules are:
- D(i(a), (lambda x)d[x], (lambda y)e[y]) contr d[a]
- D(j(b), (lambda x)d[x], (lambda y)e[y]) contr e[b]

# Prerequisites

- variable: Three variables (x, y, z) of types A, B, and A + B.
- type-formation-rules: The type A + B must be well-formed (rule 2.2.4).
- disjoint-union-of-two-types: The informal explanation from Chapter 1.

# Key Properties

1. This is the sole elimination rule for the + type.
2. The motive C[z] specifies the result type, parameterized by z of type A + B.
3. Two branches must be provided: d[x] of type C[i(x)] for the left case, and e[y] of type C[j(y)] for the right case.
4. The result has type C[c], which can depend on c.
5. The two contraction rules express the computational content: D dispatches to the appropriate branch based on whether the argument is a left or right injection.

# Construction / Recognition

## To Define a Function by Cases:
1. Identify c as a term of type A + B.
2. Choose a motive C[z] for z of type A + B.
3. For the left case: construct d[x] of type C[i(x)], where x has type A.
4. For the right case: construct e[y] of type C[j(y)], where y has type B.
5. Form D(c, (lambda x)d[x], (lambda y)e[y]); this is a term of type C[c].

## To Recognize:
A term of the form D(t, (lambda x)u, (lambda y)v) is a +-elimination (definition by cases).

# Context & Application

+-elimination formalizes proof by cases (disjunction elimination) in the propositions-as-types reading. Given a proof c of A v B, a derivation d[x] of C from A, and a derivation e[y] of C from B, one concludes C. The D operator is the formal counterpart of the informal "definition by cases" described in Section 1.8.

# Examples

To define a function from A + B to C (where C does not depend on z): provide d[x] of type C for x in A and e[y] of type C for y in B. Then D(c, (lambda x)d[x], (lambda y)e[y]) is a term of type C.

For the swap function from A + B to B + A: set d[x] = j(x) and e[y] = i(y). Then D(c, (lambda x)j(x), (lambda y)i(y)) swaps the injection.

# Relationships

## Builds Upon
- disjoint-union-of-two-types: The + type being eliminated.
- canonical-injection: The introduction forms i(a) and j(b) that D dispatches on.

## Related
- plus-introduction-rule: Elimination consumes what introduction produced.
- definition-by-cases: The informal counterpart from Chapter 1.

## Contrasts With
- plus-introduction-rule: Introduction injects into A + B; elimination dispatches out of A + B.

# Common Errors

- **Error**: Providing branches d[x] and e[y] whose types do not match the motive at i(x) and j(y).
  **Correction**: d[x] must have type C[i(x)] and e[y] must have type C[j(y)], not merely C.

# Common Confusions

- **Confusion**: Thinking D "inspects" the injection tag at runtime.
  **Clarification**: D is a term-formation rule, not a runtime operation. The contraction rules define how D computes when the argument is a canonical injection.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 2.3.8: +-elimination or definition by cases.

# Verification Notes

Confidence: high. Rule 2.3.8 is explicitly stated with all typing conditions, and the contraction rules are given in Section 2.4.2.
