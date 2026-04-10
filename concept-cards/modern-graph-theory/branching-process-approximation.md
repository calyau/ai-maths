---
# === CORE IDENTIFICATION ===
concept: Branching Process Approximation
slug: branching-process-approximation

# === CLASSIFICATION ===
category: random-graphs
subcategory: analytic-tools
tier: advanced

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 249
section: "VII.5 The Phase Transition"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Karp's approach

# === TYPED RELATIONSHIPS ===
prerequisites:
  - phase-transition
  - poisson-branching-process
extends: []
related:
  - giant-component
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is the giant component size determined?"
  - "What is the connection between random graphs and branching processes?"
---

# Quick Definition

The component of a vertex in $G_{n,p}$ with $p = c/n$ can be approximated by a Poisson branching process with mean $c$: the probability of belonging to the giant component equals the survival probability of the branching process.

# Core Definition

Karp's idea (Bollobas, p. 249) is to grow the component $C(x)$ of a fixed vertex $x$ by exploring neighbors layer by layer. At each step, the number of new neighbors is approximately $\text{Poisson}(c)$: $\mathbb{P}(u_i \text{ has } k \text{ new neighbours}) = \frac{c^k}{k!}e^{-c}(1 + O((\log n)^2/n))$. Therefore $|C(x)|$ is approximately the total population of a Poisson branching process. **Theorem 19**: The survival probability $p_\infty$ satisfies $e^{-cp_\infty} = 1 - p_\infty$, which equals $\gamma$ from Theorem 17(iii).

# Prerequisites

- **Phase transition** -- Context for the approximation
- **Poisson branching process** -- The approximating process

# Key Properties

1. Each vertex's number of new neighbors is approximately Poisson($c$)
2. The approximation is valid as long as the explored set is $o(n)$
3. The survival probability of the branching process equals $\gamma$ from the phase transition
4. This explains why $e^{-c\gamma} = 1 - \gamma$ determines the giant component size

# Construction / Recognition

## Component Exploration
1. Start at vertex $x$; set $B_0 = \{x\}$
2. At step $i$: each vertex in $V - B_i$ is added to $B_{i+1}$ independently with probability $p$
3. $|B_i|$ has binomial distribution with parameters $n-1$ and $1-(1-p)^i$
4. The component $C(x)$ is $B_\ell$ where $\ell$ is the first index with $|B_\ell| = \ell$

# Context & Application

The branching process approximation provides both intuition and rigorous tools for analyzing the phase transition. It explains why the phase transition occurs at $c = 1$: the branching process dies out a.s. when the mean offspring is $\le 1$ and survives with positive probability when $> 1$.

# Examples

**Example** (p. 250): For the Poisson branching process with $c > 1$: $1 - p_{n+1} = e^{-cp_n}$ with $p_0 = 1$. The limit $p_\infty$ satisfies $e^{-cp_\infty} = 1 - p_\infty$, matching $\gamma$.

# Relationships

## Builds Upon
- **Phase transition** -- The phenomenon being explained
- **Poisson branching process** -- The approximating model

## Enables
- Rigorous determination of $\gamma(c)$

## Related
- **Giant component** -- Size determined by the branching process survival probability

## Contrasts With
- None

# Common Errors

- **Error**: Using the branching process approximation for large components
  **Correction**: The approximation is valid only while the explored set is $o(n)$; for the giant component, additional arguments are needed

# Common Confusions

- **Confusion**: Thinking the branching process is exact
  **Clarification**: It is an approximation that becomes exact in the $n \to \infty$ limit for small components

# Source Reference

Chapter VII: Random Graphs, Section VII.5, pages 249--252. Theorem 19 on p. 250.

# Verification Notes

- Definition source: Synthesized from pp. 249--252
- Confidence rationale: Detailed discussion with explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
