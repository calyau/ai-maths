---
concept: Parity of Longest Paths Ending in Even-Degree Vertices
slug: longest-paths-even-degree-parity
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
  - "Theorem 18 (Ch IV)"
  - "Thomason-Smith theorem"
prerequisites:
  - simple-transform
extends: []
related:
  - thomasons-theorem
  - posas-lemma
contrasts_with: []
answers_questions:
  - "How many longest paths end at even-degree vertices?"
---

# Quick Definition
There is an even number of longest $x_0$-paths ending in even-degree vertices.

# Core Definition
**Theorem 18** (Ch IV): Let $W$ be the set of vertices of even degree in $G$ and let $x_0 \in V(G)$. Then there is an even number of longest $x_0$-paths ending in $W$ (Bollobás, p. 132).

# Prerequisites
- **Simple transform** — The proof uses the transform graph

# Key Properties
1. The transform graph $H$ has longest paths as vertices, simple transforms as edges
2. A path $P = x_0x_1\cdots x_k$ has degree $d(x_k) - 1$ in $H$
3. Paths ending in $W$ have odd degree in $H$; by handshaking, there are evenly many

# Context & Application
This parity result is the key to Thomason's theorem (Theorem 19) about Hamilton cycles in odd-degree graphs.

# Examples
**Example** (p. 132): If every vertex has odd degree, the even-degree set $W$ is empty, and the theorem says there are an even (possibly zero) number of longest paths ending at any specified vertex.

# Relationships
## Builds Upon
- **simple-transform** — Defines the transform graph

## Enables
- **thomasons-theorem** — Direct application

# Source Reference
Chapter IV, Section IV.3, page 132. Theorem 18.

# Verification Notes
- Definition source: Direct from p. 132
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
