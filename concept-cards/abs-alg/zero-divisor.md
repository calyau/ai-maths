---
concept: Zero Divisor
slug: zero-divisor
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
aliases: []
prerequisites:
  - ring
extends: []
related:
  - unit
  - integral-domain
  - nilpotent-element
contrasts_with:
  - unit
answers_questions:
  - "What is a zero divisor in a ring?"
  - "Can a unit be a zero divisor?"
---

# Quick Definition
A nonzero element a of a ring R is a zero divisor if there exists a nonzero element b in R such that $ab = 0$ or $ba = 0$.

# Core Definition
A nonzero element a of R is called a *zero divisor* if there is a nonzero element b in R such that either $ab = 0$ or $ba = 0$ (Dummit & Foote, p. 227).

# Prerequisites
- **Ring** — Zero divisors are elements of a ring

# Key Properties
1. A zero divisor can never be a unit (p. 227)
2. Fields contain no zero divisors (p. 228)
3. In $\mathbb{Z}/n\mathbb{Z}$, every nonzero element is either a unit or a zero divisor (p. 228)
4. In $\mathbb{Z}/n\mathbb{Z}$, $\bar{a}$ is a zero divisor iff $\gcd(a, n) > 1$ (p. 228)

# Construction / Recognition
## To Identify:
1. Find a nonzero element a such that $ab = 0$ for some nonzero b
2. In $\mathbb{Z}/n\mathbb{Z}$: $\bar{a}$ is a zero divisor iff a and n share a common factor greater than 1

# Context & Application
Zero divisors are obstructions to cancellation in rings. Their absence defines integral domains, where many familiar properties of integer arithmetic hold.

# Examples
**Example 1** (p. 228): In $\mathbb{Z}/6\mathbb{Z}$, $\bar{2}$ and $\bar{3}$ are zero divisors since $\bar{2} \cdot \bar{3} = \bar{0}$.

**Example 2** (p. 228): In the ring of functions from $[0,1]$ to $\mathbb{R}$, any non-unit nonzero function is a zero divisor.

**Example 3** (p. 228): $M_n(R)$ has zero divisors for all nonzero rings R when $n \geq 2$ (p. 244).

# Relationships

## Related
- **integral-domain** — An integral domain has no zero divisors
- **nilpotent-element** — A nilpotent element is either zero or a zero divisor

## Contrasts With
- **unit** — A unit can never be a zero divisor

# Common Errors
- **Error**: Calling 0 a zero divisor
  **Correction**: By definition, zero divisors are *nonzero* elements

# Common Confusions
- **Confusion**: Thinking that in any ring, an element is either a unit or a zero divisor
  **Clarification**: This holds in $\mathbb{Z}/n\mathbb{Z}$ but not in general; e.g., in the ring of continuous functions on $[0,1]$, $f(x) = x - 1/2$ is neither a unit nor a zero divisor (p. 228)

# Source Reference
Chapter 7, Section 7.1, Definition (1), page 227.

# Verification Notes
- Definition: Direct from p. 227
- Confidence: HIGH — explicit definition
