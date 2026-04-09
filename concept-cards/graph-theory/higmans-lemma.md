---
concept: "Higman's Lemma"
slug: higmans-lemma
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 326
section: "12.1 Well-quasi-ordering"
extraction_confidence: high
aliases:
  - "Lemma 12.1.3"
prerequisites:
  - well-quasi-ordering
extends: []
related:
  - kruskals-tree-theorem
  - graph-minor-theorem
contrasts_with: []
answers_questions:
  - "Does WQO transfer to finite subsets?"
---

# Quick Definition
Higman's lemma states that if X is well-quasi-ordered by <=, then the set [X]^{<omega} of all finite subsets of X is also well-quasi-ordered, where A <= B iff there is an injective map f: A -> B with a <= f(a) for all a.

# Core Definition
**Lemma 12.1.3**: If X is well-quasi-ordered by <=, then so is [X]^{<omega}, the set of all finite subsets of X, under the ordering A <= B iff there is an injective mapping f: A -> B such that a <= f(a) for all a in A (Diestel, pp. 326-328).

# Prerequisites
- **Well-quasi-ordering** — The base WQO from which the finite-subsets WQO is derived

# Key Properties
1. The proof uses the "minimal bad sequence" technique
2. From a hypothetical bad sequence (A_n), pick a_n from each A_n and set B_n = A_n \ {a_n}
3. Use the WQO property of X to find an increasing subsequence of the a_n
4. Derive a contradiction from the minimality of the A_n
5. This lemma is fundamental to the proofs of Kruskal's theorem and the graph minor theorem

# Context & Application
Higman's lemma is a cornerstone of WQO theory. Its proof technique (minimal bad sequences) is reused in the proofs of Kruskal's tree theorem and the graph minor theorem.

# Relationships
## Enables
- **Kruskal's tree theorem** — Uses Higman's lemma in its proof
- **Graph minor theorem** — Builds on the same technique

# Source Reference
Chapter 12, Section 12.1, pages 326-328 (Lemma 12.1.3).

# Verification Notes
- Statement and proof from pp. 326-328
- Confidence: HIGH — named lemma with full proof
