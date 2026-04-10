---
concept: "Tutte's 1-Factor Theorem"
slug: tuttes-1-factor-theorem
category: matchings
subcategory: fundamental-theorems
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.4 Tutte's 1-Factor Theorem"
extraction_confidence: high
aliases:
  - "Theorem 14"
  - "Tutte's theorem"
  - "Tutte 1947"
prerequisites:
  - one-factor
  - odd-component
  - halls-theorem
extends: []
related:
  - berges-formula
  - deficiency-version-tuttes-theorem
contrasts_with: []
answers_questions:
  - "What is a perfect matching?"
  - "When does a graph have a perfect matching?"
---

# Quick Definition
A graph $G$ has a 1-factor (perfect matching) if and only if $q(G-S) \le |S|$ for every $S \subset V(G)$, where $q$ counts odd components.

# Core Definition
**Theorem 14** (Tutte, 1947): A graph $G$ has a 1-factor iff $q(G-S) \le |S|$ for every $S \subset V(G)$ (condition (1)). The necessity is straightforward: in a 1-factor, each odd component must have at least one edge to $S$, and these edges are independent. The sufficiency is "surprising and deep" (Bollobás, pp. 90-92).

# Prerequisites
- **1-Factor** — The object whose existence is characterized
- **Odd component** — The function $q$ counts odd components
- **Hall's theorem** — Used in the proof (step (iii))

# Key Properties
1. The condition $q(G-S) \le |S|$ must hold for all $S$, including $S = \emptyset$ (which implies $G$ has even order)
2. The proof uses a maximal set $S_0$ achieving equality in (1)
3. Each even component $D_j$ of $G - S_0$ has a 1-factor
4. For each odd component $C_i$, removing any vertex yields a graph with a 1-factor
5. Hall's theorem provides the matching from $S_0$ to odd components

# Construction / Recognition
1. Check $q(G - S) \le |S|$ for all $S \subset V(G)$
2. If this holds, a 1-factor exists
3. The proof is constructive: find maximal $S_0$ with equality, then decompose

# Context & Application
Tutte's theorem extends Hall's theorem from bipartite to general graphs. It is "considerably harder" than the bipartite case (p. 74). It implies that every 2-edge-connected cubic graph has a 1-factor (Exercise 32).

# Examples
**Example** (p. 90, Fig. III.6): A graph $G$ with a 1-factor where $|S| = 4$ and $G - S$ has 2 odd components.

**Example** (p. 91, Fig. III.7): The bipartite graph $H$ used to match $S_0$ to odd components via Hall's theorem.

# Relationships
## Builds Upon
- **one-factor** — The object characterized
- **odd-component** — The obstruction measure
- **halls-theorem** — Used in step (iii) of the proof

## Enables
- **deficiency-version-tuttes-theorem** — Corollary 15

# Common Errors
- **Error**: Checking condition (1) only for $S = \emptyset$
  **Correction**: The condition must hold for every subset $S$, not just the empty set

# Common Confusions
- **Confusion**: Thinking the condition is the same as Hall's condition
  **Clarification**: Tutte's condition counts odd components; Hall's counts neighbourhood sizes in bipartite graphs

# Source Reference
Chapter III, Section III.4, pages 90-93. Theorem 14 with proof.

# Verification Notes
- Definition source: Direct theorem statement from p. 90
- Confidence rationale: Major theorem with complete proof
- Uncertainties: None
- Cross-reference status: Verified
