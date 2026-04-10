---
concept: Stable Matching in List Colouring
slug: stable-matching-in-list-colouring
category: list-coloring
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 172
section: "V.4 List Colouring"
extraction_confidence: medium
aliases:
  - "total function"
  - "preference assignment"
prerequisites:
  - list-chromatic-index
extends: []
related:
  - galvins-theorem
contrasts_with: []
answers_questions:
  - "How are stable matchings used in list edge colouring?"
---

# Quick Definition
In the proof of Galvin's theorem, stable matchings from Section III.5 are used with preference assignments and total functions to inductively prove that bipartite graphs are (t_G + 1)-choosable for edge colouring.

# Core Definition
For a bipartite graph G with preference assignment, the **total function** t_G(e) for edge e = aA is the sum of the number of vertices a prefers to A and the number A prefers to a. **Theorem 13** (Bollobás, p. 173): G is (t_G + 1)-choosable. The proof: find a stable matching M for colour i (by Theorem III.15), colour M with i, then apply induction since removing M reduces total function values.

# Prerequisites
- **List-chromatic index** — the property being established

# Key Properties
1. Every bipartite graph has a stable matching for any preference assignment
2. Stable matching removal reduces the total function by at least 1 on remaining edges
3. This drives the inductive proof of Theorem 13
4. Galvin defines preferences from an edge colouring to get t_G ≤ k − 1

# Relationships
## Enables
- **Galvin's theorem** — key technique

# Source Reference
Chapter V: Colouring, Section V.4, pages 172–174.

# Verification Notes
- Definition source: Synthesized from pp. 172–174
- Confidence rationale: Medium — relies on Chapter III material
- Uncertainties: Full theory in Chapter III
- Cross-reference status: Verified
