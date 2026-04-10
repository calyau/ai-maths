---
concept: Projective Plane as Extremal Graph
slug: projective-plane-extremal-graph
category: extremal-graph-theory
subcategory: constructions
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.2 Complete Subgraphs"
extraction_confidence: high
aliases:
  - "Theorem 12"
  - "Reiman 1958"
prerequisites:
  - zarankiewicz-problem
  - kovari-sos-turan-bound
extends: []
related:
  - moore-graph
contrasts_with: []
answers_questions:
  - "When is the Zarankiewicz bound achieved?"
---

# Quick Definition
For $n = q^2 + q + 1$ (prime power $q$), the incidence graph of the projective plane $PG(2,q)$ achieves $z(n,n;2,2) = \frac{n}{2}(1+\sqrt{4n-3})$, showing the bound is tight.

# Core Definition
**Theorem 12** (Reiman, 1958): $z(n,n;2,2) \le \frac{n}{2}(1+(4n-3)^{1/2})$, with equality for infinitely many $n$. The extremal graphs are the incidence graphs of projective planes: each has $n$ points, $n$ lines, $d = q+1$ points per line, exactly one line through any two points, and any two lines meet in one point (Bollobás, pp. 124-125).

# Prerequisites
- **Zarankiewicz problem** — The problem being solved
- **Kővári-Sós-Turán bound** — The upper bound achieved

# Key Properties
1. Equality holds for $n = q^2 + q + 1$ where $q$ is a prime power
2. The extremal graph is the incidence graph of $PG(2,q)$
3. For $q = 2$: the Heawood graph
4. $ex(n; C_4) \le n(1+\sqrt{4n-3})/4$

# Context & Application
Shows deep connections between extremal graph theory and finite geometry. Projective planes provide the densest $C_4$-free bipartite graphs.

# Examples
**Example** (p. 125): $V_1$ = points of $PG(2,q)$, $V_2$ = lines. Join $P$ to $\ell$ iff $P \in \ell$. For $q = 2$: the Heawood graph.

# Relationships
## Builds Upon
- **zarankiewicz-problem** — Solves it for $s = t = 2$
- **kovari-sos-turan-bound** — Achieves equality

## Related
- **moore-graph** — Heawood graph is both

# Source Reference
Chapter IV, Section IV.2, pages 124-126. Theorem 12.

# Verification Notes
- Definition source: Direct from pp. 124-125
- Confidence rationale: Explicitly stated with construction
- Uncertainties: None
- Cross-reference status: Verified
