---
concept: Universe of a Link Diagram
slug: universe-of-link-diagram
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
extends: []
related:
  - alternating-link-diagram
contrasts_with: []
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
The universe of a link diagram is the underlying 4-regular plane graph obtained by forgetting the over/under crossing information. A 4-regular plane graph of $n$ crossings gives rise to $2^n$ link diagrams.

# Core Definition
The universe of a link diagram is a 4-regular plane multigraph where crossing information has been removed. "A 4-regular plane graph of order $n$ gives rise to $2^n$ link diagrams" (Bollobás, p. 365). Every 4-regular plane multigraph is the universe of an alternating link diagram.

# Prerequisites
- **Link diagram** — The universe is obtained by forgetting over/under info

# Key Properties
1. 4-regular plane graph
2. $2^n$ link diagrams from $n$ crossings
3. Always the universe of at least one alternating diagram

# Examples
**Example** (Fig. X.5, p. 365): The universe of a triangle with double edges gives rise to diagrams of both right-handed and left-handed trefoil knots.

# Relationships
## Builds Upon
- **link-diagram**

## Related
- **alternating-link-diagram** — Every universe has an alternating diagram

# Source Reference
Chapter X, Section X.6, page 365. Figure X.5.

# Verification Notes
- Definition source: Direct from p. 365
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
