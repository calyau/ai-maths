---
concept: "Erdős's Girth-Chromatic Number Theorem"
slug: erdos-girth-chromatic-theorem
category: random-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Random Graphs"
chapter_number: 11
pdf_page: 311
section: "11.2 The probabilistic method"
extraction_confidence: high
aliases:
  - "Erdős 1959 theorem"
prerequisites:
  - probabilistic-method
  - markovs-inequality
  - expected-value
extends: []
related:
  - random-graph-gnp
contrasts_with: []
answers_questions:
  - "Can a graph have both large girth and large chromatic number?"
---

# Quick Definition
Erdős's theorem (1959) states that for every integer k, there exists a graph H with girth g(H) > k and chromatic number chi(H) > k. The proof uses the probabilistic method with edge probability p = n^{epsilon-1}.

# Core Definition
**Theorem 11.2.2** (Erdős 1959): For every integer k there exists a graph H with girth g(H) > k and chromatic number chi(H) > k (Diestel, p. 311).

# Prerequisites
- **Probabilistic method** — The proof technique
- **Markov's inequality** — Used to bound the number of short cycles
- **Expected value** — Used to compute expected short cycles

# Key Properties
1. The proof uses p = n^{epsilon-1} with 0 < epsilon < 1/k
2. This p makes short cycles rare (expected number < n/2)
3. The same p ensures no big independent sets (by Lemma 11.2.1)
4. Delete one vertex from each short cycle to get the desired graph H
5. The resulting H has |H| >= n/2, g(H) > k, and chi(H) > k

# Context & Application
This theorem is one of the earliest and most celebrated applications of the probabilistic method. It shows that high chromatic number does not require short cycles, a deeply counterintuitive result.

# Examples
**Example 1** (pp. 311-312): The proof in full detail, choosing epsilon, computing expectations, and applying deletion.

# Relationships
## Builds Upon
- **Probabilistic method** — The proof technique

## Related
- Corollary 11.2.3: arbitrarily large girth with large connectivity, edge-density, or minimum degree

# Source Reference
Chapter 11, Section 11.2, pages 311-312 (Theorem 11.2.2).

# Verification Notes
- Statement and proof from pp. 311-312
- Confidence: HIGH — named theorem with complete proof
