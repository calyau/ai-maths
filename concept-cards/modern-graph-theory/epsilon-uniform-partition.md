---
concept: "ε-Uniform Partition"
slug: epsilon-uniform-partition
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
  - "epsilon-regular partition"
  - "Szemerédi partition"
prerequisites:
  - equitable-partition
  - epsilon-uniform-pair
extends:
  - equitable-partition
related:
  - szemeredis-regularity-lemma
  - square-mean
contrasts_with: []
answers_questions:
  - "What is an epsilon-regular partition?"
  - "What must I know before understanding Szemerédi's regularity lemma?"
---

# Quick Definition
An $\varepsilon$-uniform partition is an equitable partition $(C_i)_{i=0}^k$ where $|C_0| \le \varepsilon n$ and all but at most $\varepsilon k^2$ of the pairs $(C_i, C_j)$ are $\varepsilon$-uniform.

# Core Definition
An $\varepsilon$-uniform partition is an equitable partition $(C_i)_{i=0}^k$ such that the exceptional class $C_0$ has at most $\varepsilon n$ vertices and, with the exception of at most $\varepsilon k^2$ pairs, the pairs $(C_i, C_j)$, $1 \le i < j \le k$, are $\varepsilon$-uniform (Bollobás, p. 139).

# Prerequisites
- **Equitable partition** — An $\varepsilon$-uniform partition is equitable
- **ε-uniform pair** — Most pairs must be uniform

# Key Properties
1. At most $\varepsilon k^2$ pairs are non-uniform (a small fraction of $\binom{k}{2}$)
2. The exceptional class is small: $|C_0| \le \varepsilon n$
3. All non-exceptional classes have equal size
4. Szemerédi's lemma guarantees existence with bounded $k$

# Construction / Recognition
1. Partition $V$ into $k$ equal classes plus exceptional class $C_0$
2. Check $|C_0| \le \varepsilon n$
3. Count non-$\varepsilon$-uniform pairs; must be $\le \varepsilon k^2$

# Context & Application
The $\varepsilon$-uniform partition is the output of Szemerédi's regularity lemma and the starting point for regularity-based arguments.

# Examples
**Example** (p. 139): The trivial partition into singletons is 0-uniform, but has $n$ classes. The regularity lemma bounds $k$.

# Relationships
## Builds Upon
- **equitable-partition** — Must be equitable
- **epsilon-uniform-pair** — Most pairs must satisfy this

## Enables
- **szemeredis-regularity-lemma** — Existence theorem

# Source Reference
Chapter IV, Section IV.5, page 139.

# Verification Notes
- Definition source: Direct from p. 139
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
