---
concept: "Petersen's Theorem (1-Factor)"
slug: petersens-theorem-1-factor
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 50
section: "2.2 Matching in general graphs"
extraction_confidence: high
aliases:
  - "Petersen 1891"
  - "bridgeless cubic 1-factor theorem"
prerequisites:
  - tuttes-theorem
  - cubic-graph
  - bridge
extends:
  - tuttes-theorem
related:
  - one-factor
contrasts_with: []
answers_questions:
  - "Does every bridgeless cubic graph have a perfect matching?"
---

# Quick Definition
Every bridgeless cubic graph has a 1-factor (perfect matching).

# Core Definition
**Corollary 2.2.2 (Petersen 1891).** Every bridgeless cubic graph has a 1-factor (Diestel, p. 50).

# Prerequisites
- **Tutte's theorem** — the proof verifies Tutte's condition
- **Cubic graph** — 3-regular graph
- **Bridge** — an edge whose removal disconnects the graph

# Key Properties
1. The graph must be cubic (3-regular) and bridgeless
2. Proof shows Tutte's condition holds: q(G-S) <= |S| for all S
3. Each odd component of G-S sends an odd number of edges to S, hence at least 3 (since no bridge)
4. Total S-to-(G-S) edges: at most 3|S| (cubic) and at least 3q(G-S), giving q(G-S) <= |S|

# Construction / Recognition
## Proof Outline
1. For any S, each odd component C of G-S sends edges to S
2. Since G is cubic, degrees in C sum to an odd number, so an odd number of edges go to S
3. Since G is bridgeless, this odd number is >= 3
4. Total: 3q(G-S) <= total edges between S and G-S <= 3|S|
5. Hence q(G-S) <= |S|, and Tutte's theorem gives a 1-factor

# Context & Application
This result, originally proved by Petersen in 1891, is one of the earliest results in graph theory. It connects the structural property of being bridgeless to the matching-theoretic property of having a 1-factor. Diestel also proves a 2-factor version: every regular graph of positive even degree has a 2-factor (Corollary 2.1.5).

# Examples
**Example**: The Petersen graph itself is a bridgeless cubic graph and indeed has a 1-factor.

# Relationships
## Builds Upon
- **Tutte's theorem** — applied to verify the condition

## Related
- **One-factor** — the theorem guarantees its existence

# Common Errors
- **Error**: Applying the theorem to cubic graphs with bridges
  **Correction**: The bridgeless condition is essential; a cubic graph with a bridge need not have a 1-factor (Exercise 16)

# Common Confusions
- **Confusion**: Confusing this with Petersen's 2-factor theorem (Corollary 2.1.5)
  **Clarification**: Corollary 2.1.5 gives 2-factors in 2k-regular graphs; Corollary 2.2.2 gives 1-factors in bridgeless cubic graphs

# Source Reference
Chapter 2, Section 2.2, Corollary 2.2.2, p. 50 (pdf p. 50).

# Verification Notes
- Statement and proof from p. 50
- Confidence: HIGH — named corollary with short proof
