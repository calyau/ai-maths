---
# === CORE IDENTIFICATION ===
concept: Finite Field
slug: finite-field

# === CLASSIFICATION ===
category: field-theory
subcategory: finite-fields
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Finite Fields"
chapter_number: 22
pdf_page: 292
section: "22.1 Structure of a Finite Field"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Galois field"
  - "GF(p^n)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - field
  - characteristic-of-a-field
  - extension-field
extends:
  - field
related:
  - splitting-field
  - cyclic-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a finite field from an infinite field?"
  - "How many elements can a finite field have?"
  - "Are finite fields unique?"
---

# Quick Definition

A finite field is a field with finitely many elements. For every prime $p$ and positive integer $n$, there exists a unique (up to isomorphism) finite field with $p^n$ elements, denoted $GF(p^n)$.

# Core Definition

A finite field has a finite number of elements. By Proposition 22.2, if $F$ is a finite field of characteristic $p$, then the order of $F$ is $p^n$ for some positive integer $n$. By Theorem 22.6, for every prime $p$ and every positive integer $n$, there exists a finite field $F$ with $p^n$ elements, and any field of order $p^n$ is isomorphic to the splitting field of $x^{p^n} - x$ over $\mathbb{Z}_p$ (Judson, pp. 292–294).

The unique finite field with $p^n$ elements is called the **Galois field** of order $p^n$, denoted $GF(p^n)$ (p. 294).

# Prerequisites

- **Field** — Finite fields are fields
- **Characteristic of a field** — Finite fields have prime characteristic
- **Extension field** — Finite fields of order $p^n$ are extensions of $\mathbb{Z}_p$

# Key Properties

1. The characteristic of a finite field is prime (Proposition 22.1)
2. The order is $p^n$ where $p$ is the characteristic (Proposition 22.2)
3. $GF(p^n)$ is the splitting field of $x^{p^n} - x$ over $\mathbb{Z}_p$ (Theorem 22.6)
4. $GF(p^n)$ is unique up to isomorphism (Theorem 22.6)
5. The multiplicative group $GF(p^n)^*$ is cyclic of order $p^n - 1$ (Corollary 22.11)
6. Every subfield has order $p^m$ where $m \mid n$, and conversely (Theorem 22.7)
7. Every finite extension of a finite field is a simple extension (Corollary 22.12)

# Construction / Recognition

## To Construct:
1. Choose a prime $p$ and positive integer $n$
2. Find an irreducible polynomial $f(x)$ of degree $n$ in $\mathbb{Z}_p[x]$
3. Form $\mathbb{Z}_p[x]/\langle f(x) \rangle$
4. This field has $p^n$ elements and is $GF(p^n)$

## To Recognize:
1. Verify the set is a field
2. Count elements: must be $p^n$ for some prime $p$ and positive integer $n$

# Context & Application

Finite fields appear throughout algebra, coding theory, and cryptography. BCH codes and other error-correcting codes are built over finite fields. Finite fields are also called Galois fields in honor of Evariste Galois.

# Examples

**Example 1** (p. 275): $GF(4) = \mathbb{Z}_2[x]/\langle x^2 + x + 1 \rangle$ has elements $\{0, 1, \alpha, 1 + \alpha\}$ where $\alpha^2 + \alpha + 1 = 0$.

**Example 2** (p. 295): $GF(2^4) \cong \mathbb{Z}_2[x]/\langle 1 + x + x^4 \rangle$ has 16 elements. Its multiplicative group is isomorphic to $\mathbb{Z}_{15}$ with generator $\alpha$.

**Example 3** (p. 294): The lattice of subfields of $GF(p^{24})$ reflects the divisors of 24.

# Relationships

## Builds Upon
- **Field** — Finite fields are fields
- **Extension field** — $GF(p^n)$ extends $\mathbb{Z}_p$

## Enables
- **Polynomial code** — Built over finite fields
- **BCH code** — Uses roots of unity in finite fields
- **Frobenius automorphism** — The key automorphism of finite fields

## Related
- **Splitting field** — $GF(p^n)$ is the splitting field of $x^{p^n} - x$
- **Cyclic group** — The multiplicative group is cyclic

# Common Errors

- **Error**: Trying to construct a finite field with 6 elements
  **Correction**: Finite fields have order $p^n$ for prime $p$; since 6 is not a prime power, there is no field with 6 elements

# Common Confusions

- **Confusion**: Thinking $\mathbb{Z}_n$ is a field for all $n$
  **Clarification**: $\mathbb{Z}_n$ is a field only when $n$ is prime. For prime powers $p^n > p$, the finite field $GF(p^n)$ is not $\mathbb{Z}_{p^n}$

# Source Reference

Chapter 22: Finite Fields, Section 22.1, pages 292–296. See Propositions 22.1, 22.2, Theorem 22.6, 22.7, Corollaries 22.11, 22.12.

# Verification Notes

- Definition source: Synthesized from multiple results in Section 22.1
- Confidence: HIGH — explicit theorems and constructions
- Cross-reference status: Verified
- Uncertainties: None
