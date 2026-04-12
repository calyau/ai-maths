---
concept: Adjoining Roots
slug: adjoining-roots
category: field-theory
subcategory: constructions
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Fields"
chapter_number: 15
pdf_page: 453
section: "15.6 Adjoining Roots"
extraction_confidence: high
aliases: []
prerequisites:
  - field-extension
  - irreducible-polynomial
extends: []
related:
  - splitting-field
  - simple-extension
contrasts_with: []
answers_questions:
  - "How do you adjoin a root of a polynomial to a field?"
---

# Quick Definition

Given a field F and an irreducible polynomial f(x) in F[x], one can construct an extension field K = F[x]/(f) in which f has a root. This is the fundamental tool for constructing field extensions.

# Core Definition

Given a polynomial f(x) with coefficients in a field F, one may adjoin a root of f to F by forming the quotient ring K = F[x]/(f) (Artin, p. 470, equation 15.6.1). If f is irreducible, then K is a field (Lemma 15.6.2), the residue x_bar of x is a root of f in K, and F embeds as a subfield of K. By iterating, one can adjoin all roots to construct a splitting field (Proposition 15.6.3).

# Prerequisites

- **Field extension** -- The construction produces a field extension
- **Irreducible polynomial** -- f must be irreducible for K to be a field

# Key Properties

1. K = F[x]/(f) is a field iff f is irreducible (15.6.2)
2. The residue x_bar is a root of f in K
3. [K:F] = deg(f) when f is irreducible
4. By iteration, every polynomial has a splitting field (15.6.3)
5. Division, gcd, and factorization in F[x] remain valid in K[x] (15.6.4)

# Context & Application

This is the fundamental construction for creating field extensions. It allows one to manufacture roots of polynomials that don't exist in the base field, essential for constructing finite fields and splitting fields.

# Examples

**Example 1** (p. 473): F_4 = F_2[x]/(x^2 + x + 1) is constructed by adjoining a root of the irreducible x^2 + x + 1 over F_2.

# Relationships

## Builds Upon
- **Irreducible polynomial** -- The polynomial being factored

## Enables
- **Splitting field** -- Constructed by repeatedly adjoining roots
- **Finite field** -- Constructed by adjoining roots over F_p

# Source Reference

Chapter 15: Fields, Section 15.6, pages 470-473. Lemma 15.6.2, Proposition 15.6.3.

# Verification Notes

- Definition source: Direct from Artin, p. 470
- Confidence rationale: Explicit construction with proof
- Uncertainties: None
- Cross-reference status: Verified
