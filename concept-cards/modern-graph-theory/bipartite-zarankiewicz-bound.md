---
# === CORE IDENTIFICATION ===
concept: Bipartite Zarankiewicz Bound
slug: bipartite-zarankiewicz-bound

# === CLASSIFICATION ===
category: probabilistic-method
subcategory: extremal-problems
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 226
section: "VII.1 The Basic Models—The Use of the Expectation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - expectation-method
extends:
  - probabilistic-method
related:
  - erdos-lower-bound-ramsey
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the probabilistic method give lower bounds for the Zarankiewicz problem?"
---

# Quick Definition

Using the probabilistic method on bipartite random graphs, there exists a $K(s,t)$-free bipartite graph $G_2(n_1, n_2)$ with $\lfloor(1 - 1/(s!t!))n_1^{1-\alpha}n_2^{1-\beta}\rfloor$ edges, where $\alpha = (s-1)/(st-1)$ and $\beta = (t-1)/(st-1)$.

# Core Definition

**Theorem 3** (Bollobas, p. 226): Let $2 \le s \le n_1$, $2 \le t \le n_2$, $\alpha = (s-1)/(st-1)$, $\beta = (t-1)/(st-1)$. There exists a $K(s,t)$-free bipartite graph with $\lfloor(1 - 1/(s!t!))n_1^{1-\alpha}n_2^{1-\beta}\rfloor$ edges. The proof uses $\mathcal{G}(K_{n_1,n_2}, M)$, computes the expected number of $K_{s,t}$ subgraphs, and deletes one edge from each.

# Prerequisites

- **Expectation method** -- The probabilistic tool

# Key Properties

1. Uses a bipartite random graph model $\mathcal{G}(K_{n_1,n_2}, M)$
2. Combines first moment bound with deletion
3. For $s = t$: gives $z(n,n;t,t) \ge cn^{2-2/(t+1)}$
4. Likely not tight: the upper bound is $cn^{2-1/t}$

# Construction / Recognition

Not applicable -- this is an existence result.

# Context & Application

This extends the probabilistic method to bipartite extremal problems. While the bound is the best known lower bound for large $s = t$, there is a significant gap with the upper bound.

# Examples

**Example** (p. 228): For $s = t = 2$: gives $K(2,2)$-free bipartite graph with $\Theta(n^{4/3})$ edges.

# Relationships

## Builds Upon
- **Expectation method**

## Enables
- Lower bounds in Zarankiewicz-type problems

## Related
- **Erdos lower bound for Ramsey numbers** -- Analogous probabilistic argument

## Contrasts With
- None

# Common Errors

- **Error**: Thinking this gives the right order for the Zarankiewicz function
  **Correction**: The bound is likely far from optimal for large $s = t$

# Common Confusions

- **Confusion**: Confusing this with the general (non-bipartite) extremal problem
  **Clarification**: This is specifically for bipartite graphs and the Zarankiewicz function

# Source Reference

Chapter VII, Section VII.1, Theorem 3, pages 226--228.

# Verification Notes

- Definition source: Direct from Theorem 3
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
