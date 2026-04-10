---
concept: "ε-Uniform Pair"
slug: epsilon-uniform-pair
category: regularity-method
subcategory: definitions
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.5 Szemerédi's Regularity Lemma"
extraction_confidence: high
aliases:
  - "epsilon-regular pair"
  - "ε-regular pair"
  - "uniform pair"
prerequisites:
  - graph-density
extends: []
related:
  - szemeredis-regularity-lemma
  - equitable-partition
contrasts_with: []
answers_questions:
  - "What is an epsilon-regular pair?"
  - "What must I know before understanding Szemerédi's regularity lemma?"
---

# Quick Definition
A pair $(X,Y)$ of disjoint vertex sets is $\varepsilon$-uniform if the edge density $d(X^*,Y^*)$ is within $\varepsilon$ of $d(X,Y)$ for all sufficiently large subsets $X^* \subset X$, $Y^* \subset Y$.

# Core Definition
Given a graph $G = (V,E)$ and disjoint non-empty sets $X, Y \subset V$, write $d(X,Y) = e(X,Y)/(|X||Y|)$ for the edge density. The pair $(X,Y)$ is $\varepsilon$-uniform if $|d(X^*,Y^*) - d(X,Y)| < \varepsilon$ whenever $X^* \subset X$, $Y^* \subset Y$ with $|X^*| \ge \varepsilon|X|$ and $|Y^*| \ge \varepsilon|Y|$ (Bollobás, p. 139).

# Prerequisites
- **Graph density** — $\varepsilon$-uniformity is about edge density consistency

# Key Properties
1. Density is approximately constant across large subsets
2. Small subsets (size $< \varepsilon|X|$ or $\varepsilon|Y|$) are excluded
3. An $\varepsilon$-uniform pair behaves like a random bipartite graph of the same density
4. Not all pairs in a partition need be uniform — up to $\varepsilon k^2$ exceptions are allowed

# Construction / Recognition
1. Compute $d(X,Y)$
2. For all subsets $X^* \subset X$ with $|X^*| \ge \varepsilon|X|$ and $Y^* \subset Y$ with $|Y^*| \ge \varepsilon|Y|$:
3. Check $|d(X^*,Y^*) - d(X,Y)| < \varepsilon$

# Context & Application
$\varepsilon$-uniform pairs are the building blocks of Szemerédi's regularity lemma. They capture the idea that the edge distribution between two vertex sets is "pseudorandom."

# Examples
**Example** (p. 139): A random bipartite graph $G(X,Y,p)$ is $\varepsilon$-uniform with high probability when $|X|$ and $|Y|$ are large.

# Relationships
## Enables
- **szemeredis-regularity-lemma** — Built on $\varepsilon$-uniform pairs
- **epsilon-uniform-partition** — Partition where most pairs are uniform

# Source Reference
Chapter IV, Section IV.5, page 139.

# Verification Notes
- Definition source: Direct from p. 139
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
