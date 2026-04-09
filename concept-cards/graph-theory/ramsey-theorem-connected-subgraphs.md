---
concept: "Ramsey's Theorem and Connectivity"
slug: ramsey-theorem-connected-subgraphs
category: ramsey-theory
subcategory: ramsey-connectivity
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 278
section: "9.4 Ramsey properties and connectivity"
extraction_confidence: high
aliases:
  - "Theorem 9.4.5"
prerequisites:
  - unavoidable-substructures-connected
  - unavoidable-substructures-2connected
  - unavoidable-substructures-3connected
  - unavoidable-substructures-4connected
  - kuratowski-set
related:
  - ramsey-theorem-finite
answers_questions:
  - "What are the unavoidable substructures for k-connected graphs?"
---

# Quick Definition
Theorem 9.4.5 unifies the unavoidable-substructure results: it gives unique Kuratowski sets for k-connected graphs (k = 1,2,3,4) with respect to appropriate containment relations.

# Core Definition
**Theorem 9.4.5**:
(i) Stars and paths form the unique 2-element Kuratowski set for connected graphs (subgraph relation).
(ii) Cycles and K_{2,r}s form the unique 2-element Kuratowski set for 2-connected graphs (topological minor).
(iii) Wheels and K_{3,r}s form the unique 2-element Kuratowski set for 3-connected graphs (minor).
(iv) Double wheels, crowns, Mobius crowns, and K_{4,r}s form the unique 4-element Kuratowski set for 4-connected graphs (minor). (Diestel, p. 270)

These sets are smallest possible and as such unique.

# Prerequisites
- All four unavoidable-substructure results
- **Kuratowski set** — The unifying framework

# Key Properties
1. As connectivity k increases, the unavoidable set may grow (2 elements for k=1,2,3; 4 for k=4)
2. The containment relation also changes: subgraph -> topological minor -> minor
3. For k >= 5, no similar results are known
4. The K^r from classical Ramsey conspicuously disappears from k >= 2 results

# Source Reference
Chapter 9, Section 9.4, Theorem 9.4.5, page 270 (pdf page 280).

# Verification Notes
- Confidence: HIGH — unifying theorem stated
