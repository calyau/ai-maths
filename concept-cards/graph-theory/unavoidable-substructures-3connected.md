---
concept: Unavoidable Substructures in 3-Connected Graphs
slug: unavoidable-substructures-3connected
category: ramsey-theory
subcategory: ramsey-connectivity
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 279
section: "9.4 Ramsey properties and connectivity"
extraction_confidence: high
aliases:
  - "Theorem 9.4.3"
prerequisites:
  - unavoidable-substructures-2connected
related:
  - kuratowski-set
  - unavoidable-substructures-4connected
answers_questions:
  - "What substructures must large 3-connected graphs contain?"
---

# Quick Definition
For every r, every sufficiently large 3-connected graph contains a wheel of order r or a K_{3,r} as a minor (Theorem 9.4.3, Oporowski-Oxley-Thomas 1993).

# Core Definition
**Theorem 9.4.3** (Oporowski, Oxley & Thomas 1993): For every r in N there is an n in N such that every 3-connected graph of order at least n contains a wheel of order r or a K_{3,r} as a minor. The unique 2-element Kuratowski set for 3-connected graphs (w.r.t. minor relation) is {wheels, K_{3,r}s}. (Diestel, p. 269)

# Prerequisites
- **Unavoidable substructures (2-connected)** — The 2-connected case

# Key Properties
1. The containment relation is now "minor" (relaxed from topological minor)
2. Wheels and K_{3,r}s are the unavoidable families
3. This Kuratowski set is unique (Theorem 9.4.5(iii))

# Source Reference
Chapter 9, Section 9.4, Theorem 9.4.3, page 269 (pdf page 279).

# Verification Notes
- Confidence: HIGH — stated theorem (proof not given)
