---
concept: Expected Number of k-Cycles
slug: expected-k-cycles
category: random-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Random Graphs"
chapter_number: 11
pdf_page: 308
section: "11.1 The notion of a random graph"
extraction_confidence: high
aliases: []
prerequisites: []
extends: []
related: []
contrasts_with: []
answers_questions:
  - "What is Expected Number of k-Cycles?"
---

# Quick Definition
The expected number of k-cycles in G(n,p) is (n)_k / (2k) * p^k, computed by summing indicator random variables over all k-cycles (Lemma 11.1.5).

# Core Definition
**Lemma 11.1.5**: The expected number of k-cycles in G in G(n,p) is E(X) = (n)_k / (2k) * p^k, where (n)_k = n(n-1)...(n-k+1). The proof uses indicator random variables X_C for each k-cycle C, with E(X_C) = p^k and linearity of expectation (Diestel, p. 308).

# Source Reference
Chapter 11, Section 11.1 The notion of a random graph, page 308.

# Verification Notes
- Extracted from source
- Confidence: HIGH
