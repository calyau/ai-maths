---
# === CORE IDENTIFICATION ===
concept: G(n,p) Model
slug: gnp-model

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
  - binomial random graph
  - "Erdos-Renyi model G(n,p)"
  - "G(n, P(edge) = p)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - random-graph
extends: []
related:
  - gnm-model
  - graph-process
  - equivalence-gnp-gnm
contrasts_with:
  - gnm-model

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes the G(n,p) model from the G(n,M) model?"
  - "What is the binomial random graph model?"
---

# Quick Definition

The space $\mathcal{G}(n, p)$ is the random graph model on vertex set $[n]$ where each of the $\binom{n}{2}$ possible edges is included independently with probability $p$.

# Core Definition

The space $\mathcal{G}(n, p)$, for $0 \le p \le 1$, has ground set consisting of all $2^N$ graphs on $[n]$, where $N = \binom{n}{2}$. The probability of a graph $H$ on $[n]$ with $m$ edges is $p^m(1-p)^{N-m}$. Writing $q = 1-p$ and $G_p = G_{n,p}$ for a random element: $\mathbb{P}_p(G_p = H) = p^{e(H)}q^{N-e(H)}$ (Bollobás, p. 222).

# Prerequisites

- **Random graph** -- The general concept of a probability space on graphs

# Key Properties

1. Each edge is included independently with probability $p$
2. The number of edges is a binomial random variable with parameters $N$ and $p$
3. Writing $q = 1 - p$, the probability of any specific graph depends only on its number of edges
4. Both $p$ and $M = M(n)$ are typically functions of $n$
5. $\mathcal{G}(n, 1/2)$ is the uniform space of all graphs on $[n]$

# Construction / Recognition

## To Sample from $\mathcal{G}(n, p)$
1. Fix vertex set $[n]$ and parameter $p \in [0, 1]$
2. For each of the $N = \binom{n}{2}$ possible edges, independently include it with probability $p$
3. The resulting graph is a sample from $\mathcal{G}(n, p)$

# Context & Application

The $\mathcal{G}(n, p)$ model is preferred for most calculations because edges are independent, making expectation and variance computations cleaner. If $G_p$ is conditioned on $e(G_p) = M$, one obtains $\mathcal{G}(n, M)$. The model is particularly natural for studying threshold phenomena.

# Examples

**Example 1** (p. 223): The expected number of $K_s$ subgraphs is $\mathbb{E}_p(X_s) = \binom{n}{s}p^S$, where $S = \binom{s}{2}$.

**Example 2** (p. 224): For subgraphs isomorphic to a fixed graph $F$ with $k$ vertices and automorphism group of order $a$: $\mathbb{E}_p(X_F) = \frac{(n)_k}{a}p^{e(F)}$.

# Relationships

## Builds Upon
- **Random graph** -- General framework

## Enables
- **Threshold function** -- Defined via $\mathcal{G}(n, p)$
- **Almost every graph** -- A.e. properties defined in $\mathcal{G}(n, p)$
- **Phase transition** -- Analyzed via $p = c/n$

## Related
- **G(n,M) model** -- The uniform alternative
- **Equivalence of G(n,p) and G(n,M)** -- Conditions for interchangeability

## Contrasts With
- **G(n,M) model** -- Fixes edge count rather than probability; edges are independent in G(n,p) but not in G(n,M)

# Common Errors

- **Error**: Forgetting that $p$ typically depends on $n$
  **Correction**: While $p$ can be fixed, the most interesting results concern $p = p(n)$ varying with $n$

# Common Confusions

- **Confusion**: Thinking $\mathcal{G}(n, p)$ always has exactly $pN$ edges
  **Clarification**: The number of edges is random with expectation $pN$; the actual count varies according to a binomial distribution

# Source Reference

Chapter VII: Random Graphs, Section VII.1, pages 222--224.

# Verification Notes

- Definition source: Direct from p. 222
- Confidence rationale: Explicit formal definition
- Uncertainties: None
- Cross-reference status: Verified
