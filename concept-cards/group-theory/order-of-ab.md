---
# === CORE IDENTIFICATION ===
concept: The Order of ab
slug: order-of-ab

# === CLASSIFICATION ===
category: subgroup-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 28
section: "The order of ab"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - group-presentation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What can we say about the order of ab given the orders of a and b?"
  - "Can elements of given orders produce a product of arbitrary order?"
---

# Quick Definition

If $a$ has order $m$ and $b$ has order $n$ in a group $G$, the order of $ab$ can be any positive integer $r$. This is Theorem 1.64.

# Core Definition

"For any integers $m, n, r > 1$, there exists a finite group $G$ with elements $a$ and $b$ such that $a$ has order $m$, $b$ has order $n$, and $ab$ has order $r$." (Milne, Theorem 1.64, p. 28)

# Prerequisites

- **Group** — the statement is about elements in a group

# Key Properties

1. There is no constraint on the order of $ab$ from the orders of $a$ and $b$ alone
2. The proof uses $\mathrm{SL}_2(\mathbb{F}_q)$ for a suitable prime power $q$
3. Elements $a, b$ of orders $2m, 2n$ in $\mathrm{SL}_2(\mathbb{F}_q)$ are constructed so $ab$ has order $2r$
4. Passing to $\mathrm{SL}_2(\mathbb{F}_q)/\{\pm I\}$ gives orders $m, n, r$

# Construction / Recognition

## Proof Sketch:
1. Choose prime $p$ not dividing $N = 2mnr$, with $q = p^k$ such that $N | (q-1)$
2. $\mathbb{F}_q^\times$ is cyclic of order $q - 1$, so contains elements $u, v, w$ of orders $2m, 2n, 2r$
3. Construct upper/lower triangular matrices $a, b \in \mathrm{SL}_2(\mathbb{F}_q)$ with eigenvalues $\{u, u^{-1}\}$ and $\{v, v^{-1}\}$
4. Choose parameter $t$ so that $ab$ has eigenvalues $\{w, w^{-1}\}$

# Context & Application

This result is used in Chapter 2 (Example 2.10) to show that in certain group presentations, elements can have prescribed orders. It demonstrates the complexity of group multiplication.

# Examples

**Example 1** (p. 28): In $\mathrm{SL}_2(\mathbb{F}_q)/\{\pm I\}$, one can find elements of any prescribed orders $m, n$ whose product has any prescribed order $r$.

# Relationships

## Related
- **group-presentation** — used to verify orders in presentations (Example 2.10)

# Source Reference

Chapter 1, Theorem 1.64, pages 28-29.

# Verification Notes

- Definition source: Direct from Theorem 1.64
- Confidence: HIGH — explicit theorem with full proof
- Uncertainties: None
