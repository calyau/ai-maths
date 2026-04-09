---
concept: Cubic Graph Cycle Packing
slug: cubic-graph-cycle-packing
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 54
section: "2.3 Packing and covering"
extraction_confidence: high
aliases:
  - "Lemma 2.3.1"
prerequisites:
  - cycle
  - cubic-graph
extends: []
related:
  - erdos-posa-theorem
contrasts_with: []
answers_questions:
  - "How many disjoint cycles must a large cubic graph contain?"
---

# Quick Definition
Every cubic multigraph on at least s_k vertices contains k disjoint cycles, where s_k is approximately 4k log k.

# Core Definition
**Lemma 2.3.1.** Let k be in N, and let H be a cubic multigraph. If |H| >= s_k, then H contains k disjoint cycles, where s_k = 4k * r_k for k >= 2 and r_k = log k + log log k + 4 (Diestel, p. 54).

# Prerequisites
- **Cycle** — the objects being packed
- **Cubic graph** — 3-regular (multi)graph

# Key Properties
1. s_k grows as O(k log k)
2. Proof by induction on k: find a shortest cycle C, show H-C contains a subdivision of a cubic graph H' with |H'| >= |H| - 2|C|
3. Uses the fact that shortest cycles in cubic graphs have logarithmic length
4. Foundation for the Erdos-Posa theorem

# Context & Application
This lemma is the core technical result behind the Erdos-Posa theorem. It shows that cubic graphs must contain many disjoint cycles when they are large enough.

# Examples
**Example**: For k=2, s_2 is small (around 8 * (log 2 + log log 2 + 4) = about 40), so cubic multigraphs on >= 40 vertices contain 2 disjoint cycles.

# Relationships
## Related
- **Erdos-Posa theorem** — uses this lemma

# Source Reference
Chapter 2, Section 2.3, Lemma 2.3.1, pp. 54-55 (pdf pp. 54-55).

# Verification Notes
- Lemma from p. 54
- Confidence: HIGH — explicit lemma with proof
