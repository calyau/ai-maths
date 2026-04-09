---
# === CORE IDENTIFICATION ===
concept: Fundamental Theorem of Algebra
slug: fundamental-theorem-of-algebra

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
  - "FTA"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - algebraically-closed-field
  - galois-group
  - splitting-field
extends: []
related:
  - fundamental-theorem-of-galois-theory
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does the Fundamental Theorem of Algebra state?"
  - "How is the Fundamental Theorem of Algebra proved using Galois theory?"
---

# Quick Definition

The Fundamental Theorem of Algebra states that the field of complex numbers $\mathbb{C}$ is algebraically closed: every polynomial in $\mathbb{C}[x]$ has a root in $\mathbb{C}$.

# Core Definition

**Theorem 23.34 (Fundamental Theorem of Algebra).** The field of complex numbers is algebraically closed; that is, every polynomial in $\mathbb{C}[x]$ has a root in $\mathbb{C}$ (Judson, p. 321).

The proof uses Galois theory, Sylow theorems, and two facts from analysis: every odd-degree real polynomial has a real root, and every positive real number has a square root.

# Prerequisites

- **Algebraically closed field** — The theorem says $\mathbb{C}$ is algebraically closed
- **Galois group** — The proof uses Galois groups and Sylow subgroups
- **Splitting field** — The proof considers splitting fields over $\mathbb{R}$

# Key Properties

1. Every nonconstant polynomial in $\mathbb{C}[x]$ factors completely into linear factors
2. Equivalently, $\mathbb{C}$ has no proper algebraic extension
3. The proof is algebraic (using Galois theory) but relies on two analytic facts about $\mathbb{R}$

# Context & Application

This theorem, first proved by Gauss in 1799, is one of the most important results in mathematics. The proof in this text uses the Galois-theoretic machinery developed throughout the book, showing that no proper finite extension of $\mathbb{C}$ can exist by arguing that the Galois group would need to be a 2-group, leading to a contradiction.

# Examples

**Example 1**: $x^2 + 1$ has roots $\pm i$ in $\mathbb{C}$, even though it has no real roots.

**Example 2**: $x^4 + 1$ factors as $(x^2 + i)(x^2 - i)$ and further into four linear factors over $\mathbb{C}$.

# Relationships

## Builds Upon
- **Algebraically closed field** — The theorem characterizes $\mathbb{C}$
- **Galois group** — Used in the proof
- **Splitting field** — Used in the proof

## Related
- **Fundamental Theorem of Galois Theory** — The proof applies Galois theory

# Common Confusions

- **Confusion**: Thinking the theorem is a purely algebraic result
  **Clarification**: Every known proof relies on some topological or analytic fact about $\mathbb{R}$, such as the intermediate value theorem or completeness

# Source Reference

Chapter 23: Galois Theory, Section 23.3, pages 321–322. Theorem 23.34.

# Verification Notes

- Definition source: Direct from Theorem 23.34, p. 321
- Confidence: HIGH — explicit theorem with proof
- Cross-reference status: Verified
- Uncertainties: None
