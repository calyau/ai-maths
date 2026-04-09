---
concept: "Dilworth's Theorem"
slug: dilworths-theorem
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 61
section: "2.5 Path covers"
extraction_confidence: high
aliases:
  - "Dilworth 1950"
prerequisites:
  - partially-ordered-set
  - chain
  - antichain
  - gallai-milgram-theorem
extends:
  - gallai-milgram-theorem
related:
  - konigs-theorem
contrasts_with: []
answers_questions:
  - "What is Dilworth's theorem?"
---

# Quick Definition
In every finite partially ordered set, the minimum number of chains needed to cover all elements equals the maximum size of an antichain.

# Core Definition
**Corollary 2.5.2 (Dilworth 1950).** In every finite partially ordered set (P, <=), the minimum number of chains with union P is equal to the maximum cardinality of an antichain in P (Diestel, p. 61).

# Prerequisites
- **Partially ordered set** — the setting of the theorem
- **Chain** — totally ordered subsets that cover P
- **Antichain** — pairwise incomparable elements (the dual measure)
- **Gallai-Milgram theorem** — Dilworth's theorem follows from it

# Key Properties
1. min chain cover = max antichain (a min-max duality)
2. Derived from Gallai-Milgram by considering the directed graph on P with edge set {(x,y) : x < y}
3. Any antichain of maximum size A requires at least |A| chains to cover P (obvious lower bound)
4. The theorem says |A| chains suffice
5. Has a dual: min antichain cover = max chain (Exercise 25)

# Construction / Recognition
## Deriving from Gallai-Milgram
1. Form a directed graph D on P with edges (x,y) whenever x < y
2. A directed path in D corresponds to a chain in (P, <=)
3. An independent set in D corresponds to an antichain in (P, <=)
4. Apply Theorem 2.5.1 to get a path cover with independent representatives
5. The path cover gives chains; the independent set gives an antichain of equal size

# Context & Application
Dilworth's theorem is a classical result in combinatorics and order theory. It is widely applied in scheduling, sorting theory, and combinatorial optimization. The graph-theoretic proof via the Gallai-Milgram theorem is elegant and shows the power of graph-theoretic methods in order theory.

# Examples
**Example**: In the poset of divisors of 12 = {1, 2, 3, 4, 6, 12} ordered by divisibility, the antichain {2, 3} has size 2 (actually {4, 6, 3} has size 3), and the minimum chain cover has the same size.

# Relationships
## Builds Upon
- **Partially ordered set**, **chain**, **antichain**, **Gallai-Milgram theorem**

## Related
- **Konig's theorem** — another min-max duality theorem
- Dual version: min antichain cover = max chain (Exercise 25)

# Common Errors
- **Error**: Applying to infinite partially ordered sets without qualification
  **Correction**: The theorem as stated requires finiteness; infinite counterexamples exist (Exercise 27)

# Common Confusions
- **Confusion**: Confusing Dilworth's theorem with its dual
  **Clarification**: Dilworth: min chain cover = max antichain. Dual (Mirsky): min antichain cover = max chain

# Source Reference
Chapter 2, Section 2.5, Corollary 2.5.2, p. 61 (pdf p. 61).

# Verification Notes
- Statement from p. 61
- Derived from Theorem 2.5.1
- Confidence: HIGH — major named theorem with proof
