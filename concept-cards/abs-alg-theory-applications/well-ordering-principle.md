---
# === CORE IDENTIFICATION ===
concept: Well-Ordering Principle
slug: well-ordering-principle

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
pdf_page: 32
section: "Mathematical Induction"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - principle of well-ordering

# === TYPED RELATIONSHIPS ===
prerequisites:
  - set
extends: []
related:
  - mathematical-induction
  - division-algorithm
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

The Well-Ordering Principle states that every nonempty subset of the natural numbers contains a least element.

# Core Definition

A nonempty subset $S$ of $\mathbb{Z}$ is **well-ordered** if $S$ contains a least element. "Every nonempty subset of the natural numbers is well-ordered" (Principle 2.6, Judson, p. 32). The Principle of Well-Ordering is equivalent to the Principle of Mathematical Induction (Theorem 2.8).

# Prerequisites

- **Set** — Stated in terms of subsets of $\mathbb{N}$

# Key Properties

1. $\mathbb{N}$ is well-ordered
2. $\mathbb{Z}$ is NOT well-ordered (no smallest integer)
3. Equivalent to the Principle of Mathematical Induction
4. Used extensively in existence proofs (e.g., Division Algorithm)

# Construction / Recognition

## To Apply the Well-Ordering Principle:
1. Define a nonempty set $S \subset \mathbb{N}$
2. Conclude that $S$ has a smallest element
3. Use this smallest element in the proof

# Context & Application

The Well-Ordering Principle is used to prove the Division Algorithm, Bezout's Identity (Theorem 2.10), and many other fundamental results. It provides a powerful tool for existence proofs in number theory and algebra.

# Examples

**Example 1** (p. 33): In the proof of the Division Algorithm, the set $S = \{a - bk : k \in \mathbb{Z}, a - bk \geq 0\}$ is shown to be a nonempty subset of $\mathbb{N} \cup \{0\}$, so by Well-Ordering it has a smallest element $r$.

# Relationships

## Enables
- **division-algorithm** — Proof uses Well-Ordering
- **greatest-common-divisor** — Bezout's identity proof uses Well-Ordering

## Related
- **mathematical-induction** — Equivalent principle

# Common Errors

- **Error**: Applying the Well-Ordering Principle to $\mathbb{Z}$ or $\mathbb{Q}$
  **Correction**: The principle applies only to $\mathbb{N}$ (or nonempty subsets of $\mathbb{N}$); $\mathbb{Z}$ has no smallest element

# Common Confusions

- **Confusion**: Thinking well-ordering means the set is "ordered" in the usual sense
  **Clarification**: Well-ordering is stronger than being ordered; it requires that EVERY nonempty subset has a least element

# Source Reference

Chapter 2: The Integers, Section 2.1, Principle 2.6, page 32.

# Verification Notes

- Definition source: Direct from Principle 2.6, p. 32
- Confidence: HIGH — explicit axiom statement
- Cross-reference status: Verified
- Uncertainties: None
