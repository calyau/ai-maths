---
# === CORE IDENTIFICATION ===
concept: "Eisenstein's Criterion"
slug: eisensteins-criterion

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
pdf_page: 231
section: "17.3 Irreducible Polynomials"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - polynomial-ring
  - gausss-lemma-polynomials
extends: []
related:
  - irreducible-polynomial
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Eisenstein's Criterion?"
  - "How do I test if a polynomial is irreducible?"
---

# Quick Definition

Eisenstein's Criterion provides a sufficient condition for a polynomial $f(x) = a_nx^n + \cdots + a_0 \in \mathbb{Z}[x]$ to be irreducible over $\mathbb{Q}$: if a prime $p$ divides $a_0, \ldots, a_{n-1}$ but not $a_n$, and $p^2$ does not divide $a_0$, then $f(x)$ is irreducible.

# Core Definition

"Let $p$ be a prime and suppose that $f(x) = a_nx^n + \cdots + a_0 \in \mathbb{Z}[x]$. If $p | a_i$ for $i = 0, 1, \ldots, n-1$, but $p \nmid a_n$ and $p^2 \nmid a_0$, then $f(x)$ is irreducible over $\mathbb{Q}$" (Judson, Theorem 17.17, p. 231).

# Prerequisites

- **Polynomial ring** — The criterion applies to $\mathbb{Z}[x]$
- **Gauss's Lemma** — Used in the proof

# Key Properties

1. Only a sufficient condition (not necessary)
2. Requires finding a suitable prime $p$
3. Three conditions: $p | a_i$ for $i < n$, $p \nmid a_n$, $p^2 \nmid a_0$
4. More useful for constructing irreducible polynomials than testing arbitrary ones

# Construction / Recognition

## To Apply:
1. Find a prime $p$ that divides all coefficients except the leading one
2. Verify $p$ does not divide the leading coefficient $a_n$
3. Verify $p^2$ does not divide the constant term $a_0$
4. If all three hold, $f(x)$ is irreducible over $\mathbb{Q}$

# Context & Application

Eisenstein's Criterion is the most powerful simple test for irreducibility. It is especially useful for constructing irreducible polynomials of any desired degree (e.g., $x^n - p$ for any prime $p$).

# Examples

**Example 1** (p. 232): $f(x) = 16x^5 - 9x^4 + 3x^2 + 6x - 21$ is irreducible over $\mathbb{Q}$ using $p = 3$ (since $3 | -9, 3, 6, -21$ but $3 \nmid 16$ and $9 \nmid -21$).

**Example 2**: $x^n - 2$ is irreducible over $\mathbb{Q}$ for any $n$ by Eisenstein with $p = 2$.

# Relationships

## Builds Upon
- **Gauss's Lemma** — Reduces to factorization over $\mathbb{Z}$

## Enables
- **Construction of irreducible polynomials** — Easy method for any degree

## Related
- **Irreducible polynomial** — Eisenstein is a test for irreducibility

# Common Errors

- **Error**: Concluding a polynomial is reducible because Eisenstein's Criterion doesn't apply
  **Correction**: Eisenstein is sufficient, not necessary; failure of the criterion says nothing about reducibility

# Common Confusions

- **Confusion**: Forgetting the $p^2 \nmid a_0$ condition
  **Clarification**: All three conditions are needed; e.g., $4x^2 + 4x + 4$ with $p = 2$ fails since $4 = 2^2 | a_0$

# Source Reference

Chapter 17: Polynomials, Section 17.3, Theorem 17.17, pages 231-232.

# Verification Notes

- Definition source: Direct from Theorem 17.17
- Confidence: HIGH — explicit theorem with proof
- Cross-reference status: Verified
- Uncertainties: None
