---
concept: Group of H-Circulations
slug: h-circulation-group
category: network-flows
subcategory: algebraic-flows
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 155
section: "6.3 Group-valued flows"
extraction_confidence: high
aliases: []
prerequisites:
  - circulation
  - h-flow
related:
  - flow-polynomial
answers_questions:
  - "Do circulations form a group?"
---

# Quick Definition
The H-circulations on a graph G form a group under pointwise addition: if f and g are H-circulations, then f + g and -f are also H-circulations. However, H-flows (nowhere-zero circulations) do NOT form a group.

# Core Definition
Let G = (V, E) be a multigraph and H an abelian group. If f and g are two H-circulations, then (f+g): e-arrow -> f(e-arrow) + g(e-arrow) and -f: e-arrow -> -f(e-arrow) are again H-circulations. The H-circulations on G thus form a group in a natural way. (Diestel, p. 145)

However, the set of H-flows is NOT closed under addition: if two H-flows sum to zero on some edge, their sum is no longer an H-flow.

# Prerequisites
- **Circulation** — H-circulations form a group
- **H-flow** — H-flows do NOT form a group

# Key Properties
1. Closure under addition and negation
2. The zero circulation is the identity element
3. H-flows are NOT a subgroup (not closed under addition)
4. This group structure is used in proofs (e.g., summing Z_k-circulations)

# Source Reference
Chapter 6, Section 6.3, page 145 (pdf page 155).

# Verification Notes
- Confidence: HIGH — explicitly stated
