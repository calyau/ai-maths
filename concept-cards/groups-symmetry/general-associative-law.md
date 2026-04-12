---
# === CORE IDENTIFICATION ===
concept: General Associative Law
slug: general-associative-law

# === CLASSIFICATION ===
category: fundamentals
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Dihedral Groups"
chapter_number: 4
pdf_page: 22
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - generalized associative law

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - associativity
extends:
  - associativity
related:
  - power-of-an-element
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
---

# Quick Definition

The general associative law states that if x_1, x_2, ..., x_n are elements of a group, then any two ways of bracketing the product x_1 x_2 ... x_n give the same result. This means the product is well-defined without specifying brackets.

# Core Definition

"If x_1, x_2, ..., x_n are elements of a group, any two ways of combining these elements in this order give the same answer. In other words the product x_1 x_2 ... x_n makes sense without any brackets" (Armstrong, Ch. 4, p. 23). Armstrong outlines a proof by induction in Exercise 4.10, where the inductive step uses the ordinary associative law for three elements.

# Prerequisites

- **Group** — The law applies to elements of a group
- **Associativity** — The general law extends the three-element associative law

# Key Properties

1. Any bracketing of x_1 x_2 ... x_n yields the same element
2. Proved by induction on n, using the ordinary associative law (for three elements) in the inductive step
3. Justifies writing products without brackets
4. Essential for the well-definedness of power notation x^m

# Construction / Recognition

## Proof Outline (Exercise 4.10):
1. Base case: for n <= 3, follows from the ordinary associative law
2. Inductive hypothesis: products of k elements are well-defined for all k < n
3. Inductive step: any two bracketings of n elements have final multiplications (x_1...x_r)(x_{r+1}...x_n) and (x_1...x_s)(x_{s+1}...x_n)
4. Rewrite (1) as (x_1...x_r)[(x_{r+1}...x_s)(x_{s+1}...x_n)] and use the ordinary associative law

# Context & Application

The general associative law justifies the convention of writing products without brackets, which is used extensively in all group calculations. Without it, expressions like r^2srs would be ambiguous.

# Examples

**Example 1** (p. 23): The product r^2srs can be computed as (r^2s)(rs) or as r^2(s(rs)) or as ((r^2s)r)s, all giving the same answer.

**Example 2** (p. 24): The inverse of a product: (x_1 x_2 ... x_n)^{-1} = x_n^{-1} ... x_2^{-1} x_1^{-1}, relying on the general associative law.

# Relationships

## Builds Upon
- **Associativity** — Generalizes the three-element case

## Enables
- **Power of an Element** — x^m is well-defined because bracketing doesn't matter

# Common Errors

- **Error**: Assuming the general associative law allows reordering of elements
  **Correction**: It allows any bracketing but the order of elements must remain fixed

# Common Confusions

- **Confusion**: Confusing associativity (bracketing) with commutativity (ordering)
  **Clarification**: The general associative law says brackets don't matter; it says nothing about changing the order of factors

# Source Reference

Chapter 4: Dihedral Groups, pages 16-17 (pdf pp. 23-24). Proof outline in Exercise 4.10 (p. 26).

# Verification Notes

- Definition source: Direct quote from p. 23; proof outline from Exercise 4.10
- Confidence rationale: High — explicitly stated with proof sketch
- Uncertainties: None
- Cross-reference status: Verified
