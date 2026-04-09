---
# === CORE IDENTIFICATION ===
concept: N-Introduction Rule
slug: n-introduction-rule

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
section: "2.3.11"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Peano's axioms (formal)"
  - "N-introduction"
  - "natural number introduction"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-formation-rules
  - natural-numbers
extends:
  - natural-numbers
  - successor-function
related:
  - n-elimination-rule
contrasts_with:
  - n-elimination-rule
  - finite-type

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes introduction rules from elimination rules?"
---

# Quick Definition

The N-introduction rule (rule 2.3.11) formalizes Peano's first and second axioms: 0 is a term of type N, and if a is a term of type N then s(a) is a term of type N.

# Core Definition

Martin-Lof writes in Section 2.3.11: "0 is a term of type N. If a is a term of type N, so is s(a). A term of type N which has the form s(s(...s(0)...)) is called a *numeral*."

The Gentzen-style schemata are:

```
                    a in N
  ──────────        ──────────
  0 in N            s(a) in N
```

These two rules correspond to Peano's first axiom (0 is a natural number) and second axiom (the successor of a natural number is a natural number).

# Prerequisites

- type-formation-rules: N must be recognized as a type (it is a term of V by rule 2.3.13, hence a small type).
- natural-numbers: The informal explanation from Chapter 1.

# Key Properties

1. The two introduction forms are 0 (zero) and s(a) (successor).
2. Every canonical term of type N is a numeral: s(s(...s(0)...)).
3. N-introduction provides the constructors; N-elimination (recursion) provides the destructor.
4. The numeral s^n(0) represents the natural number n.

# Construction / Recognition

## To Construct a Natural Number:
- The base case: 0 is a term of type N.
- The inductive case: if a is a term of type N, form s(a).

## To Recognize:
A numeral is a term of the form s(s(...s(0)...)) -- zero with some number of successor applications.

# Context & Application

N-introduction formalizes the Peano axioms within type theory. Combined with N-elimination (primitive recursion), these rules provide a complete characterization of the natural numbers. In the propositions-as-types reading, N is not a proposition but a data type; its introduction rules are constructors rather than proof rules.

# Examples

- 0 is a term of type N (the number zero).
- s(0) is a term of type N (the number one).
- s(s(s(0))) is a numeral representing the number three.
- If n is a variable of type N, then s(n) is a term of type N.

# Relationships

## Builds Upon
- natural-numbers: The informal concept from Chapter 1.
- successor: The successor operation from Chapter 1.

## Enables
- n-elimination-rule: Recursion operates on terms constructed by N-introduction.
- numeral: Numerals are the canonical forms produced by iterated N-introduction.

## Contrasts With
- n-elimination-rule: Introduction builds natural numbers; elimination defines functions from them by recursion.
- finite-type: N_n types have finitely many introduction forms (1,...,n); N has infinitely many (0, s(0), s(s(0)),...).

# Common Errors

- **Error**: Assuming all terms of type N are numerals.
  **Correction**: A variable x of type N, or R(c, d, e) of type N, are terms of type N that are not numerals. Numerals are the specific canonical forms s^n(0).

# Common Confusions

- **Confusion**: Confusing the successor function s with a general function N -> N.
  **Clarification**: s is a primitive constructor, not a defined function. It is part of the introduction rule, not a lambda-abstraction.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 2.3.11: N-introduction or Peano's first and second axioms.

# Verification Notes

Confidence: high. Rule 2.3.11 is explicitly stated, and the term "numeral" is defined in the same section.
