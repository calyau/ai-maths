---
# === CORE IDENTIFICATION ===
concept: Normal Term Structure
slug: normal-term-structure

# === CLASSIFICATION ===
category: normalization
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "An Intuitionistic Theory of Types"
source_slug: intuitionistic-types
authors: "Per Martin-Lof"
chapter: "The Normalization Theorem and Its Consequences"
chapter_number: 4
pdf_page: 34
section: "4.4"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "canonical forms"
  - "form of normal terms"
  - "canonical forms table"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normalization-theorem
  - introduction-form-vs-elimination-form
  - major-subterm
  - main-redex
extends: []
related:
  - mechanical-computability
  - decidability-of-definitional-equality
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes introduction rules from elimination rules?"
---

# Quick Definition

In the system without object constants, every closed normal term has introduction form. This determines a precise table: closed normal terms of Pi type must be lambdas, of Sigma type must be pairs, of sum type must be injections, and so on.

# Core Definition

Martin-Lof establishes the following result by "purely combinatorial reasoning" (Section 4.4):

"a normal term must either have introduction form or contain a constant or a free variable."

In the system without object constants, for closed terms this simplifies to: every closed normal term has introduction form. The complete table is:

| A closed normal term of type | must have the form |
|---|---|
| (Pi x in A) B[x] | (lambda x)b[x] |
| (Sigma x in A) B[x] | (a, b) |
| A + B | i(a) or j(b) |
| N_n | 1, 2, ..., or n |
| N | s(s(...s(0)...)) |
| V | (Pi x in A)B[x], (Sigma x in A)B[x], A+B, N_0, N_1, ..., or N |

Martin-Lof then notes: "Combining this with the normalization theorem, we can conclude that a closed term of one of the types shown in the left column reduces to a term of the form exhibited on the same line in the right column."

# Prerequisites

- **normalization-theorem**: Guarantees that normal forms exist for all terms.
- **introduction-form-vs-elimination-form**: The structural classification that the analysis depends on.
- **major-subterm**, **main-redex**: The technical tools used in the proof.

# Key Properties

1. The argument is purely combinatorial (syntactic), independent of the normalization theorem itself.
2. It relies on the observation that in a closed term without constants, tracing the major subterm chain of an elimination-form term must eventually reach a variable or constant -- but closed constant-free terms have neither available, so the term must contain a main redex, contradicting normality.
3. The key fact enabling this: "when we form a term of elimination form no free variable in its major subterm can become bound" (Section 4.4).
4. Combined with normalization, this gives a "canonical forms" result: every closed term computes to a value of the expected shape.

# Construction / Recognition

## To Determine the Form of a Closed Normal Term of Type A:
1. Consult the table above based on the type A.
2. The term must be one of the listed forms.
3. Its subterms are themselves normal terms of the appropriate subtypes.

## Why Elimination Form Is Impossible:
1. Suppose a closed normal term t (no constants) has elimination form.
2. Trace the major subterm chain: major(t), major(major(t)), ...
3. This chain must terminate at a constant or free variable (since it cannot hit an introduction form in a normal term).
4. But t is closed and has no constants -- contradiction.
5. Therefore t must have introduction form.

# Context & Application

This result is one of the most important consequences of normalization. It tells us that the type system is "canonical": every closed term of a given type computes to a value whose outermost form is determined by the type. This is the type-theoretic analogue of the fact that every natural number is either zero or a successor, every function value is a lambda, etc.

The canonical forms property is essential for:
- Proving that number theoretic functions are mechanically computable (Section 4.5).
- Understanding the computational content of proofs.
- Connecting the type theory to programming language semantics (canonical forms lemmas in modern PL theory).

# Examples

- A closed term of type N -> N normalizes to (lambda x)b[x] where b[x] is normal.
- A closed term of type N normalizes to s(s(...s(0)...)) -- a numeral.
- A closed term of type A x B (= (Sigma x in A)B where B does not depend on x) normalizes to (a, b).
- A closed term of type V normalizes to one of the type formers: a Pi type, Sigma type, sum type, or finite/natural number type.

# Relationships

## Builds Upon
- normalization-theorem: Provides the existence of normal forms.
- introduction-form-vs-elimination-form, major-subterm, main-redex: The syntactic machinery for the proof.

## Enables
- mechanical-computability: Number-theoretic functions yield numerals, so they are mechanically computable.
- decidability-of-definitional-equality: Normal forms have predictable structure, facilitating comparison.

# Common Errors

- **Error**: Assuming the canonical forms result holds in the presence of object constants.
  **Correction**: With object constants, a closed normal term of elimination form is possible (e.g., f(a) where f is a constant). The table applies only to the system without object constants.

# Common Confusions

- **Confusion**: Thinking the canonical forms table is trivial from the typing rules.
  **Clarification**: The typing rules allow forming terms of elimination form at any type. The non-trivial content is that after normalization, only introduction forms survive in the closed constant-free case.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 4.4: The form of the normal terms.

# Verification Notes

Confidence: high. The table and the reasoning are presented explicitly in Section 4.4.
