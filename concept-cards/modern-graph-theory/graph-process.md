---
# === CORE IDENTIFICATION ===
concept: Graph Process
slug: graph-process

# === CLASSIFICATION ===
category: random-graphs
subcategory: random-graph-models
tier: foundational

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 222
section: "VII.1 The Basic Models—The Use of the Expectation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - random graph process

# === TYPED RELATIONSHIPS ===
prerequisites:
  - random-graph
  - gnm-model
extends: []
related:
  - gnp-model
  - hitting-time
  - phase-transition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a graph process?"
  - "How does a random graph evolve over time?"
---

# Quick Definition

A graph process is a nested sequence of graphs $G_0 \subset G_1 \subset \cdots \subset G_N$ on $[n]$ where $G_t$ has exactly $t$ edges, representing a random graph that acquires edges one at a time.

# Core Definition

An element of $\widetilde{\mathcal{G}}^n$ is a graph process, a nested sequence of graphs $G_0 \subset G_1 \subset \cdots \subset G_N$ with $G_t$ having precisely $t$ edges, where $N = \binom{n}{2}$. Every graph process is identified with a permutation $(e_i)_1^N$ of the $N$ edges of $K_n$ via $\{e_t\} = E(G_t) - E(G_{t-1})$. The space $\widetilde{\mathcal{G}}^n$ of all $N!$ graph processes is made into a probability space by taking all processes equiprobable (Bollobás, p. 222).

# Prerequisites

- **Random graph** -- General framework of probability spaces on graphs
- **G(n,M) model** -- Each $G_t$ in the process is an element of $\mathcal{G}(n, t)$

# Key Properties

1. Contains $N!$ elements, each corresponding to a permutation of edges
2. The map $\widetilde{\mathcal{G}}^n \to \mathcal{G}(n, M)$ given by $(G_t)_0^N \mapsto G_M$ is measure-preserving
3. Couples all the spaces $\mathcal{G}(n, M)$ for $M = 0, 1, \ldots, N$
4. Starts as the empty graph $G_0 = E_n$ and evolves by acquiring one random edge at each step

# Construction / Recognition

## Interpretation
1. Start with empty graph on $[n]$
2. At time $t$, acquire one edge uniformly at random from the $N - t$ edges not yet present
3. Continue until $G_N = K_n$

# Context & Application

The graph process provides a dynamic view of random graph evolution. It is the natural framework for studying hitting times: the moment at which a property first appears. Key results like the connection between connectivity and minimum degree are best expressed in terms of graph processes.

# Examples

**Example** (p. 222): A random graph process $\widetilde{G} = (G_t)_0^N$ is described as "a living organism that starts its life as the empty graph $G_0 = E_n$ and evolves by acquiring more and more edges."

# Relationships

## Builds Upon
- **Random graph** -- General framework
- **G(n,M) model** -- Each snapshot is a $\mathcal{G}(n, M)$ random graph

## Enables
- **Hitting time** -- Defined as the first time a property appears in the process
- **Phase transition** -- Observed as the process passes through $t \approx n/2$

## Related
- **G(n,p) model** -- Related via random stopping time

## Contrasts With
- None

# Common Errors

- **Error**: Thinking the graph process and $\mathcal{G}(n, M)$ are the same thing
  **Correction**: The process couples all the $\mathcal{G}(n, M)$ spaces; it is a sequence, not a single graph

# Common Confusions

- **Confusion**: Thinking edges can be removed in a graph process
  **Clarification**: A graph process is monotone; edges are only added, never removed

# Source Reference

Chapter VII: Random Graphs, Section VII.1, page 222.

# Verification Notes

- Definition source: Direct from p. 222
- Confidence rationale: Explicit definition with formal notation
- Uncertainties: None
- Cross-reference status: Verified
