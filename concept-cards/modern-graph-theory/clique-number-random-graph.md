---
# === CORE IDENTIFICATION ===
concept: Clique Number of a Random Graph
slug: clique-number-random-graph

# === CLASSIFICATION ===
category: random-graphs
subcategory: graph-invariants
tier: advanced

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 240
section: "VII.3 Almost Determined Variables—The Use of the Variance"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variance-method
  - subgraph-count-expectation
extends: []
related:
  - chromatic-number-random-graph
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How large is the clique number of a typical random graph?"
---

# Quick Definition

For fixed $p \in (0,1)$, the clique number of almost every $G_{n,p}$ takes one of two values: $d$ or $d+1$, where $d = 2\log_b n + O(\log\log n)$ with $b = 1/p$.

# Core Definition

**Theorem 8** (Bollobás, p. 241): Let $0 < p < 1$ be fixed. Then the clique number of almost every $G_{n,p}$ is $d$ or $d+1$, where $d = d(n)$ is the greatest natural number for which $\mathbb{E}(X_d) = \binom{n}{d}p^{\binom{d}{2}} \ge \log n$. Furthermore, $d = 2\log_b n + O(\log\log n)$ where $b = 1/p$.

# Prerequisites

- **Variance method** -- Used to show $\mathbb{P}(X_d > 0) \to 1$
- **Subgraph count expectation** -- Need $\mathbb{E}(X_r)$ for the definition of $d$

# Key Properties

1. The clique number is concentrated on at most two consecutive values
2. For most values of $n$, it takes a single value (Bollobás and Erdos, 1976)
3. $d \sim 2\log_b n$ where $b = 1/p$
4. The proof uses $\mathbb{P}(X_{d+2} > 0) \to 0$ (first moment) and $\sigma_d/\mu_d \to 0$ (second moment)

# Construction / Recognition

## Proof Outline
1. Define $d$ as the largest integer with $\mathbb{E}(X_d) \ge \log n$
2. Show $\mathbb{E}(X_{d+2}) \to 0$, so $\mathbb{P}(\omega(G) \ge d+2) \to 0$
3. Show $\sigma_d^2/\mu_d^2 \to 0$ via careful second moment computation
4. By Chebyshev, $\mathbb{P}(X_d > 0) \to 1$, so $\omega(G) \ge d$ a.s.

# Context & Application

The concentration of the clique number on two values is a striking result. It feeds into the determination of the chromatic number of random graphs, via $\chi(G) \ge n/\alpha(G)$.

# Examples

**Example** (p. 241): For $p = 1/2$, $b = 2$, so $d \sim 2\log_2 n$. A.e. $G_{n,1/2}$ has clique number within 1 of $2\log_2 n$.

# Relationships

## Builds Upon
- **Variance method** -- Core technique
- **Subgraph count expectation** -- Definition of $d$

## Enables
- **Chromatic number of random graph** -- Lower bound via $\chi \ge n/\alpha$

## Related
- **Chromatic number of random graph** -- Closely linked

## Contrasts With
- None

# Common Errors

- **Error**: Assuming the clique number takes exactly one value for all large $n$
  **Correction**: For most $n$ the value is unique, but there are exceptional $n$ where both $d$ and $d+1$ occur

# Common Confusions

- **Confusion**: Confusing clique number with independence number
  **Clarification**: The independence number of $G_{n,p}$ equals the clique number of $G_{n,q}$ where $q = 1-p$

# Source Reference

Chapter VII: Random Graphs, Section VII.3, Theorem 8, pages 240--242.

# Verification Notes

- Definition source: Direct from Theorem 8, p. 241
- Confidence rationale: Explicit theorem with full proof
- Uncertainties: None
- Cross-reference status: Verified
