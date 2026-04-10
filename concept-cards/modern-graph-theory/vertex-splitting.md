---
concept: Vertex Splitting Technique
slug: vertex-splitting
category: network-flows
subcategory: proof-techniques
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.1 Flows in Directed Graphs"
extraction_confidence: high
aliases:
  - "vertex-to-edge reduction"
prerequisites:
  - vertex-capacity
  - capacity-of-edge
extends: []
related:
  - vertex-capacity-max-flow-min-cut
  - mengers-theorem
contrasts_with: []
answers_questions:
  - "How do you reduce vertex capacities to edge capacities?"
---

# Quick Definition
Replace each vertex $x$ by two copies $x_-$ (incoming) and $x_+$ (outgoing) connected by an edge with capacity $c(x)$. This reduces vertex capacity constraints to edge capacity constraints.

# Core Definition
To handle vertex capacity restrictions, replace each $x \in V - \{s,t\}$ by $x_-$ and $x_+$: send incoming edges to $x_-$, outgoing edges from $x_+$, and add edge $\vec{x_-x_+}$ with capacity $c(x)$. This establishes a 1-to-1 correspondence between flows in the original graph with vertex capacities and flows in the new graph with edge capacities (Bollobás, p. 78, Fig. III.2).

# Prerequisites
- **Vertex capacity** — The constraint being reduced
- **Capacity of an edge** — The target constraint type

# Key Properties
1. Preserves all flow properties
2. Vertex-cuts in original correspond to edge-cuts in split graph
3. The only finite-capacity edges in the split graph are the $\vec{x_-x_+}$ edges
4. Source and sink are not split

# Context & Application
Standard reduction technique used to prove Theorem 4 (vertex max-flow min-cut) and the vertex form of Menger's theorem.

# Examples
**Example** (p. 78-79, Fig. III.2): The transformation from $\vec{G}$ to $\vec{H}$ is illustrated.

# Relationships
## Enables
- **vertex-capacity-max-flow-min-cut** — Proved via splitting
- **mengers-theorem** — Vertex form uses splitting

# Source Reference
Chapter III, Section III.1, pages 78-79. Fig. III.2.

# Verification Notes
- Definition source: Direct from pp. 78-79
- Confidence rationale: Explicitly described with figure
- Uncertainties: None
- Cross-reference status: Verified
