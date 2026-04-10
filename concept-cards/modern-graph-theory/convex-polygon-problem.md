---
concept: Convex Polygon Problem (Happy Ending Problem)
slug: convex-polygon-problem
category: ramsey-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 192
section: "VI.1 The Fundamental Ramsey Theorems"
extraction_confidence: high
aliases:
  - "Erdős-Szekeres conjecture"
  - "happy ending problem"
prerequisites:
  - erdos-szekeres-cups-and-caps
extends: []
related:
  - ramsey-theorem-finite
contrasts_with: []
answers_questions:
  - "How many points in general position guarantee a convex k-gon?"
---

# Quick Definition
Every set of C(2k−4, k−2) + 1 points in general position contains the vertices of a convex k-gon. The Erdős-Szekeres conjecture states that 2^{k−2} + 1 points suffice.

# Core Definition
As a consequence of Theorem 3 (cups and caps), every set of C(2k−4, k−2) + 1 points in the plane in general position contains the vertices of a convex k-gon. Erdős and Szekeres conjectured (1935) that 2^{k−2} + 1 points suffice. If true, this is best possible (Bollobás, p. 192, Exercise 23).

# Prerequisites
- **Erdős-Szekeres cups and caps** — the theorem from which this follows

# Key Properties
1. Upper bound: C(2k−4, k−2) + 1 points guarantee a convex k-gon
2. Conjecture: 2^{k−2} + 1 points suffice (known to be best possible if true)
3. Known as the "happy ending problem" (led to the marriage of Erdős's friends)

# Context & Application
This is one of the most famous open problems in combinatorial geometry, connecting Ramsey theory to geometric convexity.

# Relationships
## Builds Upon
- **Erdős-Szekeres theorem** — provides the upper bound

# Source Reference
Chapter VI: Ramsey Theory, Section VI.1, page 192.

# Verification Notes
- Definition source: Direct from p. 192
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
