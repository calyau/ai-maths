---
concept: Non-Simplicity Proofs Using Sylow Theorems
slug: non-simplicity-proofs
category: group-structure
subcategory: sylow-theory
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Sylow Theorems"
chapter_number: 15
pdf_page: 199
section: "Examples and Applications"
extraction_confidence: high
aliases:
  - "proving a group is not simple"
prerequisites:
  - third-sylow-theorem
  - second-sylow-theorem
  - hk-order-formula
extends: []
related:
  - simple-group
  - normal-subgroup
contrasts_with: []
answers_questions:
  - "How do I use the Sylow theorems to prove a group is not simple?"
---

# Quick Definition

The Sylow theorems provide a systematic method for proving groups are not simple: if the Third Sylow Theorem forces $n_p = 1$ for some prime $p$, the unique Sylow $p$-subgroup is normal. For harder cases, counting arguments and the HK order formula can establish normal subgroups.

# Core Definition

The strategy for proving a group of order $n$ is not simple uses the Sylow theorems as follows: (1) for each prime $p$ dividing $n$, determine possible values of $n_p$ (number of Sylow $p$-subgroups) using $n_p \equiv 1 \pmod{p}$ and $n_p | n$; (2) if $n_p = 1$ for any $p$, the unique Sylow $p$-subgroup is normal; (3) if no single $n_p = 1$, use counting arguments.

# Prerequisites

- **Third Sylow theorem** — Constrains $n_p$
- **Second Sylow theorem** — All Sylow $p$-subgroups are conjugate
- **HK order formula** — For counting-based arguments

# Key Properties

1. Strategy 1: Find a prime $p$ with $n_p = 1$
2. Strategy 2: Count elements of various orders to force a contradiction
3. Strategy 3: Use the HK order formula to bound intersection sizes
4. Groups of order $p^n$ ($n > 1$) are never simple (nontrivial center)
5. Groups of order $pq$ ($p < q$ primes) are never simple

# Examples

**Example 1** (p. 199): Groups of order 20: $n_5$ divides 20 and $n_5 \equiv 1 \pmod{5}$. Only option: $n_5 = 1$. So there's a normal Sylow 5-subgroup.

**Example 2** (p. 199-200): Groups of order 56 ($= 2^3 \cdot 7$): either $n_7 = 1$ (normal Sylow 7-subgroup) or $n_7 = 8$ (giving 48 elements of order 7, leaving room for only one Sylow 2-subgroup, which is normal).

**Example 3** (p. 200): Groups of order 48: use HK formula. Two Sylow 2-subgroups $H, K$ of order 16 must have $|H \cap K| = 8$, which has normalizer equal to all of $G$.

# Relationships

## Builds Upon
- **Third Sylow theorem** — Primary tool

## Related
- **Simple group** — What we prove the group is NOT

# Source Reference

Chapter 15: The Sylow Theorems, Section 15.2, pages 199-201. Examples 15.15-15.19.

# Verification Notes

- Definition source: Synthesized from multiple examples
- Confidence: HIGH — multiple worked examples in source
