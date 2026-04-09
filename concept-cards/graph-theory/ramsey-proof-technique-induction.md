---
concept: Ramsey Proof by Iterated Halving
slug: ramsey-proof-technique-induction
category: ramsey-theory
subcategory: classical-ramsey
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 262
section: "9.1 Ramsey's original theorems"
extraction_confidence: high
aliases:
  - "vertex-selection strategy"
prerequisites:
  - ramsey-theorem-finite
related:
  - ramsey-number
  - erdos-szekeres-bound
answers_questions:
  - "How does the halving technique prove Ramsey's theorem?"
---

# Quick Definition
The proof of Ramsey's theorem selects vertices v_1, v_2, ... from shrinking sets V_1, V_2, ..., where each V_i is at least half of V_{i-1} (the half either all-adjacent or all-non-adjacent to v_{i-1}). After 2r-3 steps, pigeonhole gives r-1 vertices of the same type.

# Core Definition
Starting with |V_1| = 2^{2r-3}, at each step i:
1. Pick v_i in V_i
2. Split V_i \ {v_i} into those adjacent and non-adjacent to v_i
3. Choose the larger half as V_{i+1} (size >= 2^{2r-2-i})

After 2r-3 steps, we have vertices v_1, ..., v_{2r-3}. Each shows "adjacent to all of V_{i+1}" or "non-adjacent to all." By pigeonhole among 2r-3 vertices with 2 types, r-1 share the same type. These r-1 plus v_{2r-2} form K^r or K-bar^r. (Diestel, pp. 252-253)

# Prerequisites
- **Ramsey's theorem (finite)** — This is the proof technique

# Key Properties
1. Each step halves the set size
2. After 2r-3 steps: log_2(2^{2r-3}) = 2r-3 halvings possible
3. Pigeonhole principle applied to the 2r-3 adjacency types
4. Gives the bound R(r) <= 2^{2r-3}

# Source Reference
Chapter 9, Section 9.1, proof of Theorem 9.1.1, pages 252-253 (pdf pages 262-263).

# Verification Notes
- Confidence: HIGH — complete proof details
