---
concept: Graph Removal via Regularity
slug: regularity-removal-lemma
category: regularity-method
subcategory: applications
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.6 Simple Applications of Szemerédi's Lemma"
extraction_confidence: high
aliases:
  - "Theorem 33"
  - "graph removal lemma"
prerequisites:
  - szemeredis-regularity-lemma
  - regularity-application-subgraph-finding
extends: []
related:
  - erdos-stone-theorem
contrasts_with: []
answers_questions:
  - "How do I apply Szemerédi's regularity lemma to remove forbidden subgraphs?"
---

# Quick Definition
For any graph $F$ and $\varepsilon > 0$, if $G$ of order $n$ does not contain $F$, then removing fewer than $\varepsilon n^2$ edges yields a graph without $K_r$ (where $r = \chi(F)$).

# Core Definition
**Theorem 33**: For every $\varepsilon > 0$ and graph $F$, there is $n_0$ such that if $G$ of order $n \ge n_0$ does not contain $F$, then $G$ contains a set $E'$ of fewer than $\varepsilon n^2$ edges such that $H = G - E'$ has no $K_r$, where $r = \chi(F)$ (Bollobás, p. 150).

# Prerequisites
- **Szemerédi's regularity lemma** — Provides the partition
- **Regularity application for subgraph finding** — Theorem 30

# Key Properties
1. Extends the Erdős-Stone theorem
2. The skeleton of the $\varepsilon$-uniform partition is $K_r$-free
3. Removing sparse/non-uniform edges costs $< \varepsilon n^2$ edges
4. "Needless to say, as a proof of the Erdős-Stone theorem, this is far too heavy-handed" (p. 151)

# Construction / Recognition
1. Apply Szemerédi's lemma to get $\varepsilon$-uniform partition
2. Keep only edges in uniform, dense bipartite subgraphs
3. The removed edges are few; the remaining graph is $K_r$-free

# Context & Application
This demonstrates the "cleaning" approach: use regularity to approximate the graph, then analyze the simplified structure.

# Examples
**Example** (p. 150): Setting up with $\delta = \varepsilon/2$, take an $(m; \delta^f; d > \delta + \delta^f)$-piece. By Theorem 32, at most $\varepsilon n^2$ edges are removed. By Theorem 30, the skeleton is $K_r$-free.

# Relationships
## Builds Upon
- **szemeredis-regularity-lemma** — The key tool
- **regularity-application-subgraph-finding** — Theorem 30

## Related
- **erdos-stone-theorem** — A consequence

# Source Reference
Chapter IV, Section IV.6, pages 150-151. Theorem 33.

# Verification Notes
- Definition source: Direct theorem statement from p. 150
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
