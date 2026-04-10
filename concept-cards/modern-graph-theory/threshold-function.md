---
# === CORE IDENTIFICATION ===
concept: Threshold Function
slug: threshold-function

# === CLASSIFICATION ===
category: random-graphs
subcategory: phase-transitions
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 241
section: "VII.3 Almost Determined Variables—The Use of the Variance"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - lower threshold function
  - upper threshold function

# === TYPED RELATIONSHIPS ===
prerequisites:
  - almost-every-graph
  - monotone-increasing-property
extends: []
related:
  - balanced-graph
  - connectivity-threshold
  - phase-transition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a threshold function for a graph property?"
  - "How do graph properties emerge suddenly in random graphs?"
---

# Quick Definition

A function $p_\ell(n)$ is a lower threshold function (ltf) for a monotone increasing property $Q$ if almost no $G_{n,p_\ell}$ has $Q$; $p_u(n)$ is an upper threshold function (utf) if almost every $G_{n,p_u}$ has $Q$.

# Core Definition

A function $p_\ell(n)$ is a lower threshold function for a monotone increasing property $Q$ if almost no $G_{n,p_\ell(n)}$ has $Q$, and $p_u(n)$ is an upper threshold function for $Q$ if almost every $G_{n,p_u(n)}$ has $Q$ (Bollobás, p. 241). Theorem 7 shows that for balanced $F$ with parameters $(k, \ell)$, the threshold for containment is $n^{-k/\ell}$: $n^{-k/\ell}/\omega$ is an ltf and $\omega n^{-k/\ell}$ is a utf whenever $\omega(n) \to \infty$.

# Prerequisites

- **Almost every graph** -- The definition of "almost no" and "almost every"
- **Monotone increasing property** -- Thresholds are defined for monotone properties

# Key Properties

1. A monotone increasing property has $\mathbb{P}_p(Q)$ increasing in $p$
2. Thresholds describe sharp transitions: below the ltf, the property is absent; above the utf, it holds a.s.
3. For many properties, the ltf and utf are of the same order
4. Sometimes the ltf and utf coincide up to additive terms (e.g., connectivity)

# Construction / Recognition

## To Find a Threshold Function
1. Identify the monotone property $Q$
2. Find $p^*$ such that $\mathbb{E}(\text{obstructions}) \to \infty$ for $p \ll p^*$ (ltf)
3. Show $\mathbb{P}(Q) \to 1$ for $p \gg p^*$ (utf), typically via variance method

# Context & Application

Thresholds capture the Erdos-Renyi discovery that "all the standard properties of graphs arise rather suddenly" (p. 221). The concept is fundamental to understanding the evolution of random graphs.

# Examples

**Example 1** (p. 241): For balanced $F = G(k, \ell)$, the threshold is $n^{-k/\ell}$.

**Example 2** (p. 242): For connectivity, $p_\ell = (\log n - \omega(n))/n$ and $p_u = (\log n + \omega(n))/n$.

# Relationships

## Builds Upon
- **Almost every graph** -- Defines the limiting behavior
- **Monotone increasing property** -- Thresholds apply to these

## Enables
- **Connectivity threshold** -- Specific threshold for connectivity
- **Phase transition** -- The transition region around the threshold

## Related
- **Balanced graph** -- Clean thresholds for balanced subgraph containment
- **Hitting time** -- Related concept in graph processes

## Contrasts With
- None

# Common Errors

- **Error**: Thinking the threshold is a single value of $p$ where the property "switches on"
  **Correction**: The threshold is a function (or function class); there is typically a transition window

# Common Confusions

- **Confusion**: Confusing threshold function with hitting time
  **Clarification**: Threshold function characterizes $p$ in $\mathcal{G}(n, p)$; hitting time is a random variable in a graph process

# Source Reference

Chapter VII: Random Graphs, Section VII.3, page 241.

# Verification Notes

- Definition source: Direct from p. 241
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
