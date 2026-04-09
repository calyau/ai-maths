---
concept: Threshold for Complete Graphs
slug: threshold-for-cliques
category: random-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Random Graphs"
chapter_number: 11
pdf_page: 322
section: "11.4 Threshold functions and second moments"
extraction_confidence: high
aliases: []
prerequisites: []
extends: []
related: []
contrasts_with: []
answers_questions:
  - "What is Threshold for Complete Graphs?"
---

# Quick Definition
t(n) = n^{-2/(k-1)} is a threshold for containing K^k. K^k is balanced because epsilon(K^i) < epsilon(K^k) for i < k.

# Core Definition
**Corollary 11.4.6**: If k >= 2, then t(n) = n^{-2/(k-1)} is a threshold for containing K^k. Proof: K^k is balanced since epsilon(K^i) = (i-1)/2 < (k-1)/2 = epsilon(K^k) for i < k (Diestel, p. 322).

# Source Reference
Chapter 11, Section 11.4 Threshold functions and second moments, page 322.

# Verification Notes
- Extracted from source
- Confidence: HIGH
