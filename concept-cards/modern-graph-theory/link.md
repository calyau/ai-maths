---
concept: Link
slug: link
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
  - "n-component link"
prerequisites: []
extends: []
related:
  - knot
  - link-diagram
  - ambient-isotopy
contrasts_with:
  - knot
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
A link of $n$ components is a subset of $\mathbb{R}^3$ consisting of $n$ disjoint piecewise linear simple closed curves. A knot is a link with one component.

# Core Definition
"A link $L$ of $n$ components is a subset of $\mathbb{R}^3 \subset \mathbb{R}^3 \cup \{\infty\} = S^3$, consisting of $n$ disjoint piecewise linear simple closed curves" (Bollobás, p. 363). Links may be oriented or unoriented.

# Prerequisites
This is a foundational concept for Section X.6.

# Key Properties
1. A link has $n \geq 1$ components (disjoint closed curves)
2. May be oriented or unoriented
3. Equivalence: ambient isotopy (orientation-preserving homeomorphism of $\mathbb{R}^3$)
4. A trivial invariant: the number of components

# Examples
**Example** (Fig. X.3, p. 363): The Hopf link (two linked circles) and the Borromean rings (three linked circles, no two of which are linked).

# Relationships
## Related
- **knot** — A link with one component
- **link-diagram** — Projection to $\mathbb{R}^2$

## Contrasts With
- **knot** — A knot has exactly one component

# Source Reference
Chapter X, Section X.6, page 363.

# Verification Notes
- Definition source: Direct from p. 363
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
