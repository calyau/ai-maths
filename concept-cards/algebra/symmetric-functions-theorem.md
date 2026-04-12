---
concept: Symmetric Functions Theorem
slug: symmetric-functions-theorem
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
  - "fundamental theorem on symmetric functions"
prerequisites:
  - symmetric-function
  - elementary-symmetric-function
extends: []
related:
  - splitting-field
contrasts_with: []
answers_questions:
  - "Can every symmetric polynomial be written in terms of elementary symmetric functions?"
---

# Quick Definition

Every symmetric polynomial g(u_1, ..., u_n) with coefficients in a ring R can be written in a unique way as a polynomial in the elementary symmetric functions s_1, ..., s_n.

# Core Definition

If g(u) is a symmetric polynomial, there is a unique polynomial G(z_1, ..., z_n) with coefficients in R such that g(u_1, ..., u_n) = G(s_1, ..., s_n) (Artin, Theorem 16.1.6). The proof uses double induction: on the number of variables and on the degree of the symmetric polynomial.

# Prerequisites

- **Symmetric function** -- The theorem is about symmetric polynomials
- **Elementary symmetric function** -- They form the "basis" of symmetric polynomials

# Key Properties

1. Existence and uniqueness of the representation
2. The representation preserves weighted degree
3. Key consequence: if f splits as (x - alpha_1)...(x - alpha_n) with coefficients in F, then g(alpha_1, ..., alpha_n) is in F for any symmetric g with coefficients in F (Corollary 16.1.12)

# Context & Application

This theorem is the foundation of Galois theory. Corollary 16.1.12 is used to prove the Splitting Theorem (16.3.2), which is in turn used to prove the fundamental properties of Galois extensions.

# Examples

**Example 1** (p. 489): u_1^2 + ... + u_n^2 = s_1^2 - 2s_2.

**Example 2** (p. 489): The orbit sum u_1*u_2^2 + ... = s_1*s_2 - 3s_3 (for n >= 3 variables).

# Relationships

## Builds Upon
- **Symmetric function** and **Elementary symmetric function** -- The theorem relates these

## Enables
- **Splitting Theorem** -- Uses the symmetric functions theorem
- **Discriminant** -- Expressed via the theorem

# Source Reference

Chapter 16: Galois Theory, Section 16.1, pages 489-491. Theorem 16.1.6, Corollary 16.1.12.

# Verification Notes

- Definition source: Direct from Artin, Theorem 16.1.6
- Confidence rationale: Complete proof given
- Uncertainties: None
- Cross-reference status: Verified
