---
concept: Minimal Polynomial (Field Theory)
slug: minimal-polynomial
category: field-theory
subcategory: elements
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Fields"
chapter_number: 15
pdf_page: 453
section: "15.2 Algebraic and Transcendental Elements"
extraction_confidence: high
aliases:
  - "irreducible polynomial for alpha over F"
prerequisites:
  - algebraic-element
  - field-extension
extends: []
related:
  - degree-of-field-extension
  - simple-extension
contrasts_with: []
answers_questions:
  - "What is the minimal polynomial of an algebraic element?"
---

# Quick Definition

The minimal polynomial (or irreducible polynomial) for an algebraic element alpha over F is the unique monic polynomial of lowest degree in F[x] having alpha as a root. It is irreducible, and it divides every polynomial in F[x] with alpha as a root.

# Core Definition

Let alpha be algebraic over F. The unique monic polynomial f satisfying these equivalent conditions is called the irreducible polynomial for alpha over F (Artin, Proposition 15.2.3): (1) f is the monic polynomial of lowest degree in F[x] having alpha as a root; (2) f is irreducible in F[x] and alpha is a root; (3) the principal ideal (f) is a maximal ideal of F[x]; (4) f divides every polynomial in F[x] having alpha as a root.

# Prerequisites

- **Algebraic element** -- The minimal polynomial exists only for algebraic elements
- **Field extension** -- The polynomial depends on the base field F

# Key Properties

1. The minimal polynomial is unique (monic, irreducible with alpha as root)
2. It depends on F as well as alpha: different base fields give different minimal polynomials (p. 456)
3. Its degree equals the degree of alpha over F, which equals [F(alpha):F] (15.3.4)
4. The set (1, alpha, ..., alpha^{n-1}) is a basis for F(alpha) over F, where n = deg f (15.2.7)
5. There is an isomorphism F(alpha) to F(beta) fixing F and sending alpha to beta iff they have the same minimal polynomial (15.2.8)

# Context & Application

The minimal polynomial is the fundamental invariant of an algebraic element relative to a base field. It determines the degree of the extension, provides a basis, and characterizes when two extensions are isomorphic.

# Examples

**Example 1** (p. 456): The irreducible polynomial for omega = e^{2pi*i/3} over Q is x^2 + x + 1. So [Q(omega):Q] = 2.

**Example 2** (p. 456): The irreducible polynomial for a primitive 8th root of unity over Q is x^4 + 1, but over Q(i) it factors, and the irreducible polynomial becomes x^2 - i.

# Relationships

## Builds Upon
- **Algebraic element** -- Only algebraic elements have minimal polynomials

## Enables
- **Degree of field extension** -- Equals the degree of the minimal polynomial
- **Simple extension** -- F(alpha) is determined by the minimal polynomial

# Common Errors

- **Error**: Saying "the" irreducible polynomial without specifying the base field
  **Correction**: The irreducible polynomial depends on F. Always say "irreducible polynomial for alpha over F."

# Source Reference

Chapter 15: Fields, Section 15.2, pages 454-457. Proposition 15.2.3, Proposition 15.2.7, Proposition 15.2.8.

# Verification Notes

- Definition source: Direct from Artin, Proposition 15.2.3
- Confidence rationale: Four equivalent characterizations given
- Uncertainties: None
- Cross-reference status: Verified
