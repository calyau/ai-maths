---
concept: "Pósa's Lemma"
slug: posas-lemma
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
  - "Theorem 17"
prerequisites:
  - simple-transform
extends: []
related:
  - hamiltonian-graph
contrasts_with: []
answers_questions:
  - "How do transforms help find Hamilton cycles?"
---

# Quick Definition
If $L$ is the set of endpoints of transforms of a longest path and $R$ are the remaining vertices, there are no edges between $L$ and $R$.

# Core Definition
**Theorem 17** (Pósa's lemma): Let $S$ be a longest $x_0$-path in $G$. Let $L$ be the set of endpoints (other than $x_0$) of transforms of $S$, $N$ the neighbours of $L$ on $S$, and $R = V \setminus (N \cup L)$. Then $G$ has no $L$-$R$ edges (Bollobás, p. 132).

# Prerequisites
- **Simple transform** — The mechanism for generating new endpoints

# Key Properties
1. No edges between transform-endpoints $L$ and remainder $R$
2. $|L| + |N| + |R| = |V|$
3. Used in proving Hamilton cycle existence in random graphs

# Construction / Recognition
1. Start with longest $x_0$-path $S$
2. Compute all transforms to get endpoint set $L$
3. Compute neighbours $N$ of $L$ on $S$
4. Remainder $R$ has no edges to $L$

# Context & Application
Pósa's lemma is used in Chapter VII to prove Hamilton cycles exist in random graphs $G(n,p)$.

# Examples
**Example** (p. 132): The proof shows that if $x_i \in L$ has a neighbour $x_j \in R$ on $S_i$ (a transform ending at $x_i$), then $x_j$ would be in $N$, not $R$.

# Relationships
## Builds Upon
- **simple-transform** — Foundation for transforms

## Enables
- Hamilton cycle results for random graphs (Chapter VII)

# Source Reference
Chapter IV, Section IV.3, page 132. Theorem 17.

# Verification Notes
- Definition source: Direct from p. 132
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
