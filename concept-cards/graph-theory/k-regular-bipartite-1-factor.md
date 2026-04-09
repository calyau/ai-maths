---
concept: k-Regular Bipartite 1-Factor
slug: k-regular-bipartite-1-factor
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 48
section: "2.1 Matching in bipartite graphs"
extraction_confidence: high
aliases:
  - "Corollary 2.1.3"
prerequisites:
  - halls-marriage-theorem
  - regular-graph
  - bipartite-graph
extends:
  - halls-marriage-theorem
related:
  - one-factor
contrasts_with: []
answers_questions:
  - "Does every k-regular bipartite graph have a 1-factor?"
---

# Quick Definition
Every k-regular bipartite graph (k >= 1) has a 1-factor.

# Core Definition
**Corollary 2.1.3.** If G is k-regular with k >= 1, then G has a 1-factor (Diestel, p. 48).

# Prerequisites
- **Hall's marriage theorem** — the proof verifies the marriage condition
- **Regular graph** — all vertices have the same degree k
- **Bipartite graph** — the setting

# Key Properties
1. k-regularity implies |A| = |B| (equal partition sizes)
2. The marriage condition is automatically satisfied: k|S| edges leave S, and at most k|N(S)| edges enter N(S), so |N(S)| >= |S|
3. By Hall's theorem, a matching of A exists, which is a 1-factor since |A| = |B|
4. Foundation for Petersen's 2-factor theorem

# Construction / Recognition
## Proof
1. G is k-regular bipartite, so |A| = |B|
2. For any S in A: S sends k|S| edges to N(S), and N(S) receives at most k|N(S)| edges
3. Hence k|S| <= k|N(S)|, giving |N(S)| >= |S|
4. By Hall's theorem, G has a matching of A, which is a 1-factor

# Context & Application
This simple but powerful corollary is used in the proof of Petersen's 2-factor theorem (Corollary 2.1.5). It shows that regularity in bipartite graphs automatically ensures the existence of a perfect matching.

# Examples
**Example**: K_{3,3} is 3-regular bipartite and has a 1-factor.

# Relationships
## Builds Upon
- **Hall's marriage theorem**, **regular graph**, **bipartite graph**

## Enables
- **Petersen's 2-factor theorem** — uses this corollary

# Source Reference
Chapter 2, Section 2.1, Corollary 2.1.3, p. 48 (pdf p. 48).

# Verification Notes
- From p. 48
- Confidence: HIGH — explicit corollary with short proof
