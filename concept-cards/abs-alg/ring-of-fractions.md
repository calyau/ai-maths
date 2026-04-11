---
concept: Ring of Fractions
slug: ring-of-fractions
category: ring-theory
subcategory: ring-constructions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 260
section: "7.5 Rings of Fractions"
extraction_confidence: high
aliases:
  - "localization"
  - "ring of quotients"
prerequisites:
  - commutative-ring
  - zero-divisor
extends: []
related:
  - field-of-fractions
  - integral-domain
contrasts_with:
  - field-of-fractions
answers_questions:
  - "What is a ring of fractions?"
  - "How do we invert non-zero-divisors in a commutative ring?"
---

# Quick Definition
The ring of fractions $D^{-1}R$ of a commutative ring R with respect to a multiplicatively closed set D of non-zero-divisors is the ring of equivalence classes of pairs $(r, d)$ with $r \in R$, $d \in D$, where $\frac{r}{d} = \frac{s}{e}$ iff $re = sd$.

# Core Definition
Let R be a commutative ring and D a nonempty subset of R that does not contain 0, contains no zero divisors, and is closed under multiplication. The *ring of fractions* $D^{-1}R$ is the set of equivalence classes $\frac{r}{d}$ under the relation $(r, d) \sim (s, e)$ iff $re = sd$, with arithmetic $\frac{a}{b} + \frac{c}{d} = \frac{ad+bc}{bd}$ and $\frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd}$ (Theorem 15, Dummit & Foote, pp. 260-262).

# Prerequisites
- **Commutative ring** — R must be commutative
- **Zero divisor** — D must avoid zero divisors

# Key Properties
1. $D^{-1}R$ is a commutative ring with identity containing R as a subring (Theorem 15)
2. Every element of D is a unit in $D^{-1}R$
3. Every element of $D^{-1}R$ has the form $rd^{-1}$ for $r \in R$, $d \in D$
4. If $D = R - \{0\}$ (and R is an integral domain), $D^{-1}R$ is a field
5. $D^{-1}R$ is the smallest ring in which all elements of D become units (uniqueness, Theorem 15(2))

# Construction / Recognition
## To Construct:
1. Choose a multiplicatively closed set D of non-zero-divisors
2. Form pairs $(r, d)$ with $r \in R$, $d \in D$
3. Define equivalence: $(r, d) \sim (s, e)$ iff $re = sd$
4. Define arithmetic on equivalence classes as for fractions

# Context & Application
The ring of fractions generalizes the construction of $\mathbb{Q}$ from $\mathbb{Z}$. It allows "inverting" specified elements while preserving the ring structure.

# Examples
**Example 1** (p. 264): $\mathbb{Q}$ is the ring of fractions of $\mathbb{Z}$ with $D = \mathbb{Z} - \{0\}$.

**Example 2** (p. 264): For an integral domain R, $R[x]$ has field of fractions = the field of rational functions $R(x)$.

**Example 3** (p. 265): $R[1/d]$ for a non-zero-divisor d uses $D = \{1, d, d^2, \ldots\}$.

# Relationships

## Related
- **field-of-fractions** — Special case when R is an integral domain and $D = R - \{0\}$
- **integral-domain** — The most important case for field of fractions

## Contrasts With
- **field-of-fractions** — Field of fractions is the special case giving a field

# Common Errors
- **Error**: Trying to include zero divisors in D
  **Correction**: If $bd = 0$, then $d/1 = 0/b = 0$, causing unwanted collapsing

# Common Confusions
- **Confusion**: Thinking the ring of fractions always gives a field
  **Clarification**: Only when $D = R - \{0\}$ and R is an integral domain

# Source Reference
Chapter 7, Section 7.5, Theorem 15, pages 260-264.

# Verification Notes
- Definition: Direct from Theorem 15, pp. 260-262
- Confidence: HIGH — complete theorem with proof
