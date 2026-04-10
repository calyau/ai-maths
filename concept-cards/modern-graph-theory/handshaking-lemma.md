---
concept: Handshaking Lemma
slug: handshaking-lemma
category: graph-fundamentals
subcategory: basic-results
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.1 Definitions"
extraction_confidence: high
aliases:
  - degree-sum formula
  - first theorem of graph theory
prerequisites:
  - graph
  - vertex-degree
  - edge
extends: []
related:
  - degree-sequence
contrasts_with: []
answers_questions:
  - "What is the handshaking lemma?"
  - "What is the relationship between the sum of degrees and the number of edges?"
---

# Quick Definition

The handshaking lemma states that $\sum_{i=1}^{n} d(x_i) = 2e(G)$: the sum of all vertex degrees equals twice the number of edges. Consequently, the number of vertices of odd degree is even.

# Core Definition

"Since each edge has two endvertices, the sum of the degrees is exactly twice the number of edges: $\sum_{i=1}^{n} d(x_i) = 2e(G)$. [...] This last observation is sometimes called the handshaking lemma, since it expresses the fact that in any party the total number of hands shaken is even. Equivalently, (2) states that the number of vertices of odd degree is even" (Bollobás, p. 12).

# Prerequisites

- **Graph** — Applies to all graphs
- **Vertex degree** — Uses degrees of all vertices
- **Edge** — Each edge contributes to two degrees

# Key Properties

1. $\sum d(x_i) = 2e(G)$ — fundamental identity
2. $\sum d(x_i) \equiv 0 \pmod{2}$ — the sum is always even
3. The number of odd-degree vertices is even
4. Implies $\delta(G) \le \lfloor 2e(G)/n \rfloor$ and $\Delta(G) \ge \lceil 2e(G)/n \rceil$

# Construction / Recognition

The lemma is verified by observing that each edge $xy$ contributes 1 to $d(x)$ and 1 to $d(y)$, so each edge contributes 2 to the total sum.

# Context & Application

The handshaking lemma is one of the most basic and frequently used results in graph theory. It is used in the proof of Mantel's theorem (Theorem 2) and Corollary 8 (relating tree size to order). Its simplicity belies its usefulness in counting arguments.

# Examples

**Example** (p. 12): The bound in Mantel's theorem uses the handshaking lemma together with Cauchy's inequality to show that a triangle-free graph of order $n$ has at most $\lfloor n^2/4 \rfloor$ edges.

# Relationships

## Builds Upon
- **Graph**, **Vertex degree**, **Edge**

## Enables
- **Mantel's theorem** — Uses degree-sum relations
- Parity arguments in graph theory

# Common Errors

- **Error**: Forgetting that each edge is counted twice in the degree sum
  **Correction**: Each edge contributes 1 to each of its two endvertices' degrees, hence 2 to the total

# Common Confusions

- **Confusion**: Thinking the lemma only applies to simple graphs
  **Clarification**: It applies to multigraphs too, with loops contributing 2 to the degree

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 12.

# Verification Notes

- Definition source: Direct from p. 12
- Confidence rationale: Explicitly stated and named
- Uncertainties: None
- Cross-reference status: Verified
