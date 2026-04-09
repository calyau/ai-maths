---
# === CORE IDENTIFICATION ===
concept: Multiplicative Inverse Modulo n
slug: multiplicative-inverse-mod-n

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
pdf_page: 43
section: "Integer Equivalence Classes and Symmetries"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - integers-mod-n
  - relatively-prime
  - bezouts-identity
extends: []
related:
  - group-of-units
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
  - "How do I determine if a set with an operation forms a group?"
---

# Quick Definition

An element $a \in \mathbb{Z}_n$ has a multiplicative inverse (an element $b$ with $ab \equiv 1 \pmod{n}$) if and only if $\gcd(a, n) = 1$.

# Core Definition

**Proposition 3.4, part 6**: "Let $a$ be a nonzero integer. Then $\gcd(a, n) = 1$ if and only if there exists a multiplicative inverse $b$ for $a$ (mod $n$); that is, a nonzero integer $b$ such that $ab \equiv 1 \pmod{n}$" (Judson, p. 43).

# Prerequisites

- **Integers mod n** — Inverses are in $\mathbb{Z}_n$
- **Relatively prime** — Existence requires $\gcd(a, n) = 1$
- **Bezout's identity** — Proof uses $ar + ns = 1$

# Key Properties

1. Exists iff $\gcd(a, n) = 1$
2. Can be found via the Extended Euclidean Algorithm
3. Elements with inverses form the group $U(n)$
4. The inverse is unique modulo $n$

# Construction / Recognition

## To Find the Inverse of $a$ mod $n$:
1. Use the Extended Euclidean Algorithm to find $r, s$ with $ar + ns = 1$
2. Then $b = r \pmod{n}$ is the multiplicative inverse

# Examples

**Example 1** (p. 42): In $\mathbb{Z}_5$: $7 \cdot 3 \equiv 21 \equiv 1 \pmod{5}$, so 3 is the inverse of 7 (equivalently, of 2).

**Example 2** (p. 42): In $\mathbb{Z}_8$, 2 has no multiplicative inverse since $\gcd(2, 8) = 2 \neq 1$.

# Relationships

## Builds Upon
- **relatively-prime** — Existence criterion
- **bezouts-identity** — Construction method

## Enables
- **group-of-units** — Elements with inverses form $U(n)$

# Common Errors

- **Error**: Assuming every nonzero element has an inverse
  **Correction**: Only elements coprime to $n$ have multiplicative inverses

# Source Reference

Chapter 3: Groups, Section 3.1, Proposition 3.4, page 43.

# Verification Notes

- Definition source: Direct from Proposition 3.4, part 6
- Confidence: HIGH — explicit proposition with proof
- Cross-reference status: Verified
- Uncertainties: None
