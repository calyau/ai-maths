---
concept: External Direct Product
slug: external-direct-product
category: morphisms
subcategory: direct-products
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Isomorphisms"
chapter_number: 9
pdf_page: 131
section: "9.2 Direct Products"
extraction_confidence: high
aliases:
  - direct product
  - "$G \\times H$"
prerequisites:
  - group-isomorphism
extends: []
related:
  - internal-direct-product
  - direct-product-of-cyclic-groups
contrasts_with:
  - internal-direct-product
answers_questions:
  - "What is a direct product of groups?"
  - "How do I construct the direct product $G \\times H$?"
---

# Quick Definition

The external direct product $G \times H$ of groups $G$ and $H$ is the set of ordered pairs $(g, h)$ with componentwise multiplication: $(g_1, h_1)(g_2, h_2) = (g_1g_2, h_1h_2)$.

# Core Definition

The group $G \times H$ is called the *external direct product* of $G$ and $H$. As a set, it consists of ordered pairs $(g, h)$ where $g \in G$ and $h \in H$. The binary operation is $(g_1, h_1)(g_2, h_2) = (g_1g_2, h_1h_2)$ (Judson, p. 131). By Proposition 9.13, this is a group with identity $(e_G, e_H)$ and inverse $(g,h)^{-1} = (g^{-1}, h^{-1})$.

# Prerequisites

- **Group Isomorphism** — Direct products are studied in the context of classifying groups

# Key Properties

1. $|G \times H| = |G| \cdot |H|$
2. Identity: $(e_G, e_H)$; inverse of $(g,h)$ is $(g^{-1}, h^{-1})$
3. $G \times H$ is abelian iff both $G$ and $H$ are abelian
4. The order of $(g, h)$ is $\text{lcm}(|g|, |h|)$ (Theorem 9.17)
5. Extends to $n$-fold products: $\prod_{i=1}^n G_i$

# Construction / Recognition

## To Construct:
1. Form all ordered pairs $(g, h)$ with $g \in G$, $h \in H$
2. Define multiplication componentwise
3. Verify group axioms (Proposition 9.13)

# Context & Application

Direct products allow construction of new groups from existing ones and decomposition of groups into simpler factors. The fundamental theorem of finite abelian groups states that every finite abelian group is isomorphic to a direct product of cyclic groups.

# Examples

**Example 1** (p. 131): $\mathbb{R} \times \mathbb{R} = \mathbb{R}^2$ under componentwise addition: $(a,b) + (c,d) = (a+c, b+d)$.

**Example 2** (p. 132): $\mathbb{Z}_2 \times \mathbb{Z}_2 = \{(0,0), (0,1), (1,0), (1,1)\}$ is not isomorphic to $\mathbb{Z}_4$ (every non-identity element has order 2).

**Example 3** (p. 132): $\mathbb{Z}_2^n$ is the set of binary $n$-tuples under XOR, important in coding theory.

# Relationships

## Builds Upon
- **Group Isomorphism** — Studied as part of group classification

## Enables
- **Direct Product of Cyclic Groups** — When $\mathbb{Z}_m \times \mathbb{Z}_n \cong \mathbb{Z}_{mn}$

## Contrasts With
- **Internal Direct Product** — Decomposing an existing group vs. building a new one

# Common Errors

- **Error**: Assuming $G \times H \cong H \times G$ requires proof
  **Correction**: The map $(g, h) \mapsto (h, g)$ is clearly an isomorphism, but it should be noted

# Common Confusions

- **Confusion**: Thinking $\mathbb{Z}_m \times \mathbb{Z}_n$ is always cyclic
  **Clarification**: $\mathbb{Z}_m \times \mathbb{Z}_n$ is cyclic iff $\gcd(m, n) = 1$ (Theorem 9.21)

# Source Reference

Chapter 9: Isomorphisms, Section 9.2, "External Direct Products," Proposition 9.13, pages 131-133.

# Verification Notes

- Definition source: Direct from p. 131
- Confidence rationale: Explicit definition and proposition
- Uncertainties: None
- Cross-reference status: Verified
