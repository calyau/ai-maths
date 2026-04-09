---
# === CORE IDENTIFICATION ===
concept: Elementary Divisors
slug: elementary-divisors

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
pdf_page: 26
section: "Commutative groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - fundamental-theorem-finitely-generated-abelian-groups
extends: []
related:
  - invariant-factors
contrasts_with:
  - invariant-factors

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are elementary divisors of an abelian group?"
  - "How do elementary divisors relate to invariant factors?"
---

# Quick Definition

The elementary divisors of a finitely generated abelian group are the unique prime powers $p_1^{e_1}, \ldots, p_t^{e_t}$ (with $e_i \ge 1$) such that $M \cong C_{p_1^{e_1}} \times \cdots \times C_{p_t^{e_t}} \times C_\infty^r$.

# Core Definition

"The $n_i$ can be chosen to be powers of prime numbers, and then they are uniquely determined by $M$." (Milne, Theorem 1.57c, p. 26)

"The integers $p_1^{e_1}, \ldots, p_t^{e_t}$ are called the **elementary divisors** of $M$." (p. 26)

# Prerequisites

- **Fundamental theorem of finitely generated abelian groups**

# Key Properties

1. Each elementary divisor is a prime power $p^e$ with $e \ge 1$
2. The elementary divisors are uniquely determined
3. A prime $p$ occurs iff $M$ has an element of order $p$
4. The number of times $p$ occurs equals $\dim_{\mathbb{F}_p}(M[p])$ where $M[p] = \{x \mid px = 0\}$
5. Elementary divisors can be read off from counting elements of each prime power order

# Context & Application

Elementary divisors give the finest decomposition of a finitely generated abelian group into cyclic factors. They can be combined into invariant factors using $C_m \times C_n \cong C_{mn}$ when $\gcd(m,n) = 1$.

# Examples

**Example 1**: For $C_{12} \cong C_4 \times C_3$, the elementary divisors are $4, 3$.

**Example 2**: For $C_3 \times C_{30} \cong C_3 \times C_2 \times C_3 \times C_5$, the elementary divisors are $2, 3, 3, 5$.

# Relationships

## Builds Upon
- **fundamental-theorem-finitely-generated-abelian-groups**

## Contrasts With
- **invariant-factors** — divisibility chain form vs. prime power form

# Source Reference

Chapter 1, Theorem 1.57c, page 26.

# Verification Notes

- Definition source: Direct from Theorem 1.57c
- Confidence: HIGH
- Uncertainties: None
