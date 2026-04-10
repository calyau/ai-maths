---
concept: Three-Vertex Hitting Time Identity
slug: three-vertex-hitting-time-identity
category: random-walks
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 317
section: "IX.3 Hitting Times and Commute Times"
extraction_confidence: high
aliases:
  - "Theorem 23"
  - "tour identity"
prerequisites:
  - mean-hitting-time
extends: []
related:
  - reciprocity-law-random-walks
  - commute-time
contrasts_with: []
answers_questions:
  - "How do I compute hitting times for a random walk?"
---

# Quick Definition
For any three vertices $s, t, u$: $H(s,t) + H(t,u) + H(u,s) = H(s,u) + H(u,t) + H(t,s)$. The expected time for a round-trip $s \to t \to u \to s$ equals the expected time for the reverse trip.

# Core Definition
Theorem 23 (p. 317): "Let $s$, $t$ and $u$ be vertices of a graph $G$. Then $H(s,t) + H(t,u) + H(u,s) = H(s,u) + H(u,t) + H(t,s)$." The proof uses time-reversal: the probability of any closed walk equals the probability of tracing it backwards.

# Prerequisites
- **Mean hitting time** — The quantities in the identity

# Key Properties
1. Tour in one direction has same expected length as tour in reverse
2. Follows from reversibility of the SRW
3. Implies existence of a vertex ordering where $s \prec t$ implies $H(s,t) \leq H(t,s)$

# Relationships
## Builds Upon
- **mean-hitting-time**

## Related
- **reciprocity-law-random-walks** — Both use time-reversal
- **commute-time** — Symmetrized version of hitting time

# Source Reference
Chapter IX, Section IX.3, Theorem 23, pages 317-318.

# Verification Notes
- Definition source: Direct from Theorem 23
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
