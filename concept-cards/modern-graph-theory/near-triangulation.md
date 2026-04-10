---
concept: Near-Triangulation
slug: near-triangulation
category: planar-graphs
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 169
section: "V.4 List Colouring"
extraction_confidence: high
aliases: []
prerequisites:
  - euler-formula-for-planar-graphs
extends: []
related:
  - thomassens-list-colouring-theorem
contrasts_with: []
answers_questions:
  - "What is a near-triangulation?"
---

# Quick Definition
A near-triangulation is a plane graph whose outer face is bounded by a cycle and all inner faces are triangles.

# Core Definition
A plane graph is a **near-triangulation** if the outer face is a cycle and all the inner faces are triangles. In a maximal plane graph of order at least 4, every face is a triangle, so near-triangulations generalize maximal planar graphs by allowing the outer face to be non-triangular (Bollobás, p. 169).

# Prerequisites
- **Euler's formula for planar graphs** — near-triangulations are close to maximally planar

# Key Properties
1. All inner faces are triangles
2. The outer face is bounded by a cycle
3. Every maximal plane graph of order ≥ 4 is a near-triangulation
4. The setting for Thomassen's 5-list-colourability theorem

# Context & Application
Near-triangulations provide the right induction framework for Thomassen's theorem. The stronger statement about near-triangulations (with variable list sizes on the boundary) makes the induction work.

# Relationships
## Enables
- **Thomassen's list colouring theorem** — stated for near-triangulations

# Source Reference
Chapter V: Colouring, Section V.4, page 169.

# Verification Notes
- Definition source: Direct from p. 169
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
