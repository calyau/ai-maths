---
# === CORE IDENTIFICATION ===
concept: Cyclicity Criterion for Z_m x Z_n
slug: cyclicity-criterion

# === CLASSIFICATION ===
category: structure-theory
subcategory: products
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Products"
chapter_number: 10
pdf_page: 59
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Z_m x Z_n cyclicity theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - direct-product
extends: []
related:
  - kleins-group
  - isomorphism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When is Z_m x Z_n cyclic?"
  - "How do direct products relate to the constituent groups?"
---

# Quick Definition

$\mathbb{Z}_m \times \mathbb{Z}_n$ is cyclic if and only if $\gcd(m, n) = 1$, in which case it is isomorphic to $\mathbb{Z}_{mn}$.

# Core Definition

"(10.1) Theorem. $\mathbb{Z}_m \times \mathbb{Z}_n$ is cyclic if and only if the highest common factor of $m$ and $n$ is 1" (Armstrong, p. 60).

**If $\gcd(m,n) = 1$**: The element $(1,1)$ has order $mn$ (since $m$ and $n$ both divide $k$ implies $mn$ divides $k$), so it generates $\mathbb{Z}_m \times \mathbb{Z}_n$, which is therefore cyclic of order $mn$.

**If $\gcd(m,n) = d > 1$**: Let $m' = m/d$, $n' = n/d$. For any $(x,y)$, $m'dn' \cdot (x,y) = (0,0)$, so every element has order at most $m'dn' = mn/d < mn$. The group cannot be cyclic.

# Prerequisites

- **Direct product** — $\mathbb{Z}_m \times \mathbb{Z}_n$ is a direct product

# Key Properties

1. $\mathbb{Z}_m \times \mathbb{Z}_n$ is cyclic iff $\gcd(m, n) = 1$
2. When cyclic, $\mathbb{Z}_m \times \mathbb{Z}_n \cong \mathbb{Z}_{mn}$
3. The generator is $(1, 1)$ when $\gcd(m, n) = 1$
4. When $\gcd(m, n) > 1$, no element has order $mn$

# Construction / Recognition

## To Determine if $\mathbb{Z}_m \times \mathbb{Z}_n$ is Cyclic:
1. Compute $\gcd(m, n)$
2. If $\gcd(m, n) = 1$: the group is cyclic, isomorphic to $\mathbb{Z}_{mn}$
3. If $\gcd(m, n) > 1$: the group is not cyclic

# Context & Application

This theorem is fundamental for understanding the structure of finite abelian groups. It provides a quick way to determine when a product of cyclic groups collapses to a single cyclic group. For example, $\mathbb{Z}_2 \times \mathbb{Z}_3 \cong \mathbb{Z}_6$ but $\mathbb{Z}_2 \times \mathbb{Z}_2 \not\cong \mathbb{Z}_4$.

# Examples

**Example** (p. 59): $\mathbb{Z}_2 \times \mathbb{Z}_3 \cong \mathbb{Z}_6$ because $\gcd(2, 3) = 1$. The element $(1,1)$ generates the entire group, cycling through all six elements.

**Example** (p. 60): $\mathbb{Z}_2 \times \mathbb{Z}_2$ is not cyclic because $\gcd(2, 2) = 2$. Every element has order at most 2.

# Relationships

## Builds Upon
- **Direct product** — Applied to cyclic groups

## Related
- **Klein's group** — The case $\mathbb{Z}_2 \times \mathbb{Z}_2$ (not cyclic)
- **Isomorphism** — $\mathbb{Z}_m \times \mathbb{Z}_n \cong \mathbb{Z}_{mn}$ when coprime

# Common Errors

- **Error**: Assuming $\mathbb{Z}_m \times \mathbb{Z}_n$ always has an element of order $mn$.
  **Correction**: This is true only when $\gcd(m, n) = 1$. When $\gcd(m, n) > 1$, the maximum element order is $mn/\gcd(m,n) = \text{lcm}(m,n)$.

# Common Confusions

- **Confusion**: Thinking "cyclic" means the same as "abelian" for products.
  **Clarification**: $\mathbb{Z}_m \times \mathbb{Z}_n$ is always abelian, but it is cyclic only when $\gcd(m,n) = 1$.

# Source Reference

Chapter 10: Products, pages 60-61 (pdf pp. 60-61). Theorem 10.1 with proof.

# Verification Notes

- Theorem: Direct from p. 60, Theorem 10.1
- Both directions proved explicitly
- Confidence: HIGH — theorem with complete proof
