---
concept: Annihilator (Dual Space)
slug: annihilator-dual-space
category: linear-algebra
subcategory: dual-spaces
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Vector Spaces"
chapter_number: 11
pdf_page: 429
section: "11.3 Dual Vector Spaces"
extraction_confidence: high
aliases:
  - "Ann(S)"
prerequisites:
  - dual-space
extends: []
related:
  - dual-basis
contrasts_with: []
answers_questions:
  - "What is the annihilator of a subspace in the dual space?"
---

# Quick Definition
For a subset S of $V^*$, the annihilator $\text{Ann}(S) = \{v \in V \mid f(v) = 0 \text{ for all } f \in S\}$ is a subspace of V. For a subspace W of V, $\text{Ann}(W) = \{f \in V^* \mid f(w) = 0 \text{ for all } w \in W\}$. We have $\dim\text{Ann}(W) = \dim V - \dim W$.

# Core Definition
For a subset S of $V^*$, the annihilator is $\text{Ann}(S) = \{v \in V \mid f(v) = 0 \text{ for all } f \in S\}$. Similarly, for a subspace W of V, $\text{Ann}(W) = \{f \in V^* \mid f(w) = 0 \text{ for all } w \in W\}$. If $\dim V = n$ and $\dim W = k$, then $\dim\text{Ann}(W) = n - k$ (Dummit & Foote, Exercise 3, p. 429).

# Prerequisites
- **dual-space** — Annihilators involve the dual space

# Key Properties
1. $\dim\text{Ann}(W) = \dim V - \dim W$
2. Row rank = column rank follows from annihilator dimension counting
3. $\text{Ann}(\text{Ann}(W)) = W$ (under the natural identification $V \cong V^{**}$)

# Relationships
## Builds Upon
- **dual-space**

# Source Reference
Chapter 11, Section 11.3, Exercise 3, p. 429.

# Verification Notes
- Confidence: HIGH — standard definition from exercises
