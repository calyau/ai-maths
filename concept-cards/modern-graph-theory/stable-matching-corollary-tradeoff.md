---
concept: Stable Matching Trade-Off Corollary
slug: stable-matching-corollary-tradeoff
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
  - "Corollary 19"
prerequisites:
  - stable-matching-equal-cardinality
  - preference-oriented-cycle
extends: []
related:
  - optimal-stable-matching
  - pessimal-stable-matching
contrasts_with: []
answers_questions:
  - "If a vertex has different partners in two stable matchings, who is better off?"
---

# Quick Definition
If $aB \in M$ and $aB \notin M'$ for two stable matchings $M, M'$, then both $a$ and $B$ have mates in $M'$; one is better off in $M'$, the other worse off.

# Core Definition
**Corollary 19**: Let $M$ and $M'$ be stable matchings with some assignment of preferences. If $aB \in M$ and $aB \notin M'$, then in $M'$ both $a$ and $B$ have mates; also, one of $a$ and $B$ is better off in $M'$ than in $M$, and the other is worse off (Bollobás, p. 98).

# Prerequisites
- **Equal cardinality of stable matchings** — All match same vertices
- **Preference-oriented cycle** — Structural basis

# Key Properties
1. Both vertices remain matched in any stable matching
2. The trade-off is strict: one improves, the other worsens
3. Implies the $V_1$-optimal = $V_2$-pessimal result

# Context & Application
This corollary explains why stable matchings form a lattice where improving one side hurts the other.

# Examples
**Example** (p. 98): In a preference-oriented cycle from Lemma 17, preferences alternate, so partners trade off around the cycle.

# Relationships
## Builds Upon
- **preference-oriented-cycle** — Structural lemma

## Enables
- **pessimal-stable-matching** — $V_1$-optimal is $V_2$-pessimal

# Source Reference
Chapter III, Section III.5, page 98. Corollary 19.

# Verification Notes
- Definition source: Direct from p. 98
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
