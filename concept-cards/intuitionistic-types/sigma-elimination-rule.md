---
# === CORE IDENTIFICATION ===
concept: Sigma-Elimination Rule
slug: sigma-elimination-rule

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
section: "2.3.6"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "E operator"
  - "Sigma-elimination"
  - "dependent pair elimination"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variable
  - type-formation-rules
  - sigma-introduction-rule
  - sigma-type
extends: []
related:
  - pi-elimination-rule
contrasts_with:
  - sigma-introduction-rule

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I eliminate a pair (Sigma elimination)?"
  - "What distinguishes introduction rules from elimination rules?"
---

# Quick Definition

The Sigma-elimination rule (rule 2.3.6) states that the E operator decomposes a term c of Sigma type by applying a function d[x,y] to its two components, yielding a term E(c, (lambda x)(lambda y)d[x,y]) of type C[c].

# Core Definition

Martin-Lof writes in Section 2.3.6: "Let x, y and z be variables of type A, B[x] and (Sigma x in A)B[x], respectively, and let C[z] be a type. Then, if c and d[x,y] are terms of types (Sigma x in A)B[x] and C[(x,y)], respectively, E(c,(lambda x)(lambda y)d[x,y]) is a term of type C[c]."

The Gentzen-style schema is:

```
  x in A    y in B[x]
  c in (Sigma x in A)B[x]    d[x,y] in C[(x,y)]
  ─────────────────────────────────────────────────
  E(c, (lambda x)(lambda y)d[x,y]) in C[c]
```

The E operator takes the pair c apart: assuming c = (a, b), it computes d[a, b]. The contraction rule is: E((a,b), (lambda x)(lambda y)d[x,y]) contr d[a,b].

# Prerequisites

- variable: Three variables (x, y, z) of specific types are used.
- type-formation-rules: The Sigma type and the motive type C[z] must be well-formed.
- sigma-introduction-rule: The term c was typically formed by pairing.
- disjoint-union-of-a-family-of-types: The informal explanation from Chapter 1.

# Key Properties

1. This is the sole elimination rule for Sigma types.
2. The "motive" C[z] specifies what type of result is desired, parameterized over the Sigma type.
3. The body d[x,y] must have type C[(x,y)] -- the motive evaluated at the pair formed from the hypothetical components x and y.
4. The result has type C[c], which depends on the specific pair c being eliminated.
5. The contraction rule E((a,b), (lambda x)(lambda y)d[x,y]) contr d[a,b] shows the computational content: substitute the actual components for x and y.
6. The left and right projections p(c) and q(c) are definable using E: p(c) = E(c, (lambda x)(lambda y)x) and q(c) = E(c, (lambda x)(lambda y)y).

# Construction / Recognition

## To Eliminate a Pair:
1. Identify c as a term of type (Sigma x in A)B[x].
2. Choose a motive C[z] -- the desired result type, parameterized by z of Sigma type.
3. Construct d[x,y] of type C[(x,y)], where x has type A and y has type B[x].
4. Form E(c, (lambda x)(lambda y)d[x,y]); this is a term of type C[c].

## To Recognize:
A term of the form E(t, (lambda x)(lambda y)u) is a Sigma-elimination.

# Context & Application

Sigma-elimination formalizes the principle that to use a dependent pair, one may assume it has the form (x, y) and work with the components. In the propositions-as-types reading, it corresponds to existential elimination: given a proof c of (exists x in A)B(x) and a derivation d[x,y] of C assuming x in A and y in B(x), one concludes C[c].

The E operator is more general than simple projections because the motive C[z] can depend on z, enabling dependent elimination. When C does not depend on z, it reduces to a simple "let (x,y) = c in d[x,y]" pattern.

# Examples

To extract the first component of a pair c in (Sigma x in A)B[x]:
- Set d[x,y] = x, so C[(x,y)] = A.
- Then p(c) = E(c, (lambda x)(lambda y)x) is a term of type A.

To extract the second component:
- Set d[x,y] = y, so C[(x,y)] = B[x].
- Then q(c) = E(c, (lambda x)(lambda y)y) is a term of type B[p(c)].

# Relationships

## Builds Upon
- sigma-introduction-rule: Elimination decomposes what introduction constructed.
- disjoint-union-of-a-family-of-types: The informal counterpart.

## Enables
- Projections p(c) and q(c) are definable via E.

## Related
- pi-elimination-rule: Another elimination rule, but for function types rather than pair types.

## Contrasts With
- sigma-introduction-rule: Introduction forms pairs; elimination decomposes them.

# Common Errors

- **Error**: Forgetting that d[x,y] must have type C[(x,y)], not just C[z] for some other z.
  **Correction**: The body of the elimination must be typed at the motive applied to the reconstructed pair (x,y).

# Common Confusions

- **Confusion**: Thinking Sigma-elimination is just projection.
  **Clarification**: The E operator is dependent elimination, which is strictly more general than projection. It allows the result type to depend on the pair being eliminated, which simple projection does not.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 2.3.6: Sigma-elimination.

# Verification Notes

Confidence: high. Rule 2.3.6 is explicitly stated with all typing conditions.
