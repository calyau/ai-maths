---
concept: Minimum Degree Subgraph Lemma
slug: minimum-degree-subgraph-lemma
category: extremal-graph-theory
subcategory: technical-lemmas
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.4 The Structure of Graphs"
extraction_confidence: high
aliases:
  - "Lemma 21"
prerequisites:
  - extremal-function
extends: []
related:
  - erdos-stone-theorem
contrasts_with: []
answers_questions:
  - "How do you extract a dense subgraph from a dense graph?"
---

# Quick Definition
Every graph of order $n$ and size at least $(c + \varepsilon)\binom{n}{2}$ contains a subgraph $H$ with $\delta(H) \ge c|H|$ and $|H| \ge \varepsilon^{1/2}n$.

# Core Definition
**Lemma 21**: Let $c, \varepsilon > 0$. If $n > 3/\varepsilon$, then every graph of order $n$ and size at least $(c+\varepsilon)\binom{n}{2}$ contains a subgraph $H$ with $\delta(H) \ge c|H|$ and $|H| \ge \varepsilon^{1/2}n$ (Bollobás, p. 136).

# Prerequisites
- **Extremal function** — Context for dense graph analysis

# Key Properties
1. Converts size condition to minimum degree condition
2. The subgraph is large: $|H| \ge \varepsilon^{1/2}n$
3. Proof: iteratively remove low-degree vertices; at most $cn$ edges removed per step

# Context & Application
This lemma bridges Theorems 20 and 22: it reduces the size condition in the Erdős-Stone theorem to a minimum degree condition.

# Examples
**Example** (p. 136): If deleting low-degree vertices produces $G_\ell$ with $\ell = \lfloor\varepsilon^{1/2}n\rfloor$ vertices, the remaining graph has more than $\binom{\ell}{2}$ edges, a contradiction.

# Relationships
## Enables
- **erdos-stone-theorem** — Theorem 22 uses this lemma

# Source Reference
Chapter IV, Section IV.4, page 136. Lemma 21.

# Verification Notes
- Definition source: Direct from p. 136
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
