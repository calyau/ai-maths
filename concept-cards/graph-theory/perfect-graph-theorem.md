---
concept: Perfect Graph Theorem
slug: perfect-graph-theorem
category: graph-colouring
subcategory: perfect-graphs
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.5 Perfect graphs"
extraction_confidence: high
aliases:
  - "Theorem 5.5.4"
  - "Lovasz 1972"
  - "weak perfect graph theorem"
  - "Berge's weak conjecture"
prerequisites:
  - perfect-graph
extends: []
related:
  - strong-perfect-graph-theorem
  - lovasz-theta
contrasts_with: []
answers_questions:
  - "Is the complement of a perfect graph also perfect?"
---

# Quick Definition
The Perfect Graph Theorem (Lovasz 1972) states that a graph is perfect if and only if its complement is perfect. Perfection is a self-complementary property.

# Core Definition
**Theorem 5.5.4** (Lovasz 1972): "A graph is perfect if and only if its complement is perfect" (Diestel, p. 129).

# Prerequisites
- **Perfect graph** -- The theorem relates G's perfection to complement(G)'s

# Key Properties
1. Perfection is symmetric under complementation
2. Two proofs given: Lovasz's original (using vertex expansion) and Gasparian's (linear algebra)
3. Formerly the "weak perfect graph conjecture" of Berge
4. Implied by the strong perfect graph theorem, but has independent elementary proofs

# Context & Application
The perfect graph theorem was a major breakthrough in structural graph theory. The proof by Lovasz (1972) introduced the technique of vertex expansion, while Gasparian's proof (1996) uses linear algebra (the characterization |H| <= alpha(H) * omega(H)). Both proofs are given in the text.

# Relationships
## Builds Upon
- **Perfect graph**

## Related
- **Strong perfect graph theorem** -- Stronger result that implies this one
- **Lovasz's characterization** (Theorem 5.5.6) -- |H| <= alpha * omega characterizes perfection

# Source Reference
Chapter 5, Section 5.5, Theorem 5.5.4, pages 129-132.

# Verification Notes
- Two complete proofs given
- Confidence: HIGH -- named theorem with two proofs
