---
# === CORE IDENTIFICATION ===
concept: Expectation Method
slug: expectation-method

# === CLASSIFICATION ===
category: probabilistic-method
subcategory: first-moment-method
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
aliases:
  - first moment method
  - use of the expectation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - probabilistic-method
  - indicator-random-variable
extends:
  - probabilistic-method
related:
  - markovs-inequality
  - variance-method
  - subgraph-count-expectation
contrasts_with:
  - variance-method

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use expectation to prove graph existence results?"
  - "What is the first moment method in random graph theory?"
---

# Quick Definition

The expectation method (first moment method) proves existence of graphs with desired properties by computing the expected value of a random variable: if $\mathbb{E}(X) < 1$ for a non-negative integer-valued $X$, then $X = 0$ for some element of the space.

# Core Definition

The expectation method is the simplest application of the probabilistic method. For a non-negative random variable $X$ on a probability space, $\mathbb{E}(X) \ge \mathbb{P}(X \ge c\mu) \cdot c\mu$ (Markov's inequality). In particular, if $X$ is integer-valued and $\mathbb{E}(X) < 1$, then $\mathbb{P}(X = 0) > 0$. The key computational tool is the additivity of expectation: if $X = \sum_\alpha Y_\alpha$ where $Y_\alpha$ are indicator random variables, then $\mathbb{E}(X) = \sum_\alpha \mathbb{E}(Y_\alpha)$, regardless of dependence (Bollobás, pp. 223--225).

# Prerequisites

- **Probabilistic method** -- The general framework of proving existence via probability
- **Indicator random variable** -- The building blocks of subgraph counts

# Key Properties

1. Relies only on linearity of expectation -- does not require independence
2. If $\mathbb{E}(X) < 1$ for a non-negative integer-valued $X$, then $\mathbb{P}(X = 0) > 0$
3. If $\mathbb{E}(X)$ is very small, then $X$ is small for most graphs
4. Cannot directly show that $X > 0$ for most graphs (need variance for that)

# Construction / Recognition

## To Apply the Expectation Method
1. Express the count of "bad" substructures as $X = \sum_\alpha Y_\alpha$ using indicator variables
2. Compute $\mathbb{E}(X) = \sum_\alpha \mathbb{P}(Y_\alpha = 1)$ by linearity
3. If $\mathbb{E}(X) < 1$, conclude existence of a graph where $X = 0$

# Context & Application

As Bollobás writes, "it is surprising that even this minimal use of probability theory enables us to prove substantial results about graphs" (p. 223). The method suffices for the Erdos lower bound on Ramsey numbers and the Zarankiewicz problem lower bound.

# Examples

**Example 1** (p. 225): For $R(s,s)$, set $X = X_s + X_s'$ (number of $K_s$ plus number of independent sets of order $s$). In $\mathcal{G}(n, 1/2)$, $\mathbb{E}(X) = 2\binom{n}{s}2^{-\binom{s}{2}} < 1$ for suitable $n$, giving $R(s,s) > \frac{s}{e\sqrt{2}} 2^{s/2}$.

**Example 2** (pp. 226--227): For the bipartite Zarankiewicz problem, computing the expected number of $K_{s,t}$ subgraphs in $\mathcal{G}(K_{n_1,n_2}, M)$ and using deletion gives a lower bound.

# Relationships

## Builds Upon
- **Probabilistic method** -- This is the simplest form
- **Indicator random variable** -- The computational building block

## Enables
- **Erdos lower bound for Ramsey numbers** -- Direct application
- **Graphs of large girth and chromatic number** -- Combined with deletion

## Related
- **Markov's inequality** -- The formal justification
- **Subgraph count expectation** -- The key computation

## Contrasts With
- **Variance method** -- More powerful; can show $X > 0$ a.s., not just existence

# Common Errors

- **Error**: Trying to use the expectation method to show $X > 0$ for almost every graph
  **Correction**: The first moment method can only show existence; to prove $\mathbb{P}(X > 0) \to 1$, use the second moment method

# Common Confusions

- **Confusion**: Thinking linearity of expectation requires independence
  **Clarification**: $\mathbb{E}(\sum Y_i) = \sum \mathbb{E}(Y_i)$ always holds, regardless of dependence

# Source Reference

Chapter VII: Random Graphs, Section VII.1, pages 223--232.

# Verification Notes

- Definition source: Synthesized from discussion in Section VII.1
- Confidence rationale: Explicit method with multiple detailed examples
- Uncertainties: None
- Cross-reference status: Verified
