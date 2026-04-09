---
concept: Girth Forcing Minors
slug: girth-forcing-minors
category: extremal-graph-theory
subcategory: minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 181
section: "7.2 Minors"
extraction_confidence: high
aliases:
  - "Thomassen's theorem on girth and minors"
  - "Theorem 7.2.4"
prerequisites:
  - graph
  - kostochka-theorem
related:
  - mader-theorem-topological-minors
  - hadwiger-conjecture
answers_questions:
  - "Can large girth force large complete minors?"
---

# Quick Definition
There exists a function f: N -> N such that every graph of minimum degree at least 3 and girth at least f(r) has a K^r minor (Thomassen 1983).

# Core Definition
**Theorem 7.2.4** (Thomassen 1983): There exists a function f: N -> N such that every graph of minimum degree at least 3 and girth at least f(r) has a K^r minor, for all r in N. The proof uses f(r) := 8 log r + 4 log log r + c, based on Lemma 7.2.3 which shows that large girth with minimum degree d produces minors of minimum degree d(d-1)^k. (Diestel, p. 171-172)

**Theorem 7.2.5** (Kuhn & Osthus 2002): There exists a constant g such that G contains TK^r for every graph G satisfying delta(G) >= r-1 and g(G) >= g.

# Prerequisites
- **Graph** — The theorem concerns girth and minimum degree
- **Kostochka's theorem** — Used to convert high-minimum-degree minors into K^r minors

# Key Properties
1. At first paradoxical: large girth (no short cycles) forces large complete minors
2. The mechanism: large-girth graphs with minimum degree >= 3 have trees with many leaves, each sending edges elsewhere; contracting these trees creates minors of high degree
3. For topological minors: assuming delta >= r-1 and large constant girth suffices (Theorem 7.2.5)

# Relationships
## Builds Upon
- **Kostochka's theorem** — Converts high-degree minors to K^r minors

## Related
- **Hadwiger's conjecture** — Corollary 7.3.9 proves it for large-girth graphs

# Source Reference
Chapter 7, Section 7.2, Theorems 7.2.4 and 7.2.5, pages 171-172 (pdf pages 181-182). Lemma 7.2.3.

# Verification Notes
- Confidence: HIGH — theorems with proofs
