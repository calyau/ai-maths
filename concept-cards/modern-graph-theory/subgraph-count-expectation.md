---
# === CORE IDENTIFICATION ===
concept: Subgraph Count Expectation
slug: subgraph-count-expectation

# === CLASSIFICATION ===
category: probabilistic-method
subcategory: expectation-calculations
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 223
section: "VII.1 The Basic Models—The Use of the Expectation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gnp-model
  - indicator-random-variable
extends:
  - expectation-method
related:
  - balanced-graph
  - erdos-lower-bound-ramsey
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I compute the expected number of copies of a fixed subgraph in a random graph?"
---

# Quick Definition

In $\mathcal{G}(n, p)$, the expected number of subgraphs isomorphic to a fixed graph $F$ with $k$ vertices, $e(F)$ edges, and automorphism group of order $a$ is $\mathbb{E}_p(X_F) = \frac{(n)_k}{a} p^{e(F)}$.

# Core Definition

Writing $X_F = X_F(G_p)$ for the number of subgraphs of $G_p$ isomorphic to $F$, and $N_F$ for the number of subgraphs of $K_n$ isomorphic to $F$: $\mathbb{E}_p(X_F) = N_F p^{e(F)}$. If $F$ has $k$ vertices and automorphism group of order $a$, then $N_F = (n)_k / a$ where $(n)_k = n(n-1)\cdots(n-k+1)$. Special cases: for $F = K_s$, $\mathbb{E}_p(X_s) = \binom{n}{s}p^{\binom{s}{2}}$; for $F = C_k$ (a $k$-cycle), $\mathbb{E}_p(X_{C_k}) = \frac{(n)_k}{2k}p^k$ (Bollobás, pp. 223--224).

# Prerequisites

- **G(n,p) model** -- The probability space
- **Indicator random variable** -- The method of decomposition

# Key Properties

1. Formula depends on $n$, $p$, the number of edges $e(F)$, and the automorphism group order $a$
2. For induced subgraph counts, multiply by $q^{\binom{k}{2}-e(F)}$
3. The formula is exact, not approximate
4. Applies uniformly to all choices of $F$

# Construction / Recognition

## To Compute $\mathbb{E}_p(X_F)$
1. Determine $k = |V(F)|$ and $e(F) = |E(F)|$
2. Compute $a = |\text{Aut}(F)|$, the order of the automorphism group
3. Apply $\mathbb{E}_p(X_F) = \frac{(n)_k}{a} p^{e(F)}$

# Context & Application

This formula is the workhorse of the first moment method in random graph theory. It provides the starting point for proving thresholds for subgraph containment and is the basis of the Erdos lower bound on Ramsey numbers.

# Examples

**Example 1** (p. 224): For $k$-cycles: $\mathbb{E}_p(X_{C_k}) = \frac{(n)_k}{2k}p^k$ (automorphism group of $C_k$ has order $2k$).

**Example 2** (p. 224): For induced $k$-cycles: $\mathbb{E}_p(Y_{C_k}) = \frac{(n)_k}{2k}p^k q^{k(k-3)/2}$.

# Relationships

## Builds Upon
- **G(n,p) model** -- The probability space
- **Indicator random variable** -- Decomposition tool
- **Expectation method** -- The general framework

## Enables
- **Erdos lower bound for Ramsey numbers** -- Uses $\mathbb{E}(X_s + X_s')$
- **Balanced graph** -- Threshold determined by this expectation
- **Threshold function** -- Transition occurs where expectation changes from $\to 0$ to $\to \infty$

## Related
- **Balanced graph** -- Determines when the expectation tends to infinity

## Contrasts With
- None

# Common Errors

- **Error**: Forgetting the automorphism factor $a$ in $N_F$
  **Correction**: $N_F = (n)_k / a$, not $(n)_k$ or $\binom{n}{k} k!$

# Common Confusions

- **Confusion**: Confusing the count of labeled copies with unlabeled copies
  **Clarification**: $X_F$ counts labeled copies (subgraphs isomorphic to $F$), not induced subgraphs

# Source Reference

Chapter VII: Random Graphs, Section VII.1, pages 223--225. Theorem 1 (p. 224).

# Verification Notes

- Definition source: Direct from pp. 223--225, equations (4) and (5)
- Confidence rationale: Explicit formulas with detailed derivation
- Uncertainties: None
- Cross-reference status: Verified
