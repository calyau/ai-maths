---
concept: Fundamental Theorem of Finite Abelian Groups
slug: fundamental-theorem-of-finite-abelian-groups
category: group-structure
subcategory: classification-theorems
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Structure of Groups"
chapter_number: 13
pdf_page: 172
section: "Finite Abelian Groups"
extraction_confidence: high
aliases:
  - "structure theorem for finite abelian groups"
prerequisites:
  - p-group
  - direct-product
  - cyclic-group
  - lagranges-theorem
extends: []
related:
  - fundamental-theorem-of-finitely-generated-abelian-groups
  - internal-direct-product
contrasts_with: []
answers_questions:
  - "How are finite abelian groups classified?"
  - "What is the Fundamental Theorem of Finite Abelian Groups?"
---

# Quick Definition

Every finite abelian group is isomorphic to a direct product of cyclic groups of prime power order: $G \cong \mathbb{Z}_{p_1^{\alpha_1}} \times \mathbb{Z}_{p_2^{\alpha_2}} \times \cdots \times \mathbb{Z}_{p_n^{\alpha_n}}$, where the $p_i$ are primes (not necessarily distinct). This decomposition is unique up to reordering.

# Core Definition

**Theorem 13.4 (Fundamental Theorem of Finite Abelian Groups)**: "Every finite abelian group $G$ is isomorphic to a direct product of cyclic groups of the form $\mathbb{Z}_{p_1^{\alpha_1}} \times \mathbb{Z}_{p_2^{\alpha_2}} \times \cdots \times \mathbb{Z}_{p_n^{\alpha_n}}$ where the $p_i$'s are primes (not necessarily distinct)" (Judson, p. 172).

# Prerequisites

- **$p$-group** — The proof reduces to $p$-groups
- **Direct product** — The decomposition is a direct product
- **Cyclic group** — The factors are cyclic
- **Lagrange's theorem** — Used in the proof

# Key Properties

1. Existence: every finite abelian group has such a decomposition
2. Uniqueness: the decomposition is unique up to reordering of factors
3. To classify abelian groups of order $n$, factor $n = p_1^{a_1} \cdots p_k^{a_k}$ and find all partitions of each exponent $a_i$

# Construction / Recognition

## To Classify All Abelian Groups of Order $n$:
1. Factor $n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$
2. For each prime $p_i$, find all partitions of $a_i$
3. Each combination of partitions gives a distinct abelian group
4. The number of abelian groups of order $n$ is the product of the number of partitions of each $a_i$

# Context & Application

This theorem completely solves the classification problem for finite abelian groups. The proof proceeds through: (1) decomposing $G$ into $p$-group components (Lemma 13.8), and (2) decomposing each $p$-group component into cyclic factors (Lemma 13.9).

# Examples

**Example 1** (p. 172): The abelian groups of order $540 = 2^2 \cdot 3^3 \cdot 5$ are:
- $\mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_3 \times \mathbb{Z}_3 \times \mathbb{Z}_3 \times \mathbb{Z}_5$
- $\mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_3 \times \mathbb{Z}_9 \times \mathbb{Z}_5$
- $\mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_{27} \times \mathbb{Z}_5$
- $\mathbb{Z}_4 \times \mathbb{Z}_3 \times \mathbb{Z}_3 \times \mathbb{Z}_3 \times \mathbb{Z}_5$
- $\mathbb{Z}_4 \times \mathbb{Z}_3 \times \mathbb{Z}_9 \times \mathbb{Z}_5$
- $\mathbb{Z}_4 \times \mathbb{Z}_{27} \times \mathbb{Z}_5$

There are 6 groups: partitions of 2 give $\{2, 1+1\}$ (2 choices), partitions of 3 give $\{3, 2+1, 1+1+1\}$ (3 choices), partitions of 1 give $\{1\}$ (1 choice), yielding $2 \times 3 \times 1 = 6$.

# Relationships

## Builds Upon
- **$p$-group** — The proof decomposes into $p$-groups first
- **Direct product** — The structural decomposition

## Enables
- **Classification of finite abelian groups** — Complete classification

## Related
- **Fundamental Theorem of Finitely Generated Abelian Groups** — Generalization to infinite groups

# Common Errors

- **Error**: Forgetting that the $p_i$ need not be distinct
  **Correction**: Different factors can have the same prime base; e.g., $\mathbb{Z}_4 \times \mathbb{Z}_2$ has two factors with $p = 2$

# Common Confusions

- **Confusion**: Thinking $\mathbb{Z}_4$ and $\mathbb{Z}_2 \times \mathbb{Z}_2$ are the same group
  **Clarification**: They are distinct non-isomorphic abelian groups of order 4: $\mathbb{Z}_4$ is cyclic, $\mathbb{Z}_2 \times \mathbb{Z}_2$ is not

# Source Reference

Chapter 13: The Structure of Groups, Section 13.1, pages 172-175. Theorem 13.4. Lemmas 13.6-13.9 provide the proof.

# Verification Notes

- Definition source: Direct quote of Theorem 13.4
- Proof: Complete, using Lemmas 13.6-13.9
- Confidence: HIGH — major theorem with full proof
