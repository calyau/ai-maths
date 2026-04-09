---
concept: "Tur\u00E1n Number Asymptotics"
slug: turan-number-asymptotics
category: extremal-graph-theory
subcategory: subgraph-density
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 178
section: "7.1 Subgraphs"
extraction_confidence: high
aliases:
  - "Lemma 7.1.4"
prerequisites:
  - turan-graph
  - extremal-number
related:
  - erdos-stone-theorem
  - asymptotic-extremal-density
answers_questions:
  - "What is the asymptotic behaviour of t_{r-1}(n)?"
---

# Quick Definition
t_{r-1}(n)/C(n,2) converges to (r-2)/(r-1) as n -> infinity, and t_{r-1}(n) <= (1/2)n^2(r-2)/(r-1) with equality when (r-1) divides n.

# Core Definition
**Lemma 7.1.4**: lim_{n->infinity} t_{r-1}(n)/C(n,2) = (r-2)/(r-1).

Also: t_{r-1}(n) <= (1/2)n^2(r-2)/(r-1), with equality whenever r-1 divides n. (Diestel, pp. 167-168)

# Prerequisites
- **Turan graph** — t_{r-1}(n) counts edges in T^{r-1}(n)
- **Extremal number** — t_{r-1}(n) = ex(n, K^r)

# Key Properties
1. The Turan number is approximately (r-2)/(2(r-1)) * n^2
2. Exact when (r-1) divides n
3. Used as a lemma in the proof of Corollary 7.1.3

# Source Reference
Chapter 7, Section 7.1, Lemma 7.1.4, page 168 (pdf page 178).

# Verification Notes
- Confidence: HIGH — explicit lemma
