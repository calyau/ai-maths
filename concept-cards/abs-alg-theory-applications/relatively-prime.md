---
# === CORE IDENTIFICATION ===
concept: Relatively Prime
slug: relatively-prime

# === CLASSIFICATION ===
category: foundations
subcategory: number-theory
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Integers"
chapter_number: 2
pdf_page: 33
section: "The Division Algorithm"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - coprime

# === TYPED RELATIONSHIPS ===
prerequisites:
  - greatest-common-divisor
extends: []
related:
  - group-of-units
  - bezouts-identity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

Two integers $a$ and $b$ are relatively prime (or coprime) if their greatest common divisor is 1: $\gcd(a, b) = 1$.

# Core Definition

"We say that two integers $a$ and $b$ are relatively prime if $\gcd(a, b) = 1$" (Judson, p. 33).

**Corollary 2.11**: If $a$ and $b$ are relatively prime, then there exist integers $r$ and $s$ such that $ar + bs = 1$.

# Prerequisites

- **Greatest common divisor** — Defined as $\gcd(a, b) = 1$

# Key Properties

1. $\gcd(a, b) = 1$ if and only if there exist integers $r, s$ with $ar + bs = 1$
2. If $p$ is prime and $p \nmid a$, then $\gcd(a, p) = 1$
3. An element $a$ has a multiplicative inverse in $\mathbb{Z}_n$ if and only if $\gcd(a, n) = 1$

# Construction / Recognition

## To Check if $a$ and $b$ are Relatively Prime:
1. Compute $\gcd(a, b)$ using the Euclidean Algorithm
2. If $\gcd(a, b) = 1$, they are relatively prime

# Context & Application

Relative primality determines which elements of $\mathbb{Z}_n$ have multiplicative inverses, which in turn defines the group of units $U(n)$. It also determines which elements generate cyclic groups: $r$ generates $\mathbb{Z}_n$ if and only if $\gcd(r, n) = 1$.

# Examples

**Example 1** (p. 33): $\gcd(24, 36) = 12 \neq 1$, so 24 and 36 are NOT relatively prime.

**Example 2**: $\gcd(8, 15) = 1$, so 8 and 15 are relatively prime.

# Relationships

## Builds Upon
- **greatest-common-divisor** — Defined via GCD

## Enables
- **group-of-units** — $U(n) = \{a \in \mathbb{Z}_n : \gcd(a, n) = 1\}$
- **generator** — Generators of $\mathbb{Z}_n$ are elements relatively prime to $n$

# Common Confusions

- **Confusion**: Thinking relatively prime means both numbers are prime
  **Clarification**: "Relatively prime" means their GCD is 1; neither number needs to be prime (e.g., 8 and 15)

# Source Reference

Chapter 2: The Integers, Section 2.2, page 33. Corollary 2.11.

# Verification Notes

- Definition source: Direct from p. 33
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
