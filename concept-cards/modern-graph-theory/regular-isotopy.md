---
concept: Regular Isotopy
slug: regular-isotopy
category: knot-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 365
section: "X.6 Polynomials of Knots and Links"
extraction_confidence: high
aliases: []
prerequisites:
  - link-diagram
  - reidemeister-moves
extends: []
related:
  - ambient-isotopy
  - kauffman-bracket
contrasts_with:
  - ambient-isotopy
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
Two link diagrams are regularly isotopic if they can be transformed into each other by planar isotopy and Reidemeister moves of Types II and III only (no Type I moves, which add/remove curls).

# Core Definition
"Two link diagrams are said to be regularly isotopic if they can be transformed into each other by planar isotopy and moves of Types II and III" (Bollobás, p. 365).

# Prerequisites
- **Link diagram** — Regular isotopy relates diagrams
- **Reidemeister moves** — Types II and III generate regular isotopy

# Key Properties
1. Weaker than ambient isotopy (does not include Type I)
2. The Kauffman bracket $\langle L \rangle$ is a regular isotopy invariant
3. The writhe $w(L)$ is a regular isotopy invariant

# Relationships
## Builds Upon
- **link-diagram**, **reidemeister-moves**

## Related
- **kauffman-bracket** — Invariant under regular isotopy

## Contrasts With
- **ambient-isotopy** — Includes Type I moves

# Source Reference
Chapter X, Section X.6, page 365.

# Verification Notes
- Definition source: Direct from p. 365
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
