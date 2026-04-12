---
concept: Greatest Common Divisor (Polynomials)
slug: greatest-common-divisor-polynomials
category: ring-theory
subcategory: polynomial-rings
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Rings"
chapter_number: 11
pdf_page: 339
section: "Homomorphisms and Ideals"
extraction_confidence: high
aliases:
  - "gcd of polynomials"
prerequisites:
  - ideals-in-polynomial-rings
extends: []
related:
  - euclidean-algorithm
  - greatest-common-divisor
contrasts_with: []
answers_questions:
  - "How do I find the gcd of two polynomials?"
---

# Quick Definition

The greatest common divisor of polynomials f and g over a field F is the unique monic polynomial d that generates the ideal (f, g). It satisfies: d divides f and g, and any common divisor of f and g divides d.

# Core Definition

Let R = F[x] and let f and g be elements of R, not both zero. Their greatest common divisor d(x) is the unique monic polynomial that generates the ideal (f, g). It has these properties: (a) Rd = Rf + Rg, (b) d divides f and g, (c) if e divides both f and g, then e divides d, (d) there are polynomials p and q such that d = pf + qg (Artin, Corollary 11.3.25, p. 350).

# Prerequisites

- **Ideals in polynomial rings over fields** -- Every ideal in F[x] is principal

# Key Properties

1. d is the unique monic generator of the ideal (f, g)
2. d can be expressed as a linear combination pf + qg
3. f and g are relatively prime if and only if gcd(f, g) = 1

# Context & Application

The gcd is computable via the Euclidean algorithm. The linear combination property pf + qg = d is essential for proving that irreducible polynomials are prime elements.

# Examples

**Example 1** (p. 350): If f(x) = x^3 - 2 is irreducible in Q[x], then gcd(f, g) = f if f divides g, and gcd(f, g) = 1 otherwise.

# Relationships

## Builds Upon
- **Ideals in polynomial rings over fields** -- The gcd generates the ideal (f, g)

## Enables
- **Euclidean algorithm** -- Method for computing the gcd

# Source Reference

Chapter 11: Rings, Section 11.3, Corollary 11.3.25, page 350.

# Verification Notes

- Definition source: Direct from Corollary 11.3.25
- Confidence rationale: Explicit statement
- Uncertainties: None
- Cross-reference status: Verified
