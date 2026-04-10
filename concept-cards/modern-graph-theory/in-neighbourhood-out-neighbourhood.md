---
concept: In-Neighbourhood and Out-Neighbourhood
slug: in-neighbourhood-out-neighbourhood
category: network-flows
subcategory: directed-graph-definitions
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.1 Flows in Directed Graphs"
extraction_confidence: high
aliases:
  - "Γ⁺(x)"
  - "Γ⁻(x)"
  - "out-neighbourhood"
  - "in-neighbourhood"
prerequisites: []
extends: []
related:
  - flow-in-directed-graph
contrasts_with: []
answers_questions:
  - "What are in-neighbourhood and out-neighbourhood in a directed graph?"
---

# Quick Definition
The out-neighbourhood $\Gamma^+(x) = \{y : \vec{xy} \in \vec{E}\}$ is the set of vertices reachable by a single directed edge from $x$. The in-neighbourhood $\Gamma^-(x) = \{y : \vec{yx} \in \vec{E}\}$ is the set from which $x$ is directly reachable.

# Core Definition
$\Gamma^+(x) = \{y \in V : \vec{xy} \in \vec{E}\}$ and $\Gamma^-(x) = \{y \in V : \vec{yx} \in \vec{E}\}$ (Bollobás, p. 74).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Used in the definition of Kirchhoff's current law
2. Flow out of $x$: $\sum_{y \in \Gamma^+(x)} f(x,y)$
3. Flow into $x$: $\sum_{z \in \Gamma^-(x)} f(z,x)$

# Context & Application
Fundamental notation for directed graph flows.

# Examples
**Example** (p. 74): Kirchhoff's law: $\sum_{y \in \Gamma^+(x)} f(x,y) = \sum_{z \in \Gamma^-(x)} f(z,x)$ for $x \ne s, t$.

# Relationships
## Enables
- **flow-in-directed-graph** — Uses this notation

# Source Reference
Chapter III, Section III.1, page 74.

# Verification Notes
- Definition source: Direct from p. 74
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
