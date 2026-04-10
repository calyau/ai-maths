---
concept: 2-Edge-Connected Cubic Graph Has 1-Factor
slug: two-edge-connected-cubic-one-factor
category: matchings
subcategory: structural-results
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.4 Tutte's 1-Factor Theorem"
extraction_confidence: high
aliases: []
prerequisites:
  - tuttes-1-factor-theorem
extends: []
related:
  - thomasons-theorem
contrasts_with: []
answers_questions:
  - "Does every 2-edge-connected cubic graph have a perfect matching?"
---

# Quick Definition
Every 2-edge-connected cubic graph has a 1-factor (perfect matching). This follows from Tutte's theorem.

# Core Definition
Tutte's theorem implies that every 2-edge-connected cubic graph has a 1-factor (Exercise 32). This is a consequence of the Tutte condition $q(G-S) \le |S|$ being automatically satisfied for such graphs (Bollobás, p. 93).

# Prerequisites
- **Tutte's 1-factor theorem** — The general characterization

# Key Properties
1. Cubic = every vertex has degree 3
2. 2-edge-connected = no bridges
3. The Tutte condition can be verified by analyzing odd components of $G-S$

# Context & Application
This is one of the "numerous beautiful consequences" of Tutte's theorem (p. 93). It connects to Thomason's result about Hamilton cycles in cubic graphs.

# Examples
**Example**: The Petersen graph is 3-regular and 3-connected; it has 1-factors.

# Relationships
## Builds Upon
- **tuttes-1-factor-theorem** — Direct consequence

## Related
- **thomasons-theorem** — Hamilton cycles in cubic graphs

# Source Reference
Chapter III, Section III.4, page 93. Exercise 32.

# Verification Notes
- Definition source: Stated as consequence on p. 93
- Confidence rationale: Explicitly noted
- Uncertainties: Full proof is Exercise 32
- Cross-reference status: Verified
