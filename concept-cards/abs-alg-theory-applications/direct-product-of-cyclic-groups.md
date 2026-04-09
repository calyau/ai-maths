---
concept: Direct Product of Cyclic Groups
slug: direct-product-of-cyclic-groups
category: morphisms
subcategory: direct-products
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Isomorphisms"
chapter_number: 9
pdf_page: 132
section: "9.2 Direct Products"
extraction_confidence: high
aliases: []
prerequisites:
  - external-direct-product
  - order-in-direct-product
extends: []
related:
  - cyclic-group-classification
contrasts_with: []
answers_questions:
  - "When is $\\mathbb{Z}_m \\times \\mathbb{Z}_n$ cyclic?"
  - "When is $\\mathbb{Z}_m \\times \\mathbb{Z}_n \\cong \\mathbb{Z}_{mn}$?"
---

# Quick Definition

$\mathbb{Z}_m \times \mathbb{Z}_n \cong \mathbb{Z}_{mn}$ if and only if $\gcd(m, n) = 1$. More generally, $\prod \mathbb{Z}_{n_i} \cong \mathbb{Z}_{n_1 \cdots n_k}$ iff the $n_i$ are pairwise coprime.

# Core Definition

**Theorem 9.21:** "The group $\mathbb{Z}_m \times \mathbb{Z}_n$ is isomorphic to $\mathbb{Z}_{mn}$ if and only if $\gcd(m, n) = 1$" (Judson, p. 132).

**Corollary 9.22:** $\prod_{i=1}^k \mathbb{Z}_{n_i} \cong \mathbb{Z}_{n_1 \cdots n_k}$ iff $\gcd(n_i, n_j) = 1$ for $i \neq j$.

**Corollary 9.23:** If $m = p_1^{e_1} \cdots p_k^{e_k}$, then $\mathbb{Z}_m \cong \mathbb{Z}_{p_1^{e_1}} \times \cdots \times \mathbb{Z}_{p_k^{e_k}}$.

# Prerequisites

- **External Direct Product** — The direct product construction
- **Order in Direct Product** — Key to the proof

# Key Properties

1. $\mathbb{Z}_m \times \mathbb{Z}_n$ is cyclic iff $\gcd(m, n) = 1$
2. When $\gcd(m,n) = 1$, $(1,1)$ generates $\mathbb{Z}_m \times \mathbb{Z}_n$
3. When $\gcd(m,n) > 1$, no element has order $mn$, so the product is not cyclic
4. Every $\mathbb{Z}_m$ decomposes into prime power cyclic factors

# Construction / Recognition

## To Determine if $\mathbb{Z}_m \times \mathbb{Z}_n$ is Cyclic:
1. Compute $\gcd(m, n)$
2. If $\gcd(m, n) = 1$, then $\mathbb{Z}_m \times \mathbb{Z}_n \cong \mathbb{Z}_{mn}$ (cyclic)
3. If $\gcd(m, n) > 1$, the product is not cyclic

# Context & Application

This theorem is fundamental to the classification of finite abelian groups. Every finite abelian group decomposes into a product of cyclic groups of prime power order.

# Examples

**Example 1** (p. 132): $\mathbb{Z}_2 \times \mathbb{Z}_3 \cong \mathbb{Z}_6$ since $\gcd(2, 3) = 1$. The element $(1, 1)$ generates the group.

**Example 2** (p. 131-132): $\mathbb{Z}_2 \times \mathbb{Z}_2 \not\cong \mathbb{Z}_4$ since $\gcd(2, 2) = 2 \neq 1$. Every non-identity element of $\mathbb{Z}_2 \times \mathbb{Z}_2$ has order 2.

# Relationships

## Builds Upon
- **External Direct Product** — The construction
- **Order in Direct Product** — $\text{lcm}(m,n) = mn$ iff $\gcd(m,n) = 1$

## Related
- **Cyclic Group Classification** — Cyclic groups are classified by order

# Common Errors

- **Error**: Assuming $\mathbb{Z}_4 \times \mathbb{Z}_6 \cong \mathbb{Z}_{24}$
  **Correction**: $\gcd(4, 6) = 2 \neq 1$, so they are not isomorphic

# Common Confusions

- **Confusion**: Thinking $\mathbb{Z}_2 \times \mathbb{Z}_2$ and $\mathbb{Z}_4$ are the same because both have 4 elements
  **Clarification**: $\mathbb{Z}_4$ is cyclic (has element of order 4); $\mathbb{Z}_2 \times \mathbb{Z}_2$ has no element of order 4

# Source Reference

Chapter 9: Isomorphisms, Section 9.2, Theorem 9.21, Corollaries 9.22-9.23, pages 132-133.

# Verification Notes

- Definition source: Direct from Theorem 9.21
- Confidence rationale: Explicit theorem with corollaries
- Uncertainties: None
- Cross-reference status: Verified
