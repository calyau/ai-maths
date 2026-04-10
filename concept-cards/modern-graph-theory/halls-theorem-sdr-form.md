---
concept: "Hall's Theorem (SDR Form)"
slug: halls-theorem-sdr-form
category: matchings
subcategory: fundamental-theorems
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.3 Matching"
extraction_confidence: high
aliases:
  - "Theorem 8"
prerequisites:
  - halls-theorem
  - system-of-distinct-representatives
extends:
  - halls-theorem
related: []
contrasts_with: []
answers_questions:
  - "When does a family of sets have a system of distinct representatives?"
---

# Quick Definition
A family $\mathcal{A} = \{A_1, \ldots, A_m\}$ has a system of distinct representatives iff $|\bigcup_{i \in F} A_i| \ge |F|$ for every $F \subset \{1, \ldots, m\}$.

# Core Definition
**Theorem 8**: A family $\mathcal{A} = \{A_1, A_2, \ldots, A_m\}$ of sets has a set of distinct representatives iff $|\bigcup_{i \in F} A_i| \ge |F|$ for every $F \subset \{1, 2, \ldots, m\}$ (Bollobás, p. 87).

# Prerequisites
- **Hall's theorem** — This is the SDR reformulation
- **System of distinct representatives** — The objects characterized

# Key Properties
1. Equivalent to Hall's theorem (Theorem 7) for bipartite graphs
2. The condition checks that every subfamily covers enough elements

# Context & Application
The set-theoretic formulation of Hall's theorem, useful in combinatorics of set systems.

# Examples
**Example** (p. 87): If $F = \{1, 2, 3\}$ and $|A_1 \cup A_2 \cup A_3| \ge 3$, the condition for this subset holds.

# Relationships
## Builds Upon
- **halls-theorem** — Reformulation

# Source Reference
Chapter III, Section III.3, page 87. Theorem 8.

# Verification Notes
- Definition source: Direct from p. 87
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
