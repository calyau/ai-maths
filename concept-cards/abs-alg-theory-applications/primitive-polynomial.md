---
# === CORE IDENTIFICATION ===
concept: Primitive Polynomial
slug: primitive-polynomial

# === CLASSIFICATION ===
category: domain-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Integral Domains"
chapter_number: 18
pdf_page: 247
section: "18.2 Factorization in Integral Domains"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - content-of-polynomial
extends: []
related:
  - gausss-lemma-ufd
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a primitive polynomial?"
---

# Quick Definition

A polynomial over a UFD is primitive if the GCD of its coefficients (its content) is $1$.

# Core Definition

"We say that $p(x)$ is primitive if $\gcd(a_0, \ldots, a_n) = 1$" (Judson, p. 247).

# Prerequisites

- **Content of polynomial** — A polynomial is primitive when its content is $1$

# Key Properties

1. $\gcd$ of all coefficients is $1$
2. Product of primitive polynomials is primitive (Gauss's Lemma, Theorem 18.24)
3. Every polynomial equals its content times a primitive polynomial

# Construction / Recognition

## To Verify:
1. Compute the GCD of all coefficients
2. If the GCD is $1$, the polynomial is primitive

# Context & Application

Primitive polynomials are central to the proof that $D[x]$ is a UFD when $D$ is. They enable clean separation of "constant factors" from "polynomial structure."

# Examples

**Example 1** (p. 247): $5x^4 - 3x^3 + x - 4$ is primitive (GCD of $5, -3, 0, 1, -4$ is $1$).

**Example 2** (p. 247): $4x^2 - 6x + 8$ is not primitive (content is $2$).

# Relationships

## Enables
- **Gauss's Lemma (UFD)** — Product of primitives is primitive

# Common Errors

- **Error**: Assuming "primitive" means "irreducible"
  **Correction**: Primitive means content $= 1$; $x^2 - 1 = (x-1)(x+1)$ is primitive but reducible

# Common Confusions

- **Confusion**: Confusing primitive polynomial with irreducible polynomial
  **Clarification**: All irreducible polynomials over $\mathbb{Z}$ with content $1$ are primitive, but not all primitive polynomials are irreducible

# Source Reference

Chapter 18: Integral Domains, Section 18.2, page 247.

# Verification Notes

- Definition source: Direct from p. 247
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
