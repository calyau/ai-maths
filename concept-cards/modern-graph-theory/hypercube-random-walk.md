---
concept: Random Walk on the Hypercube
slug: hypercube-random-walk
category: conductance-and-mixing
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 326
section: "IX.4 Conductance and Rapid Mixing"
extraction_confidence: high
aliases: []
prerequisites:
  - conductance-of-graph
  - rapid-mixing
extends: []
related:
  - lazy-random-walk
contrasts_with: []
answers_questions:
  - "How does conductance relate to mixing time of random walks?"
---

# Quick Definition
The $d$-dimensional hypercube $Q^d$ has conductance $\Phi_{Q^d} = 1/d = 1/\log n$ where $n = 2^d$. Lazy random walks on $(Q^d)_{d=1}^\infty$ are rapidly mixing.

# Core Definition
$Q^d = \{0,1\}^d$ is $d$-regular with $n = 2^d$ vertices. "It is rather easy to prove that $\Phi_{Q^d} = 1/d$" (Bollobás, p. 326). The worst bottleneck is $U = \{x : x_1 = 1\}$, $\bar{U} = \{x : x_1 = 0\}$, with $e(U, \bar{U}) = 2^{d-1}$, giving $\Phi = 1/d$.

# Prerequisites
- **Conductance of a graph** — $\Phi_{Q^d} = 1/d$
- **Rapid mixing** — Follows from $\Phi \geq (\log n)^{-1}$

# Key Properties
1. $\Phi_{Q^d} = 1/d = 1/\log_2 n$
2. LRW mixing rate: $1 - 1/d$ (from eigenvalue $\lambda_2 = 1 - 2/d$)
3. LRW is rapidly mixing since $\Phi_{Q^d} = (\log n)^{-1}$
4. $Q^d = K_2^d$ (product of $d$ copies of $K_2$)

# Examples
**Example** (p. 326): $\Phi_{Q^d} = 1/d$ achieved by the cut $\{x : x_1 = 0\}$ vs $\{x : x_1 = 1\}$.

# Relationships
## Builds Upon
- **conductance-of-graph**, **rapid-mixing**

## Related
- **lazy-random-walk** — Applied to $Q^d$

# Source Reference
Chapter IX, Section IX.4, page 326. Exercise 48.

# Verification Notes
- Definition source: Direct from p. 326
- Confidence rationale: Explicit computation
- Uncertainties: None
- Cross-reference status: Verified
