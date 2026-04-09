---
# === CORE IDENTIFICATION ===
concept: Primitive Nth Root of Unity
slug: primitive-nth-root-of-unity

# === CLASSIFICATION ===
category: galois-theory
subcategory: solvability
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Galois Theory"
chapter_number: 23
pdf_page: 307
section: "23.3 Applications"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "primitive root of unity"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - nth-root-of-unity
  - cyclic-group
extends:
  - nth-root-of-unity
related:
  - bch-code
  - finite-field
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a primitive nth root of unity?"
---

# Quick Definition

A primitive $n$th root of unity is a generator of the cyclic group of $n$th roots of unity. Equivalently, $\omega$ is a primitive $n$th root of unity if $\omega^n = 1$ and $\omega^k \neq 1$ for $0 < k < n$.

# Core Definition

Any generator of the cyclic group of $n$th roots of unity is called a **primitive $n$th root of unity** (Judson, p. 317).

# Prerequisites

- **Nth root of unity** — A primitive root is a generator of the group of roots
- **Cyclic group** — The roots of unity form a cyclic group

# Key Properties

1. $\omega$ is primitive if and only if $\omega$ has order $n$ in the multiplicative group
2. There are $\phi(n)$ primitive $n$th roots of unity, where $\phi$ is Euler's totient function
3. Over $\mathbb{C}$: $\omega = e^{2\pi i/n} = \cos(2\pi/n) + i\sin(2\pi/n)$ is a primitive $n$th root
4. Over $GF(p^n)$: primitive roots of unity exist for $n \mid (p^n - 1)$

# Context & Application

Primitive roots of unity are essential in Galois theory (for studying cyclotomic extensions and solvability by radicals), in finite field theory (for constructing BCH codes), and in applied mathematics (FFT algorithms).

# Examples

**Example 1** (p. 317): $\omega = \cos(2\pi/n) + i\sin(2\pi/n)$ is a primitive $n$th root of unity in $\mathbb{C}$.

**Example 2** (p. 302): In $GF(2^4)$, $\alpha$ (a root of $1 + x + x^4$) is a primitive 15th root of unity.

# Relationships

## Builds Upon
- **Nth root of unity** — A primitive root generates all roots
- **Cyclic group** — It is a generator

## Related
- **BCH code** — Uses primitive roots of unity in $GF(2^n)$
- **Finite field** — Contains primitive roots of unity

# Source Reference

Chapter 23: Galois Theory, Section 23.3, page 317.

# Verification Notes

- Definition source: Direct from p. 317
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
