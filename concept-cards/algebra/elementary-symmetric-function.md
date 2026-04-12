---
concept: Elementary Symmetric Function
slug: elementary-symmetric-function
category: galois-theory
subcategory: symmetric-functions
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Galois Theory"
chapter_number: 16
pdf_page: 488
section: "16.1 Symmetric Functions"
extraction_confidence: high
aliases:
  - "elementary symmetric polynomial"
prerequisites:
  - symmetric-function
extends: []
related:
  - symmetric-functions-theorem
  - discriminant
contrasts_with: []
answers_questions:
  - "What are the elementary symmetric functions?"
---

# Quick Definition

The elementary symmetric functions s_1, s_2, ..., s_n in n variables are the coefficients (up to sign) of the polynomial (x - u_1)(x - u_2)...(x - u_n). Every symmetric polynomial can be expressed uniquely in terms of them.

# Core Definition

The elementary symmetric functions in n variables u_1, ..., u_n are (Artin, p. 488): s_1 = sum of u_i, s_2 = sum of u_i*u_j (i < j), ..., s_n = u_1*u_2*...*u_n. They are the coefficients of the polynomial P(x) = (x - u_1)...(x - u_n) = x^n - s_1*x^{n-1} + s_2*x^{n-2} - ... +/- s_n (equation 16.1.2).

# Prerequisites

- **Symmetric function** -- Elementary symmetric functions are special symmetric functions

# Key Properties

1. s_k is the sum of all products of k distinct variables
2. They are the coefficients (with alternating signs) of the polynomial with variable roots
3. Every symmetric polynomial is uniquely a polynomial in s_1, ..., s_n (Theorem 16.1.6)
4. If a polynomial f(x) = x^n - a_1*x^{n-1} + ... has roots alpha_i, then a_j = s_j(alpha) (Lemma 16.1.5)

# Context & Application

Elementary symmetric functions provide the bridge between the coefficients and roots of a polynomial. Vieta's formulas are instances of this relationship. They are the generators of the ring of symmetric polynomials.

# Examples

**Example 1** (p. 488): For n = 3: s_1 = u_1 + u_2 + u_3, s_2 = u_1*u_2 + u_1*u_3 + u_2*u_3, s_3 = u_1*u_2*u_3.

**Example 2** (p. 489): For n = 2: (x - u_1)(x - u_2) = x^2 - (u_1 + u_2)x + u_1*u_2 = x^2 - s_1*x + s_2.

# Relationships

## Builds Upon
- **Symmetric function** -- Elementary symmetric functions are a special class

## Enables
- **Symmetric Functions Theorem** -- Every symmetric polynomial is a polynomial in the elementary ones
- **Discriminant** -- Expressed as a polynomial in the elementary symmetric functions

# Source Reference

Chapter 16: Galois Theory, Section 16.1, pages 488-489. Theorem 16.1.6.

# Verification Notes

- Definition source: Direct from Artin, p. 488
- Confidence rationale: Explicitly defined with formulas
- Uncertainties: None
- Cross-reference status: Verified
