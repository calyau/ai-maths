---
concept: Cyclic Group Classification
slug: cyclic-group-classification
category: morphisms
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Isomorphisms"
chapter_number: 9
pdf_page: 129
section: "9.1 Definition and Examples"
extraction_confidence: high
aliases: []
prerequisites:
  - group-isomorphism
extends: []
related:
  - isomorphism-properties
  - direct-product-of-cyclic-groups
contrasts_with: []
answers_questions:
  - "How are cyclic groups classified up to isomorphism?"
---

# Quick Definition

Every infinite cyclic group is isomorphic to $\mathbb{Z}$, and every cyclic group of order $n$ is isomorphic to $\mathbb{Z}_n$. A group of prime order $p$ must be cyclic, hence isomorphic to $\mathbb{Z}_p$.

# Core Definition

**Theorem 9.7:** "All cyclic groups of infinite order are isomorphic to $\mathbb{Z}$" (p. 129).
**Theorem 9.8:** "If $G$ is a cyclic group of order $n$, then $G$ is isomorphic to $\mathbb{Z}_n$" (p. 129).
**Corollary 9.9:** "If $G$ is a group of order $p$, where $p$ is a prime number, then $G$ is isomorphic to $\mathbb{Z}_p$" (p. 129).

# Prerequisites

- **Group Isomorphism** — Classification is up to isomorphism

# Key Properties

1. Up to isomorphism, there is exactly one cyclic group of each order $n$
2. Up to isomorphism, there is exactly one infinite cyclic group
3. Every group of prime order is cyclic
4. This means we can speak of "*the* cyclic group of order $n$"

# Construction / Recognition

## To Classify:
1. If $G$ is cyclic and infinite, then $G \cong \mathbb{Z}$
2. If $G$ is cyclic and $|G| = n$, then $G \cong \mathbb{Z}_n$
3. If $|G| = p$ (prime), then $G \cong \mathbb{Z}_p$ (no need to check cyclicity)

# Context & Application

This classification theorem means cyclic groups are completely understood. The isomorphism is given by $\phi(k) = a^k$ where $a$ is a generator. This motivates the broader classification problem for all finite groups.

# Examples

**Example 1** (p. 127): $\mathbb{Z}_4 \cong \langle i \rangle$ where $i$ is the imaginary unit, via $\phi(n) = i^n$.

**Example 2** (p. 129): Corollary 6.12 shows groups of prime order are cyclic, so Corollary 9.9 follows.

# Relationships

## Builds Upon
- **Group Isomorphism** — Classification is stated in terms of isomorphism

## Enables
- **Direct Product of Cyclic Groups** — Decomposition of $\mathbb{Z}_{mn}$ into cyclic factors

# Common Errors

- **Error**: Assuming two groups of the same order are isomorphic
  **Correction**: Only works when the order is prime; $\mathbb{Z}_4 \not\cong \mathbb{Z}_2 \times \mathbb{Z}_2$

# Common Confusions

- **Confusion**: Thinking all abelian groups are cyclic
  **Clarification**: $\mathbb{Z}_2 \times \mathbb{Z}_2$ is abelian but not cyclic

# Source Reference

Chapter 9: Isomorphisms, Section 9.1, Theorems 9.7-9.8, Corollary 9.9, pages 129-130.

# Verification Notes

- Definition source: Direct from Theorems 9.7-9.8
- Confidence rationale: Explicit theorems
- Uncertainties: None
- Cross-reference status: Verified
