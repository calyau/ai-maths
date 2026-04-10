---
concept: Acyclic Maximal Flow
slug: acyclic-maximal-flow
category: network-flows
subcategory: flow-properties
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
  - "acyclic flow"
prerequisites:
  - max-flow-min-cut-theorem
  - integrality-theorem
extends: []
related:
  - ford-fulkerson-algorithm
contrasts_with: []
answers_questions:
  - "Can a maximum flow avoid circular flow?"
---

# Quick Definition
A maximal acyclic flow exists: one that does not send positive flow around any directed cycle.

# Core Definition
There is a maximal acyclic flow, that is, one that does not contain a flow around a cycle. For no cycle $x_1x_2\cdots x_k$ do we have $f(x_1,x_2) > 0, f(x_2,x_3) > 0, \ldots, f(x_k,x_1) > 0$. The existence follows from the Ford-Fulkerson algorithm (Bollobás, p. 77).

# Prerequisites
- **Max-flow min-cut theorem** — Ensures a maximal flow exists
- **Integrality theorem** — Algorithm produces acyclic flows

# Key Properties
1. Circular flows can be removed without decreasing flow value
2. The augmenting path algorithm naturally produces acyclic flows

# Context & Application
Acyclic flows are more efficient and natural; they avoid "wasted" circular flow.

# Examples
**Example** (p. 77): The Ford-Fulkerson algorithm starting from the zero flow produces acyclic flows, since each augmentation follows a path (not a cycle).

# Relationships
## Builds Upon
- **max-flow-min-cut-theorem** — Existence
- **ford-fulkerson-algorithm** — Construction

# Source Reference
Chapter III, Section III.1, page 77.

# Verification Notes
- Definition source: Direct from p. 77
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
