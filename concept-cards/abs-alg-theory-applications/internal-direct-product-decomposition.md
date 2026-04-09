---
concept: Internal Direct Product Decomposition
slug: internal-direct-product-decomposition
category: group-structure
subcategory: group-constructions
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Structure of Groups"
chapter_number: 13
pdf_page: 173
section: "Finite Abelian Groups"
extraction_confidence: high
aliases:
  - "primary decomposition"
prerequisites:
  - direct-product
  - p-group
extends: []
related:
  - fundamental-theorem-of-finite-abelian-groups
contrasts_with: []
answers_questions:
  - "How is a finite abelian group decomposed into p-group components?"
---

# Quick Definition

Every finite abelian group of order $n = p_1^{\alpha_1} \cdots p_k^{\alpha_k}$ is the internal direct product of subgroups $G_1, \ldots, G_k$ where each $G_i$ consists of all elements whose order is a power of $p_i$.

# Core Definition

**Lemma 13.8**: "Let $G$ be a finite abelian group of order $n = p_1^{\alpha_1} \cdots p_k^{\alpha_k}$. Then $G$ is the internal direct product of subgroups $G_1, G_2, \ldots, G_k$, where $G_i$ is the subgroup of $G$ consisting of all elements of order $p_i^r$ for some integer $r$" (Judson, p. 173).

# Prerequisites

- **Direct product** — Internal direct product structure
- **$p$-group** — Each component is a $p_i$-group

# Key Properties

1. $G = G_1 G_2 \cdots G_k$ (every element is a product)
2. $G_i \cap G_j = \{e\}$ for $i \neq j$
3. Each $G_i$ is a $p_i$-group of order $p_i^{\alpha_i}$
4. $G_i = \{g \in G : |g| = p_i^r \text{ for some } r\}$

# Relationships

## Enables
- **Fundamental Theorem of Finite Abelian Groups** — Reduces the problem to $p$-groups

# Source Reference

Chapter 13: The Structure of Groups, Section 13.1, p. 173-174. Lemma 13.8.

# Verification Notes

- Definition source: Lemma 13.8
- Confidence: HIGH
