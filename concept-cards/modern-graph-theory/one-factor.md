---
concept: 1-Factor
slug: one-factor
category: matchings
subcategory: basic-definitions
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.4 Tutte's 1-Factor Theorem"
extraction_confidence: high
aliases:
  - "perfect matching"
  - "1-factor"
prerequisites:
  - matching
extends:
  - matching
related:
  - factor-of-graph
  - tuttes-1-factor-theorem
contrasts_with:
  - complete-matching
answers_questions:
  - "What is a perfect matching?"
  - "What distinguishes a matching from a perfect matching?"
---

# Quick Definition
A 1-factor of a graph $G$ is a spanning subgraph (a factor) in which every vertex has degree 1 — equivalently, a perfect matching covering all vertices of $G$.

# Core Definition
A factor of a graph is a spanning subgraph: a subgraph whose vertex set is that of the whole graph. If every vertex of a factor has degree $r$, then we call it an $r$-factor. A 1-factor is a factor in which every vertex has degree 1 (Bollobás, p. 90).

# Prerequisites
- **Matching** — A 1-factor is a matching that covers every vertex

# Key Properties
1. A 1-factor exists only if $|V(G)|$ is even
2. Every vertex is incident with exactly one edge of the 1-factor
3. The edges form a perfect matching
4. Existence characterized by Tutte's theorem: $q(G-S) \le |S|$ for all $S$

# Construction / Recognition
1. Find a matching $M$ of size $|V|/2$
2. If it covers every vertex, it is a 1-factor

# Context & Application
The existence of 1-factors is characterized by Tutte's theorem (Theorem 14), one of the deepest results in matching theory. Every 2-edge-connected cubic graph has a 1-factor.

# Examples
**Example** (p. 90, Fig. III.6): A graph $G$ with a 1-factor is shown. The set $S$ has 4 vertices and $G - S$ has 2 odd components, satisfying $q(G-S) \le |S|$.

# Relationships
## Builds Upon
- **matching** — A 1-factor is a special matching

## Enables
- **tuttes-1-factor-theorem** — Characterizes existence of 1-factors

## Contrasts With
- **complete-matching** — A complete matching covers one class; a 1-factor covers all vertices

# Common Errors
- **Error**: Looking for a 1-factor in a graph with odd order
  **Correction**: A 1-factor requires even order

# Common Confusions
- **Confusion**: Confusing 1-factor with maximum matching
  **Clarification**: A maximum matching need not cover all vertices; a 1-factor must

# Source Reference
Chapter III, Section III.4, page 90.

# Verification Notes
- Definition source: Direct from p. 90
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
