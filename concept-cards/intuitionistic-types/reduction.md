---
# === CORE IDENTIFICATION ===
concept: Reduction
slug: reduction

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
section: "2.4.2-2.4.3"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "red"
  - "reduces to"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - contraction
  - redex-and-contractum
extends:
  - contraction
related:
  - conversion
  - normal-form
  - one-step-reduction
  - church-rosser-property
contrasts_with:
  - contraction
  - conversion

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes contraction from reduction from conversion?"
---

# Quick Definition

An expression a reduces to an expression b (written a red b) if b can be obtained from a by repeated contractions of subexpressions within a. Reduction is the reflexive-transitive closure of contraction applied to parts of an expression.

# Core Definition

Martin-Lof writes (2.4.2): "An expression a reduces to an expression b, abbreviated a red b, if b can be obtained from a by repeated contractions of parts of the expression a."

More precisely, reduction in n steps (a red_n b) is defined inductively:
- a red_0 a (zero steps: identity)
- a red_{n+1} b means there exists c such that a red_n c and c red_1 b (n steps followed by one step)

One-step reduction (a red_1 b) means b is obtained by contracting some, possibly all or none, of the redexes in a, starting from within and proceeding outwards.

# Prerequisites

- contraction: Reduction is built from contraction steps.
- redex-and-contractum: The individual steps of reduction contract redexes.

# Key Properties

1. Reduction is reflexive: a red a (by doing zero contractions).
2. Reduction is transitive: if a red b and b red c, then a red c.
3. Reduction is NOT symmetric: a red b does not imply b red a.
4. The Church-Rosser property (2.4.3) holds: if a red b and a red c, then there exists d such that b red d and c red d.
5. Terms of a given type are closed under reduction (Theorem 2.4.7): reducing a well-typed term always yields a well-typed term of the same type.
6. Types are closed under reduction (Corollary 2.4.8).

# Construction / Recognition

## To Perform Reduction:
Repeatedly identify redexes within the expression and contract them. Any order of contraction is valid; Church-Rosser guarantees confluence.

## To Verify a Reduction:
Check that each step is either a contraction of a subexpression or the identity (no contraction).

# Context & Application

Reduction is the computational mechanism of the theory of types. It formalizes how terms evaluate to simpler forms. The Church-Rosser property ensures that the order of evaluation does not matter for the final result. The normalization theorem (Chapter 4) establishes that reduction of well-typed terms always terminates.

# Examples

A multi-step reduction:
- (lambda x)(x, x)(a) red_1 (a, a) (one beta-contraction)
- E((a, a), (lambda x)(lambda y)x) red_1 a (one Sigma-contraction)
- So (lambda x)(x, x)(a) followed by E gives a two-step reduction to the first projection.

# Relationships

## Builds Upon
- contraction: Reduction is repeated contraction.

## Enables
- conversion: Conversion is defined in terms of reduction (a conv b iff there exists c with a red c and b red c).
- normal-form: An expression is in normal form when no further reduction is possible.
- church-rosser-property: States that reduction is confluent.

## Contrasts With
- contraction: Contraction is a single rule application; reduction is the closure.
- conversion: Conversion is symmetric (an equivalence relation); reduction is not.

# Common Errors

- **Error**: Assuming reduction is symmetric.
  **Correction**: Reduction is one-directional. If a red b, it does not follow that b red a. Symmetry belongs to conversion.

# Common Confusions

- **Confusion**: Whether different reduction strategies can lead to different results.
  **Clarification**: No. The Church-Rosser property guarantees that all reduction paths from a given expression can be brought to a common reduct.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 2.4.2 (definition) and 2.4.3 (Church-Rosser property).

# Verification Notes

Confidence: high. Explicitly defined in the text of 2.4.2 with formal notation.
