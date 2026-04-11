---
concept: Integral Domain
slug: integral-domain
category: ring-theory
subcategory: basic-definitions
tier: foundational
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 223
section: "7.1 Basic Definitions and Examples"
extraction_confidence: high
aliases:
  - "entire ring"
prerequisites:
  - commutative-ring
  - ring-with-identity
  - zero-divisor
extends:
  - commutative-ring
related:
  - field
  - unique-factorization-domain
  - field-of-fractions
contrasts_with:
  - field
  - unique-factorization-domain
answers_questions:
  - "What is an integral domain?"
  - "What distinguishes an integral domain from a field?"
  - "What is the cancellation property in rings?"
---

# Quick Definition
An integral domain is a commutative ring with identity $1 \neq 0$ that has no zero divisors.

# Core Definition
A commutative ring with identity $1 \neq 0$ is called an *integral domain* if it has no zero divisors (Dummit & Foote, p. 229).

# Prerequisites
- **Commutative ring** — Must be commutative
- **Ring with identity** — Must have $1 \neq 0$
- **Zero divisor** — Defined by the absence of zero divisors

# Key Properties
1. If $ab = ac$ and $a \neq 0$, then $b = c$ (cancellation, Proposition 2, p. 229)
2. Any finite integral domain is a field (Corollary 3, p. 229)
3. Any subring of a field containing the identity is an integral domain (p. 230)
4. $R[x]$ is an integral domain whenever R is (Proposition 4, p. 236)
5. 0 is a prime ideal in an integral domain (p. 258)

# Construction / Recognition
## To Recognize:
1. Check R is a commutative ring with $1 \neq 0$
2. Verify: if $ab = 0$ then $a = 0$ or $b = 0$

# Context & Application
Integral domains generalize the integers $\mathbb{Z}$, where the familiar cancellation law holds. They sit in the hierarchy: fields $\subset$ Euclidean Domains $\subset$ PIDs $\subset$ UFDs $\subset$ integral domains (p. 290).

# Examples
**Example 1** (p. 229): $\mathbb{Z}$ is an integral domain (but not a field).

**Example 2** (p. 224): $\mathbb{Z}/p\mathbb{Z}$ for prime p is an integral domain (in fact a field).

**Example 3** (p. 228): $\mathbb{Z}/6\mathbb{Z}$ is *not* an integral domain since $\bar{2} \cdot \bar{3} = \bar{0}$.

**Example 4** (p. 229): The quadratic integer ring $\mathcal{O}$ is an integral domain.

# Relationships

## Builds Upon
- **commutative-ring** — With additional conditions

## Enables
- **field-of-fractions** — Every integral domain embeds in its field of fractions
- **unique-factorization-domain** — A UFD is an integral domain with unique factorization

## Contrasts With
- **field** — A field is an integral domain where every nonzero element is invertible

# Common Errors
- **Error**: Assuming every integral domain is a UFD
  **Correction**: $\mathbb{Z}[\sqrt{-5}]$ is an integral domain that is not a UFD

# Common Confusions
- **Confusion**: Thinking "no zero divisors" is the same as "every nonzero element is a unit"
  **Clarification**: No zero divisors means cancellation holds; being a unit means having a multiplicative inverse. $\mathbb{Z}$ has no zero divisors but $2$ is not a unit

# Source Reference
Chapter 7, Section 7.1, Definition on page 229. See Proposition 2 and Corollary 3 on page 229.

# Verification Notes
- Definition: Direct from p. 229
- Confidence: HIGH — explicit definition
