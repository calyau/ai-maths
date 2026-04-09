---
concept: "Wagner's Theorem (K^5 Minors)"
slug: wagner-theorem
category: extremal-graph-theory
subcategory: minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 184
section: "7.3 Hadwiger's conjecture"
extraction_confidence: high
aliases:
  - "Theorem 7.3.4"
  - "Wagner graph"
prerequisites:
  - hadwiger-conjecture
related:
  - four-colour-theorem
answers_questions:
  - "What do graphs without a K^5 minor look like?"
---

# Quick Definition
Every edge-maximal graph without a K^5 minor can be constructed recursively, by pasting along triangles and K^2s, from plane triangulations and copies of the Wagner graph W.

# Core Definition
**Theorem 7.3.4** (Wagner 1937): Let G be an edge-maximal graph without a K^5 minor. If |G| >= 4 then G can be constructed recursively, by pasting along triangles and K^2s, from plane triangulations and copies of the graph W (the Wagner graph, also known as the Mobius-Kantor graph M_8). (Diestel, p. 175)

**Corollary 7.3.5**: A graph with n vertices and no K^5 minor has at most 3n - 6 edges.
**Corollary 7.3.6**: Hadwiger's conjecture holds for r = 5 (since chi(W) = 3 and the four colour theorem handles plane triangulations).

# Prerequisites
- **Hadwiger's conjecture** — Wagner's theorem implies Hadwiger for r = 5

# Key Properties
1. Structural decomposition of K^5-minor-free graphs
2. Building blocks: plane triangulations and the Wagner graph W
3. W has chi(W) = 3, so the 4CT suffices for 4-colourability
4. Extremal: at most 3n-6 edges without K^5 minor

# Relationships
## Enables
- Hadwiger's conjecture for r = 5

## Related
- **Four colour theorem** — Needed to complete the proof for r = 5

# Source Reference
Chapter 7, Section 7.3, Theorem 7.3.4, page 175 (pdf page 184). See Fig. 7.3.1.

# Verification Notes
- Confidence: HIGH — stated without proof but with clear implications
