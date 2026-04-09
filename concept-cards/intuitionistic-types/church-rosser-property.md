---
# === CORE IDENTIFICATION ===
concept: Church-Rosser Property
slug: church-rosser-property

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
section: "2.4.3"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "confluence"
  - "diamond property"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - reduction
  - one-step-reduction
extends: []
related:
  - normal-form
  - conversion
  - contraction
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Church-Rosser property?"
---

# Quick Definition

The Church-Rosser property states that if an expression a reduces to both b and c (a red b and a red c), then there exists an expression d such that b red d and c red d. In other words, divergent reduction paths can always be brought back together.

# Core Definition

Martin-Lof states (2.4.3): "If a red b and a red c, then there is an expression d such that b red d and c red d."

The proof, adapted from a proof for the type-free combinator calculus shown to Martin-Lof by William Tait, proceeds in three steps:

1. **Substitution lemma** (2.4.3.1): If a red_1 c and b[x] red_1 d[x], then b[a] red_1 d[c].
2. **One-step diamond** (2.4.3.2): If a red_1 b and a red_1 c, then there exists d such that b red_1 d and c red_1 d. Proved by induction on the construction of a, with seven cases corresponding to the seven contraction rules.
3. **Multi-step diamond** (2.4.3.3): If a red_m b and a red_n c, then there exists d such that b red_n d and c red_m d. This follows by mn applications of the one-step diamond.

The property is proved for all formal expressions, not just well-typed terms.

# Prerequisites

- reduction: The property is a statement about the reduction relation.
- one-step-reduction: The proof strategy works through one-step reduction first.

# Key Properties

1. Church-Rosser is a property of the reduction relation on formal expressions (including ill-typed ones).
2. It guarantees that reduction is confluent: no matter what reduction choices are made, the results can always be reconciled.
3. Key consequences:
   - Conversion is an equivalence relation (2.4.4).
   - Normal forms are unique (2.4.5).
   - An expression that converts to a normal form must reduce to it.

# Construction / Recognition

## To Apply:
Given two reduction paths from the same expression, Church-Rosser guarantees the existence of a common reduct. In practice, reducing both results further (e.g., to normal form) witnesses this.

# Context & Application

The Church-Rosser property is the key combinatorial result that makes the reduction theory well-behaved. Without it, the notion of conversion would not be transitive, normal forms might not be unique, and the computational content of the theory would be ambiguous.

Martin-Lof's proof strategy -- establishing the one-step diamond first, then lifting to multi-step -- is a standard technique in rewriting theory. The crucial insight is that one-step reduction contracts "some, possibly all or none" of the redexes simultaneously, which gives enough flexibility for the induction to go through.

# Examples

Consider a term with two independent redexes:
- a = (lambda x)x(u) + (lambda y)y(v)
- Reducing the first redex gives b = u + (lambda y)y(v)
- Reducing the second gives c = (lambda x)x(u) + v
- Both reduce to d = u + v

This illustrates confluence: the two reduction paths rejoin.

# Relationships

## Builds Upon
- reduction: The property is about the reduction relation.
- one-step-reduction: The proof proceeds via one-step reduction.

## Enables
- conversion: Transitivity of conversion depends on Church-Rosser (2.4.4).
- normal-form: Uniqueness of normal forms depends on Church-Rosser (2.4.5).

# Common Errors

- **Error**: Thinking Church-Rosser implies termination.
  **Correction**: Church-Rosser says nothing about termination; it only says that if reduction paths diverge, they can be brought back together. Termination (normalization) is a separate theorem (Chapter 4).

# Common Confusions

- **Confusion**: Why prove Church-Rosser for all expressions, not just well-typed terms?
  **Clarification**: The proof requires induction on syntactic structure, not on typing derivations. Working with the broader class of expressions avoids having to track type information during the combinatorial argument.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 2.4.3. The proof method is credited to William Tait.

# Verification Notes

Confidence: high. The theorem is explicitly stated and proved in detail across 2.4.3-2.4.3.3.
