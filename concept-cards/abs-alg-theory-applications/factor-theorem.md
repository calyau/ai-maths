---
# === CORE IDENTIFICATION ===
concept: Factor Theorem
slug: factor-theorem

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
pdf_page: 228
section: "17.2 The Division Algorithm"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - division-algorithm-polynomials
  - zero-of-polynomial
extends: []
related:
  - irreducible-polynomial
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Factor Theorem?"
  - "How are zeros of polynomials related to linear factors?"
---

# Quick Definition

An element $\alpha \in F$ is a zero of $p(x) \in F[x]$ if and only if $(x - \alpha)$ is a factor of $p(x)$.

# Core Definition

"Let $F$ be a field. An element $\alpha \in F$ is a zero of $p(x) \in F[x]$ if and only if $x - \alpha$ is a factor of $p(x)$ in $F[x]$" (Judson, Corollary 17.8, p. 228).

# Prerequisites

- **Division algorithm for polynomials** — Used in the proof
- **Zero of polynomial** — The theorem characterizes zeros

# Key Properties

1. $p(\alpha) = 0$ iff $p(x) = (x - \alpha)q(x)$ for some $q(x) \in F[x]$
2. If $\alpha$ is a zero, $\deg q(x) = \deg p(x) - 1$
3. Repeated application gives the factorization by all linear factors

# Construction / Recognition

## To Apply:
1. If you know $p(\alpha) = 0$, divide $p(x)$ by $(x - \alpha)$ to get $q(x)$
2. If you know $(x - \alpha) | p(x)$, conclude $\alpha$ is a zero

# Context & Application

The Factor Theorem is fundamental for polynomial factorization. It connects the abstract notion of zeros to concrete factorization and is used repeatedly in irreducibility testing.

# Examples

**Example 1** (p. 227): $p(x) = x^3 - x^2 + 2x - 3$ evaluated at $x = 2$ gives $p(2) = 8 - 4 + 4 - 3 = 5 \neq 0$, so $(x - 2)$ is not a factor; indeed, the remainder is $5$.

# Relationships

## Builds Upon
- **Division algorithm** — The proof divides $p(x)$ by $(x - \alpha)$ and shows the remainder is $p(\alpha)$

## Enables
- **Irreducibility testing** — For low-degree polynomials, check for zeros

# Common Errors

- **Error**: Using the Factor Theorem over rings that are not fields
  **Correction**: The theorem requires $F$ to be a field

# Common Confusions

- **Confusion**: Thinking the Factor Theorem gives complete factorization
  **Clarification**: It only factors out one linear factor per zero; further factorization of $q(x)$ may be needed

# Source Reference

Chapter 17: Polynomials, Section 17.2, Corollary 17.8, page 228.

# Verification Notes

- Definition source: Direct from Corollary 17.8
- Confidence: HIGH — explicit corollary
- Cross-reference status: Verified
- Uncertainties: None
