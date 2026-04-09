---
concept: Unavoidable Substructures in 4-Connected Graphs
slug: unavoidable-substructures-4connected
category: ramsey-theory
subcategory: ramsey-connectivity
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 280
section: "9.4 Ramsey properties and connectivity"
extraction_confidence: high
aliases:
  - "Theorem 9.4.4"
  - "double wheel"
  - "crown graph"
  - "Mobius crown"
prerequisites:
  - unavoidable-substructures-3connected
related:
  - kuratowski-set
answers_questions:
  - "What substructures must large 4-connected graphs contain?"
---

# Quick Definition
For every r, every sufficiently large 4-connected graph has a minor of order >= r that is a double wheel, a crown, a Mobius crown, or a K_{4,s}.

# Core Definition
**Theorem 9.4.4** (Oporowski, Oxley & Thomas 1993): For every r in N there is an n in N such that every 4-connected graph with at least n vertices has a minor of order >= r that is a double wheel (C^n * K-bar^2), a crown (triangulation of cylinder), a Mobius crown (triangulation of Mobius strip), or a K_{4,s}. The unique 4-element Kuratowski set for 4-connected graphs is {double wheels, crowns, Mobius crowns, K_{4,r}s}. (Diestel, pp. 269-270)

# Prerequisites
- **Unavoidable substructures (3-connected)** — The 3-connected case

# Key Properties
1. Four families are unavoidable (compared to 2 for lower connectivity)
2. Double wheel: C^n * K-bar^2
3. Crown: 1-skeleton of a triangulated cylinder
4. Mobius crown: 1-skeleton of a triangulated Mobius strip
5. This Kuratowski set is unique (Theorem 9.4.5(iv))
6. For higher k, no similar results are known

# Examples
**Example** (p. 269, Fig. 9.4.1): A crown and a Mobius crown illustrated.

# Source Reference
Chapter 9, Section 9.4, Theorem 9.4.4, pages 269-270 (pdf pages 279-280).

# Verification Notes
- Confidence: HIGH — stated theorem with figures
