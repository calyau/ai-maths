---
# === CORE IDENTIFICATION ===
concept: Fundamental Theorem of Finitely Generated Abelian Groups
slug: fundamental-theorem-finitely-generated-abelian-groups

# === CLASSIFICATION ===
category: subgroup-theory
subcategory: commutative-groups
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 25
section: "Commutative groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - structure theorem for finitely generated abelian groups

# === TYPED RELATIONSHIPS ===
prerequisites:
  - basis-of-commutative-group
  - direct-product-internal
extends: []
related:
  - invariant-factors
  - elementary-divisors
  - rank-of-abelian-group
  - torsion-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can finitely generated abelian groups be classified?"
  - "What is the structure theorem for finitely generated abelian groups?"
---

# Quick Definition

Every finitely generated commutative group is isomorphic to $C_{n_1} \times \cdots \times C_{n_s} \times C_\infty^r$ for uniquely determined integers $r \ge 0$ and $n_i \ge 2$. The $n_i$ can be chosen as invariant factors or as elementary divisors.

# Core Definition

"Every finitely generated commutative group $M$ has a basis; hence it is a finite direct sum of cyclic groups." (Milne, Theorem 1.54, p. 25)

"A nonzero finitely generated commutative group $M$ can be expressed $M \approx C_{n_1} \times \cdots \times C_{n_s} \times C_\infty^r$ for certain integers $n_1, \ldots, n_s \ge 2$ and $r \ge 0$." (Milne, Theorem 1.57, p. 26)

# Prerequisites

- **Basis of a commutative group** — existence of a basis gives the decomposition
- **Internal direct product** — the group decomposes as a direct product

# Key Properties

1. $r$ (the rank) is uniquely determined (proved using $M/pM$)
2. Invariant factor form: $n_1 | n_2 | \cdots | n_s$, uniquely determined (Theorem 1.57b)
3. Elementary divisor form: each $n_i$ is a prime power, uniquely determined (Theorem 1.57c)
4. $C_m \times C_n \cong C_{mn}$ when $\gcd(m,n) = 1$ (Equation 13)
5. Each finite commutative group is isomorphic to exactly one $C_{n_1} \times \cdots \times C_{n_r}$ with $n_1 | \cdots | n_r$ (Summary 1.58)

# Construction / Recognition

## To Classify a Finite Abelian Group:
1. Factor the order into prime powers
2. List all possible elementary divisor decompositions
3. Alternatively, list invariant factor decompositions with $n_1 | n_2 | \cdots | n_s$

# Context & Application

This is one of the most complete classification theorems in algebra. Every finitely generated abelian group is completely determined by its rank and invariant factors (or elementary divisors). Milne notes the first proof for finite groups was given by Kronecker in 1870.

# Examples

**Example 1** (p. 27): Each commutative group of order 90 is isomorphic to exactly one of $C_{90}$ or $C_3 \times C_{30}$.

**Example 2**: Groups of order 8: $C_8$, $C_2 \times C_4$, $C_2 \times C_2 \times C_2$.

# Relationships

## Builds Upon
- **basis-of-commutative-group**, **direct-product-internal**

## Related
- **invariant-factors** — one form of the uniqueness statement
- **elementary-divisors** — another form of the uniqueness statement
- **rank-of-abelian-group** — the number of infinite cyclic factors
- **torsion-subgroup** — the finite-order part

# Common Errors

- **Error**: Assuming two abelian groups of the same order are isomorphic
  **Correction**: E.g., $C_4 \not\cong C_2 \times C_2$, though both have order 4

# Source Reference

Chapter 1, Theorems 1.54 and 1.57, Summary 1.58, pages 25-27.

# Verification Notes

- Definition source: Direct from Theorems 1.54, 1.57
- Confidence: HIGH — explicit theorems
- Uncertainties: None
