---
concept: Ramsey Numbers for Bounded-Degree Graphs
slug: ramsey-for-bounded-degree
category: ramsey-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 203
section: "VI.3 Ramsey Theory For Graphs"
extraction_confidence: high
aliases:
  - "Theorem VI.18"
  - "Chvátal-Rödl-Szemerédi-Trotter theorem"
prerequisites:
  - graphical-ramsey-number
extends: []
related:
  - ramsey-number-for-trees
contrasts_with: []
answers_questions:
  - "How do Ramsey numbers grow for bounded-degree graphs?"
---

# Quick Definition
For every d ≥ 1, there is a constant c = c(d) such that if Δ(H) ≤ d then r(H, H) ≤ c|H|. Ramsey numbers of bounded-degree graphs grow linearly in the number of vertices.

# Core Definition
**Theorem 18** (Bollobás, p. 203): For every d ≥ 1 there is a constant c = c(d) such that if Δ(H) ≤ d then r(H, H) ≤ c|H|. This deep result was proved by Chvátal, Rödl, Szemerédi and Trotter in 1983.

The Burr-Erdős conjecture (1975) proposes the stronger statement with maximum degree replaced by maximum minimum degree of subgraphs.

# Prerequisites
- **Graphical Ramsey number** — the quantity being bounded

# Key Properties
1. r(H, H) = O(|H|) when Δ(H) is bounded
2. This is optimal order of magnitude since r(H, H) ≥ |H|
3. The constant c depends only on Δ(H)
4. Chen and Schelp: r(H) ≤ c|H| for planar H
5. Rödl and Thomas: r(H) ≤ c(k)|H| if H has no K_k minor

# Context & Application
This theorem shows that the exponential growth of Ramsey numbers is driven by high-degree vertices. For sparse graphs (bounded degree), Ramsey numbers grow only linearly.

# Relationships
## Related
- **Ramsey number for trees** — special case (trees have bounded degree in a sense)

# Source Reference
Chapter VI: Ramsey Theory, Section VI.3, Theorem 18, page 203.

# Verification Notes
- Definition source: Direct theorem statement from p. 203
- Confidence rationale: Explicitly stated, proof not given (deep result)
- Uncertainties: None
- Cross-reference status: Verified
