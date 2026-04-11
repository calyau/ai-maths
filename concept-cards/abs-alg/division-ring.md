---
concept: Division Ring
slug: division-ring
category: ring-theory
subcategory: basic-definitions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 223
section: "7.1 Basic Definitions and Examples"
extraction_confidence: high
aliases:
  - "skew field"
prerequisites:
  - ring-with-identity
  - unit
extends:
  - ring-with-identity
related:
  - field
  - hamilton-quaternions
contrasts_with:
  - field
  - integral-domain
answers_questions:
  - "What is a division ring?"
  - "What is a skew field?"
  - "What distinguishes a division ring from a field?"
---

# Quick Definition
A division ring (or skew field) is a ring with identity $1 \neq 0$ in which every nonzero element has a multiplicative inverse.

# Core Definition
A ring R with identity $1 \neq 0$ is called a *division ring* (or *skew field*) if every nonzero element $a \in R$ has a multiplicative inverse, i.e., there exists $b \in R$ such that $ab = ba = 1$. A commutative division ring is called a *field* (Dummit & Foote, p. 224).

# Prerequisites
- **Ring with identity** — Must have a multiplicative identity $1 \neq 0$
- **Unit** — Every nonzero element must be a unit

# Key Properties
1. Every nonzero element is a unit: $R^{\times} = R - \{0\}$
2. Contains no zero divisors (since units cannot be zero divisors)
3. If D is finite, then D is necessarily commutative (Wedderburn's theorem, p. 229)
4. Only left/right ideals are 0 and D (p. 258)

# Construction / Recognition
## To Recognize:
1. Verify R is a ring with $1 \neq 0$
2. Check that every nonzero element has a two-sided multiplicative inverse

# Context & Application
Division rings are important in the study of noncommutative algebra. Wedderburn's theorem shows that every finite division ring is a field, so noncommutative division rings must be infinite.

# Examples
**Example 1** (p. 225): The real Hamilton Quaternions $\mathbb{H}$ form a noncommutative division ring, with inverses given by $(a+bi+cj+dk)^{-1} = \frac{a-bi-cj-dk}{a^2+b^2+c^2+d^2}$.

**Example 2** (p. 224): $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ are commutative division rings (i.e., fields).

# Relationships

## Builds Upon
- **ring-with-identity** — A ring with identity where all nonzero elements are units

## Enables
- **field** — A commutative division ring

## Contrasts With
- **field** — A field is a *commutative* division ring
- **integral-domain** — Has no zero divisors but elements need not be invertible

# Common Errors
- **Error**: Assuming all division rings are fields
  **Correction**: The Hamilton Quaternions $\mathbb{H}$ are a noncommutative division ring

# Common Confusions
- **Confusion**: Thinking "skew field" means something different from "division ring"
  **Clarification**: These are synonymous terms

# Source Reference
Chapter 7, Section 7.1, Definition following the ring axioms, page 224.

# Verification Notes
- Definition: Direct from p. 224
- Confidence: HIGH — explicit definition
