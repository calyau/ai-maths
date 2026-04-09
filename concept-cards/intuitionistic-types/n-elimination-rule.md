---
# === CORE IDENTIFICATION ===
concept: N-Elimination Rule
slug: n-elimination-rule

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
section: "2.3.12"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "recursion"
  - "N-elimination"
  - "primitive recursion (formal)"
  - "R operator"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variable
  - type-formation-rules
  - n-introduction-rule
  - natural-numbers
  - primitive-recursion
extends:
  - primitive-recursion
related:
  - n-introduction-rule
contrasts_with:
  - n-introduction-rule

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define a function by recursion on natural numbers?"
  - "What distinguishes introduction rules from elimination rules?"
---

# Quick Definition

The N-elimination rule (rule 2.3.12) states that the R operator defines a function from natural numbers by recursion: given a base case d for 0 and a step case e[x,y] for s(x), R(c, d, (lambda x)(lambda y)e[x,y]) is a term of type C[c].

# Core Definition

Martin-Lof writes in Section 2.3.12: "Let x and y be variables of types N and C[x], respectively. Then, if c, d and e[x,y] are terms of types N, C[0] and C[s(x)], respectively, R(c, d, (lambda x)(lambda y)e[x,y]) is a term of type C[c]."

The Gentzen-style schema is:

```
  c in N    d in C[0]    e[x,y] in C[s(x)]
  ──────────────────────────────────────────────────
  R(c, d, (lambda x)(lambda y)e[x,y]) in C[c]
```

The contraction rules are:
- R(0, d, (lambda x)(lambda y)e[x,y]) contr d
- R(s(a), d, (lambda x)(lambda y)e[x,y]) contr e[a, R(a, d, (lambda x)(lambda y)e[x,y])]

# Prerequisites

- variable: Two variables x (of type N) and y (of type C[x]) appear in the step case.
- type-formation-rules: The type N and the motive C[x] must be well-formed.
- n-introduction-rule: The rule dispatches on the introduction forms 0 and s(a).
- natural-numbers, primitive-recursion: The informal explanations from Chapter 1.

# Key Properties

1. This is the sole elimination rule for N.
2. The motive C[x] specifies the result type, which may depend on the natural number x.
3. The base case d must have type C[0].
4. The step case e[x,y] must have type C[s(x)], where x has type N and y has type C[x] (the recursive result).
5. The variable y in the step case represents the result of the recursive call -- this is what makes R a primitive recursor.
6. The contraction rules show that R computes by recursion: the base case returns d, and the successor case applies e to the predecessor and the recursive result.

# Construction / Recognition

## To Define a Function by Recursion:
1. Choose a motive C[x] for x of type N.
2. Provide a base case d of type C[0].
3. Provide a step case e[x,y] of type C[s(x)], where x is the current number and y is the result for x.
4. Form R(c, d, (lambda x)(lambda y)e[x,y]) for any c of type N; this has type C[c].

## To Recognize:
A term of the form R(t, u, (lambda x)(lambda y)v) is an N-elimination (recursion).

# Context & Application

N-elimination formalizes the principle of definition by primitive recursion and, in the dependent case, mathematical induction. When C[x] does not depend on x, R defines an ordinary recursive function. When C[x] depends on x, R simultaneously defines a function and proves it has the desired type at each step -- this is induction.

In the propositions-as-types reading, N-elimination is the induction principle: to prove (forall x in N)C(x), prove C(0) and prove C(s(x)) assuming C(x).

# Examples

Addition: Define add(m, n) = R(m, n, (lambda x)(lambda y)s(y)).
- add(0, n) = R(0, n, ...) contr n.
- add(s(a), n) = R(s(a), n, ...) contr s(R(a, n, ...)) = s(add(a, n)).

The factorial function: Define fact(n) = R(n, s(0), (lambda x)(lambda y)mult(s(x), y)) where mult is defined by a separate recursion.

# Relationships

## Builds Upon
- n-introduction-rule: The recursion dispatches on 0 and s(a).
- primitive-recursion: The informal concept from Chapter 1.

## Enables
- Definition of all primitive recursive functions within the theory.
- Mathematical induction as a special case of dependent recursion.

## Contrasts With
- n-introduction-rule: Introduction builds natural numbers; elimination defines functions from them.

# Common Errors

- **Error**: Forgetting that y in the step case e[x,y] has type C[x], not type N.
  **Correction**: y represents the result of the recursive call on x, which has type C[x] (the motive at x), not type N.

- **Error**: Writing the step case with type C[x] instead of C[s(x)].
  **Correction**: The step case e[x,y] must produce a term of type C[s(x)] -- the motive at the successor.

# Common Confusions

- **Confusion**: Thinking R is limited to non-dependent (simple) recursion.
  **Clarification**: R handles dependent recursion (induction) because the motive C[x] can depend on x. Simple recursion is the special case where C is constant.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 2.3.12: N-elimination or recursion. Contraction rules in Section 2.4.2.

# Verification Notes

Confidence: high. Rule 2.3.12 is explicitly stated, and the contraction rules are given in Section 2.4.2.
