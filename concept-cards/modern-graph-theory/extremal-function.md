---
concept: Extremal Function
slug: extremal-function
category: extremal-graph-theory
subcategory: basic-definitions
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV Extremal Problems"
extraction_confidence: high
aliases:
  - "ex(n; F)"
  - "extremal number"
prerequisites:
  - extremal-graph
extends: []
related:
  - forbidden-subgraph-problem
  - turan-graph
contrasts_with: []
answers_questions:
  - "What is the extremal function ex(n; F)?"
---

# Quick Definition
The extremal function $ex(n; F)$ is the maximum number of edges in a graph of order $n$ that does not contain $F$ as a subgraph.

# Core Definition
Given a graph $F$, the extremal function $ex(n; F)$ is the maximal number of edges in a graph of order $n$ not containing $F$. Equivalently, $ex(n; F) + 1$ edges guarantee that a graph of order $n$ contains $F$ (Bollobás, p. 110).

# Prerequisites
- **Extremal graph** — $EX(n;F)$ is the set of graphs achieving $ex(n;F)$

# Key Properties
1. $ex(n; K_3) = \lfloor n^2/4 \rfloor$ (Mantel's theorem)
2. $ex(n; K_{r+1}) = t_r(n)$ (Turán's theorem)
3. For non-bipartite $F$ with $\chi(F) = r+1$: $ex(n;F) = (1-1/r)\binom{n}{2} + o(n^2)$ (Erdős-Stone)
4. For bipartite $F$: $ex(n;F) = o(n^2)$

# Construction / Recognition
1. Identify the forbidden graph $F$
2. Determine the maximum number of edges possible while avoiding $F$
3. This maximum is $ex(n;F)$

# Context & Application
The extremal function is "the quintessential extremal problem" (p. 110). Determining $ex(n;F)$ and $EX(n;F)$ for various $F$ is the central theme of the chapter.

# Examples
**Example** (p. 110): $ex(n; K_3) = \lfloor n^2/4 \rfloor$ by Mantel's theorem; $EX(n; K_3) = \{K_{\lfloor n/2 \rfloor, \lceil n/2 \rceil}\}$.

# Relationships
## Builds Upon
- **extremal-graph** — The graphs achieving the extremal function

## Enables
- **turans-theorem** — Determines $ex(n; K_{r+1})$
- **erdos-stone-theorem** — Determines $ex(n; F)$ asymptotically

# Source Reference
Chapter IV, introductory section, page 110.

# Verification Notes
- Definition source: Direct from p. 110
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
