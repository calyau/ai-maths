---
# === CORE IDENTIFICATION ===
concept: Division Ring
slug: division-ring

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
aliases:
  - "skew field"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ring-with-unity
  - unit-in-ring
extends:
  - ring-with-unity
related:
  - quaternions
contrasts_with:
  - field
  - integral-domain

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a division ring?"
  - "What distinguishes a division ring from a field?"
---

# Quick Definition

A division ring is a ring with identity in which every nonzero element is a unit (has a multiplicative inverse). Unlike a field, multiplication need not be commutative.

# Core Definition

"A division ring is a ring $R$, with an identity, in which every nonzero element in $R$ is a unit; that is, for each $a \in R$ with $a \neq 0$, there exists a unique element $a^{-1}$ such that $a^{-1}a = aa^{-1} = 1$" (Judson, p. 204).

# Prerequisites

- **Ring with unity** — A division ring must have a multiplicative identity
- **Unit in ring** — Every nonzero element must be a unit

# Key Properties

1. Has multiplicative identity $1 \neq 0$
2. Every nonzero element has a multiplicative inverse
3. Multiplication need not be commutative
4. Has no zero divisors (if $ab = 0$ and $a \neq 0$, multiply by $a^{-1}$)

# Construction / Recognition

## To Verify:
1. Confirm $R$ is a ring with identity
2. Show every nonzero element $a$ has an inverse $a^{-1}$ with $aa^{-1} = a^{-1}a = 1$

# Context & Application

Division rings generalize fields by dropping the commutativity requirement for multiplication. The quaternions $\mathbb{H}$ are the most important example of a noncommutative division ring. By Wedderburn's theorem, every finite division ring is a field.

# Examples

**Example 1** (p. 205): The quaternions $\mathbb{H}$ form a noncommutative division ring. Elements have the form $a + b\mathbf{i} + c\mathbf{j} + d\mathbf{k}$ where $\mathbf{i}^2 = \mathbf{j}^2 = \mathbf{k}^2 = -1$. The inverse of a nonzero quaternion $a + b\mathbf{i} + c\mathbf{j} + d\mathbf{k}$ is $\frac{a - b\mathbf{i} - c\mathbf{j} - d\mathbf{k}}{a^2 + b^2 + c^2 + d^2}$.

**Example 2** (p. 205): Every field is a (commutative) division ring.

# Relationships

## Builds Upon
- **Ring with unity** — Adds the condition that every nonzero element is invertible

## Enables
- **Field** — A commutative division ring is a field

## Contrasts With
- **Field** — A field is a commutative division ring; the quaternions show division rings need not be commutative
- **Integral domain** — An integral domain has no zero divisors but elements need not have inverses

# Common Errors

- **Error**: Assuming all division rings are fields
  **Correction**: The quaternions $\mathbb{H}$ are a division ring but not a field since $\mathbf{i}\mathbf{j} = \mathbf{k} \neq -\mathbf{k} = \mathbf{j}\mathbf{i}$

# Common Confusions

- **Confusion**: Confusing division ring with integral domain
  **Clarification**: In a division ring every nonzero element has an inverse; in an integral domain there are merely no zero divisors. $\mathbb{Z}$ is an integral domain but not a division ring.

# Source Reference

Chapter 16: Rings, Section 16.1, pages 204-207. See especially Example 16.7 (quaternions).

# Verification Notes

- Definition source: Direct quote from p. 204
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
