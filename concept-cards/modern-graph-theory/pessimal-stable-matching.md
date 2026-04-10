---
concept: Pessimal Stable Matching
slug: pessimal-stable-matching
category: matchings
subcategory: stable-matchings
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.5 Stable Matchings"
extraction_confidence: high
aliases:
  - "V₂-pessimal matching"
  - "worst stable matching"
prerequisites:
  - optimal-stable-matching
  - stable-matching-equal-cardinality
extends: []
related:
  - gale-shapley-algorithm
contrasts_with:
  - optimal-stable-matching
answers_questions:
  - "Is the best matching for one side the worst for the other?"
---

# Quick Definition
The $V_2$-pessimal stable matching gives every girl her worst possible partner across all stable matchings. It is exactly the $V_1$-optimal stable matching.

# Core Definition
A stable matching $M$ is $V_2$-pessimal if no girl is better off in $M$ than in any other stable matching. By Corollary 19, the $V_1$-optimal stable matching is precisely the $V_2$-pessimal stable matching (Bollobás, p. 99).

# Prerequisites
- **Optimal stable matching** — The same matching from the other side
- **Equal cardinality of stable matchings** — All match same vertices

# Key Properties
1. Unique (follows from uniqueness of $V_1$-optimal)
2. Produced by Gale-Shapley with boys proposing
3. Swapping roles (girls propose) gives $V_2$-optimal = $V_1$-pessimal

# Context & Application
Shows the inherent asymmetry of the Gale-Shapley algorithm: the proposing side benefits at the expense of the receiving side.

# Examples
**Example** (p. 99): By Corollary 19, if boy $a$ gets a different partner in two stable matchings, one partner is better for $a$ and the other is better for the partner.

# Relationships
## Contrasts With
- **optimal-stable-matching** — Same matching, viewed from opposite side

# Source Reference
Chapter III, Section III.5, page 99.

# Verification Notes
- Definition source: Direct from p. 99
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
