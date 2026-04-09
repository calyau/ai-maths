---
concept: Exceeds (Path System)
slug: exceeds-path-system
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 73
section: "3.3 Menger's theorem"
extraction_confidence: high
aliases: []
prerequisites:
  - mengers-theorem
  - path
extends: []
related:
  - alternating-walk
contrasts_with: []
answers_questions:
  - "What does it mean for one path system to exceed another?"
---

# Quick Definition
A set Q of disjoint A-B paths exceeds a set P if the A-endpoints of P are a proper subset of those of Q, and likewise for B-endpoints.

# Core Definition
Let P be a set of disjoint A-B paths, and let Q be another such set. We say that Q **exceeds** P if the set of vertices in A that lie on a path in P is a proper subset of the set in A on a path in Q, and likewise for B. In particular, |Q| >= |P| + 1 (Diestel, p. 73).

# Prerequisites
- **Menger's theorem** — exceeding is used in the second proof
- **Path** — path systems are the objects being compared

# Key Properties
1. Q has strictly more A-endpoints and B-endpoints than P
2. |Q| >= |P| + 1
3. Used in the second proof of Menger's theorem
4. The proof shows: if P is suboptimal, a system exceeding P exists

# Context & Application
The "exceeds" relation provides the inductive step in the second proof of Menger's theorem: starting from any suboptimal path system, one can always find a system that exceeds it.

# Examples
**Example** (p. 73, Fig. 3.3.1): The path R from A to B avoids the B-endpoints of P, leading to a construction of Q exceeding P.

# Relationships
## Related
- **Menger's theorem** — second proof uses this concept

# Source Reference
Chapter 3, Section 3.3, p. 73 (pdf p. 73).

# Verification Notes
- Definition from p. 73
- Confidence: HIGH — explicitly defined
