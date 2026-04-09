---
concept: Flow Polynomial
slug: flow-polynomial
category: network-flows
subcategory: algebraic-flows
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 156
section: "6.3 Group-valued flows"
extraction_confidence: high
aliases: []
prerequisites:
  - h-flow
  - circulation
related:
  - k-flow
  - flow-number
answers_questions:
  - "How does the flow polynomial count flows?"
---

# Quick Definition
The flow polynomial P of a multigraph G is a polynomial such that for any finite abelian group H, the number of H-flows on G equals P(|H| - 1).

# Core Definition
**Theorem 6.3.1** (Tutte 1954): For every multigraph G there exists a polynomial P such that, for any finite abelian group H, the number of H-flows on G is P(|H| - 1). This polynomial P is called the **flow polynomial** of G. (Diestel, p. 145-146)

The proof uses induction on |E|, with the key identity: the number of H-flows on G equals P_2(k) - P_1(k), where P_1 counts flows on G - e_0 and P_2 counts flows on G / e_0, for k = |H| - 1.

# Prerequisites
- **H-flow** — The flow polynomial counts H-flows
- **Circulation** — The proof relates circulations on G, G - e, and G / e

# Key Properties
1. The number of H-flows depends only on |H|, not on the group structure
2. Proved by deletion-contraction: P(G) = P(G/e) - P(G-e)
3. For a graph of all loops with m edges: P = x^m
4. Related to the chromatic polynomial and the Tutte polynomial

# Context & Application
The flow polynomial is the algebraic foundation that shows group-valued flow theory reduces to integer-valued flow theory. It is an analogue of the chromatic polynomial and a specialization of the Tutte polynomial.

# Relationships
## Builds Upon
- **H-flow** — Counts H-flows

## Related
- **k-flow** — Existence of k-flows can be determined via the flow polynomial

# Source Reference
Chapter 6: Flows, Section 6.3, Theorem 6.3.1, pages 145-146 (pdf pages 155-156).

# Verification Notes
- Confidence: HIGH — named theorem with full proof
