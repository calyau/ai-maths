---
concept: Kummer Extension
slug: kummer-extension
category: galois-theory
subcategory: special-extensions
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Galois Theory"
chapter_number: 16
pdf_page: 488
section: "16.11 Kummer Extensions"
extraction_confidence: high
aliases: []
prerequisites:
  - galois-extension
  - cyclotomic-field
  - roots-of-unity
extends: []
related:
  - solvability-by-radicals
contrasts_with: []
answers_questions:
  - "What is a Kummer extension?"
---

# Quick Definition

A Kummer extension is a Galois extension of prime degree p over a field F containing the pth roots of unity, obtained by adjoining a pth root: K = F(beta) where beta^p is in F. Its Galois group is cyclic of order p.

# Core Definition

Let F be a subfield of C that contains the pth root of unity zeta = e^{2*pi*i/p} (p prime), and let K/F be a Galois extension of degree p. Then K is obtained by adjoining a pth root: K = F(beta) with beta^p in F (Artin, Theorem 16.11.1). Moreover, x^p - b is either irreducible over F or splits completely (Proposition 16.11.2).

# Prerequisites

- **Galois extension** -- Kummer extensions are Galois
- **Cyclotomic field** -- The base field must contain roots of unity

# Key Properties

1. The Galois group is cyclic of order p
2. x^p - b is irreducible over F or splits completely (16.11.2)
3. Every degree 2 extension is Kummer (adjoin a square root)
4. The proof uses eigenvalues of the Galois group acting as linear operators on K
5. Cardano's formula for cubics follows from Kummer theory (16.11.4)

# Context & Application

Kummer extensions are the building blocks of solvability by radicals. Each step in a radical tower that involves a pth root is a Kummer extension (after ensuring the base field contains the necessary roots of unity). This is the connection between Galois theory and radical solvability.

# Examples

**Example 1** (p. 510): For p = 2, every quadratic extension is Kummer: K = F(sqrt(d)).

**Example 2** (p. 510-512): For the cubic x^3 + 3px + 2q with discriminant a square in F (so G = A_3), Kummer theory leads to Cardano's formula: u_1 = cube_root(-q + sqrt(q^2+p^3)) + cube_root(-q - sqrt(q^2+p^3)).

# Relationships

## Builds Upon
- **Galois extension** -- Kummer extensions have cyclic Galois groups
- **Cyclotomic field** -- Roots of unity must be present

## Enables
- **Solvability by radicals** -- Each radical step is Kummer
- **Cardano's formula** -- Derived from Kummer theory for cubics

# Source Reference

Chapter 16: Galois Theory, Section 16.11, pages 510-513. Theorem 16.11.1, Proposition 16.11.2.

# Verification Notes

- Definition source: Direct from Artin, Theorem 16.11.1
- Confidence rationale: Complete proof using eigenvalue argument
- Uncertainties: None
- Cross-reference status: Verified
