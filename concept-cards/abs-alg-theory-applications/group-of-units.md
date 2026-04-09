---
# === CORE IDENTIFICATION ===
concept: Group of Units
slug: group-of-units

# === CLASSIFICATION ===
category: group-theory
subcategory: group-examples
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Groups"
chapter_number: 3
pdf_page: 48
section: "Definitions and Examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "U(n)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - integers-mod-n
  - relatively-prime
  - group
extends: []
related:
  - cyclic-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
  - "How do I determine if a set with an operation forms a group?"
---

# Quick Definition

The group of units $U(n)$ is the set of all elements in $\mathbb{Z}_n$ that are relatively prime to $n$, forming a group under multiplication modulo $n$.

# Core Definition

"Denote the set of all such nonzero elements in $\mathbb{Z}_n$ [that have multiplicative inverses] by $U(n)$. Then $U(n)$ is a group called the group of units of $\mathbb{Z}_n$" (Judson, p. 48). By Proposition 3.4, an element $a$ has a multiplicative inverse mod $n$ if and only if $\gcd(a, n) = 1$.

# Prerequisites

- **Integers mod n** — $U(n) \subset \mathbb{Z}_n$
- **Relatively prime** — Elements of $U(n)$ satisfy $\gcd(a, n) = 1$
- **Group** — $U(n)$ satisfies the group axioms

# Key Properties

1. $U(n) = \{a \in \mathbb{Z}_n : \gcd(a, n) = 1\}$
2. The group operation is multiplication modulo $n$
3. The identity element is 1
4. $|U(n)| = \phi(n)$ (Euler's totient function)
5. $U(n)$ may or may not be cyclic

# Construction / Recognition

## To Construct $U(n)$:
1. List all integers from 1 to $n - 1$
2. Keep only those relatively prime to $n$
3. The resulting set with multiplication mod $n$ is $U(n)$

# Context & Application

$U(n)$ is an important example of a finite group. When $n$ is prime, $U(n) = \{1, 2, \ldots, n-1\}$ and is cyclic. $U(n)$ appears in cryptography (RSA) and in determining generators of cyclic groups.

# Examples

**Example 1** (p. 48): $U(8) = \{1, 3, 5, 7\}$ with multiplication table shown in Figure 3.12.

**Example 2** (p. 60): $U(9) = \{1, 2, 4, 5, 7, 8\}$ is cyclic with generator 2.

# Relationships

## Builds Upon
- **integers-mod-n** — $U(n) \subset \mathbb{Z}_n$
- **relatively-prime** — Membership criterion

## Related
- **cyclic-group** — $U(n)$ is sometimes cyclic

# Common Errors

- **Error**: Including 0 in $U(n)$
  **Correction**: 0 never has a multiplicative inverse; $U(n)$ only contains nonzero elements coprime to $n$

# Common Confusions

- **Confusion**: Assuming $U(n)$ is always cyclic
  **Clarification**: $U(8) = \{1, 3, 5, 7\}$ is NOT cyclic (every element has order 1 or 2)

# Source Reference

Chapter 3: Groups, Section 3.2, page 48. Figure 3.12.

# Verification Notes

- Definition source: Direct from p. 48
- Confidence: HIGH — explicit definition with examples
- Cross-reference status: Verified
- Uncertainties: None
