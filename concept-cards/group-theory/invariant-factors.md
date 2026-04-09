---
# === CORE IDENTIFICATION ===
concept: Invariant Factors
slug: invariant-factors

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
  - elementary-divisors
contrasts_with:
  - elementary-divisors

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are invariant factors of an abelian group?"
  - "How are invariant factors determined?"
---

# Quick Definition

The invariant factors of a finitely generated abelian group are the unique integers $n_1 | n_2 | \cdots | n_s$ (each $\ge 2$) such that $M \cong C_{n_1} \times \cdots \times C_{n_s} \times C_\infty^r$.

# Core Definition

"The $n_i$ can be chosen so that $n_1 \ge 2$ and $n_1 | n_2, \ldots, n_{s-1} | n_s$, and then they are uniquely determined by $M$." (Milne, Theorem 1.57b, p. 26)

"The integers $n_1, \ldots, n_s$ in (b) are called the *invariant factors* of $M$." (p. 26)

# Prerequisites

- **Fundamental theorem of finitely generated abelian groups** — provides the decomposition

# Key Properties

1. Invariant factors satisfy divisibility: $n_1 | n_2 | \cdots | n_s$
2. They are uniquely determined by the group
3. $n_s$ is the exponent of the torsion part (smallest $m > 0$ with $mM_{\mathrm{tors}} = 0$)
4. $n_{s-1}$ is the smallest $m > 0$ such that $mM$ is cyclic
5. Related to elementary divisors by factoring/combining using $C_m \times C_n \cong C_{mn}$ for $\gcd(m,n) = 1$

# Context & Application

Invariant factors provide a canonical form for finitely generated abelian groups. They are the group-theoretic analogue of the invariant factors of a matrix (Smith normal form).

# Examples

**Example 1** (p. 27): For order 90, the invariant factor decompositions are: $C_{90}$ (invariant factors: $90$) and $C_3 \times C_{30}$ (invariant factors: $3, 30$, since $3 | 30$).

# Relationships

## Builds Upon
- **fundamental-theorem-finitely-generated-abelian-groups**

## Contrasts With
- **elementary-divisors** — prime-power decomposition vs. divisibility chain

# Source Reference

Chapter 1, Theorem 1.57b, Summary 1.58, pages 26-27.

# Verification Notes

- Definition source: Direct from Theorem 1.57b
- Confidence: HIGH
- Uncertainties: None
