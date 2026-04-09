---
concept: "Vizing's Theorem"
slug: vizing-theorem
category: graph-colouring
subcategory: edge-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.3 Colouring edges"
extraction_confidence: high
aliases:
  - "Theorem 5.3.2"
  - "Vizing 1964"
prerequisites:
  - chromatic-index
extends: []
related:
  - konig-edge-colouring-theorem
  - class-one-class-two
  - brooks-theorem
contrasts_with: []
answers_questions:
  - "What are the possible values of the chromatic index?"
  - "How tight is the lower bound chi' >= Delta?"
---

# Quick Definition
Vizing's theorem states that every graph G satisfies Delta(G) <= chi'(G) <= Delta(G) + 1. The chromatic index is always either Delta or Delta + 1.

# Core Definition
**Theorem 5.3.2** (Vizing 1964): "Every graph G satisfies Delta(G) <= chi'(G) <= Delta(G) + 1" (Diestel, p. 119).

# Prerequisites
- **Chromatic index** -- The theorem bounds chi'(G)

# Key Properties
1. chi'(G) in {Delta(G), Delta(G) + 1} for every graph G
2. The proof uses "missing colours" at vertices and alpha/beta alternating paths
3. Contrasts sharply with vertex colouring, where chi can be much larger than Delta
4. Bipartite graphs always achieve chi' = Delta (Konig)
5. Determining which value applies is NP-complete in general

# Context & Application
Vizing's theorem is one of the most elegant results in graph theory, showing that edge colouring is much more constrained than vertex colouring. While chi(G) can be arbitrarily far from Delta(G), chi'(G) is always within 1. This divides graphs into "class 1" (chi' = Delta) and "class 2" (chi' = Delta + 1).

# Examples
**Example**: Bipartite graphs are class 1 (chi' = Delta) by Konig's theorem.

**Example**: The Petersen graph has Delta = 3 but chi' = 4 (class 2).

**Example**: Odd cycles have Delta = 2 and chi' = 3 (class 2).

# Relationships
## Builds Upon
- **Chromatic index**

## Enables
- **Class one/class two** classification

## Related
- **Konig's theorem** -- The bipartite special case
- **Brooks' theorem** -- Analogous "Delta or Delta + 1" story for vertex colouring (but with exceptions)

# Common Errors
- **Error**: Assuming all graphs are class 1
  **Correction**: Many graphs (odd cycles, Petersen graph) are class 2

# Source Reference
Chapter 5, Section 5.3, Theorem 5.3.2, pages 119-121.

# Verification Notes
- Full proof given pp. 119-121
- Confidence: HIGH -- named classical theorem with complete proof
