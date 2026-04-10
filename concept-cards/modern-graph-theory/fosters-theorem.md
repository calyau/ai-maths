---
concept: Foster's Theorem
slug: fosters-theorem
category: random-walks
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 318
section: "IX.3 Hitting Times and Commute Times"
extraction_confidence: high
aliases: []
prerequisites:
  - effective-resistance
  - commute-time
  - mean-hitting-time
extends: []
related:
  - stationary-distribution
contrasts_with: []
answers_questions:
  - "How do electrical networks relate to random walks on graphs?"
---

# Quick Definition
Foster's theorem states that for any connected graph of order $n$, the sum of effective resistances over all edges equals $n - 1$: $\sum_{st \in E(G)} R_{\text{eff}}(s,t) = n - 1$.

# Core Definition
Theorem 25 (p. 319): "Let $G$ be a connected graph of order $n$. Then $\sum_{st \in E(G)} R_{\text{eff}}(s,t) = n - 1$."

# Prerequisites
- **Effective resistance** — The quantity being summed
- **Commute time** — Used in the second proof via $C(s,t) = 2m R_{\text{eff}}(s,t)$
- **Mean hitting time** — Used in the first proof

# Key Properties
1. The sum $\sum_{st \in E(G)} R_{\text{eff}}(s,t) = n-1$ depends only on $n$, not on the graph structure
2. For trees: each edge has $R_{\text{eff}} = 1$, and there are $n-1$ edges, giving sum $n-1$
3. If all edges have equal effective resistance $(n-1)/m$, the sum is again $n-1$
4. Generalizes to weighted networks: $\sum_{xy \in E(G)} R_{\text{eff}}(x,y)/r_{xy} = n - 1$

# Construction / Recognition
**First Proof** (Tetali, 1991): Uses $d(s)S_x(s \to t) = d(x)S_s(x \to t)$ (Theorem 24) and Theorem 20.

**Second Proof** (Tetali, 1994): By Theorems 18 and 19: $n-1 = \frac{1}{2m}\sum C(s,t) = \frac{1}{2m}\sum 2m R_{\text{eff}}(s,t) = \sum R_{\text{eff}}(s,t)$.

# Context & Application
"The surprising result that this sum is $n-1$ for every connected graph of order $n$ was proved by Foster in 1949" (p. 318). The two proofs by Tetali (1991, 1994) "illustrate the power of the intricate edifice of relations we have constructed."

# Examples
**Example**: For a tree of order $n$, each edge has effective resistance 1, so the sum is $n-1$.

**Example**: For $K_n$ (where each edge has the same effective resistance by symmetry), $\binom{n}{2} \cdot R_{\text{eff}} = n-1$, giving $R_{\text{eff}} = 2/n$ for each edge.

# Relationships
## Builds Upon
- **effective-resistance**, **commute-time**, **mean-hitting-time**

## Related
- **stationary-distribution** — Used in the proof via Theorem 18

# Common Errors
- **Error**: Summing $R_{\text{eff}}$ over all pairs of vertices rather than over edges.
  **Correction**: Foster's theorem sums over edges $st \in E(G)$, not all vertex pairs.

# Source Reference
Chapter IX, Section IX.3, Theorem 25, pages 318-319.

# Verification Notes
- Definition source: Direct from Theorem 25
- Confidence rationale: Named theorem with two proofs
- Uncertainties: None
- Cross-reference status: Verified
