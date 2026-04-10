---
concept: Edge Traversal Time
slug: edge-traversal-time
category: random-walks
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 313
section: "IX.3 Hitting Times and Commute Times"
extraction_confidence: high
aliases: []
prerequisites:
  - simple-random-walk
  - mean-return-time
extends: []
related:
  - fosters-theorem
contrasts_with: []
answers_questions:
  - "How do I compute hitting times for a random walk?"
---

# Quick Definition
The expected time for the SRW, started at $x$, to return to $x$ through a specific edge $yx$ is exactly $2m$, independent of the graph structure (Theorem 17).

# Core Definition
Theorem 17 (p. 313): "Let $xy$ be a fixed edge of our graph $G$. The expected time it takes for the simple random walk on $G$, started at $x$, to return to $x$ through $yx$ is $2m$."

# Prerequisites
- **Simple random walk** — The walk on which the result applies
- **Mean return time** — $H(x,x) = 2m/d(x)$ is the total return time

# Key Properties
1. Expected return time through a specific edge $yx$ is exactly $2m$
2. Independent of graph structure, edge position, or starting vertex
3. "Loosely speaking, this means that our SRW spends equal amounts of time in each edge, going in either direction" (p. 313)
4. $S_k(uv)/k \to 1/2m$ in probability for any oriented edge $uv$

# Relationships
## Builds Upon
- **simple-random-walk**, **mean-return-time**

## Related
- **fosters-theorem** — Both express universal constants for SRW

# Source Reference
Chapter IX, Section IX.3, Theorem 17, page 313.

# Verification Notes
- Definition source: Direct from Theorem 17
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
