---
# === CORE IDENTIFICATION ===
concept: Sigma-Introduction Rule
slug: sigma-introduction-rule

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
section: "2.3.5"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "pairing"
  - "Sigma-introduction"
  - "dependent pairing"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variable
  - type-formation-rules
  - sigma-type
extends: []
related:
  - sigma-elimination-rule
contrasts_with:
  - sigma-elimination-rule
  - pi-introduction-rule

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I form a pair (Sigma introduction)?"
  - "What distinguishes introduction rules from elimination rules?"
---

# Quick Definition

The Sigma-introduction rule (rule 2.3.5) states that pairing (a, b) produces a term of the Sigma type (Sigma x in A)B[x], given that a is a term of type A and b is a term of type B[a].

# Core Definition

Martin-Lof writes in Section 2.3.5: "Let x be a variable of type A and B[x] a type. Then, if a and b are terms of types A and B[a], respectively, (a,b) is a term of type (Sigma x in A)B[x]."

The Gentzen-style schema is:

```
  a in A    b in B[a]
  ──────────────────────────────
  (a,b) in (Sigma x in A)B[x]
```

The second component b must have type B[a] -- the type family B evaluated at the first component a. This is the dependent character of Sigma: the type of the second component depends on the value of the first.

# Prerequisites

- variable: The Sigma type is formed with a variable x of type A.
- type-formation-rules: The Sigma type (Sigma x in A)B[x] must be well-formed (rule 2.2.3).
- disjoint-union-of-a-family-of-types: The informal explanation from Chapter 1.

# Key Properties

1. This is the sole introduction rule for Sigma types.
2. The pair (a, b) is the canonical form of a Sigma type.
3. The type of the second component b depends on the value of the first component a: b must have type B[a], not just B[x] for arbitrary x.
4. When B does not depend on x, the Sigma type is the Cartesian product A x B, and pairing is ordinary (non-dependent) pairing.
5. The corresponding contraction rule is: E((a,b), (lambda x)(lambda y)d[x,y]) contr d[a,b].

# Construction / Recognition

## To Form a Pair:
1. Identify the Sigma type (Sigma x in A)B[x].
2. Construct a term a of type A (the first component).
3. Construct a term b of type B[a] (the second component, whose type depends on a).
4. Form (a, b); this is a term of type (Sigma x in A)B[x].

## To Recognize:
A term of the form (t, u) is a pair and was introduced by Sigma-introduction.

# Context & Application

Sigma-introduction formalizes the construction of dependent pairs. In the propositions-as-types reading, it corresponds to existential introduction: to prove (exists x in A)B(x), provide a witness a in A together with a proof b of B(a). The pair (a, b) is then a proof of the existential proposition.

In the non-dependent case, it reduces to ordinary pairing for conjunction: a proof of A & B is a pair of a proof of A and a proof of B.

# Examples

If a is a term of type N and b is a term of type B[a] (e.g., a proof that a is prime), then (a, b) is a term of type (Sigma x in N)B[x] -- a number together with a proof that it satisfies property B.

In the non-dependent case: if a is a term of type A and b is a term of type B, then (a, b) is a term of type A x B.

# Relationships

## Builds Upon
- disjoint-union-of-a-family-of-types: The Sigma type is the target type.
- variable, type-formation-rules: Required for the Sigma type to be well-formed.

## Enables
- sigma-elimination-rule: Pairs produced by Sigma-introduction are consumed by Sigma-elimination.

## Contrasts With
- sigma-elimination-rule: Introduction constructs pairs; elimination decomposes them.
- pi-introduction-rule: Pi-introduction builds functions; Sigma-introduction builds pairs.

# Common Errors

- **Error**: Giving the second component a type B[x] for an arbitrary x rather than B[a] for the specific first component a.
  **Correction**: The second component's type must be B[a], where a is the actual first component of the pair.

# Common Confusions

- **Confusion**: Thinking of (a, b) as an unordered set.
  **Clarification**: The pair is ordered: a is the first component (of type A) and b is the second (of type B[a]). The type of b depends on the value of a.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 2.3.5: Sigma-introduction or pairing.

# Verification Notes

Confidence: high. Rule 2.3.5 is explicitly stated.
