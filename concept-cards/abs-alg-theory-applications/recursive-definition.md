---
# === CORE IDENTIFICATION ===
concept: Recursive Definition
slug: recursive-definition

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
  - inductive definition

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mathematical-induction
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

A recursive (or inductive) definition defines a quantity by specifying a base case and a rule for computing each subsequent case from previous ones.

# Core Definition

Induction can be used in formulating definitions. Two approaches to defining $n!$:
- **Explicit**: $n! = 1 \cdot 2 \cdot 3 \cdots (n-1) \cdot n$
- **Recursive**: $1! = 1$ and $n! = n(n-1)!$ for $n > 1$

"Every good mathematician or computer scientist knows that looking at problems recursively, as opposed to explicitly, often results in better understanding of complex issues" (Judson, p. 32).

# Prerequisites

- **Mathematical induction** — Recursive definitions are justified by induction

# Key Properties

1. Requires a base case
2. Each subsequent value defined in terms of previous values
3. Equivalent to explicit definitions when both exist
4. Often more natural and illuminating

# Examples

**Example 1** (p. 32): Factorial: $1! = 1$ and $n! = n(n-1)!$ for $n > 1$.

**Example 2**: Group exponentiation: $g^0 = e$ and $g^n = g \cdot g^{n-1}$.

# Relationships

## Builds Upon
- **mathematical-induction** — Justifies recursive definitions

# Source Reference

Chapter 2: The Integers, Section 2.1, page 32.

# Verification Notes

- Definition source: Direct from p. 32
- Confidence: HIGH — explicit discussion
- Cross-reference status: Verified
- Uncertainties: None
