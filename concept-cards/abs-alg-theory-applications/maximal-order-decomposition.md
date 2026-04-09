---
concept: Maximal Order Decomposition of p-Groups
slug: maximal-order-decomposition
category: group-structure
subcategory: classification-theorems
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Structure of Groups"
chapter_number: 13
pdf_page: 174
section: "Finite Abelian Groups"
extraction_confidence: high
aliases: []
prerequisites:
  - p-group
  - direct-product
  - cyclic-group
extends: []
related:
  - fundamental-theorem-of-finite-abelian-groups
contrasts_with: []
answers_questions:
  - "How is a finite abelian p-group decomposed into cyclic factors?"
---

# Quick Definition

If $G$ is a finite abelian $p$-group and $g \in G$ has maximal order, then $G \cong \langle g \rangle \times H$ for some subgroup $H$. By induction, this decomposes $G$ into a direct product of cyclic $p$-groups.

# Core Definition

**Lemma 13.9**: "Let $G$ be a finite abelian $p$-group and suppose that $g \in G$ has maximal order. Then $G$ is isomorphic to $\langle g \rangle \times H$ for some subgroup $H$ of $G$" (Judson, p. 174).

# Prerequisites

- **$p$-group** — $G$ is a finite abelian $p$-group
- **Direct product** — The decomposition uses direct products
- **Cyclic group** — $\langle g \rangle$ is cyclic

# Key Properties

1. Choose $g$ with maximal order $p^m$
2. Find $h \notin \langle g \rangle$ of smallest possible order
3. Construct element $a = g^{-s}h$ of order $p$ with $a \notin \langle g \rangle$
4. Show $\langle g \rangle \cap \langle a \rangle = \{e\}$
5. Apply induction on $G/\langle a \rangle$
6. Result: $G \cong \langle g \rangle \times H$

# Relationships

## Enables
- **Fundamental Theorem of Finite Abelian Groups** — This is the inductive step

# Source Reference

Chapter 13: The Structure of Groups, Section 13.1, p. 174-175. Lemma 13.9.

# Verification Notes

- Definition source: Lemma 13.9
- Confidence: HIGH — complete proof given
