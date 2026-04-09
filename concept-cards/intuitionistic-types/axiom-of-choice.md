---
# === CORE IDENTIFICATION ===
concept: Axiom of Choice (in Type Theory)
slug: axiom-of-choice

# === CLASSIFICATION ===
category: reduction-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "An Intuitionistic Theory of Types"
source_slug: intuitionistic-types
authors: "Per Martin-Lof"
chapter: "Formalization of an Intuitionistic Theory of Types"
chapter_number: 2
pdf_page: 9
section: "2.5"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "AC"
  - "type-theoretic axiom of choice"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sigma-elimination
  - pi-elimination-rule
extends: []
related:
  - translation-of-finite-type-arithmetic
  - translation-of-arithmetical-analysis
contrasts_with:
  - law-of-excluded-middle

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the axiom of choice relate to the Sigma and Pi types?"
  - "What distinguishes the intuitionistic axiom of choice from its classical counterpart?"
---

# Quick Definition

The axiom of choice is not an axiom in the theory of types but a theorem: Martin-Lof constructs an explicit closed term inhabiting the type (Pi x in A)(Sigma y in B[x])C[x,y] -> (Sigma f in (Pi x in A)B[x])(Pi x in A)C[x,f(x)].

# Core Definition

Section 2.5 constructs the proof term explicitly. Given variables x of type A, y of type B[x], and a type C[x,y], the axiom of choice states that from a function producing dependent pairs, one can extract a choice function and a proof that it satisfies the property.

The proof term is: (lambda z)((lambda x)p[z(x)], (lambda x)q[z(x)])

where p[c] = E(c, (lambda x)(lambda y)x) and q[c] = E(c, (lambda x)(lambda y)y) are the left and right projections satisfying p[(a,b)] contr a and q[(a,b)] contr b.

The construction proceeds as follows:
1. Given z of type (Pi x in A)(Sigma y in B[x])C[x,y], apply Pi-elimination to get z(x) of type (Sigma y in B[x])C[x,y].
2. Project: p[z(x)] of type B[x] and q[z(x)] of type C[x, p[z(x)]].
3. Lambda-abstract over x to get (lambda x)p[z(x)] of type (Pi x in A)B[x] -- this is the choice function.
4. Similarly, (lambda x)q[z(x)] of type (Pi x in A)C[x, (lambda x)p[z(x)](x)] -- this is the proof the choice function works.
5. Pair and lambda-abstract over z to complete the proof.

# Prerequisites

- sigma-elimination: The projections p and q are instances of Sigma-elimination.
- pi-elimination: Application z(x) is Pi-elimination.

# Key Properties

1. The axiom of choice is PROVABLE in the theory of types -- it is a theorem, not an axiom.
2. The proof is entirely constructive: it gives an explicit choice function.
3. The proof works because Sigma types carry witnesses: an element of (Sigma y in B[x])C[x,y] is a pair (y, c) where y is the witness and c is the proof.
4. The key type conversion step uses the fact that q[z(x)] has type C[x, p[z(x)]] which converts to C[x, (lambda x)p[z(x)](x)] since (lambda x)p[z(x)](x) contr p[z(x)].
5. This result is used in sections 3.3 and 3.4 to translate the axiom of choice from finite-type arithmetic and arithmetical analysis.

# Construction / Recognition

## The Proof Term:
(lambda z)((lambda x)p[z(x)], (lambda x)q[z(x)])

where p[c] = E(c, (lambda x)(lambda y)x) and q[c] = E(c, (lambda x)(lambda y)y).

# Context & Application

The provability of the axiom of choice is one of the most striking features of Martin-Lof's type theory. In classical set theory, the axiom of choice is independent of ZF and highly non-constructive. In type theory, it is trivially provable because the existential quantifier (Sigma type) inherently carries a witness.

This difference is fundamental: in classical logic, "there exists y such that C[x,y]" merely asserts existence; in type theory, an element of (Sigma y in B[x])C[x,y] is an actual pair containing the witness y. Extracting these witnesses into a function is straightforward.

# Examples

Simple instance: If for every natural number n there exists a natural number m with P(n,m), then there is a function f: N -> N such that P(n, f(n)) for all n.

The proof term: given z witnessing the hypothesis, the choice function is (lambda n)p[z(n)] and the proof is (lambda n)q[z(n)].

# Relationships

## Builds Upon
- sigma-elimination: The projections p and q.
- pi-elimination: Function application.

## Enables
- translation-of-finite-type-arithmetic: The AC of finite-type arithmetic (3.3) is an instance.
- translation-of-arithmetical-analysis: The AC of analysis (3.4) is an instance.

## Contrasts With
- law-of-excluded-middle: While AC is provable, the law of excluded middle is NOT consistent relative to the theory (3.3.3).

# Common Errors

- **Error**: Treating the axiom of choice as an additional axiom that must be postulated.
  **Correction**: In type theory, it is a theorem with an explicit proof term. No additional axiom is needed.

# Common Confusions

- **Confusion**: Why is AC trivial here but controversial in set theory?
  **Clarification**: The difference lies in the meaning of "exists." In type theory, existence (Sigma type) is inherently witnessed -- an element of (Sigma y in B)C[y] literally contains a y. In classical set theory, existence is merely a truth value, and extracting witnesses requires the axiom of choice.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 2.5: Axiom of choice.

# Verification Notes

Confidence: high. The full proof term is constructed explicitly in 2.5 with every step justified.
