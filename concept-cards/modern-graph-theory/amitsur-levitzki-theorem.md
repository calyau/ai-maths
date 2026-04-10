---
concept: Amitsur-Levitzki Theorem
slug: amitsur-levitzki-theorem
category: paths-and-cycles
subcategory: hamilton-euler
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.5 An Application of Euler Trails to Algebra"
extraction_confidence: high
aliases:
  - standard polynomial identity
prerequisites:
  - euler-trail
  - directed-graph
extends: []
related:
  - euler-circuit
contrasts_with: []
answers_questions:
  - "How do Euler trails apply to algebra?"
---

# Quick Definition

The Amitsur-Levitzki theorem states that the ring $M_k(R)$ of $k \times k$ matrices over a commutative ring $R$ satisfies the $2k$th standard polynomial identity: $[A_1, A_2, \ldots, A_{2k}] = 0$ for all $A_i \in M_k(R)$.

# Core Definition

"**Theorem 19.** Let $R$ be a commutative ring and let the matrices $A_1, A_2, \ldots, A_{2k}$ be in $M_k(R)$. Then $[A_1, A_2, \ldots, A_{2k}] = 0$" (Bollobás, p. 34), where $[A_1, \ldots, A_{2k}] = \sum_\sigma \text{sgn}(\sigma) A_{\sigma 1} \cdots A_{\sigma 2k}$. The proof reduces to Lemma 20: if a directed multigraph has $m \ge 2n$ edges, then $\varepsilon(\vec{G}; x, y) = 0$.

# Prerequisites

- **Euler trail** — The proof uses Euler trails in directed multigraphs
- **Directed graph** — Matrix products correspond to directed walks

# Key Properties

1. The $2k$th standard polynomial identity is the smallest such identity for $M_k(R)$
2. The proof converts matrix multiplication to directed Euler trails
3. A product $A_{\sigma 1} \cdots A_{\sigma 2n}$ (where $A_k = E_{i_k j_k}$) is nonzero iff the corresponding edge sequence is an Euler trail
4. The key lemma shows that the signed sum over all Euler trails vanishes when $m \ge 2n$

# Construction / Recognition

The proof strategy:
1. Reduce to basis matrices $E_{ij}$
2. Build a directed multigraph from the index pairs
3. Show $\varepsilon(\vec{G}; i, j) = 0$ for all $i, j$ when $m \ge 2n$ (Lemma 20)
4. Prove Lemma 20 by induction using graph transformations

# Context & Application

This section demonstrates that "even simple notions like the ones presented so far may be of use in proving important results" (Bollobás, p. 33). It connects graph theory with ring theory and polynomial identities.

# Examples

**Example** (p. 33): The commutator $[a_1, a_2, a_3] = a_1 a_2 a_3 - a_1 a_3 a_2 + a_3 a_1 a_2 - a_3 a_2 a_1 + a_2 a_3 a_1 - a_2 a_1 a_3$.

# Relationships

## Builds Upon
- **Euler trail**, **Directed graph**

## Related
- **Euler circuit** — The proof uses Euler trail counting in digraphs

# Common Errors

- **Error**: Thinking the theorem holds for $k$th polynomial identity rather than $2k$th
  **Correction**: The identity is the $2k$th; $M_k(R)$ does not satisfy a lower polynomial identity in general

# Common Confusions

- **Confusion**: Thinking this is purely an algebra result
  **Clarification**: The proof is essentially graph-theoretic, using Euler trail counting

# Source Reference

Chapter I: Fundamentals, Section I.5, Theorem 19 and Lemma 20, pages 33-36.

# Verification Notes

- Definition source: Direct theorem statement from p. 34
- Confidence rationale: Explicitly stated with full proof
- Uncertainties: None
- Cross-reference status: Verified
