---
concept: Equal Cardinality of Stable Matchings
slug: stable-matching-equal-cardinality
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
  - "Theorem 18"
prerequisites:
  - stable-matching
  - preference-oriented-cycle
extends:
  - stable-matching-existence
related:
  - optimal-stable-matching
contrasts_with: []
answers_questions:
  - "Do all stable matchings match the same vertices?"
---

# Quick Definition
All stable matchings in a bipartite graph with given preferences have the same cardinality and match exactly the same set of vertices.

# Core Definition
**Theorem 18**: For every assignment of preferences in a bipartite graph with bipartition $(V_1, V_2)$, there are subsets $U_1 \subset V_1$ and $U_2 \subset V_2$ such that every stable matching is a complete matching from $U_1$ to $U_2$. In particular, all stable matchings have the same cardinality (Bollobás, p. 97).

# Prerequisites
- **Stable matching** — The objects being compared
- **Preference-oriented cycle** — Used via Lemma 17

# Key Properties
1. The matched vertex set is the same for all stable matchings
2. Any unmatched vertex in one stable matching is unmatched in all
3. Follows from Lemma 17: components of the symmetric difference of two stable matchings are preference-oriented cycles

# Construction / Recognition
1. Find any stable matching $M$
2. The set of matched vertices is fixed for all stable matchings

# Context & Application
This surprising result means stability determines which vertices get matched, regardless of which stable matching is chosen. Only the specific pairings vary.

# Examples
**Example** (p. 97): If $aA \in M$ but $a$ is not matched in $M'$, then some $bA \in M'$, creating a path component (not a cycle) in $M \cup M'$, contradicting Lemma 17.

# Relationships
## Builds Upon
- **stable-matching-existence** — There exist stable matchings to compare
- **preference-oriented-cycle** — Key structural lemma

## Enables
- **optimal-stable-matching** — Since all match the same vertices, optimality is well-defined

# Source Reference
Chapter III, Section III.5, pages 97-98. Theorem 18.

# Verification Notes
- Definition source: Direct theorem statement from p. 97
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
