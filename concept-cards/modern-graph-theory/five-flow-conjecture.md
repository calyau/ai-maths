---
concept: Tutte's Five-Flow Conjecture
slug: five-flow-conjecture
category: tutte-polynomial
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 355
section: "X.4 Special Values of the Tutte Polynomial"
extraction_confidence: high
aliases:
  - "5-flow conjecture"
prerequisites:
  - nowhere-zero-flow
  - flow-polynomial
extends: []
related:
  - chromatic-polynomial-from-tutte
contrasts_with: []
answers_questions:
  - "How does the Tutte polynomial generalize the chromatic and flow polynomials?"
---

# Quick Definition
Tutte conjectured (1954) that every bridgeless graph has a nowhere-zero 5-flow. This is the flow-theoretic dual of the four colour conjecture.

# Core Definition
"Tutte conjectured in 1954 that every bridgeless graph has a nowhere-zero 5-flow" (Bollobás, p. 355). Jaeger (1979) proved every bridgeless graph has a nowhere-zero 8-flow; Seymour later proved nowhere-zero 6-flow. The conjecture remains open.

# Prerequisites
- **Nowhere-zero flow** — The objects in the conjecture
- **Flow polynomial** — Counting tool

# Key Properties
1. Equivalent to $q_G(5) > 0$ for every bridgeless $G$
2. Dual to the four colour theorem for planar graphs
3. Best known result: Seymour's 6-flow theorem
4. Still open as of 1998

# Context & Application
"The four colour theorem is equivalent to the fact that every bridgeless planar graph has a nowhere-zero 4-flow" (p. 355). Tutte's conjecture extends this to all bridgeless graphs with one extra colour/flow value.

# Relationships
## Builds Upon
- **nowhere-zero-flow**, **flow-polynomial**

## Related
- **chromatic-polynomial-from-tutte** — Dual relationship

# Source Reference
Chapter X, Section X.4, page 355.

# Verification Notes
- Definition source: Direct from p. 355
- Confidence rationale: Explicit statement of open conjecture
- Uncertainties: None
- Cross-reference status: Verified
