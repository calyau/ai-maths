---
# === CORE IDENTIFICATION ===
concept: Mathematical Induction
slug: mathematical-induction

# === CLASSIFICATION ===
category: foundations
subcategory: proof-techniques
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Integers"
chapter_number: 2
pdf_page: 30
section: "Mathematical Induction"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - first principle of mathematical induction
  - proof by induction
  - induction

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mathematical-proof
extends: []
related:
  - well-ordering-principle
  - second-principle-of-induction
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
  - "What is mathematical induction?"
---

# Quick Definition

Mathematical induction is a proof technique for establishing that a statement $S(n)$ holds for all integers $n \geq n_0$: prove the base case $S(n_0)$, then show that $S(k)$ implies $S(k+1)$.

# Core Definition

**Principle 2.1 (First Principle of Mathematical Induction)**: "Let $S(n)$ be a statement about integers for $n \in \mathbb{N}$ and suppose $S(n_0)$ is true for some integer $n_0$. If for all integers $k$ with $k \geq n_0$, $S(k)$ implies that $S(k+1)$ is true, then $S(n)$ is true for all integers $n$ greater than or equal to $n_0$" (Judson, p. 30).

# Prerequisites

- **Mathematical proof** — Induction is a proof technique

# Key Properties

1. Requires a **base case**: verifying $S(n_0)$
2. Requires an **inductive step**: showing $S(k) \Rightarrow S(k+1)$ for all $k \geq n_0$
3. The assumption $S(k)$ in the inductive step is called the **induction hypothesis**
4. Equivalent to the Principle of Well-Ordering (Theorem 2.8)
5. Can be used for both proofs and definitions (recursive definitions)

# Construction / Recognition

## To Prove by Induction:
1. State clearly what $S(n)$ is
2. **Base case**: Verify $S(n_0)$ is true
3. **Inductive step**: Assume $S(k)$ is true for some $k \geq n_0$ (induction hypothesis)
4. Show that $S(k+1)$ follows from $S(k)$
5. Conclude $S(n)$ is true for all $n \geq n_0$

# Context & Application

Induction is used throughout abstract algebra to prove results about integers, groups, and other structures. It is essential for proving the uniqueness part of the Fundamental Theorem of Arithmetic and for establishing properties of group elements raised to integer powers.

# Examples

**Example 1** (p. 30): Prove $1 + 2 + \cdots + n = \frac{n(n+1)}{2}$. Base case $n = 1$: $1 = \frac{1(2)}{2}$. Inductive step: assuming the formula for $n$, then $1 + 2 + \cdots + n + (n+1) = \frac{n(n+1)}{2} + (n+1) = \frac{(n+1)(n+2)}{2}$.

**Example 2** (p. 31): For all $n \geq 3$, $2^n > n + 4$. Base case $n = 3$: $8 > 7$. Inductive step uses $2^{k+1} = 2 \cdot 2^k > 2(k+4) > (k+1) + 4$.

# Relationships

## Builds Upon
- **mathematical-proof** — Induction is a proof technique

## Enables
- **binomial-theorem** — Proved by induction
- **fundamental-theorem-of-arithmetic** — Uses induction in uniqueness proof
- **demoivres-theorem** — Proved by induction

## Related
- **well-ordering-principle** — Equivalent principle
- **second-principle-of-induction** — Stronger induction variant

# Common Errors

- **Error**: Forgetting the base case and only proving the inductive step
  **Correction**: Both the base case and inductive step are required

- **Error**: Using $S(k+1)$ in the proof of $S(k+1)$ (circular reasoning)
  **Correction**: Only the assumption $S(k)$ (or $S(j)$ for $j \leq k$) may be used

# Common Confusions

- **Confusion**: Thinking induction only works starting at $n = 1$
  **Clarification**: Induction can start at any integer $n_0$

# Source Reference

Chapter 2: The Integers, Section 2.1, pages 30-33.

# Verification Notes

- Definition source: Direct quote from Principle 2.1, p. 30
- Confidence: HIGH — explicit axiom statement
- Cross-reference status: Verified
- Uncertainties: None
