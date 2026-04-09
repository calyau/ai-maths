---
# === CORE IDENTIFICATION ===
concept: Equality Type (for Natural Numbers)
slug: equality-type

# === CLASSIFICATION ===
category: translations
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "An Intuitionistic Theory of Types"
source_slug: intuitionistic-types
authors: "Per Martin-Lof"
chapter: "Reduction of Some Other Formal Theories to the Theory of Types"
chapter_number: 3
pdf_page: 24
section: "3.2.2.1.6"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "E(a,b)"
  - "decidable equality on N"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - natural-numbers
  - primitive-recursion
  - universe
extends: []
related:
  - translation-of-first-order-arithmetic
  - conversion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does first order arithmetic embed into the theory of types?"
---

# Quick Definition

The equality type E(a,b) for natural numbers is a type defined by double recursion that is inhabited (equivalent to top) when a and b are equal numerals, and empty (equivalent to bottom) when they differ. It translates numerical equations a = b into types.

# Core Definition

Section 3.2.2.1.6 defines E(a,b) as:

R(a, (lambda z)R(z, top, (lambda x)(lambda y)bottom), (lambda u)(lambda v)(lambda z)R(z, bottom, (lambda x)(lambda y)v(x)))(b)

This is a term of type V (by the reflection principle, using the axioms bottom in V and top in V), and hence E(a,b) is a type. It satisfies the reduction schema:

- E(0, 0) red top
- E(s(a), 0) red bottom
- E(0, s(b)) red bottom
- E(s(a), s(b)) red E(a, b)

This is a double recursion: the outer recursion is on a, and for each case the inner recursion is on b.

# Prerequisites

- natural-numbers: E(a,b) is defined for terms of type N.
- primitive-recursion: The definition uses the recursion operator R twice (nested).
- universe: E(a,b) is a term of type V, so it is a small type. The axioms bottom in V and top in V (part of the reflection principle) are needed.

# Key Properties

1. E(a,b) is a small type (an element of V).
2. For numerals, E reduces to either top (N_1) or bottom (N_0), making equality decidable.
3. The definition works by peeling off successors simultaneously: E(s(a), s(b)) reduces to E(a,b).
4. The four reduction cases correspond exactly to the four equality axioms of Peano arithmetic:
   - 0 = 0 is true
   - s(a) = 0 is false
   - 0 = s(b) is false
   - s(a) = s(b) iff a = b
5. Composite formulae involving equality are then translated using the standard connective mapping.

# Construction / Recognition

## To Construct:
Apply the double-recursion definition above to terms a, b of type N.

## To Recognize:
E(a,b) is the unique type-valued function on N x N that satisfies the four reduction rules above.

# Context & Application

The equality type is the key technical device for translating first order arithmetic into the theory of types. Without it, there would be no type-theoretic counterpart of numerical equations. The definition exploits the universe V and the reflection principle: since top and bottom are both in V, and V is closed under the type-forming operations, the recursion can build a type-valued function.

Note that this is a "propositional" equality specific to natural numbers, defined by recursion. It is distinct from the general notion of definitional equality (conversion) and from identity types in later versions of Martin-Lof's type theory.

# Examples

- E(0, 0) reduces to top (= N_1), which has the element 1. So 0 = 0 is provable.
- E(s(0), 0) reduces to bottom (= N_0), which has no elements. So 1 = 0 is refutable.
- E(s(s(0)), s(s(0))) reduces to E(s(0), s(0)) reduces to E(0, 0) reduces to top. So 2 = 2 is provable.

# Relationships

## Builds Upon
- natural-numbers: Domain of E.
- primitive-recursion: E is defined by nested R.
- universe: E(a,b) lives in V.

## Enables
- translation-of-first-order-arithmetic: E(a,b) provides the translation of numerical equations.

# Common Errors

- **Error**: Confusing E(a,b) with a general identity type.
  **Correction**: E(a,b) is specific to natural numbers and is defined by recursion. It is not the general intensional or extensional identity type of later type theories.

# Common Confusions

- **Confusion**: Why is double recursion needed?
  **Clarification**: Single recursion on a alone would give a function from N to types, but equality requires comparing two numbers. The outer recursion on a produces, for each a, a function that takes b and returns a type, and this inner function is itself defined by recursion on b (via the inner R).

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 3.2.2.1.6.

# Verification Notes

Confidence: high. The definition and its four reduction rules are given explicitly in 3.2.2.1.6.
