---
# === CORE IDENTIFICATION ===
concept: Commutative Ring
slug: commutative-ring

# === CLASSIFICATION ===
category: ring-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Rings"
chapter_number: 16
pdf_page: 204
section: "16.1 Rings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ring
extends:
  - ring
related:
  - ring-with-unity
  - integral-domain
contrasts_with:
  - noncommutative-ring

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a commutative ring?"
  - "What distinguishes a ring from a commutative ring?"
---

# Quick Definition

A commutative ring is a ring in which multiplication is commutative: $ab = ba$ for all elements $a$ and $b$.

# Core Definition

"A ring $R$ for which $ab = ba$ for all $a, b$ in $R$ is called a commutative ring" (Judson, p. 204). This adds commutativity of multiplication to the six ring axioms.

# Prerequisites

- **Ring** — A commutative ring is a ring with an additional property

# Key Properties

1. All ring axioms are satisfied
2. Multiplication is commutative: $ab = ba$ for all $a, b \in R$
3. Left and right ideals coincide (every ideal is two-sided)

# Construction / Recognition

## To Verify:
1. Verify all ring axioms
2. Check that $ab = ba$ for all $a, b \in R$

## To Recognize:
1. Integer-like structures are typically commutative
2. Matrix rings and quaternion rings are typically not commutative

# Context & Application

Most rings encountered in number theory and algebraic geometry are commutative. The study of commutative rings (commutative algebra) is a major branch of algebra, foundational to algebraic geometry and algebraic number theory.

# Examples

**Example 1** (p. 204): $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, and $\mathbb{C}$ are all commutative rings.

**Example 2** (p. 205): $\mathbb{Z}_n$ is a commutative ring under modular arithmetic.

**Example 3** (p. 205): The continuous real-valued functions on $[a, b]$ form a commutative ring.

# Relationships

## Builds Upon
- **Ring** — A commutative ring is a ring with commutative multiplication

## Enables
- **Integral domain** — A commutative ring with identity and no zero divisors
- **Field** — A commutative division ring

## Contrasts With
- **Matrix ring** — $M_2(\mathbb{R})$ is a ring where $AB \neq BA$ in general

# Common Errors

- **Error**: Assuming all subrings of a commutative ring inherit all properties
  **Correction**: Subrings always inherit commutativity, but may not inherit the identity element

# Common Confusions

- **Confusion**: Believing commutativity of addition is the distinguishing feature
  **Clarification**: All rings have commutative addition; a commutative ring has commutative *multiplication*

# Source Reference

Chapter 16: Rings, Section 16.1, page 204.

# Verification Notes

- Definition source: Direct quote from p. 204
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
