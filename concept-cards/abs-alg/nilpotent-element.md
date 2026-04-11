---
concept: Nilpotent Element
slug: nilpotent-element
category: ring-theory
subcategory: ring-elements
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 233
section: "7.1 Basic Definitions and Examples"
extraction_confidence: high
aliases: []
prerequisites:
  - ring
extends: []
related:
  - nilradical
  - zero-divisor
contrasts_with:
  - unit
answers_questions:
  - "What is a nilpotent element?"
  - "How do nilpotent elements relate to zero divisors?"
---

# Quick Definition
An element $x$ in a ring R is nilpotent if $x^m = 0$ for some positive integer m.

# Core Definition
An element $x$ in R is called *nilpotent* if $x^m = 0$ for some $m \in \mathbb{Z}^+$ (Exercise 13, Dummit & Foote, p. 233).

# Prerequisites
- **Ring** — Nilpotent elements are elements of a ring

# Key Properties
1. A nilpotent element is either zero or a zero divisor (Exercise 14(a), p. 234)
2. If x is nilpotent and R is commutative, then $rx$ is nilpotent for all $r \in R$ (Exercise 14(b))
3. If x is nilpotent in a commutative ring with 1, then $1 + x$ is a unit (Exercise 14(c))
4. The sum of a nilpotent element and a unit is a unit (Exercise 14(d))
5. In a commutative ring, the set of nilpotent elements forms an ideal (the nilradical, Exercise 29, p. 251)

# Construction / Recognition
## To Recognize:
1. Check if some positive power of x equals 0
2. In $\mathbb{Z}/n\mathbb{Z}$: $\bar{a}$ is nilpotent iff every prime divisor of n divides a (Exercise 13(b))

# Context & Application
Nilpotent elements represent "infinitesimal" elements algebraically. They arise in quotient rings and are important in algebraic geometry (nilpotent elements correspond to non-reduced structure).

# Examples
**Example 1** (p. 233): In $\mathbb{Z}/8\mathbb{Z}$, $\bar{2}$ is nilpotent since $\bar{2}^3 = \bar{8} = \bar{0}$.

**Example 2** (p. 233): The nilpotent elements of $\mathbb{Z}/72\mathbb{Z}$ are the multiples of 6 (since $72 = 2^3 \cdot 3^2$).

# Relationships

## Related
- **nilradical** — The ideal of all nilpotent elements in a commutative ring
- **zero-divisor** — Every nonzero nilpotent element is a zero divisor

## Contrasts With
- **unit** — A unit cannot be nilpotent (since $u^m \neq 0$ for a unit)

# Common Errors
- **Error**: Assuming the set of nilpotent elements is an ideal in noncommutative rings
  **Correction**: In $M_2(\mathbb{Z})$, the sum of two nilpotent matrices need not be nilpotent (Exercise 31, p. 251)

# Common Confusions
- **Confusion**: Confusing nilpotent elements with zero divisors
  **Clarification**: Every nonzero nilpotent is a zero divisor, but not every zero divisor is nilpotent

# Source Reference
Chapter 7, Section 7.1, Exercise 13, page 233. See also Section 7.3 Exercises 29-30.

# Verification Notes
- Definition: From Exercise 13, p. 233
- Properties: From Exercises 14, 29 in later sections
- Confidence: HIGH — explicit definition in exercises, used throughout
