---
concept: Mader's Theorem
slug: mader-theorem

category: connectivity
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 22
section: "1.4 Connectivity"

extraction_confidence: high

aliases:
  - "Theorem 1.4.3"

prerequisites:
  - graph
  - average-degree
  - k-connected
  - edge-density
extends: []
related:
  - minimum-degree-subgraph
contrasts_with: []

answers_questions:
  - "Does large average degree force a highly connected subgraph?"
---

# Quick Definition
Every graph G with average degree d(G) >= 4k has a (k+1)-connected subgraph H with epsilon(H) > epsilon(G) - k (Mader, 1972).

# Core Definition
Theorem 1.4.3 (Mader 1972): Let 0 != k in N. Every graph G with d(G) >= 4k has a (k+1)-connected subgraph H such that epsilon(H) > epsilon(G) - k (Diestel, p. 12).

# Prerequisites
- **Graph**, **average-degree**, **k-connected**, **edge-density**

# Key Properties
1. Large average degree (at least 4k) guarantees a (k+1)-connected subgraph
2. The subgraph nearly preserves the edge density
3. The proof uses an extremal argument based on (*)-type subgraphs

# Context & Application
This theorem connects the global measure of average degree to the structural property of high connectivity. It shows that minimum degree alone does not ensure high connectivity, but dense graphs must contain highly connected subgraphs.

# Relationships
## Builds Upon
- **average-degree**, **k-connected**, **edge-density**

## Related
- **minimum-degree-subgraph** — Proposition 1.2.2 is a weaker version

# Source Reference
Chapter 1: The Basics, Section 1.4, Theorem 1.4.3, pages 12-13 (pdf pp. 22-23).

# Verification Notes
- Theorem statement and proof from pp. 12-13
- Confidence: HIGH — explicitly stated theorem with proof
