---
concept: Nowhere-Zero Flow
slug: nowhere-zero-flow
category: tutte-polynomial
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 354
section: "X.4 Special Values of the Tutte Polynomial"
extraction_confidence: high
aliases:
  - "nowhere-zero A-flow"
  - "k-flow"
prerequisites:
  - tutte-polynomial
extends: []
related:
  - flow-polynomial
  - five-flow-conjecture
contrasts_with: []
answers_questions:
  - "How does the Tutte polynomial generalize the chromatic and flow polynomials?"
---

# Quick Definition
A nowhere-zero $A$-flow on a multigraph $G$ is a function $f: \vec{E} \to A$ (where $A$ is a finite Abelian group) satisfying Kirchhoff's current law at each vertex, with $f(e) \neq 0$ for every edge.

# Core Definition
An $A$-flow is a map $f: \vec{E} \to A$ such that the total flow out of each vertex equals the total flow in. "An $A$-flow is said to be nowhere-zero if it has a non-zero value in every edge" (Bollobás, p. 354). The number of nowhere-zero $A$-flows depends only on $|A|$, not on the group structure.

# Prerequisites
- **Tutte polynomial** — Nowhere-zero flows are counted by the flow polynomial, a specialization of $T_G$

# Key Properties
1. Satisfies KCL at every vertex
2. Non-zero value on every edge
3. Number depends only on $|A|$ (Theorem 7)
4. If $G$ has a bridge: no nowhere-zero flows exist
5. A $k$-flow means an $A$-flow with $|A| = k$ (or a $\mathbb{Z}_k$-flow)

# Context & Application
Nowhere-zero flows are dual to proper colourings for planar graphs. The four colour theorem is equivalent to every bridgeless planar graph having a nowhere-zero 4-flow.

# Examples
**Example** (p. 354): On $C_n$: every nowhere-zero $A$-flow assigns the same element to each edge, giving $|A| - 1$ nowhere-zero flows.

# Relationships
## Builds Upon
- **tutte-polynomial**

## Enables
- **flow-polynomial** — Counts nowhere-zero flows
- **five-flow-conjecture**

# Source Reference
Chapter X, Section X.4, pages 354-355.

# Verification Notes
- Definition source: Direct from p. 354
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
