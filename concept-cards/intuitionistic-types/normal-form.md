---
# === CORE IDENTIFICATION ===
concept: Normal Form
slug: normal-form

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
section: "2.4.2, 2.4.5"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "irreducible expression"
  - "normal expression"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - redex-and-contractum
  - reduction
extends: []
related:
  - church-rosser-property
  - conversion
contrasts_with:
  - redex-and-contractum

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a redex, and what is a normal form?"
---

# Quick Definition

An expression is in normal form (or is irreducible) if it contains no redexes -- that is, no further contraction is possible.

# Core Definition

Martin-Lof writes (2.4.2): "an expression is irreducible or normal if it cannot be further reduced."

An expression in normal form contains no subexpression matching the left-hand side of any contraction rule. It is the fully computed, canonical result of evaluation.

# Prerequisites

- redex-and-contractum: Normal form is defined as the absence of redexes.
- reduction: Normal form is the endpoint of the reduction process.

# Key Properties

1. A normal expression contains no redexes at any depth.
2. **Uniqueness** (2.4.5): An expression can convert into at most one normal expression. This follows from the Church-Rosser property.
3. If a red b and a red c where b and c are both normal, then b = c (syntactically, up to renaming of bound variables).
4. The normalization theorem (Chapter 4) guarantees that every well-typed term has a normal form.

# Construction / Recognition

## To Construct/Create:
Reduce an expression by repeatedly contracting redexes until none remain.

## To Identify/Recognize:
Inspect the expression for any subexpression matching a redex pattern. If none is found, the expression is in normal form.

# Context & Application

Normal forms represent the fully evaluated results of computation in type theory. The uniqueness of normal forms (2.4.5) ensures that computation is deterministic in the sense that the final answer, if it exists, does not depend on the order of evaluation. For well-typed terms, the normalization theorem guarantees that this final answer always exists.

Martin-Lof notes (2.4.5): "First note that, because of the Church-Rosser property, an expression which converts into a normal expression must necessarily reduce to it."

# Examples

- The numeral s(s(0)) is in normal form -- it contains no redexes.
- The expression (lambda x)b[x] is in normal form (assuming b[x] is) -- a lambda abstraction without an argument applied to it is not a redex.
- The pair (a, b) is in normal form if a and b are both in normal form.
- The expression (lambda x)x(a) is NOT in normal form -- it is a beta-redex.

# Relationships

## Builds Upon
- redex-and-contractum: Normal form means no redexes.
- reduction: Normal form is the endpoint of reduction.

## Related
- church-rosser-property: Guarantees uniqueness of normal forms.
- conversion: Two expressions in normal form that are convertible must be identical.

## Contrasts With
- redex-and-contractum: A redex is the opposite of being in normal form.

# Common Errors

- **Error**: Assuming every expression has a normal form.
  **Correction**: Only well-typed terms are guaranteed to have normal forms (by the normalization theorem). Arbitrary untyped expressions may reduce indefinitely.

# Common Confusions

- **Confusion**: Whether normal form depends on the reduction strategy used.
  **Clarification**: No. By the uniqueness of normal forms (2.4.5), if a normal form exists, it is unique regardless of the reduction path taken.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 2.4.2 (definition) and 2.4.5 (uniqueness).

# Verification Notes

Confidence: high. Explicitly defined in 2.4.2 and the uniqueness property is proved in 2.4.5.
