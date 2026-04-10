---
concept: Zarankiewicz Problem
slug: zarankiewicz-problem
category: extremal-graph-theory
subcategory: bipartite-extremal
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.2 Complete Subgraphs"
extraction_confidence: high
aliases:
  - "z(m,n;s,t)"
  - "Zarankiewicz function"
prerequisites:
  - extremal-function
  - turans-theorem
extends: []
related:
  - kovari-sos-turan-bound
contrasts_with: []
answers_questions:
  - "What is the Zarankiewicz problem?"
---

# Quick Definition
The Zarankiewicz problem asks for $z(m,n;s,t)$, the maximum number of edges in an $m \times n$ bipartite graph that does not contain a $K_{s,t}$ subgraph.

# Core Definition
$z(m,n;s,t)$ is the maximal size of a bipartite graph $G_2(m,n)$ if it does not contain a complete bipartite graph with $s$ vertices in the first class and $t$ in the second (Bollobás, p. 121). This is the bipartite analogue of Turán's problem.

# Prerequisites
- **Extremal function** — Zarankiewicz is the bipartite extremal problem
- **Turán's theorem** — The non-bipartite analogue

# Key Properties
1. $z(n,n;s,2) \le \frac{n}{2}(1 + \sqrt{4(s-1)(n-1)+1})$ (inequality (4))
2. $z(n,n;t,t) \le (t-1)^{1/t}n^{2-1/t} + (t-1)n$ (inequality (5))
3. Proved for $t = 2,3$ that the bound gives the correct order
4. Double counting argument is the key proof technique

# Construction / Recognition
1. Take bipartite graph $G_2(m,n)$ without $K_{s,t}$
2. Count $t$-sets covered by vertices: each covered by at most $s-1$ vertices
3. Apply convexity to get the upper bound

# Context & Application
"It is rather hard to find nontrivial lower bounds for $z(m,n;s,t)$" (p. 123). The problem connects to projective planes and finite geometry.

# Examples
**Example** (p. 124): For $n = q^2+q+1$ (prime power $q$), the incidence graph of $PG(2,q)$ achieves equality for $z(n,n;2,2)$.

# Relationships
## Builds Upon
- **extremal-function** — Bipartite version

## Related
- **kovari-sos-turan-bound** — Upper bound technique

# Source Reference
Chapter IV, Section IV.2, pages 121-126.

# Verification Notes
- Definition source: Direct from p. 121
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
