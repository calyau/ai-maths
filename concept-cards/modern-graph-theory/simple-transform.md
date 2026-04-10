---
concept: Simple Transform
slug: simple-transform
category: extremal-graph-theory
subcategory: hamilton-theory
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.3 Hamilton Paths and Cycles"
extraction_confidence: high
aliases:
  - "path rotation"
  - "transform"
prerequisites:
  - hamiltonian-graph
extends: []
related:
  - posas-lemma
contrasts_with: []
answers_questions:
  - "What is a simple transform of a path?"
---

# Quick Definition
A simple transform of a longest path $S = x_0x_1\cdots x_k$ is obtained by erasing the edge $x_jx_{j+1}$ and adding $x_kx_j$ (where $x_k$ is adjacent to $x_j$), giving another longest path with the same start but a different end.

# Core Definition
Let $S = x_0x_1\cdots x_k$ be a longest $x_0$-path. If $x_k$ is adjacent to $x_j$ ($0 \le j < k-1$), then $S' = x_0x_1\cdots x_j x_k x_{k-1}\cdots x_{j+1}$ is a simple transform of $S$. The vertex $x_k$ has exactly $d(x_k)-1$ simple transforms. A transform is the result of a sequence of simple transforms (Bollobás, p. 131).

# Prerequisites
- **Hamiltonian graph** — Transforms are used to study Hamilton cycles

# Key Properties
1. $S'$ is also a longest $x_0$-path
2. $S$ is a simple transform of $S'$ (the operation is symmetric)
3. The endpoint changes from $x_k$ to $x_{j+1}$
4. Used in Pósa's lemma and Thomason's theorem

# Construction / Recognition
1. Take longest path $S = x_0\cdots x_k$
2. Find $j$ with $x_kx_j \in E(G)$ and $j < k-1$
3. Reverse the segment $x_{j+1}\cdots x_k$ and reconnect via $x_kx_j$

# Context & Application
Simple transforms are the key technique for proving Pósa's lemma and related results about Hamilton cycles in random graphs (Chapter VII).

# Examples
**Example** (p. 131, Fig. IV.4): An $x$-path and its simple transform are illustrated.

# Relationships
## Enables
- **posas-lemma** — Uses simple transforms

# Source Reference
Chapter IV, Section IV.3, page 131. Fig. IV.4.

# Verification Notes
- Definition source: Direct from p. 131
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
