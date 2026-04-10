---
concept: General Graph Zarankiewicz Bound
slug: general-zarankiewicz-bound
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
  - "Theorem 11"
  - "ex(n; K_{s,t})"
prerequisites:
  - kovari-sos-turan-bound
  - duplication-argument
extends:
  - kovari-sos-turan-bound
related:
  - zarankiewicz-problem
contrasts_with: []
answers_questions:
  - "What is ex(n; K_{s,t}) for non-bipartite graphs?"
---

# Quick Definition
$ex(n; K_{s,t}) \le \frac{1}{2}(s-1)^{1/t}n^{2-1/t} + \frac{1}{2}(t-1)n$ for any graph (not just bipartite).

# Core Definition
**Theorem 11**: If $G$ has order $n$ and no $K_{s,t}$, then $n\binom{y}{t} \le (n-r)\binom{k}{t} + r\binom{k+1}{t} \le (s-1)\binom{n}{t}$ and $ex(n; K_{s,t}) \le \frac{1}{2}(s-1)^{1/t}n^{2-1/t} + \frac{1}{2}(t-1)n$ (Bollobás, p. 124).

# Prerequisites
- **Kővári-Sós-Turán bound** — Same technique applied to $D(G)$
- **Duplication argument** — Reduces to bipartite case

# Key Properties
1. Same proof as the bipartite case, applied to the bipartite double $D(G)$
2. Gives $ex(n; C_4) \le n(1+\sqrt{4n-3})/4$

# Context & Application
Extends bipartite density bounds to general graphs, halving the bipartite bound.

# Examples
**Example** (p. 124): $ex(n; C_4) \le n(1+\sqrt{4n-3})/4$ is essentially best possible.

# Relationships
## Builds Upon
- **kovari-sos-turan-bound** — Via duplication
- **duplication-argument** — The reduction

# Source Reference
Chapter IV, Section IV.2, page 124. Theorem 11.

# Verification Notes
- Definition source: Direct from p. 124
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
