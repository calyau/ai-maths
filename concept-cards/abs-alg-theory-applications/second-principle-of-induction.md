---
# === CORE IDENTIFICATION ===
concept: Second Principle of Mathematical Induction
slug: second-principle-of-induction

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
pdf_page: 32
section: "Mathematical Induction"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - strong induction
  - complete induction

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mathematical-induction
extends:
  - mathematical-induction
related:
  - well-ordering-principle
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

The Second Principle of Mathematical Induction (strong induction) allows the inductive step to assume $S(n_0), S(n_0+1), \ldots, S(k)$ are all true when proving $S(k+1)$.

# Core Definition

**Principle 2.5**: "Let $S(n)$ be a statement about integers for $n \in \mathbb{N}$ and suppose $S(n_0)$ is true for some integer $n_0$. If $S(n_0), S(n_0+1), \ldots, S(k)$ imply that $S(k+1)$ for $k \geq n_0$, then the statement $S(n)$ is true for all integers $n \geq n_0$" (Judson, p. 32).

# Prerequisites

- **Mathematical induction** — Strong induction is a strengthened form

# Key Properties

1. The inductive hypothesis assumes ALL preceding cases, not just one
2. Equivalent to ordinary induction and the Well-Ordering Principle
3. Sometimes easier to apply than ordinary induction
4. Used in the uniqueness proof of the Fundamental Theorem of Arithmetic

# Context & Application

Strong induction is used when the proof of $S(k+1)$ requires knowledge of $S(j)$ for some $j < k$, not just $S(k)$. It is essential for the uniqueness proof of prime factorization.

# Examples

**Example 1** (p. 36): The uniqueness proof of the Fundamental Theorem of Arithmetic uses strong induction on $n$, assuming unique factorization holds for all integers $m$ with $1 \leq m < n$.

# Relationships

## Builds Upon
- **mathematical-induction** — Strengthened form

## Enables
- **fundamental-theorem-of-arithmetic** — Uniqueness proof uses strong induction

## Related
- **well-ordering-principle** — Equivalent principle

# Common Confusions

- **Confusion**: Thinking strong induction is "stronger" than ordinary induction
  **Clarification**: The two forms are logically equivalent; "strong" refers to the stronger hypothesis, not a stronger conclusion

# Source Reference

Chapter 2: The Integers, Section 2.1, Principle 2.5, page 32.

# Verification Notes

- Definition source: Direct quote from Principle 2.5, p. 32
- Confidence: HIGH — explicit axiom statement
- Cross-reference status: Verified
- Uncertainties: None
