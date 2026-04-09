---
# === CORE IDENTIFICATION ===
concept: Evaluation Homomorphism for Polynomials
slug: evaluation-homomorphism-polynomials

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
pdf_page: 226
section: "17.1 Polynomial Rings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - polynomial-ring
  - ring-homomorphism
extends:
  - ring-homomorphism
related:
  - zero-of-polynomial
  - factor-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the evaluation homomorphism for polynomials?"
  - "How does evaluating a polynomial relate to ring homomorphisms?"
---

# Quick Definition

The evaluation homomorphism at $\alpha \in R$ is the ring homomorphism $\phi_\alpha : R[x] \to R$ defined by $\phi_\alpha(p(x)) = p(\alpha)$, which substitutes $\alpha$ for $x$.

# Core Definition

"The map $\phi_\alpha : R[x] \to R$ is called the evaluation homomorphism at $\alpha$" (Judson, Theorem 17.5, p. 226). It is defined by $\phi_\alpha(p(x)) = p(\alpha) = a_n\alpha^n + \cdots + a_1\alpha + a_0$ for $p(x) = a_nx^n + \cdots + a_0$.

# Prerequisites

- **Polynomial ring** — The domain is $R[x]$
- **Ring homomorphism** — The evaluation map preserves both operations

# Key Properties

1. $\phi_\alpha(p(x) + q(x)) = \phi_\alpha(p(x)) + \phi_\alpha(q(x))$
2. $\phi_\alpha(p(x)q(x)) = \phi_\alpha(p(x))\phi_\alpha(q(x))$
3. $\ker\phi_\alpha = \{p(x) \in R[x] : p(\alpha) = 0\}$
4. $\alpha$ is a zero of $p(x)$ iff $p(x) \in \ker\phi_\alpha$

# Construction / Recognition

## To Apply:
1. Fix an element $\alpha \in R$
2. For any $p(x) \in R[x]$, compute $p(\alpha)$ by substituting $\alpha$ for $x$

# Context & Application

The evaluation homomorphism connects abstract polynomial theory to concrete computation. It underlies the Factor Theorem and is the tool for finding zeros of polynomials.

# Examples

**Example 1** (p. 226): If $p(x) = x^3 - 2x + 1$ and $\alpha = 2$, then $\phi_2(p(x)) = 8 - 4 + 1 = 5$.

# Relationships

## Builds Upon
- **Ring homomorphism** — Evaluation is a ring homomorphism

## Enables
- **Zero of polynomial** — A zero is an element in the kernel of the evaluation map
- **Factor Theorem** — $\alpha$ is a zero iff $(x - \alpha)$ divides $p(x)$

# Common Errors

- **Error**: Treating evaluation as just substitution without recognizing it as a homomorphism
  **Correction**: The homomorphism property is what makes the Factor Theorem work

# Common Confusions

- **Confusion**: Thinking evaluation always yields zero
  **Clarification**: Evaluation yields $p(\alpha)$; this is zero only when $\alpha$ is a root

# Source Reference

Chapter 17: Polynomials, Section 17.1, Theorem 17.5, page 226.

# Verification Notes

- Definition source: Direct from Theorem 17.5
- Confidence: HIGH — explicit theorem
- Cross-reference status: Verified
- Uncertainties: None
