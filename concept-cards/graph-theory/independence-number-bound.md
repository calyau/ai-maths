---
concept: Independence Number Bound
slug: independence-number-bound
category: random-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Random Graphs"
chapter_number: 11
pdf_page: 306
section: "11.1 The notion of a random graph"
extraction_confidence: high
aliases: []
prerequisites: []
extends: []
related: []
contrasts_with: []
answers_questions:
  - "What is Independence Number Bound?"
---

# Quick Definition
The probability that G(n,p) has an independent set of size k is at most C(n,k) * q^{C(k,2)} (Lemma 11.1.2). This gives lower bounds for Ramsey numbers.

# Core Definition
**Lemma 11.1.2**: For all n, k with n >= k >= 2, P[alpha(G) >= k] <= C(n,k) * q^{C(k,2)} for G in G(n,p). Similarly P[omega(G) >= k] <= C(n,k) * p^{C(k,2)} (Diestel, p. 306).

# Source Reference
Chapter 11, Section 11.1 The notion of a random graph, page 306.

# Verification Notes
- Extracted from source
- Confidence: HIGH
