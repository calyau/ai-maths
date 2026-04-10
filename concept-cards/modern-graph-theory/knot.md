---
concept: Knot
slug: knot
category: knot-theory
subcategory: null
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 363
section: "X.6 Polynomials of Knots and Links"
extraction_confidence: high
aliases:
  - "tame knot"
prerequisites: []
extends: []
related:
  - link
  - link-diagram
  - ambient-isotopy
contrasts_with:
  - link
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
A knot is a piecewise linear simple closed curve in $\mathbb{R}^3$. Two knots are equivalent if one can be continuously deformed into the other (ambient isotopy).

# Core Definition
"A knot is a connected link" (Bollobás, p. 363). More precisely, a link of one component: a single piecewise linear simple closed curve in $\mathbb{R}^3 \subset S^3$.

# Prerequisites
This is a foundational concept for Section X.6.

# Key Properties
1. A knot is a link with exactly one component
2. Equivalence is by ambient isotopy (orientation-preserving homeomorphism of $\mathbb{R}^3$)
3. The unknot (trivial knot) has a diagram with no crossings
4. Knots are studied via their diagrams (projections to $\mathbb{R}^2$)

# Context & Application
"Knot theory proper was really started only in the 1920s" with work by Dehn, Alexander, and Reidemeister. The connection to the Tutte polynomial via the Jones and Kauffman polynomials was discovered in the 1980s.

# Examples
**Example** (Fig. X.3, p. 363): The right-handed trefoil knot.

# Relationships
## Related
- **link** — A knot is a connected link
- **link-diagram** — How knots are represented
- **ambient-isotopy** — Equivalence relation

## Contrasts With
- **link** — A link may have multiple components

# Source Reference
Chapter X, Section X.6, pages 363-364.

# Verification Notes
- Definition source: Direct from p. 363
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
