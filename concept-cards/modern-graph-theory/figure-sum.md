---
# === CORE IDENTIFICATION ===
concept: Figure Sum
slug: figure-sum

# === CLASSIFICATION ===
category: graph-enumeration
subcategory: polya-framework
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 287
section: "VIII.4 Enumeration and Pólya's Theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - power sum of weights

# === TYPED RELATIONSHIPS ===
prerequisites:
  - polya-enumeration-theorem
extends: []
related:
  - cycle-index
  - pattern-enumeration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are figure sums in Pólya enumeration?"
---

# Quick Definition

The $k$th figure sum is $s_k = \sum_{r \in R} w(r)^k$, the sum of $k$th powers of the weights of all figures. Substituting figure sums into the cycle index gives the pattern sum.

# Core Definition

Let $A$ be a commutative ring, $w: R \to A$ a weight function on the range (set of figures). For $k = 1, 2, \ldots$, the $k$th figure sum is $s_k = \sum_{r \in R} w(r)^k$. The weight of a configuration $f \in R^D$ is $w(f) = \prod_{d \in D} w(f(d))$. Polya's theorem states $|\Gamma|S = \widetilde{Z}(\Gamma; s_1, s_2, \ldots, s_d)$: substitute $a_k = s_k$ in the cycle sum (Bollobas, p. 287).

# Prerequisites

- **Polya's enumeration theorem** -- The framework in which figure sums are used

# Key Properties

1. $s_k$ is the $k$th power sum of weights
2. For $w \equiv 1$: $s_k = |R|$ for all $k$
3. For polynomial weights: $s_k$ is a polynomial
4. The choice of weight function determines what information $S$ encodes

# Construction / Recognition

## To Compute Figure Sums
1. Define $w: R \to A$ (weight function on figures)
2. For each $k = 1, \ldots, d$: $s_k = \sum_{r \in R} w(r)^k$
3. Substitute into the cycle sum to get $|\Gamma|S$

# Context & Application

Figure sums are the bridge between the cycle structure of the symmetry group and the counting problem. By choosing different weight functions, one can extract different enumerative information from the same cycle index.

# Examples

**Example** (p. 289): 3 colors with $w(r) = 1, w(b) = x, w(g) = y$ in $\mathbb{Z}[x,y]$: $s_k = 1 + x^k + y^k$.

# Relationships

## Builds Upon
- **Polya's enumeration theorem** -- The framework

## Enables
- Pattern counting by type

## Related
- **Cycle index** -- Figure sums are substituted into it
- **Pattern enumeration** -- The output

## Contrasts With
- None

# Common Errors

- **Error**: Using $s_1$ for all $k$
  **Correction**: Each $s_k$ involves the $k$th powers of weights, not just the first

# Common Confusions

- **Confusion**: Thinking $s_k = s_1^k$
  **Clarification**: $s_k = \sum w(r)^k$, not $(\sum w(r))^k$; these are power sums, not powers of the first sum

# Source Reference

Chapter VIII, Section VIII.4, page 287.

# Verification Notes

- Definition source: Direct from p. 287
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
