---
# === CORE IDENTIFICATION ===
concept: Random Graph
slug: random-graph

# === CLASSIFICATION ===
category: random-graphs
subcategory: basic-definitions
tier: foundational

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 221
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - stochastic graph

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - gnp-model
  - gnm-model
  - graph-process
  - probabilistic-method
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a random graph?"
  - "Why are random graphs important in graph theory?"
---

# Quick Definition

A random graph is a graph drawn from a probability space whose elements are graphs on a fixed vertex set. The theory studies what properties typical graphs possess as the number of vertices tends to infinity.

# Core Definition

A random graph arises from any probability space whose points are graphs. Bollobás identifies three principal models: $\mathcal{G}(n, M)$ (uniform random graph with $M$ edges), $\mathcal{G}(n, p)$ (binomial random graph with edge probability $p$), and $\widetilde{\mathcal{G}}^n$ (the graph process). In each model, the vertex set is $V = [n] = \{1, 2, \ldots, n\}$, and the study concerns asymptotic behavior as $n \to \infty$ (Bollobás, pp. 221--223).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Every graph invariant becomes a random variable on a space of random graphs
2. The theory addresses "what do most graphs look like" rather than extremal values
3. Properties of random graphs tend to arise suddenly (phase transitions)
4. Random graphs serve dual purposes: as objects of study and as tools for existence proofs

# Construction / Recognition

## To Study Random Graphs
1. Fix a probability space of graphs (e.g., $\mathcal{G}(n, p)$)
2. Express the graph property of interest as a random variable or event
3. Use probabilistic tools (expectation, variance, concentration) to analyze behavior as $n \to \infty$

# Context & Application

The systematic study of random graphs was initiated by Erdos and Renyi in 1959. Random graph theory serves two purposes: (1) understanding what typical graphs look like, and (2) using probabilistic arguments to prove existence of graphs with specific properties without explicit construction. Applications extend to computer science, network theory, and combinatorial optimization.

# Examples

**Example 1** (p. 221): Erdos used random graphs to give an exponential lower bound for the Ramsey number $R(s, s)$, demonstrating graphs where neither the graph nor its complement contains $K_s$.

**Example 2** (p. 221): Erdos showed that for all natural numbers $k$ and $g$ there exist $k$-chromatic graphs of girth at least $g$, using probabilistic methods.

# Relationships

## Builds Upon
- No prerequisites -- this is the foundational concept of the chapter

## Enables
- **G(n,p) model** -- The primary probability space for random graphs
- **G(n,M) model** -- The uniform probability space for random graphs
- **Phase transition** -- The central phenomenon in random graph evolution

## Related
- **Probabilistic method** -- The technique of proving existence via random graphs
- **Graph process** -- The dynamic model of random graph evolution

## Contrasts With
- None

# Common Errors

- **Error**: Assuming random graph results give information about specific graphs
  **Correction**: Random graph theorems describe typical behavior; specific graphs may violate any "almost sure" property

# Common Confusions

- **Confusion**: Thinking random graphs are always $\mathcal{G}(n, 1/2)$
  **Clarification**: There are many random graph models; the parameter $p$ or $M$ typically depends on $n$

# Source Reference

Chapter VII: Random Graphs, introductory section, pages 221--223.

# Verification Notes

- Definition source: Synthesized from introductory discussion pp. 221--223
- Confidence rationale: Concept is extensively discussed with clear characterization
- Uncertainties: None
- Cross-reference status: Verified against planned extractions
