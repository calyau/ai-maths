---
concept: k-Connected Characterization
slug: k-connected-characterization
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 77
section: "3.3 Menger's theorem"
extraction_confidence: high
aliases:
  - "Whitney characterization"
prerequisites:
  - k-connected-graph
  - mengers-theorem
  - independent-paths
extends:
  - mengers-theorem
related:
  - global-mengers-theorem
contrasts_with: []
answers_questions:
  - "How is k-connectivity equivalent to k independent paths?"
---

# Quick Definition
A graph is k-connected if and only if it has more than k vertices and contains k independent paths between any two vertices (Theorem 3.3.6(i)).

# Core Definition
The equivalence of two characterizations of k-connectivity: (1) G has more than k vertices and removing any k-1 vertices leaves G connected; (2) G has more than k vertices and any two vertices are linked by k independent paths (Diestel, Theorem 3.3.6(i), p. 77).

# Prerequisites
- **k-connected graph** — the graph property being characterized
- **Menger's theorem** — the foundation for the equivalence
- **Independent paths** — the alternative characterization

# Key Properties
1. The "removal" characterization is the definition of k-connectivity
2. The "paths" characterization is more constructive and often more useful
3. Their equivalence is a consequence of the global version of Menger's theorem
4. For k=2: 2-connected iff any two vertices lie on a common cycle

# Context & Application
This characterization resolves the apparent tension between the defensive (resilience to removal) and offensive (existence of many paths) views of connectivity. Both are equivalent, making k-connectivity a very natural and robust concept.

# Examples
**Example**: K4 is 3-connected: removing any 2 vertices leaves a connected graph, and any two vertices have 3 independent paths.

# Relationships
## Builds Upon
- **k-connected graph**, **Menger's theorem**, **independent paths**

## Related
- **Global Menger's theorem** — provides the equivalence

# Source Reference
Chapter 3, Section 3.3, Theorem 3.3.6(i), p. 77 (pdf p. 77).

# Verification Notes
- From Theorem 3.3.6
- Confidence: HIGH
