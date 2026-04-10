---
# === CORE IDENTIFICATION ===
concept: G(n,M) Model
slug: gnm-model

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
  - uniform random graph model
  - "Erdos-Renyi model G(n,M)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - random-graph
extends: []
related:
  - gnp-model
  - graph-process
  - equivalence-gnp-gnm
contrasts_with:
  - gnp-model

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes the G(n,p) model from the G(n,M) model?"
  - "What is the G(n,M) random graph model?"
---

# Quick Definition

The space $\mathcal{G}(n, M)$ consists of all graphs on vertex set $[n]$ with exactly $M$ edges, each chosen with equal probability. It is the uniform model of random graphs.

# Core Definition

For $0 \le M \le N = \binom{n}{2}$, the space $\mathcal{G}(n, M)$ consists of all $\binom{N}{M}$ subgraphs of $K_n$ with $M$ edges, with elements taken to be equiprobable. Writing $G_M = G_{n,M}$ for a random graph in this space, the probability that $G_M$ equals a fixed graph $H$ on $[n]$ with $M$ edges is $\mathbb{P}_M(G_M = H) = \binom{N}{M}^{-1}$ (Bollobás, p. 222).

# Prerequisites

- **Random graph** -- The general concept of a probability space on graphs

# Key Properties

1. The vertex set is always $V = [n] = \{1, 2, \ldots, n\}$
2. All graphs with exactly $M$ edges on $[n]$ are equiprobable
3. Typically $M = M(n)$ depends on $n$
4. For fixed $M$ as $n \to \infty$, with probability tending to 1, $G_{n,M}$ is just $M$ independent edges and $n - 2M$ isolated vertices

# Construction / Recognition

## To Sample from $\mathcal{G}(n, M)$
1. Fix vertex set $[n]$ with $N = \binom{n}{2}$ possible edges
2. Choose uniformly at random one of the $\binom{N}{M}$ subsets of size $M$ from the $N$ possible edges
3. The resulting graph is a sample from $\mathcal{G}(n, M)$

# Context & Application

The $\mathcal{G}(n, M)$ model is natural when the exact number of edges is important. It was the original model studied by Erdos and Renyi. While calculations are often simpler in $\mathcal{G}(n, p)$, the models are asymptotically equivalent for $M \sim pN$ under appropriate conditions.

# Examples

**Example 1** (p. 222): The expected number of complete subgraphs of order $s$ in $\mathcal{G}(n, M)$ is $\mathbb{E}_M(X_s) = \binom{n}{s}\binom{N-S}{M-S}\binom{N}{M}^{-1}$, where $S = \binom{s}{2}$.

**Example 2** (p. 224): The Erdos lower bound on Ramsey numbers can be proved via $\mathcal{G}(n, M)$ with $M = N/2$, yielding $\mathbb{E}_M(X_s) \le \mathbb{E}_{1/2}(X_s)$.

# Relationships

## Builds Upon
- **Random graph** -- General framework

## Enables
- **Graph process** -- The process couples all $\mathcal{G}(n, M)$ spaces
- **Equivalence of G(n,p) and G(n,M)** -- Asymptotic equivalence under appropriate conditions

## Related
- **G(n,p) model** -- The binomial alternative
- **Graph process** -- Nested sequence connecting all $M$ values

## Contrasts With
- **G(n,p) model** -- Fixes edge probability rather than edge count; edges are not independent in $\mathcal{G}(n, M)$

# Common Errors

- **Error**: Assuming edges are independent in $\mathcal{G}(n, M)$
  **Correction**: Edges are not independent since the total count is fixed; this contrasts with $\mathcal{G}(n, p)$

# Common Confusions

- **Confusion**: Thinking $\mathcal{G}(n, M)$ and $\mathcal{G}(n, p)$ always give the same results
  **Clarification**: They are asymptotically equivalent for convex properties when $M \sim pN$, but can differ for non-convex properties

# Source Reference

Chapter VII: Random Graphs, Section VII.1, pages 222--224.

# Verification Notes

- Definition source: Direct from p. 222
- Confidence rationale: Explicit formal definition with notation
- Uncertainties: None
- Cross-reference status: Verified
