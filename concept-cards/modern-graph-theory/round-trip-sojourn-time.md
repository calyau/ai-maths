---
concept: Round-Trip Sojourn Time
slug: round-trip-sojourn-time
category: random-walks
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 316
section: "IX.3 Hitting Times and Commute Times"
extraction_confidence: high
aliases:
  - "S_x(s <-> t)"
prerequisites:
  - sojourn-time
  - effective-resistance
extends:
  - sojourn-time
related:
  - commute-time
  - fosters-theorem
contrasts_with: []
answers_questions:
  - "How do electrical networks relate to random walks on graphs?"
---

# Quick Definition
The expected round-trip sojourn time $S_{xy}(s \leftrightarrow t)$ at edge $xy$ during a round trip from $s$ to $t$ and back equals $R_{\text{eff}}(s,t)$ for every edge $xy$ (Theorem 20).

# Core Definition
Theorem 20 (p. 316): "For a connected graph $G$, vertices $s \neq t$, and edge $xy \in E(G)$, $R_{\text{eff}}(s,t) = S_{xy}(s \leftrightarrow t)$." Since there are $2m$ directed edges, $C(s,t) = \sum 2m \cdot R_{\text{eff}}(s,t)$ gives another proof of $C(s,t) = 2m R_{\text{eff}}(s,t)$.

# Prerequisites
- **Sojourn time** — One-way sojourn generalized to round trips
- **Effective resistance** — Equals the round-trip sojourn time per edge

# Key Properties
1. $S_{xy}(s \leftrightarrow t) = R_{\text{eff}}(s,t)$ for every directed edge $xy$
2. Follows from the superposition principle: $V_z(s \to t) + V_z(t \to s) = R_{\text{eff}}(s,t)$
3. Gives an alternative proof of $C(s,t) = 2m R_{\text{eff}}(s,t)$

# Relationships
## Builds Upon
- **sojourn-time**, **effective-resistance**

## Enables
- **fosters-theorem** — Second proof uses this result

# Source Reference
Chapter IX, Section IX.3, Theorem 20, pages 316-317.

# Verification Notes
- Definition source: Direct from Theorem 20
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
