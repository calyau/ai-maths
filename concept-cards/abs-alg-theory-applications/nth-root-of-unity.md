---
# === CORE IDENTIFICATION ===
concept: Nth Root of Unity
slug: nth-root-of-unity

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
  - "root of unity"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cyclic-group
  - splitting-field
extends: []
related:
  - primitive-nth-root-of-unity
  - solvable-by-radicals
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an nth root of unity?"
  - "What group do the nth roots of unity form?"
---

# Quick Definition

The $n$th roots of unity are the roots of the polynomial $x^n - 1$. They form a cyclic group of order $n$ under multiplication.

# Core Definition

The roots of $x^n - 1$ are called the **$n$th roots of unity**. These roots form a finite subgroup of the splitting field of $x^n - 1$. By Corollary 22.11, the $n$th roots of unity form a cyclic group (Judson, p. 317).

Over $\mathbb{C}$, the $n$th roots of unity are $1, \omega, \omega^2, \ldots, \omega^{n-1}$ where $\omega = \cos(2\pi/n) + i\sin(2\pi/n)$.

# Prerequisites

- **Cyclic group** — The roots of unity form a cyclic group
- **Splitting field** — The roots live in the splitting field of $x^n - 1$

# Key Properties

1. The $n$th roots of unity form a cyclic group of order $n$
2. Any generator of this group is a primitive $n$th root of unity
3. $x^n - 1$ is always solvable by radicals (Example 23.27)
4. The Galois group of $x^n - 1$ over $\mathbb{Q}$ is abelian

# Examples

**Example 1** (p. 317): The roots of $x^n - 1$ over $\mathbb{Q}$ are $1, \omega, \omega^2, \ldots, \omega^{n-1}$ where $\omega = \cos(2\pi/n) + i\sin(2\pi/n)$. The splitting field is $\mathbb{Q}(\omega)$.

# Relationships

## Enables
- **Primitive nth root of unity** — A generator of the cyclic group of roots of unity
- **Solvable by radicals** — $x^n - a$ is solvable because it involves roots of unity

# Source Reference

Chapter 23: Galois Theory, Section 23.3, page 317. Also Chapter 4 and Corollary 22.11.

# Verification Notes

- Definition source: Direct from p. 317
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
