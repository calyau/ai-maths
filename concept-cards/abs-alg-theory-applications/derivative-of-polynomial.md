---
# === CORE IDENTIFICATION ===
concept: Derivative of a Polynomial
slug: derivative-of-polynomial

# === CLASSIFICATION ===
category: field-theory
subcategory: finite-fields
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Finite Fields"
chapter_number: 22
pdf_page: 292
section: "22.1 Structure of a Finite Field"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "formal derivative"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - polynomial
extends: []
related:
  - separable-polynomial
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is the derivative of a polynomial defined algebraically?"
---

# Quick Definition

The formal derivative of a polynomial $f(x) = a_0 + a_1x + \cdots + a_nx^n$ over a field $F$ is $f'(x) = a_1 + 2a_2x + \cdots + na_nx^{n-1}$. This is a purely algebraic definition requiring no notion of limits.

# Core Definition

Let $f(x) = a_0 + a_1x + \cdots + a_nx^n$ be any polynomial in $F[x]$. Define the **derivative** of $f(x)$ to be

$$f'(x) = a_1 + 2a_2x + \cdots + na_nx^{n-1}$$

(Judson, p. 293).

# Prerequisites

- **Polynomial** — The derivative operates on polynomials

# Key Properties

1. The derivative is a purely formal/algebraic operation — no limits or continuity
2. In characteristic $p$, the derivative of $x^p$ is $px^{p-1} = 0$
3. $f(x)$ is separable if and only if $\gcd(f(x), f'(x)) = 1$ (Lemma 22.5)
4. Standard rules hold: $(f + g)' = f' + g'$, $(cf)' = cf'$, product rule

# Context & Application

The formal derivative provides a test for repeated roots without requiring factorization or knowledge of the roots themselves. It is essential for the separability criterion.

# Examples

**Example 1**: If $f(x) = x^3 - 3x + 2 \in \mathbb{Q}[x]$, then $f'(x) = 3x^2 - 3$.

**Example 2**: If $f(x) = x^{p^n} - x \in \mathbb{Z}_p[x]$, then $f'(x) = p^n x^{p^n - 1} - 1 = -1$ (since $p^n \equiv 0$ mod $p$). So $\gcd(f, f') = 1$ and $f$ is separable.

# Relationships

## Enables
- **Separable polynomial** — The derivative provides the separability test

# Source Reference

Chapter 22: Finite Fields, Section 22.1, page 293.

# Verification Notes

- Definition source: Direct from p. 293
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
