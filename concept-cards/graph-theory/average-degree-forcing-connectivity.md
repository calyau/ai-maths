---
concept: Average Degree Forcing Connectivity
slug: average-degree-forcing-connectivity
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 80
section: "3.5 Linking pairs of vertices"
extraction_confidence: high
aliases: []
prerequisites:
  - k-connected-graph
  - topological-minor
extends: []
related:
  - linkedness-theorem
  - thomas-wollan-theorem
contrasts_with: []
answers_questions:
  - "How does average degree force topological minors?"
---

# Quick Definition
There is a function h(r) such that every graph of average degree at least h(r) contains K^r as a topological minor.

# Core Definition
**Lemma 3.5.1.** There is a function h: N -> N such that every graph of average degree at least h(r) contains K^r as a topological minor, for every r in N (Diestel, p. 80).

# Prerequisites
- **k-connected graph** — high average degree implies high connectivity
- **Topological minor** — the structure being forced

# Key Properties
1. h(r) = 2^(r choose 2) suffices (exponential)
2. Proof by induction on m = r, ..., (r choose 2)
3. Uses the fact that high average degree implies long cycles
4. Foundation for proving k-linkedness from high connectivity

# Context & Application
This lemma is the bridge between high average degree (or connectivity) and the existence of large complete topological minors. It is used in the proof of Theorem 3.5.2 to find TK^{3k} in a highly connected graph.

# Examples
**Example** (p. 80): For r=3, h(3) = 2^3 = 8 suffices. Any graph with average degree >= 8 contains TK^3 (a subdivision of K3, which is just a cycle of length >= 3).

# Relationships
## Related
- **Linkedness theorem** — uses this lemma
- **Thomas-Wollan theorem** — improved bound

# Source Reference
Chapter 3, Section 3.5, Lemma 3.5.1, p. 80 (pdf p. 80).

# Verification Notes
- Lemma from p. 80
- Confidence: HIGH — explicit lemma with proof
