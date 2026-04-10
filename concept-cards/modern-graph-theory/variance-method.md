---
# === CORE IDENTIFICATION ===
concept: Variance Method
slug: variance-method

# === CLASSIFICATION ===
category: probabilistic-method
subcategory: second-moment-method
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 238
section: "VII.3 Almost Determined Variables—The Use of the Variance"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - second moment method
  - use of the variance

# === TYPED RELATIONSHIPS ===
prerequisites:
  - chebyshevs-inequality
  - expectation-method
extends:
  - expectation-method
related:
  - balanced-graph
  - clique-number-random-graph
contrasts_with:
  - expectation-method

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I show that almost every random graph contains a given subgraph?"
  - "What must I know before understanding random graph phase transitions?"
---

# Quick Definition

The variance method (second moment method) proves that a random variable $X$ is positive for almost every graph by showing $\sigma^2(X)/\mathbb{E}(X)^2 \to 0$, using Chebyshev's inequality.

# Core Definition

For $X = \sum_i Y_i$ where $Y_i$ are indicator variables, the second moment is $\mathbb{E}(X^2) = \sum_{i,j} \mathbb{E}(Y_i Y_j) = \sum_{(F_i, F_j)} \mathbb{P}(G \supset F_i \cup F_j)$ (equation (14), Bollobás, p. 238). The key computation splits pairs $(F_i, F_j)$ by the number of shared vertices $s$: $\mathbb{E}(X^2)/\mu^2 = \sum_{s=0}^k A_s/\mu^2$, where $A_s$ sums over pairs sharing $s$ vertices. If $\mathbb{E}(X^2)/\mu^2 \to 1$, then $\sigma^2/\mu^2 \to 0$ and $\mathbb{P}(X > 0) \to 1$.

# Prerequisites

- **Chebyshev's inequality** -- The inequality that bounds $\mathbb{P}(X = 0)$ by $\sigma^2/\mu^2$
- **Expectation method** -- The first moment is a prerequisite computation

# Key Properties

1. Requires computing $\mathbb{E}(X^2)$, which involves summing over pairs of subgraphs
2. The critical terms in $\mathbb{E}(X^2)$ are those where the pair shares vertices
3. The $s = 0$ term equals $\mu^2$ (independent copies)
4. Success requires showing the contributions with $s \ge 1$ are negligible

# Construction / Recognition

## To Apply the Variance Method
1. Express $X = \sum_i Y_i$ using indicator variables
2. Compute $\mu = \mathbb{E}(X)$ and verify $\mu \to \infty$
3. Compute $\mathbb{E}(X^2) = \sum_{s=0}^k A_s$ by partitioning pairs by overlap
4. Show $\sum_{s=1}^k A_s / \mu^2 \to 0$
5. Conclude $\sigma^2/\mu^2 \to 0$ and $\mathbb{P}(X > 0) \to 1$

# Context & Application

The variance method goes beyond mere existence (first moment) to show that the desired property holds for almost every graph. It is essential for proving thresholds for subgraph containment and for determining the clique number of random graphs.

# Examples

**Example** (p. 239): For balanced graph $F = G(k, \ell)$ with $p = \gamma n^{-k/\ell}$, the variance computation yields $\mathbb{E}(X^2)/\mu^2 \le 1 + c_4\gamma^{-1} \to 1$ as $\gamma \to \infty$, proving a.e. $G_{n,p}$ contains $F$.

# Relationships

## Builds Upon
- **Chebyshev's inequality** -- Foundational inequality
- **Expectation method** -- First moment is computed first

## Enables
- **Balanced graph** -- Threshold proof uses the variance method
- **Clique number of random graph** -- Concentration result
- **Connectivity threshold** -- Variance of isolated vertex count

## Related
- **Balanced graph** -- Key application

## Contrasts With
- **Expectation method** -- First moment only gives existence; second moment gives almost sure results

# Common Errors

- **Error**: Only computing the diagonal ($s = 0$) terms of $\mathbb{E}(X^2)$
  **Correction**: The off-diagonal terms ($s \ge 1$) are precisely what determines whether the variance is small

# Common Confusions

- **Confusion**: Thinking the variance method always works when $\mu \to \infty$
  **Clarification**: The method fails if the variance grows faster than $\mu^2$; in some cases, more sophisticated methods (e.g., Stein-Chen) are needed

# Source Reference

Chapter VII: Random Graphs, Section VII.3, pages 238--242.

# Verification Notes

- Definition source: Synthesized from Section VII.3 discussion
- Confidence rationale: Explicit method with detailed examples
- Uncertainties: None
- Cross-reference status: Verified
