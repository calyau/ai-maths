---
# === CORE IDENTIFICATION ===
concept: Indicator Random Variable
slug: indicator-random-variable

# === CLASSIFICATION ===
category: probabilistic-method
subcategory: basic-tools
tier: foundational

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
  - indicator function
  - characteristic function of an event

# === TYPED RELATIONSHIPS ===
prerequisites:
  - random-graph
extends: []
related:
  - expectation-method
  - subgraph-count-expectation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are subgraph counts expressed as sums of indicator variables?"
---

# Quick Definition

An indicator random variable $Y_\alpha$ for a subgraph $F_\alpha$ takes value 1 if $F_\alpha$ is a subgraph of the random graph and 0 otherwise. Subgraph counts are sums of such indicators.

# Core Definition

For a family $\mathcal{F} = \{F_1, F_2, \ldots\}$ of graphs with $V(F_i) \subset [n]$, the indicator function $Y_i = Y_{F_i}(G)$ is defined as $Y_i(G) = 1$ if $F_i \subset G$ and $Y_i(G) = 0$ otherwise. Then the count $X = \sum_i Y_i$ counts the number of copies of structures from $\mathcal{F}$ in $G$. By linearity of expectation, $\mathbb{E}(X) = \sum_i \mathbb{P}(F_i \subset G)$ regardless of dependence (Bollobás, p. 223).

# Prerequisites

- **Random graph** -- The probability space on which indicators are defined

# Key Properties

1. $\mathbb{E}(Y_\alpha) = \mathbb{P}(Y_\alpha = 1) = \mathbb{P}(F_\alpha \subset G)$
2. In $\mathcal{G}(n, p)$: $\mathbb{E}(Y_\alpha) = p^{e(F_\alpha)}$ for a subgraph $F_\alpha$ with $e(F_\alpha)$ edges
3. Linearity of expectation applies to sums of indicators without requiring independence
4. For second moment calculations: $\mathbb{E}(Y_i Y_j) = \mathbb{P}(F_i \cup F_j \subset G)$

# Construction / Recognition

## To Set Up a Subgraph Count
1. Fix the family $\mathcal{F}$ of labeled subgraphs (e.g., all copies of $K_s$ on $[n]$)
2. Define $Y_i(G) = 1$ if $F_i \subset G$, $0$ otherwise
3. Set $X = \sum_i Y_i$; then $X$ counts copies of the target structure
4. Compute $\mathbb{E}(X) = |\mathcal{F}| \cdot p^{e(F)}$ in $\mathcal{G}(n, p)$ if all $F_i$ are isomorphic

# Context & Application

Indicator variables are the basic computational tool in random graph theory. They decompose complicated counting random variables into simple Bernoulli trials, enabling expectation calculations via linearity without needing to address dependence.

# Examples

**Example** (p. 223): Let $S = [n]^{(s)}$ be the set of $s$-subsets of $[n]$, and for $\alpha \in S$ let $Y_\alpha(G) = 1$ if $G[\alpha] = K_\alpha$. Then $X_s(G) = \sum_{\alpha \in S} Y_\alpha(G)$ counts complete subgraphs of order $s$, and $\mathbb{E}_p(X_s) = \binom{n}{s}p^{\binom{s}{2}}$.

# Relationships

## Builds Upon
- **Random graph** -- Defined on random graph spaces

## Enables
- **Expectation method** -- Computed via sums of indicators
- **Subgraph count expectation** -- The standard application
- **Variance method** -- Second moments involve products $Y_i Y_j$

## Related
- **Subgraph count expectation** -- Direct use of indicator sums

## Contrasts With
- None

# Common Errors

- **Error**: Assuming $\mathbb{E}(X^2) = (\mathbb{E}(X))^2$ for sums of indicators
  **Correction**: $\mathbb{E}(X^2) = \sum_{i,j} \mathbb{E}(Y_i Y_j)$, which involves correlations between pairs

# Common Confusions

- **Confusion**: Thinking the indicators must be independent for linearity of expectation to hold
  **Clarification**: $\mathbb{E}(\sum Y_i) = \sum \mathbb{E}(Y_i)$ always, regardless of dependence

# Source Reference

Chapter VII: Random Graphs, Section VII.1, pages 223--224.

# Verification Notes

- Definition source: Direct from pp. 223--224
- Confidence rationale: Explicit definition with worked examples
- Uncertainties: None
- Cross-reference status: Verified
