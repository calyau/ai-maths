---
concept: Three-Colouring of a Link Diagram
slug: three-colouring-of-link
category: knot-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 366
section: "X.6 Polynomials of Knots and Links"
extraction_confidence: high
aliases:
  - "proper 3-colouring of strands"
  - "Fox colouring"
prerequisites:
  - link-diagram
extends: []
related:
  - ambient-isotopy
  - knot
contrasts_with: []
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
A proper 3-colouring of a link diagram colours each strand (arc from one undercrossing to the next) with one of 3 colours such that at no crossing are exactly two colours present. A non-trivial such colouring (using at least two colours) is an ambient isotopy invariant.

# Core Definition
"Call a 3-colouring of the strands of a diagram proper if at no crossing do we find precisely two colours. A 3-colouring is non-trivial if at least two colours are used" (Bollobás, p. 366). The existence of a non-trivial proper 3-colouring is preserved by all three Reidemeister moves.

# Prerequisites
- **Link diagram** — 3-colourings are defined on link diagrams

# Key Properties
1. At each crossing: either all three colours appear, or only one colour
2. Non-trivial: at least two colours are used
3. Ambient isotopy invariant
4. The unknot has no non-trivial proper 3-colouring
5. Can be generalized to mod $p$ labellings (Exercise 32)

# Context & Application
"The unknot does not have a non-trivial proper 3-colouring, and therefore a knot whose diagram has a non-trivial proper 3-colouring is not equivalent to the unknot" (p. 366). This provides a simple combinatorial test for knottedness.

# Examples
**Example** (Fig. X.7, p. 366): A non-trivial proper 3-colouring of knot $8_{15}$.

**Example** (p. 366): The trefoil knot has a non-trivial proper 3-colouring, proving it is knotted.

# Relationships
## Builds Upon
- **link-diagram**

## Related
- **ambient-isotopy** — 3-colouring count is invariant
- **knot** — Used to prove knots are non-trivial

# Source Reference
Chapter X, Section X.6, pages 366-367. Figure X.7.

# Verification Notes
- Definition source: Direct from p. 366
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
