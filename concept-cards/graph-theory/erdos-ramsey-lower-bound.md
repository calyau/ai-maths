---
concept: "Erdős's Ramsey Lower Bound"
slug: erdos-ramsey-lower-bound
category: random-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Random Graphs"
chapter_number: 11
pdf_page: 307
section: "11.1 The notion of a random graph"
extraction_confidence: high
aliases:
  - "Erdős 1947"
prerequisites:
  - random-graph-gnp
extends: []
related:
  - probabilistic-method
contrasts_with: []
answers_questions:
  - "What is the probabilistic lower bound for Ramsey numbers?"
---

# Quick Definition
Erdős (1947) proved R(k) > 2^{k/2} using the probabilistic method: in G(n, 1/2) with n <= 2^{k/2}, both P[alpha >= k] and P[omega >= k] are less than 1/2.

# Core Definition
**Theorem 11.1.3** (Erdős 1947): For every integer k >= 3, the Ramsey number of k satisfies R(k) > 2^{k/2} (Diestel, p. 307).

# Prerequisites
- **Random graph G(n,p)** — The probability space used

# Key Properties
1. One of the earliest applications of the probabilistic method
2. Uses p = q = 1/2 and Lemma 11.1.2
3. Close to the upper bound of 2^{2k-3} from the direct Ramsey proof

# Source Reference
Chapter 11, Section 11.1, pages 307-308 (Theorem 11.1.3).

# Verification Notes
- Statement and proof from pp. 307-308
- Confidence: HIGH — named theorem with complete proof
