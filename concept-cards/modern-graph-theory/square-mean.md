---
concept: Square Mean of a Partition
slug: square-mean
category: regularity-method
subcategory: proof-technique
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.5 Szemerédi's Regularity Lemma"
extraction_confidence: high
aliases:
  - "q(P)"
  - "energy"
prerequisites:
  - equitable-partition
  - epsilon-uniform-pair
extends: []
related:
  - szemeredis-regularity-lemma
contrasts_with: []
answers_questions:
  - "What is the square mean used in the regularity lemma proof?"
---

# Quick Definition
The square mean $q(\mathcal{P})$ of an equitable partition is $\frac{1}{k^2}\sum_{1 \le i < j \le k} d^2(C_i, C_j)$, always in $[0, 1/2)$.

# Core Definition
Given an equitable partition $\mathcal{P} = (C_i)_{i=0}^k$ with exceptional class $C_0$, the square mean is $q(\mathcal{P}) = \frac{1}{k^2}\sum_{1 \le i < j \le k} d^2(C_i, C_j)$. Since $d^2(C_i,C_j) \le 1$ and the sum has $\binom{k}{2}$ terms, $0 \le q(\mathcal{P}) < 1/2$ (Bollobás, p. 141).

# Prerequisites
- **Equitable partition** — The partition being measured
- **ε-uniform pair** — Non-uniform pairs increase $q$

# Key Properties
1. $0 \le q(\mathcal{P}) < 1/2$
2. If $\mathcal{P}$ is not $\varepsilon$-uniform, there exists $\mathcal{P}'$ with $q(\mathcal{P}') \ge q(\mathcal{P}) + \varepsilon^5/2$ (Lemma 28)
3. The bounded range of $q$ ensures termination: at most $\lfloor\varepsilon^{-5}\rfloor$ refinements needed
4. Acts as a "potential function" for the iterative proof

# Construction / Recognition
1. Compute $d(C_i, C_j)$ for each pair
2. Sum the squares, divide by $k^2$

# Context & Application
The square mean is the key technical tool in the proof of Szemerédi's regularity lemma. It provides the monotone quantity that guarantees convergence.

# Examples
**Example** (p. 143): If $\mathcal{P}$ is not $\varepsilon$-uniform, Lemma 28 constructs $\mathcal{P}'$ with $q(\mathcal{P}') \ge q(\mathcal{P}) + \varepsilon^5/2$. Since $q < 1/2$, this can happen at most $\lfloor 1/(2 \cdot \varepsilon^5/2)\rfloor = \lfloor\varepsilon^{-5}\rfloor$ times.

# Relationships
## Enables
- **szemeredis-regularity-lemma** — The proof mechanism

## Related
- **equitable-partition** — The partition being measured

# Source Reference
Chapter IV, Section IV.5, pages 141-145.

# Verification Notes
- Definition source: Direct from p. 141
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
