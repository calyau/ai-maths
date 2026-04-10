---
# === CORE IDENTIFICATION ===
concept: Property Hitting Time
slug: property-hitting-time

# === CLASSIFICATION ===
category: random-graphs
subcategory: graph-process
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 243
section: "VII.3 Almost Determined Variables—The Use of the Variance"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - hitting time of a graph property

# === TYPED RELATIONSHIPS ===
prerequisites:
  - graph-process
  - monotone-increasing-property
extends: []
related:
  - threshold-function
  - connectivity-threshold
  - hamilton-cycle-random-graph
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When does a property first appear in a random graph process?"
---

# Quick Definition

The hitting time $\tau_Q$ of a monotone increasing property $Q$ in a graph process $\widetilde{G} = (G_t)_0^N$ is $\tau_Q = \min\{t : G_t \text{ has } Q\}$, the first time the evolving graph acquires the property.

# Core Definition

Given a monotone increasing property $Q$, the time $\tau$ at which $Q$ appears in a graph process $\widetilde{G} = (G_t)_0^N$ is the hitting time of $Q$: $\tau = \tau_Q = \tau(\widetilde{G}; Q) = \min\{t : G_t \text{ has } Q\}$ (Bollobas, p. 243). Threshold functions in $\mathcal{G}(n, M)$ are characterized by hitting times.

# Prerequisites

- **Graph process** -- The setting for property hitting times
- **Monotone increasing property** -- Ensures the hitting time is well-defined

# Key Properties

1. $\tau_Q$ is a random variable on $\widetilde{\mathcal{G}}^n$
2. Once $Q$ holds, it continues to hold (by monotonicity)
3. $m_\ell$ is an ltf for $Q$ iff $\tau > m_\ell$ for a.e. process
4. Remarkable coincidences: $\tau(\text{conn}) = \tau(\delta \ge 1)$ and $\tau(\text{Ham}) = \tau(\delta \ge 2)$ a.s.

# Construction / Recognition

Not applicable -- this is a random variable on the space of graph processes.

# Context & Application

Property hitting times provide the sharpest possible description of when graph properties emerge. The coincidence $\tau(\text{conn}) = \tau(\delta \ge 1)$ (Theorem 11) means that the very edge removing the last isolated vertex makes the graph connected. Similarly, $\tau(\text{Ham}) = \tau(\delta \ge 2)$ (Theorem 15) means the edge removing the last degree-1 vertex creates a Hamilton cycle.

# Examples

**Example 1** (p. 243): $\tau(\widetilde{G}; \text{conn}) = \tau(\widetilde{G}; \delta \ge 1)$ for a.e. graph process (Theorem 11).

**Example 2** (p. 245): $\tau(\widetilde{G}; \text{Ham}) = \tau(\widetilde{G}; \delta \ge 2)$ for a.e. graph process (Theorem 15).

# Relationships

## Builds Upon
- **Graph process** -- The dynamic framework
- **Monotone increasing property** -- Required for well-definedness

## Enables
- Connectivity and Hamiltonicity results

## Related
- **Threshold function** -- Hitting times determine thresholds in $\mathcal{G}(n, M)$

## Contrasts With
- None

# Common Errors

- **Error**: Confusing property hitting time with random walk hitting time
  **Correction**: Property hitting time is the first edge-addition time at which a graph property holds; random walk hitting time is the first visit to a vertex set

# Common Confusions

- **Confusion**: Thinking $\tau(\text{conn}) = \tau(\delta \ge 1)$ is trivial
  **Clarification**: It is a deep result; the last isolated vertex could be in a small component that is not yet connected to the rest

# Source Reference

Chapter VII: Random Graphs, Section VII.3, pages 243--244.

# Verification Notes

- Definition source: Direct from p. 243
- Confidence rationale: Explicit definition with striking examples
- Uncertainties: None
- Cross-reference status: Verified
