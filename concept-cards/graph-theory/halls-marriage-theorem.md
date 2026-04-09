---
concept: "Hall's Marriage Theorem"
slug: halls-marriage-theorem
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 46
section: "2.1 Matching in bipartite graphs"
extraction_confidence: high
aliases:
  - "Hall's theorem"
  - "marriage theorem"
  - "Hall 1935"
prerequisites:
  - matching
  - bipartite-graph
  - marriage-condition
extends:
  - konigs-theorem
related:
  - konigs-theorem
  - one-factor
  - tuttes-theorem
contrasts_with: []
answers_questions:
  - "When does a bipartite graph have a matching of A?"
  - "What is the marriage condition?"
---

# Quick Definition
A bipartite graph G = (A, B; E) contains a matching of A if and only if every subset S of A has at least |S| neighbours in B (the marriage condition).

# Core Definition
**Theorem 2.1.2 (Hall 1935).** A bipartite graph G with bipartition {A, B} contains a matching of A if and only if |N(S)| >= |S| for all S contained in A (Diestel, p. 46).

# Prerequisites
- **Matching** — the theorem characterizes when a complete matching of A exists
- **Bipartite graph** — the setting of the theorem
- **Marriage condition** — the necessary and sufficient condition

# Key Properties
1. The marriage condition |N(S)| >= |S| for all S in A is necessary (obvious) and sufficient (the theorem)
2. Three proofs are given: algorithmic (alternating paths), inductive, and minimality-based
3. Can be derived from Konig's theorem (Exercise 4, p. 51)
4. When |A| = |B|, a matching of A is a 1-factor of G
5. If G is k-regular with k >= 1, the marriage condition is automatically satisfied (Corollary 2.1.3)

# Construction / Recognition
## To Check the Marriage Condition
1. For each subset S of A
2. Compute N(S) = set of all vertices in B adjacent to some vertex in S
3. Verify |N(S)| >= |S|
4. If all subsets pass, the marriage condition holds and a matching of A exists

## To Find the Matching (First Proof Strategy)
1. Start with any matching M
2. If M does not cover all of A, find an unmatched vertex a0 in A
3. Construct an augmenting path using the marriage condition
4. Augment M and repeat

# Context & Application
Despite its seemingly narrow formulation, the marriage theorem counts among the most frequently applied graph theorems, both outside graph theory and within (Diestel, p. 49). The name comes from the interpretation: if A represents a set of people and B a set of potential partners, with edges representing acceptable pairings, the marriage condition ensures everyone in A can be matched.

# Examples
**Example** (p. 46, Fig. 2.1.3): The proof construction shows a maximal alternating sequence a0, b1, a1, b2, a2, ... used to build an augmenting path.

**Example** (Corollary 2.1.3, p. 48): Every k-regular bipartite graph (k >= 1) has a 1-factor, because the marriage condition is satisfied: every set S in A sends k|S| edges to N(S), and these are among the k|N(S)| edges at N(S), so |N(S)| >= |S|.

# Relationships
## Builds Upon
- **Matching**, **bipartite graph**, **marriage condition**

## Enables
- **Corollary 2.1.3** — k-regular bipartite graphs have 1-factors
- **Corollary 2.1.5** — every regular graph of positive even degree has a 2-factor
- **Stable matching** — extends the marriage problem with preferences

## Related
- **Konig's theorem** — Hall's theorem can be derived from it
- **Tutte's theorem** — generalizes to non-bipartite 1-factor existence

# Common Errors
- **Error**: Checking only |N(A)| >= |A| instead of all subsets
  **Correction**: The marriage condition must hold for every subset S of A, not just A itself

# Common Confusions
- **Confusion**: Believing Hall's theorem gives a maximum matching
  **Clarification**: Hall's theorem characterizes when a complete matching of A exists; for maximum matching size in general, use Konig's theorem or the Tutte-Berge formula

# Source Reference
Chapter 2, Section 2.1, Theorem 2.1.2, pp. 46-48 (pdf pp. 46-48). Three proofs given.

# Verification Notes
- Theorem statement from p. 46
- Three proofs from pp. 46-48
- Confidence: HIGH — major named theorem with three full proofs
