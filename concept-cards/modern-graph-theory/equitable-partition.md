---
concept: Equitable Partition
slug: equitable-partition
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
  - "balanced partition"
prerequisites: []
extends: []
related:
  - epsilon-uniform-partition
  - szemeredis-regularity-lemma
contrasts_with: []
answers_questions:
  - "What is an equitable partition in the regularity lemma?"
---

# Quick Definition
An equitable partition $\mathcal{P} = (C_i)_{i=0}^k$ has an exceptional class $C_0$ and equal-sized classes $|C_1| = |C_2| = \cdots = |C_k|$.

# Core Definition
A partition $\mathcal{P} = (C_i)_{i=0}^k$ of the vertex set $V$ is an equitable partition with exceptional class $C_0$ if $|C_1| = |C_2| = \cdots = |C_k|$ (Bollobás, p. 139).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. All non-exceptional classes have equal size
2. The exceptional class $C_0$ absorbs remainder vertices
3. In an $\varepsilon$-uniform partition, $|C_0| \le \varepsilon n$

# Context & Application
Equitable partitions are the framework for Szemerédi's regularity lemma. Equal class sizes simplify the analysis.

# Examples
**Example**: Partition $n$ vertices into $k$ classes of size $\lfloor n/k \rfloor$ with exceptional class of size $n - k\lfloor n/k \rfloor < k$.

# Relationships
## Enables
- **epsilon-uniform-partition** — An equitable partition with uniformity conditions

# Source Reference
Chapter IV, Section IV.5, page 139.

# Verification Notes
- Definition source: Direct from p. 139
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
