---
# === CORE IDENTIFICATION ===
concept: Modular Arithmetic
slug: modular-arithmetic

# === CLASSIFICATION ===
category: foundations
subcategory: number-theory
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Groups"
chapter_number: 3
pdf_page: 42
section: "Integer Equivalence Classes and Symmetries"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - arithmetic modulo n
  - clock arithmetic

# === TYPED RELATIONSHIPS ===
prerequisites:
  - integers-mod-n
  - division-algorithm
extends: []
related:
  - congruence-modulo-n
  - well-defined-function
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

Modular arithmetic is the system of addition and multiplication on the integers modulo $n$, where results are reduced to their remainder upon division by $n$.

# Core Definition

On $\mathbb{Z}_n$, addition is defined as $(a + b) \pmod{n}$ and multiplication as $(ab) \pmod{n}$ (Judson, p. 42). By Proposition 3.4, these operations satisfy commutativity, associativity, distributivity, and the existence of additive identities and inverses. Multiplicative inverses exist for $a$ if and only if $\gcd(a, n) = 1$.

# Prerequisites

- **Integers mod n** — Modular arithmetic operates on $\mathbb{Z}_n$
- **Division Algorithm** — Defines the remainder operation

# Key Properties

1. Addition is commutative and associative mod $n$
2. Multiplication is commutative and associative mod $n$
3. Distributive law: $a(b + c) \equiv ab + ac \pmod{n}$
4. Additive identity: 0; multiplicative identity: 1
5. Every element has an additive inverse: $a + (-a) \equiv 0$
6. $a$ has a multiplicative inverse iff $\gcd(a, n) = 1$ (Proposition 3.4, part 6)

# Construction / Recognition

## To Perform Modular Addition:
1. Add the integers normally
2. Take the remainder when divided by $n$

## To Perform Modular Multiplication:
1. Multiply the integers normally
2. Take the remainder when divided by $n$

# Context & Application

Modular arithmetic provides the algebraic structure for $\mathbb{Z}_n$ and is used extensively in cryptography, coding theory, error detection (UPC codes, ISBN codes), and computer science.

# Examples

**Example 1** (p. 42): $7 + 4 \equiv 1 \pmod{5}$, $7 \cdot 3 \equiv 1 \pmod{5}$, $3 + 5 \equiv 0 \pmod{8}$, $3 \cdot 5 \equiv 7 \pmod{8}$.

# Relationships

## Builds Upon
- **integers-mod-n** — Arithmetic on this set
- **division-algorithm** — Defines the remainder

## Enables
- **group** — $(\mathbb{Z}_n, +)$ is a group
- **group-of-units** — $(U(n), \cdot)$ is a group

# Common Errors

- **Error**: Performing operations on representatives without reducing mod $n$
  **Correction**: Always reduce the result modulo $n$

# Common Confusions

- **Confusion**: Thinking modular arithmetic behaves exactly like ordinary arithmetic
  **Clarification**: Important differences exist: zero divisors can occur ($3 \cdot 4 \equiv 0 \pmod{12}$) and not all nonzero elements have multiplicative inverses

# Source Reference

Chapter 3: Groups, Section 3.1, pages 42-43. Proposition 3.4.

# Verification Notes

- Definition source: Synthesized from Proposition 3.4 and surrounding text
- Confidence: HIGH — explicit properties listed
- Cross-reference status: Verified
- Uncertainties: None
