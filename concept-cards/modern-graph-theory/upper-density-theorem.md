---
concept: Upper Density Theorem
slug: upper-density-theorem
category: extremal-graph-theory
subcategory: fundamental-theorems
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.4 The Structure of Graphs"
extraction_confidence: high
aliases:
  - "Corollary 25"
prerequisites:
  - erdos-stone-theorem
  - graph-density
extends:
  - erdos-stone-theorem
related: []
contrasts_with: []
answers_questions:
  - "What values can the upper density of an infinite graph take?"
---

# Quick Definition
The upper density of an infinite graph is one of $0, 1/2, 2/3, 3/4, \ldots, 1$ — no other values are possible.

# Core Definition
**Corollary 25**: The upper density of an infinite graph $G$ is $1, 1/2, 2/3, 3/4, \ldots$, or $0$. Each of these values is the upper density of some infinite graph (Bollobás, p. 138).

# Prerequisites
- **Erdős-Stone theorem** — The key tool
- **Graph density** — Upper density is defined from density

# Key Properties
1. The possible values are $1 - 1/r$ for $r = 1, 2, \ldots$ and $0$
2. Complete $r$-partite graphs with infinite classes achieve $1-1/r$
3. The gaps are dictated by the Erdős-Stone theorem

# Context & Application
A surprising and elegant consequence of Erdős-Stone: the upper density takes only countably many values.

# Examples
**Example** (p. 138): The complete $r$-partite graph $G_r$ with infinite classes has upper density $1 - 1/r$.

# Relationships
## Builds Upon
- **erdos-stone-theorem** — Direct corollary

# Source Reference
Chapter IV, Section IV.4, page 138. Corollary 25.

# Verification Notes
- Definition source: Direct from p. 138
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
