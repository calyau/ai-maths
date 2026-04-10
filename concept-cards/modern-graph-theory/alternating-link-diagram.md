---
concept: Alternating Link Diagram
slug: alternating-link-diagram
category: knot-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 375
section: "X.6 Polynomials of Knots and Links"
extraction_confidence: high
aliases:
  - "alternating diagram"
  - "alternating link"
prerequisites:
  - link-diagram
  - signed-plane-graph
extends:
  - link-diagram
related:
  - tutte-polynomial-and-jones-polynomial
  - tait-conjecture-crossing-number
contrasts_with: []
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
A link diagram is alternating if its crossings alternate as one travels along each component: over, under, over, under, and so on. Equivalently, all edges of the associated signed graph have the same sign.

# Core Definition
"A link diagram is alternating if its crossings alternate as one travels along the arcs of the link: over, under, over, under, ..." (Bollobás, p. 375). Equivalently, "a connected link diagram is alternating if, and only if, each of its regions has only $A$-channels or only $B$-channels."

# Prerequisites
- **Link diagram** — Alternating diagrams are a special type
- **Signed plane graph** — All edges have the same sign

# Key Properties
1. Every 4-regular plane multigraph is the universe of an alternating diagram
2. For alternating diagrams: Kauffman/Jones polynomial determined by Tutte polynomial
3. Associated signed graph $G^+(L)$ (all + signs) or $G^-(L)$ (all - signs)
4. Theorem 21: $V_L(t) = (-1)^w t^{(b-a+3w)/4} T_{G^+(L)}(-t, -1/t)$

# Context & Application
Alternating diagrams are central because for these diagrams, the Jones polynomial is a direct evaluation of the Tutte polynomial of the associated graph. This is the deepest connection between graph theory and knot theory in the chapter.

# Examples
**Example** (p. 375): Trefoil, figure of eight, Hopf link, and Borromean rings all have alternating diagrams.

# Relationships
## Builds Upon
- **link-diagram**, **signed-plane-graph**

## Enables
- **tutte-polynomial-and-jones-polynomial** — Theorem 21
- **tait-conjecture-crossing-number** — Theorem 22

# Source Reference
Chapter X, Section X.6, pages 375-376.

# Verification Notes
- Definition source: Direct from p. 375
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
