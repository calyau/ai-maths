---
concept: Regularity and Subgraph Finding Theorem
slug: regularity-subgraph-theorem
category: regularity-method
subcategory: applications
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.6 Simple Applications of Szemerédi's Lemma"
extraction_confidence: high
aliases:
  - "Theorem 31"
prerequisites:
  - regularity-application-subgraph-finding
  - epsilon-uniform-pair
extends:
  - regularity-application-subgraph-finding
related:
  - szemeredis-regularity-lemma
contrasts_with: []
answers_questions:
  - "How does regularity guarantee small subgraphs?"
---

# Quick Definition
If $r$ disjoint sets are pairwise $\delta^f$-regular with density at least $\delta + \delta^f$, and each set has $\ge \delta^{-f}$ vertices, then every $r$-partite graph of order $f$ appears as a subgraph.

# Core Definition
**Theorem 31**: Let $f \ge 2$, $r \ge 2$, $0 < \delta < 1/r$, and let $V_1, \ldots, V_r$ be disjoint sets with $|V_i| \ge \delta^{-f}$ for every $i$, with all pairs $(V_i, V_j)$ being $\delta^f$-regular with density at least $\delta + \delta^f$. Then $G$ contains every $r$-partite graph of order $f$ (Bollobás, p. 148).

# Prerequisites
- **Regularity application for subgraph finding** — Theorem 30
- **ε-uniform pair** — The regularity condition

# Key Properties
1. Cleaner formulation than Theorem 30
2. Commonly used in conjunction with Szemerédi partition
3. The density excess $\delta^f$ over regularity parameter ensures subgraph finding

# Context & Application
This is the standard formulation used when applying regularity to find specific subgraphs.

# Examples
**Example** (p. 148): With appropriate $\delta$ derived from the forbidden subgraph $F$, the skeleton of the regularity partition determines which subgraphs exist.

# Relationships
## Builds Upon
- **regularity-application-subgraph-finding** — Reformulation

# Source Reference
Chapter IV, Section IV.6, page 148. Theorem 31.

# Verification Notes
- Definition source: Direct from p. 148
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
