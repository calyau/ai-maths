---
concept: Deficiency Version of Hall's Theorem
slug: deficiency-version-halls-theorem
category: matchings
subcategory: fundamental-theorems
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.3 Matching"
extraction_confidence: high
aliases:
  - "Corollary 9"
  - "defect form of Hall's theorem"
prerequisites:
  - halls-theorem
extends:
  - halls-theorem
related:
  - konigs-theorem
contrasts_with: []
answers_questions:
  - "What happens when Hall's condition fails?"
---

# Quick Definition
If $|\Gamma(S)| \ge |S| - d$ for every $S \subset V_1$ in a bipartite graph, then $G$ contains $m - d$ independent edges (where $m = |V_1|$).

# Core Definition
**Corollary 9**: Suppose a bipartite graph $G = G_2(m,n)$ with vertex sets $V_1, V_2$ satisfies $|\Gamma(S)| \ge |S| - d$ for every $S \subset V_1$. Then $G$ contains $m - d$ independent edges (Bollobás, p. 87).

# Prerequisites
- **Hall's theorem** — This is the deficiency version

# Key Properties
1. Reduces to Hall's theorem by adding $d$ vertices to $V_2$ joined to all of $V_1$
2. Tells us how close we can get to a complete matching when Hall's condition fails
3. The deficiency $d$ measures the maximum "shortfall" in Hall's condition

# Construction / Recognition
1. Compute $d = \max_{S \subset V_1}(|S| - |\Gamma(S)|)$
2. The maximum matching has size at least $m - d$

# Context & Application
When Hall's condition fails, this tells us exactly how many vertices of $V_1$ we can still match.

# Examples
**Example** (p. 87): Add $d$ vertices to $V_2$ joined to all of $V_1$. The new graph satisfies Hall's condition, and at least $m - d$ matching edges belong to the original graph.

# Relationships
## Builds Upon
- **halls-theorem** — Direct generalization

## Enables
- **konigs-theorem** — Corollary 10

# Source Reference
Chapter III, Section III.3, page 87. Corollary 9.

# Verification Notes
- Definition source: Direct from p. 87
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
