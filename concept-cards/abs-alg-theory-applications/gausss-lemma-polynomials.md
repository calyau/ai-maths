---
# === CORE IDENTIFICATION ===
concept: "Gauss's Lemma (Polynomials)"
slug: gausss-lemma-polynomials

# === CLASSIFICATION ===
category: polynomial-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Polynomials"
chapter_number: 17
pdf_page: 230
section: "17.3 Irreducible Polynomials"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - polynomial-ring
  - integral-domain
extends: []
related:
  - irreducible-polynomial
  - rational-root-test
  - eisensteins-criterion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Gauss's Lemma for polynomials?"
  - "How does factoring over the rationals relate to factoring over the integers?"
---

# Quick Definition

Gauss's Lemma states that if a monic polynomial $p(x) \in \mathbb{Z}[x]$ factors into two polynomials in $\mathbb{Q}[x]$, then it factors into two monic polynomials with the same degrees in $\mathbb{Z}[x]$.

# Core Definition

"Let $p(x) \in \mathbb{Z}[x]$ be a monic polynomial such that $p(x)$ factors into a product of two polynomials $\alpha(x)$ and $\beta(x)$ in $\mathbb{Q}[x]$, where the degrees of both $\alpha(x)$ and $\beta(x)$ are less than the degree of $p(x)$. Then $p(x) = a(x)b(x)$, where $a(x)$ and $b(x)$ are monic polynomials in $\mathbb{Z}[x]$ with $\deg\alpha(x) = \deg a(x)$ and $\deg\beta(x) = \deg b(x)$" (Judson, Theorem 17.14, p. 230).

# Prerequisites

- **Polynomial ring** — The lemma concerns $\mathbb{Z}[x]$ and $\mathbb{Q}[x]$
- **Integral domain** — Uses the fact that $\mathbb{Z}_p[x]$ is an integral domain

# Key Properties

1. Factorization over $\mathbb{Q}$ implies factorization over $\mathbb{Z}$ (for monic polynomials)
2. To test irreducibility over $\mathbb{Q}$, it suffices to test over $\mathbb{Z}$
3. Degrees are preserved in the integer factorization

# Construction / Recognition

## To Apply:
1. Given a monic $p(x) \in \mathbb{Z}[x]$
2. If $p(x)$ is irreducible in $\mathbb{Z}[x]$, it is irreducible in $\mathbb{Q}[x]$
3. Contrapositive: if $p(x)$ factors in $\mathbb{Q}[x]$, it factors in $\mathbb{Z}[x]$

# Context & Application

Gauss's Lemma reduces the problem of testing irreducibility over $\mathbb{Q}$ to testing over $\mathbb{Z}$, where integer arguments (divisibility, modular reduction) are available. It is the foundation for the Rational Root Test and Eisenstein's Criterion.

# Examples

**Example 1** (p. 231): To show $x^4 - 2x^3 + x + 1$ is irreducible over $\mathbb{Q}$, by Gauss's Lemma it suffices to show it doesn't factor over $\mathbb{Z}$.

# Relationships

## Enables
- **Rational Root Test** — Corollary of Gauss's Lemma (Corollary 17.15)
- **Eisenstein's Criterion** — Uses Gauss's Lemma in its proof

## Related
- **Irreducible polynomial** — Gauss's Lemma is a key tool for testing irreducibility

# Common Errors

- **Error**: Applying Gauss's Lemma to non-monic polynomials without adjustment
  **Correction**: The standard version assumes monic; for non-monic polynomials, factor out content first

# Common Confusions

- **Confusion**: Confusing Gauss's Lemma for polynomials with Gauss's Lemma for UFDs (Theorem 18.24)
  **Clarification**: The polynomial version (Theorem 17.14) concerns $\mathbb{Z}[x] \to \mathbb{Q}[x]$; the UFD version (Theorem 18.24) concerns primitive polynomials over any UFD

# Source Reference

Chapter 17: Polynomials, Section 17.3, Theorem 17.14, pages 230-231.

# Verification Notes

- Definition source: Direct from Theorem 17.14
- Confidence: HIGH — explicit theorem with proof
- Cross-reference status: Verified
- Uncertainties: None
