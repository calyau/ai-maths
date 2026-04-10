---
concept: Nugatory Crossing
slug: nugatory-crossing
category: knot-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 377
section: "X.6 Polynomials of Knots and Links"
extraction_confidence: high
aliases:
  - "isthmus crossing"
prerequisites:
  - link-diagram
extends: []
related:
  - tait-conjecture-crossing-number
  - alternating-link-diagram
contrasts_with: []
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
A nugatory crossing in a link diagram is one where two of the four local regions at the crossing belong to the same global region. It appears as a loop or bridge in the associated signed graph and contributes nothing to the knottedness.

# Core Definition
"A crossing is said to be an isthmus or a nugatory crossing if some two of the local regions appearing at the crossing are parts of the same region in the whole diagram" (Bollobás, p. 377). In $G^+(L)$ and $G^-(L)$, a nugatory crossing corresponds to a loop or bridge.

# Prerequisites
- **Link diagram** — Nugatory crossings are a property of diagrams

# Key Properties
1. Nugatory crossings make no contribution to knottedness
2. Appear as loops or bridges in the associated signed graph
3. Alternating diagrams without nugatory crossings have minimal crossing number (Theorem 22)

# Relationships
## Builds Upon
- **link-diagram**

## Related
- **tait-conjecture-crossing-number** — Applies to diagrams without nugatory crossings
- **alternating-link-diagram** — Combined with alternating property

# Source Reference
Chapter X, Section X.6, page 377. Figure X.16.

# Verification Notes
- Definition source: Direct from p. 377
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
