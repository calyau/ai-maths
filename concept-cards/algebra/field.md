---
concept: Field
slug: field
category: linear-algebra
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Vector Spaces"
chapter_number: 3
pdf_page: 89
section: "3.2 Fields"
extraction_confidence: high
aliases: []
prerequisites:
  - group
  - abelian-group
extends: []
related:
  - vector-space
  - prime-field
  - characteristic-of-a-field
contrasts_with: []
answers_questions:
  - "What is a field?"
---

# Quick Definition

A field F is a set with two operations (addition and multiplication) such that F forms an abelian group under addition, the nonzero elements form an abelian group under multiplication, and the distributive law a(b+c) = ab + ac holds.

# Core Definition

A field F is a set with addition and multiplication satisfying (Definition 3.2.2, Artin, p. 91):
(i) Addition makes F into an abelian group F+ with identity 0
(ii) Multiplication is commutative, and makes the nonzero elements into an abelian group F* with identity 1
(iii) Distributive law: a(b+c) = ab + ac for all a, b, c in F

# Prerequisites

- **Group** — Both addition and multiplication are group operations
- **Abelian group** — Both groups are abelian

# Key Properties

1. 0 and 1 are distinct elements
2. a*0 = 0 for all a
3. Cancellation: if ab = 0, then a = 0 or b = 0
4. The characteristic is either 0 or prime (Lemma 3.2.10)
5. Subfields of C include Q, R, Q[sqrt(2)]

# Construction / Recognition

## To Construct:
1. Define a set with +, * operations
2. Verify the three field axioms

## To Recognize:
1. A commutative ring where every nonzero element is invertible

# Context & Application

Fields are the scalar systems for vector spaces. Artin introduces fields here so that linear algebra can be done over any field, not just R or C. The prime fields F_p = Z/pZ are finite fields of p elements.

# Examples

**Example 1** (p. 91): Q, R, C are subfields of C.

**Example 2** (pp. 92-93): F_p = Z/pZ is a field of p elements (Theorem 3.2.5).

**Example 3** (p. 91): Q[sqrt(2)] = {a + b*sqrt(2) : a, b in Q} is a field.

# Relationships

## Builds Upon
- **Abelian group** — Two abelian group structures (additive and multiplicative)

## Enables
- **Vector space** — Vector spaces are defined over fields
- **Linear algebra** — All of linear algebra works over any field

## Related
- **Prime field** — F_p = Z/pZ, the simplest finite field

# Common Errors

- **Error**: Treating Z (integers) as a field
  **Correction**: Z is not a field because most integers lack multiplicative inverses

# Common Confusions

- **Confusion**: Thinking all fields are subfields of C
  **Clarification**: Finite fields F_p are not subfields of C

# Source Reference

Chapter 3: Vector Spaces, Section 3.2, pages 90-96.

# Verification Notes

- Definition source: Direct from Definition 3.2.2, p. 91
- Confidence rationale: Explicitly defined with axioms
- Uncertainties: None
- Cross-reference status: Verified
