---
concept: Internal Direct Product
slug: internal-direct-product
category: morphisms
subcategory: direct-products
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Isomorphisms"
chapter_number: 9
pdf_page: 133
section: "9.2 Direct Products"
extraction_confidence: high
aliases: []
prerequisites:
  - external-direct-product
  - group-isomorphism
extends: []
related:
  - direct-product-of-cyclic-groups
contrasts_with:
  - external-direct-product
answers_questions:
  - "What is an internal direct product?"
  - "When is a group the internal direct product of two subgroups?"
---

# Quick Definition

A group $G$ is the internal direct product of subgroups $H$ and $K$ if $G = HK$, $H \cap K = \{e\}$, and $hk = kh$ for all $h \in H$, $k \in K$. In this case, $G \cong H \times K$.

# Core Definition

Let $G$ be a group with subgroups $H$ and $K$ satisfying:
1. $G = HK = \{hk : h \in H, k \in K\}$
2. $H \cap K = \{e\}$
3. $hk = kh$ for all $k \in K$ and $h \in H$

Then $G$ is the *internal direct product* of $H$ and $K$ (Judson, p. 133). By Theorem 9.27, $G \cong H \times K$.

# Prerequisites

- **External Direct Product** — The internal product is isomorphic to the external product
- **Group Isomorphism** — The equivalence is stated via isomorphism

# Key Properties

1. $G = HK$ (every $g \in G$ can be written as $hk$)
2. $H \cap K = \{e\}$ (the subgroups share only the identity)
3. Elements of $H$ and $K$ commute
4. Every $g \in G$ has a unique representation $g = hk$ (Theorem 9.27 proof)
5. $G \cong H \times K$ (Theorem 9.27)
6. Not every group can be decomposed this way

# Construction / Recognition

## To Verify:
1. Identify candidate subgroups $H$ and $K$
2. Check $G = HK$ (every element is a product $hk$)
3. Check $H \cap K = \{e\}$
4. Check $hk = kh$ for all $h \in H$, $k \in K$

# Context & Application

Internal direct products allow decomposing a group into simpler factors. This reverses the construction of external direct products and is key to the structure theory of finite abelian groups.

# Examples

**Example 1** (p. 133): $U(8)$ is the internal direct product of $H = \{1, 3\}$ and $K = \{1, 5\}$.

**Example 2** (p. 133): $D_6$ is the internal direct product of $H = \{\text{id}, r^3\}$ and $K = \{\text{id}, r^2, r^4, s, r^2s, r^4s\}$. Since $K \cong S_3$, we get $D_6 \cong \mathbb{Z}_2 \times S_3$.

**Example 3** (p. 134): $S_3$ is not an internal direct product of any two proper subgroups (the commutativity condition $hk = kh$ fails).

**Example 4** (p. 134): $\mathbb{Z}_6$ is an internal direct product: $\mathbb{Z}_6 \cong \{0, 2, 4\} \times \{0, 3\}$.

# Relationships

## Builds Upon
- **External Direct Product** — Internal and external products are isomorphic
- **Group Isomorphism** — $G \cong H \times K$

## Contrasts With
- **External Direct Product** — External builds up; internal decomposes

# Common Errors

- **Error**: Forgetting to check the commutativity condition $hk = kh$
  **Correction**: All three conditions must hold; $S_3$ fails because elements of its subgroups don't commute

# Common Confusions

- **Confusion**: Thinking every group is an internal direct product
  **Clarification**: Many groups (e.g., $S_3$) cannot be decomposed as internal direct products

# Source Reference

Chapter 9: Isomorphisms, Section 9.2, "Internal Direct Products," Theorem 9.27, pages 133-134.

# Verification Notes

- Definition source: Direct from p. 133
- Confidence rationale: Explicit definition with theorem
- Uncertainties: None
- Cross-reference status: Verified
