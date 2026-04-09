---
concept: "Burr-Erd\u0151s Conjecture"
slug: burr-erdos-conjecture
category: ramsey-theory
subcategory: graph-ramsey
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 282
section: "Notes"
extraction_confidence: medium
aliases: []
prerequisites:
  - ramsey-number-bounded-degree
  - graph-ramsey-number
related:
  - ramsey-theorem-finite
answers_questions:
  - "What is the Burr-Erdos conjecture?"
---

# Quick Definition
The Burr-Erdos conjecture (1975) asserts that for every d, there exists c such that R(H) <= c|H| for all graphs H with d(H') <= d for all H' subset H (bounded average degree in every subgraph). Theorem 9.2.2 proves the weaker version with bounded maximum degree.

# Core Definition
The **Burr-Erdos conjecture** (1975) asserts that the Ramsey numbers of graphs with bounded average degree in every subgraph are linear: for every d in N, there exists a constant c such that R(H) <= c|H| for all graphs H with d(H') <= d for all H' subset H.

Theorem 9.2.2 verifies this for bounded maximum degree. Kostochka and Sudakov (2003) proved R(H) <= |H|^{1+o(1)} for the Burr-Erdos class. (Diestel, pp. 272-273, Notes)

# Prerequisites
- **Ramsey number (bounded degree)** — Partial result toward the conjecture
- **Graph Ramsey number** — R(H) is the quantity of interest

# Key Properties
1. Generalizes from bounded Delta to bounded average degree
2. Theorem 9.2.2 is a breakthrough toward this conjecture
3. The approximate version R(H) <= |H|^{1+o(1)} was proved

# Source Reference
Chapter 9, Notes, pages 272-273 (pdf pages 282-283).

# Verification Notes
- Confidence: MEDIUM — discussed in notes, not main text
