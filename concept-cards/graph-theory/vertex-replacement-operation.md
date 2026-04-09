---
concept: Vertex Replacement Operation
slug: vertex-replacement-operation
category: ramsey-theory
subcategory: induced-ramsey
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 269
section: "9.3 Induced Ramsey theorems"
extraction_confidence: high
aliases:
  - "G[U -> H]"
prerequisites:
  - graph
related:
  - induced-ramsey-theorem
answers_questions:
  - "What is vertex replacement in graph construction?"
---

# Quick Definition
For a graph G, vertex set U, and graph H, the graph G[U -> H] is obtained by replacing each vertex u in U with a copy H(u) of H, joining H(u) completely to copies H(u') for adjacent u, u' and to remaining vertices v with uv in E(G).

# Core Definition
For a vertex set U subset V and graph H, **G[U -> H]** is the graph on (U x V(H)) union ((V \ U) x {emptyset}) where (v,w) and (v',w') are adjacent iff vv' in E(G), or v = v' in U and ww' in E(H). (Diestel, p. 260)

# Prerequisites
- **Graph** — The operation is between graphs

# Key Properties
1. Each u in U becomes |H| vertices forming a copy H(u)
2. Adjacent copies are completely joined
3. Used in the first proof of the induced Ramsey theorem
4. Preserves graph structure while "inflating" selected vertices

# Examples
**Example** (p. 260, Fig. 9.3.1): G[U -> K^3] showing vertex replacement with triangles.

# Relationships
## Enables
- **Induced Ramsey theorem** — First proof uses iterated vertex replacement

# Source Reference
Chapter 9, Section 9.3, page 260 (pdf page 269). Fig. 9.3.1.

# Verification Notes
- Confidence: HIGH — formally defined with figure
