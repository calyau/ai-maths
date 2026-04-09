---
concept: Monochromatic Subgraph
slug: monochromatic-subgraph
category: ramsey-theory
subcategory: classical-ramsey
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 263
section: "9.1 Ramsey's original theorems"
extraction_confidence: high
aliases:
  - "monochromatic set"
  - "red subgraph"
prerequisites:
  - c-colouring
related:
  - ramsey-theorem-finite
  - ramsey-number
answers_questions:
  - "What is a monochromatic subgraph?"
---

# Quick Definition
A subgraph H of G is monochromatic (in a given edge colouring) if all edges of H have the same colour.

# Core Definition
Given a c-colouring of [X]^k, a set Y subset X is called **monochromatic** if all elements of [Y]^k have the same colour. If G = (V, E) is a graph and all edges of H subset G have the same colour in some colouring of E, we call H a **monochromatic subgraph** of G. We speak of a "red H in G," etc. (Diestel, p. 253)

# Prerequisites
- **c-colouring** — Monochromatic subgraphs exist within colourings

# Key Properties
1. All edges of the subgraph have the same colour
2. The central object sought in Ramsey theory
3. For graph Ramsey theory: every 2-colouring of K^n yields a monochromatic K^r for n >= R(r)

# Relationships
## Builds Upon
- **c-colouring** — Monochromatic subgraphs arise within colourings

## Related
- **Ramsey's theorem** — Guarantees monochromatic complete or empty subgraphs
- **Ramsey number** — Quantifies how large G must be

# Source Reference
Chapter 9, Section 9.1, page 253 (pdf page 263).

# Verification Notes
- Confidence: HIGH — explicitly defined
