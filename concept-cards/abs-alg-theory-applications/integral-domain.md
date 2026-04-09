---
# === CORE IDENTIFICATION ===
concept: Integral Domain
slug: integral-domain

# === CLASSIFICATION ===
category: ring-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Rings"
chapter_number: 16
pdf_page: 204
section: "16.2 Integral Domains and Fields"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - commutative-ring
  - ring-with-unity
  - zero-divisor
extends:
  - commutative-ring
  - ring-with-unity
related:
  - cancellation-law-integral-domains
  - characteristic-of-ring
contrasts_with:
  - field
  - division-ring

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an integral domain?"
  - "What distinguishes an integral domain from a field?"
  - "How do rings relate to integral domains and fields?"
---

# Quick Definition

An integral domain is a commutative ring with identity that has no zero divisors: if $ab = 0$, then $a = 0$ or $b = 0$.

# Core Definition

"A commutative ring with identity is said to be an integral domain if it has no zero divisors" (Judson, p. 207). Equivalently, a commutative ring $D$ with identity is an integral domain if for every $a, b \in D$ with $ab = 0$, either $a = 0$ or $b = 0$.

# Prerequisites

- **Commutative ring** — An integral domain must have commutative multiplication
- **Ring with unity** — An integral domain must have a multiplicative identity
- **Zero divisor** — The defining condition is the absence of zero divisors

# Key Properties

1. Commutative multiplication: $ab = ba$
2. Has multiplicative identity $1 \neq 0$
3. No zero divisors: $ab = 0 \Rightarrow a = 0$ or $b = 0$
4. Cancellation law holds: if $a \neq 0$ and $ab = ac$, then $b = c$ (Proposition 16.15)
5. Characteristic is either $0$ or prime (Theorem 16.19)
6. Every finite integral domain is a field (Theorem 16.16)

# Construction / Recognition

## To Verify:
1. Confirm $R$ is a commutative ring with identity
2. Show that if $ab = 0$ then $a = 0$ or $b = 0$
3. Alternatively, verify the cancellation law holds

## To Recognize:
1. $\mathbb{Z}_p$ for prime $p$ is always an integral domain (and a field)
2. $\mathbb{Z}_n$ for composite $n$ is never an integral domain (has zero divisors)

# Context & Application

Integral domains are the natural generalization of the integers. They are the setting for factorization theory: concepts like irreducible elements, prime elements, and unique factorization are studied in integral domains. Every integral domain can be embedded in a field of fractions, generalizing how $\mathbb{Z}$ embeds in $\mathbb{Q}$.

# Examples

**Example 1** (p. 205): $\mathbb{Z}$ is an integral domain but not a field (e.g., $1/2 \notin \mathbb{Z}$).

**Example 2** (p. 205): $\mathbb{Z}_{12}$ is not an integral domain since $3 \cdot 4 \equiv 0 \pmod{12}$ with $3 \neq 0$ and $4 \neq 0$.

**Example 3** (p. 208): The Gaussian integers $\mathbb{Z}[i] = \{m + ni : m, n \in \mathbb{Z}\}$ form an integral domain.

# Relationships

## Builds Upon
- **Commutative ring** — Adds the no-zero-divisor condition
- **Ring with unity** — Requires multiplicative identity

## Enables
- **Field of fractions** — Every integral domain embeds in its field of fractions
- **Unique factorization domain** — A UFD is an integral domain with unique factorization
- **Principal ideal domain** — A PID is an integral domain where every ideal is principal

## Contrasts With
- **Field** — Every field is an integral domain, but not conversely ($\mathbb{Z}$ is not a field)
- **$\mathbb{Z}_n$ for composite $n$** — Has zero divisors, so is not an integral domain

# Common Errors

- **Error**: Assuming every integral domain is a field
  **Correction**: Only finite integral domains are automatically fields (Theorem 16.16); $\mathbb{Z}$ is an infinite integral domain that is not a field

# Common Confusions

- **Confusion**: Thinking "no zero divisors" is the same as "every nonzero element has an inverse"
  **Clarification**: No zero divisors means $ab = 0 \Rightarrow a = 0$ or $b = 0$; having inverses is a stronger property that characterizes fields

# Source Reference

Chapter 16: Rings, Section 16.1 (definition, p. 204) and Section 16.2 "Integral Domains and Fields" (pp. 207-209).

# Verification Notes

- Definition source: Direct from pp. 204 and 207
- Confidence: HIGH — explicit definition given twice
- Cross-reference status: Verified
- Uncertainties: None
