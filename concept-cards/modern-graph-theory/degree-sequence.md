---
concept: Degree Sequence
slug: degree-sequence
category: graph-fundamentals
subcategory: basic-definitions
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.1 Definitions"
extraction_confidence: high
aliases: []
prerequisites:
  - graph
  - vertex-degree
extends: []
related:
  - handshaking-lemma
  - graph-isomorphism
contrasts_with: []
answers_questions:
  - "What is the degree sequence of a graph?"
---

# Quick Definition

The degree sequence of a graph $G$ with $V(G) = \{x_1, \ldots, x_n\}$ is the sequence $(d(x_i))_1^n$, usually ordered so that $\delta(G) = d(x_1) \le \cdots \le d(x_n) = \Delta(G)$.

# Core Definition

"If $V(G) = \{x_1, x_2, \ldots, x_n\}$, then $(d(x_i))_1^n$ is a degree sequence of $G$. Usually we order the vertices in such a way that the degree sequence obtained in this way is monotone increasing or monotone decreasing" (Bollobás, p. 12).

# Prerequisites

- **Graph** — The degree sequence is a property of a graph
- **Vertex degree** — Each entry is a vertex degree

# Key Properties

1. A degree sequence has $n$ entries, one per vertex
2. The sum of all entries equals $2e(G)$ by the handshaking lemma
3. Two isomorphic graphs have the same degree sequence (but the converse fails)
4. A tree of order $n$ has degree sequence summing to $2n - 2$

# Construction / Recognition

1. Compute $d(x)$ for each vertex $x \in V(G)$
2. Sort in non-decreasing (or non-increasing) order

# Context & Application

Degree sequences are a basic invariant used for graph comparison and classification. Characterizing which integer sequences are degree sequences of graphs (the Erdos-Gallai theorem) is a classical problem.

# Examples

**Example** (p. 12): A tree of order $n$ has degree sequence satisfying $d_1 \ge 1$ and $\sum d_i = 2n - 2$.

# Relationships

## Builds Upon
- **Graph**, **Vertex degree**

## Enables
- **Handshaking lemma** — The degree sum property
- Graph isomorphism testing (necessary condition)

# Common Errors

- **Error**: Concluding isomorphism from equal degree sequences
  **Correction**: Equal degree sequences are necessary but not sufficient for isomorphism

# Common Confusions

- **Confusion**: Thinking degree sequence determines the graph uniquely
  **Clarification**: Many non-isomorphic graphs share the same degree sequence

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 12.

# Verification Notes

- Definition source: Direct from p. 12
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
