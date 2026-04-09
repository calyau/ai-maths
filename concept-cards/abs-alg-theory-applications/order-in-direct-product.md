---
concept: Order in Direct Product
slug: order-in-direct-product
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
extends: []
related:
  - direct-product-of-cyclic-groups
contrasts_with: []
answers_questions:
  - "What is the order of an element in a direct product?"
---

# Quick Definition

The order of $(g, h) \in G \times H$ is $\text{lcm}(|g|, |h|)$, where $|g|$ and $|h|$ are the orders of $g$ in $G$ and $h$ in $H$ respectively.

# Core Definition

**Theorem 9.17:** "Let $(g,h) \in G \times H$. If $g$ and $h$ have finite orders $r$ and $s$ respectively, then the order of $(g,h)$ in $G \times H$ is the least common multiple of $r$ and $s$" (Judson, p. 132).

# Prerequisites

- **External Direct Product** — The setting for this theorem

# Key Properties

1. $|(g,h)| = \text{lcm}(|g|, |h|)$
2. Extends to $n$-fold products: $|(g_1, \ldots, g_n)| = \text{lcm}(|g_1|, \ldots, |g_n|)$ (Corollary 9.18)
3. Key for determining when direct products are cyclic

# Construction / Recognition

## To Compute:
1. Find the order of $g$ in $G$
2. Find the order of $h$ in $H$
3. Compute $\text{lcm}(|g|, |h|)$

# Context & Application

This theorem is essential for determining the structure of direct products and for proving when $\mathbb{Z}_m \times \mathbb{Z}_n \cong \mathbb{Z}_{mn}$.

# Examples

**Example 1** (p. 132): $(8, 56) \in \mathbb{Z}_{12} \times \mathbb{Z}_{60}$. Order of 8 in $\mathbb{Z}_{12}$ is $12/\gcd(8,12) = 3$. Order of 56 in $\mathbb{Z}_{60}$ is $60/\gcd(56,60) = 15$. So $|(8,56)| = \text{lcm}(3, 15) = 15$.

# Relationships

## Builds Upon
- **External Direct Product** — Elements of direct products

## Enables
- **Direct Product of Cyclic Groups** — Key to Theorem 9.21

# Common Errors

- **Error**: Computing $|g| \cdot |h|$ instead of $\text{lcm}(|g|, |h|)$
  **Correction**: Use lcm, not product; they differ when $\gcd(|g|, |h|) > 1$

# Common Confusions

- **Confusion**: Thinking $(1,1) \in \mathbb{Z}_2 \times \mathbb{Z}_4$ has order 8
  **Clarification**: $|(1,1)| = \text{lcm}(2, 4) = 4$, not $2 \cdot 4 = 8$

# Source Reference

Chapter 9: Isomorphisms, Section 9.2, Theorem 9.17, Corollary 9.18, page 132.

# Verification Notes

- Definition source: Direct from Theorem 9.17
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
