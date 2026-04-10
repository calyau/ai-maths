---
concept: Link Diagram
slug: link-diagram
category: knot-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 364
section: "X.6 Polynomials of Knots and Links"
extraction_confidence: high
aliases:
  - "knot diagram"
prerequisites:
  - link
extends: []
related:
  - reidemeister-moves
  - ambient-isotopy
  - kauffman-bracket
contrasts_with: []
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
A link diagram is a projection of a link into $\mathbb{R}^2$, forming a 4-regular plane multigraph where at each crossing, one strand goes over and the other goes under.

# Core Definition
"A link diagram is a (finite) 4-regular plane graph with some extra structure, namely at each vertex the two pairs of edges cross in one of two ways: one goes either under or over the other" (Bollobás, p. 364). The 4-regular graph without crossing information is the *universe* of the diagram. A 4-regular plane graph of order $n$ gives rise to $2^n$ link diagrams.

# Prerequisites
- **Link** — A link diagram represents a link

# Key Properties
1. 4-regular plane multigraph
2. At each vertex: over/under crossing information
3. Two diagrams represent equivalent links iff connected by Reidemeister moves
4. A 4-regular graph of $n$ crossings yields $2^n$ possible diagrams
5. Planar isotopic diagrams are considered the same

# Context & Application
"It is very easy to view links as purely combinatorial objects" via link diagrams (p. 364). All knot and link invariants in this section are defined on diagrams.

# Examples
**Example** (Fig. X.5, p. 365): Diagrams of the right-handed and left-handed trefoil knots from the same universe (triangle with double edges).

# Relationships
## Builds Upon
- **link**

## Enables
- **reidemeister-moves** — Transform between equivalent diagrams
- **kauffman-bracket** — Defined on link diagrams

# Source Reference
Chapter X, Section X.6, pages 364-365.

# Verification Notes
- Definition source: Direct from p. 364
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
