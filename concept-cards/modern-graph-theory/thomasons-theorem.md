---
concept: "Thomason's Theorem on Hamilton Cycles"
slug: thomasons-theorem
category: extremal-graph-theory
subcategory: hamilton-theory
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.3 Hamilton Paths and Cycles"
extraction_confidence: high
aliases:
  - "Theorem 19"
prerequisites:
  - simple-transform
  - hamiltonian-graph
extends: []
related:
  - posas-lemma
contrasts_with: []
answers_questions:
  - "How many Hamilton cycles contain a given edge?"
---

# Quick Definition
In a graph where every vertex has odd degree, every edge is contained in an even number of Hamilton cycles.

# Core Definition
**Theorem 19** (Thomason): Let $G$ be a graph in which every vertex has odd degree. Then every edge of $G$ is contained in an even number of Hamilton cycles (Bollobás, p. 133).

# Prerequisites
- **Simple transform** — The proof uses transforms
- **Hamiltonian graph** — The property being studied

# Key Properties
1. In a cubic graph, every edge is in an even number of Hamilton cycles
2. For every edge of a Hamilton cycle in a cubic graph, there is another Hamilton cycle containing it
3. Proof uses Theorem 18: longest paths ending in even-degree vertices come in pairs

# Context & Application
"The most striking case... is that in a cubic graph every edge is contained in an even number of Hamilton cycles" (p. 133).

# Examples
**Example** (p. 133): For edge $x_0y$ in $G$, consider $G' = G - x_0y$. In $G'$, only $x_0$ and $y$ have even degree, so longest $x_0$-paths ending at $y$ come in pairs.

# Relationships
## Builds Upon
- **simple-transform** — Key proof technique

# Source Reference
Chapter IV, Section IV.3, page 133. Theorem 19.

# Verification Notes
- Definition source: Direct from p. 133
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
