---
# === CORE IDENTIFICATION ===
concept: Connectivity Threshold
slug: connectivity-threshold

# === CLASSIFICATION ===
category: random-graphs
subcategory: threshold-phenomena
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 242
section: "VII.3 Almost Determined Variables—The Use of the Variance"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Erdos-Renyi connectivity threshold

# === TYPED RELATIONSHIPS ===
prerequisites:
  - threshold-function
  - variance-method
extends: []
related:
  - property-hitting-time
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "At what edge probability does a random graph become connected?"
---

# Quick Definition

The threshold for connectivity in $\mathcal{G}(n, p)$ is $p^* = \log n / n$: for $p = (\log n - \omega)/n$ a.e. graph is disconnected, while for $p = (\log n + \omega)/n$ a.e. graph is connected, where $\omega(n) \to \infty$.

# Core Definition

**Theorem 9** (Bollobas, p. 242): Let $\omega(n) \to \infty$ and set $p_\ell = (\log n - \omega(n))/n$ and $p_u = (\log n + \omega(n))/n$. Then a.e. $G_{p_\ell}$ is disconnected and a.e. $G_{p_u}$ is connected. The proof for $p_\ell$ shows that the expected number of isolated vertices $\mu = ne^{-\log n + \omega} = e^\omega \to \infty$ and $\sigma^2/\mu^2 \to 0$. The proof for $p_u$ uses a first moment bound on the number of small components.

# Prerequisites

- **Threshold function** -- The framework for the result
- **Variance method** -- Used in the subcritical direction

# Key Properties

1. The threshold is $\log n / n$, matching the threshold for minimum degree $\ge 1$
2. Below the threshold, isolated vertices are the obstruction
3. Above the threshold, not only are there no isolated vertices, but the graph is connected
4. Theorem 11 sharpens this: $\tau(\text{conn}) = \tau(\delta \ge 1)$ a.s. in graph processes

# Construction / Recognition

## Proof Structure
1. **Below threshold** ($p = p_\ell$): Show $\mathbb{E}(X_1) = e^\omega \to \infty$ and $\sigma^2/\mu^2 \to 0$, so $X_1 > 0$ a.s.
2. **Above threshold** ($p = p_u$): Bound $\mathbb{P}(\text{disconnected}) \le \sum_{k=1}^{n/2} \binom{n}{k}(1-p)^{k(n-k)} \to 0$

# Context & Application

This is one of the most classical results in random graph theory. It illustrates the sharp threshold phenomenon: connectivity transitions from absent to present over a tiny window of $p$ values around $\log n / n$.

# Examples

**Example** (p. 243): For $p_\ell$, the expected number of isolated vertices is $e^{\omega(n)} \to \infty$. For $p_u$, the probability of disconnection is at most $4e^{-\omega(n)} \to 0$.

# Relationships

## Builds Upon
- **Threshold function** -- Framework
- **Variance method** -- For the subcritical direction

## Enables
- **Connectivity hitting time** -- $\tau(\text{conn}) = \tau(\delta \ge 1)$

## Related
- **Property hitting time** -- Connectivity has a clean hitting time characterization

## Contrasts With
- None

# Common Errors

- **Error**: Stating the threshold as $p = 1/n$ (the phase transition threshold)
  **Correction**: $1/n$ is the threshold for the giant component, not connectivity; connectivity requires $p = \log n / n$

# Common Confusions

- **Confusion**: Confusing the connectivity threshold with the giant component threshold
  **Clarification**: Giant component emerges at $p \sim 1/n$; connectivity requires $p \sim \log n / n$, which is much larger

# Source Reference

Chapter VII: Random Graphs, Section VII.3, Theorem 9, pages 242--243.

# Verification Notes

- Definition source: Direct from Theorem 9, p. 242
- Confidence rationale: Explicit theorem with full proof
- Uncertainties: None
- Cross-reference status: Verified
