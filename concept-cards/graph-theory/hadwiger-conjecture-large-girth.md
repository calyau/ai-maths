---
concept: "Hadwiger's Conjecture for Large Girth"
slug: hadwiger-conjecture-large-girth
category: extremal-graph-theory
subcategory: minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 185
section: "7.3 Hadwiger's conjecture"
extraction_confidence: high
aliases:
  - "Corollary 7.3.9"
  - "Theorem 7.3.8"
prerequisites:
  - hadwiger-conjecture
  - girth-forcing-minors
related:
  - hajos-conjecture
answers_questions:
  - "Is Hadwiger's conjecture true for graphs of large girth?"
---

# Quick Definition
There is a constant g such that all graphs of girth at least g satisfy Hadwiger's conjecture: chi(G) >= r implies G contains K^r as a minor, for all r.

# Core Definition
**Corollary 7.3.9**: There is a constant g such that all graphs G of girth at least g satisfy chi(G) >= r => G contains TK^r for all r. If chi(G) >= r then G has a subgraph H with delta(H) >= r-1 (by Corollary 5.2.3), and Theorem 7.2.5 gives TK^r in H.

**Theorem 7.3.8** (Kuhn & Osthus 2005): For every integer s there is an integer r_s such that Hadwiger's conjecture holds for all graphs G not containing K_{s,s} and r >= r_s. (Diestel, pp. 175-176)

# Prerequisites
- **Hadwiger's conjecture** — The result proves special cases
- **Girth forcing minors** — The key tool (Theorem 7.2.5)

# Key Properties
1. Hadwiger's conjecture holds for large-girth graphs (all r simultaneously)
2. Also holds for K_{s,s}-free graphs for large enough r
3. Hajos's conjecture (topological version) also holds for large girth

# Source Reference
Chapter 7, Section 7.3, Corollary 7.3.9 and Theorem 7.3.8, pages 175-176 (pdf pages 185-186).

# Verification Notes
- Confidence: HIGH — corollary with proof
