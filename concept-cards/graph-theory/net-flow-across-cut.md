---
concept: Net Flow Across a Cut
slug: net-flow-across-cut
category: network-flows
subcategory: algebraic-flows
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 150
section: "6.1 Circulations"
extraction_confidence: high
aliases:
  - "Proposition 6.1.1"
prerequisites:
  - circulation
  - cut-in-network
related:
  - total-flow-value
answers_questions:
  - "What is the net flow across a cut in a circulation?"
---

# Quick Definition
In a circulation, the net flow across any cut is zero: f(X, X-bar) = 0 for every vertex subset X (Proposition 6.1.1).

# Core Definition
**Proposition 6.1.1**: If f is a circulation, then f(X, X-bar) = 0 for every set X subset of V. Proof: f(X, X-bar) = f(X, V) - f(X, X) = 0 - 0 = 0, using (F2) and (F1) respectively.

Consequence: circulations are zero on bridges (Corollary 6.1.2), since a bridge forms a cut by itself. (Diestel, p. 141)

# Prerequisites
- **Circulation** — The proposition characterizes circulations
- **Cut in network** — The cut (X, X-bar) is the partition being considered

# Key Properties
1. Fundamental property of circulations
2. For network flows (not circulations): f(S, S-bar) = |f| for cuts (S, S-bar) separating s from t
3. Implies circulations are zero on bridges

# Source Reference
Chapter 6, Section 6.1, Proposition 6.1.1, page 141 (pdf page 151).

# Verification Notes
- Confidence: HIGH — proposition with proof
