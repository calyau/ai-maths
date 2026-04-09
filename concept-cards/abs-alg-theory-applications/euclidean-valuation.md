---
# === CORE IDENTIFICATION ===
concept: Euclidean Valuation
slug: euclidean-valuation

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
pdf_page: 245
section: "18.2 Factorization in Integral Domains"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Euclidean function"
  - "Euclidean norm"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - integral-domain
extends: []
related:
  - euclidean-domain
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Euclidean valuation?"
---

# Quick Definition

A Euclidean valuation on an integral domain $D$ is a function $\nu : D \setminus \{0\} \to \mathbb{N}$ satisfying $\nu(a) \leq \nu(ab)$ and enabling division with remainder: $a = bq + r$ with $r = 0$ or $\nu(r) < \nu(b)$.

# Core Definition

A function $\nu : D \setminus \{0\} \to \mathbb{N}$ on an integral domain $D$ is a Euclidean valuation if: (1) $\nu(a) \leq \nu(ab)$ for all nonzero $a, b$; (2) for all $a, b \in D$ with $b \neq 0$, there exist $q, r \in D$ with $a = bq + r$ where $r = 0$ or $\nu(r) < \nu(b)$ (Judson, pp. 245-246).

# Prerequisites

- **Integral domain** — The valuation is defined on an integral domain

# Key Properties

1. $\nu$ maps nonzero elements to natural numbers
2. $\nu(a) \leq \nu(ab)$ (monotonicity under multiplication)
3. Enables a division algorithm
4. Different valuations can make the same domain Euclidean

# Construction / Recognition

## Common Examples:
1. $\mathbb{Z}$: $\nu(a) = |a|$
2. $F[x]$: $\nu(p(x)) = \deg p(x)$
3. $\mathbb{Z}[i]$: $\nu(a+bi) = a^2 + b^2$

# Context & Application

The Euclidean valuation is the key ingredient that makes the division algorithm and Euclidean algorithm work. It measures the "size" of elements.

# Examples

**Example 1** (p. 246): $\nu(a) = |a|$ on $\mathbb{Z}$.

**Example 2** (p. 246): $\nu(p(x)) = \deg p(x)$ on $F[x]$.

**Example 3** (p. 246): $\nu(a+bi) = a^2 + b^2$ on $\mathbb{Z}[i]$.

# Relationships

## Enables
- **Euclidean domain** — A domain with a Euclidean valuation is a Euclidean domain

# Common Errors

- **Error**: Assuming the valuation must be unique
  **Correction**: Multiple different functions can serve as Euclidean valuations on the same domain

# Common Confusions

- **Confusion**: Confusing with absolute value or norm
  **Clarification**: A Euclidean valuation is any function satisfying the two axioms; it need not be the usual norm

# Source Reference

Chapter 18: Integral Domains, Section 18.2, pages 245-246.

# Verification Notes

- Definition source: Direct from pp. 245-246
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
