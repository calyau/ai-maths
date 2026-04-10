---
concept: "Hall's Theorem (Rado's Proof)"
slug: halls-theorem-third-proof
category: matchings
subcategory: proof-techniques
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
  - "third proof of Hall's theorem"
  - "Rado's proof"
prerequisites:
  - halls-theorem
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How is Hall's theorem proved via minimal graphs?"
---

# Quick Definition
Rado's proof shows a minimal graph satisfying Hall's condition must consist of $|V_1|$ independent edges: if two edges share a vertex in $V_2$, deleting either invalidates the condition, leading to a contradiction via inclusion-exclusion.

# Core Definition
Let $G$ be a minimal graph satisfying Hall's condition. If $G$ is not $|V_1|$ independent edges, two edges $a_1x, a_2x$ share a vertex $x \in V_2$. Deleting either invalidates the condition, giving tight sets $A_1, A_2 \subset V_1$. The inclusion-exclusion argument shows $|\Gamma(A_1 \cup A_2)| < |A_1 \cup A_2|$, contradicting the condition (Bollobás, pp. 86-87).

# Prerequisites
- **Hall's theorem** — The theorem being proved

# Key Properties
1. Minimality argument: if Hall's condition holds in a minimal graph, the graph must be a matching
2. Uses set intersection/union arguments
3. Shortest proof of the three given

# Context & Application
Rado's proof is the most elegant: it reduces the problem to showing the minimal satisfying graph is the desired matching.

# Examples
**Example** (pp. 86-87): Sets $A_1, A_2$ with $|\Gamma(A_i)| = |A_i|$ and $a_i$ the only vertex of $A_i$ adjacent to $x$ satisfy $|\Gamma(A_1) \cap \Gamma(A_2)| \ge |\Gamma(A_1 \cap A_2)| + 1$, giving the contradiction.

# Relationships
## Builds Upon
- **halls-theorem** — Alternative proof

# Source Reference
Chapter III, Section III.3, pages 86-87.

# Verification Notes
- Definition source: Synthesized from proof
- Confidence rationale: Complete proof given
- Uncertainties: None
- Cross-reference status: Verified
