---
# === CORE IDENTIFICATION ===
concept: "Gauss's Lemma (UFD Version)"
slug: gausss-lemma-ufd

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
  - unique-factorization-domain
  - primitive-polynomial
extends: []
related:
  - gausss-lemma-polynomials
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Gauss's Lemma for UFDs?"
  - "Why is the product of primitive polynomials primitive?"
---

# Quick Definition

Gauss's Lemma for UFDs states that the product of two primitive polynomials over a UFD is again primitive.

# Core Definition

"Let $D$ be a UFD and let $f(x)$ and $g(x)$ be primitive polynomials in $D[x]$. Then $f(x)g(x)$ is primitive" (Judson, Theorem 18.24, p. 247). This is used to prove $D[x]$ is a UFD whenever $D$ is.

# Prerequisites

- **UFD** — The base ring must be a UFD
- **Primitive polynomial** — Both factors must be primitive

# Key Properties

1. Product of primitives is primitive
2. Content of product = product of contents (Lemma 18.25)
3. Key step in proving $D[x]$ is a UFD (Theorem 18.29)

# Construction / Recognition

## To Apply:
1. Verify $D$ is a UFD
2. Verify $f(x)$ and $g(x)$ are primitive
3. Conclude $f(x)g(x)$ is primitive

# Context & Application

This generalization of Gauss's Lemma from $\mathbb{Z}[x]$ to $D[x]$ is crucial for the inductive proof that $D[x_1, \ldots, x_n]$ is a UFD when $D$ is.

# Examples

**Example 1**: $(2x + 1)(3x - 1) = 6x^2 + x - 1$ in $\mathbb{Z}[x]$: both factors are primitive, and so is the product.

# Relationships

## Enables
- **$D[x]$ is a UFD** — Key lemma in Theorem 18.29

## Related
- **Gauss's Lemma (polynomials)** — The $\mathbb{Z}[x] \to \mathbb{Q}[x]$ version (Theorem 17.14)

# Common Errors

- **Error**: Applying Gauss's Lemma when the base ring is not a UFD
  **Correction**: The result requires $D$ to be a UFD

# Common Confusions

- **Confusion**: Confusing the two versions of Gauss's Lemma
  **Clarification**: Theorem 17.14 concerns factoring monic polynomials over $\mathbb{Q}$ vs $\mathbb{Z}$; Theorem 18.24 concerns products of primitive polynomials over any UFD

# Source Reference

Chapter 18: Integral Domains, Section 18.2, Theorem 18.24, page 247.

# Verification Notes

- Definition source: Direct from Theorem 18.24
- Confidence: HIGH — explicit theorem
- Cross-reference status: Verified
- Uncertainties: None
