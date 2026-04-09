---
concept: "Szemer\u00E9di's Regularity Lemma"
slug: regularity-lemma
category: extremal-graph-theory
subcategory: regularity
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 186
section: "7.4 Szemeredi's regularity lemma"
extraction_confidence: high
aliases:
  - "Szemeredi regularity lemma"
  - "uniformity lemma"
  - "Lemma 7.4.1"
prerequisites:
  - epsilon-regular-partition
  - epsilon-regular-pair
  - density-of-pair
related:
  - regularity-graph
  - embedding-lemma
  - erdos-stone-theorem
answers_questions:
  - "How do I apply Szemeredi's regularity lemma?"
  - "What must I know before understanding the regularity lemma?"
---

# Quick Definition
For every epsilon > 0 and every integer m >= 1, there exists an integer M such that every graph of order at least m admits an epsilon-regular partition with between m and M non-exceptional parts.

# Core Definition
**Lemma 7.4.1** (Regularity Lemma): For every epsilon > 0 and every integer m >= 1 there exists an integer M such that every graph of order at least m admits an epsilon-regular partition {V_0, V_1, ..., V_k} with m <= k <= M. (Diestel, p. 177)

The proof uses an energy argument: define the index q(P) of a partition P as a measure of non-uniformity (bounded by 1). If a partition is not epsilon-regular, refining irregular pairs increases q by at least epsilon^5/2. Since q <= 1, this can happen at most 2/epsilon^5 times. Starting from m parts and refining up to s times yields the bound M.

# Prerequisites
- **Epsilon-regular partition** — The lemma guarantees these exist
- **Epsilon-regular pair** — The building blocks of regular partitions
- **Density of pair** — The density concept underlying regularity

# Key Properties
1. The bound M depends only on epsilon and m, not on the graph
2. For large graphs, partition sets are large (since k <= M is bounded)
3. The lemma is designed for DENSE graphs; for sparse graphs it becomes trivial
4. The lower bound m on partition size can be used to ensure most edges are between parts
5. The proof is iterative: refine until regular, using an energy increment argument
6. M grows extremely fast (tower-type) as a function of epsilon

# Construction / Recognition
## Outline of the Proof
1. Start with any partition of V into m equal parts (plus small exceptional set)
2. Compute the index q(P) = sum of q(C_i, C_j) measuring density variation
3. If the partition is not epsilon-regular, there are > epsilon*k^2 irregular pairs
4. Refine: split irregular pairs (A, B) into (A_1, A_2), (B_1, B_2) witnessing irregularity
5. This increases q by >= epsilon^5/2 (Lemma 7.4.4)
6. Since q <= 1, at most s = 2/epsilon^5 refinements are possible
7. The resulting partition has at most M = max{f^s(k), 2k/epsilon} parts

# Context & Application
The regularity lemma is one of the most powerful tools in modern combinatorics. Diestel calls it "a graph theoretical tool whose fundamental importance has been realized more and more in recent years." It says every graph can be partitioned into a bounded number of pieces so that edges between most pairs are distributed uniformly—as if generated at random.

Applications include:
- Proof of the Erdos-Stone theorem (Section 7.5)
- Proof of Theorem 9.2.2 (Ramsey numbers of bounded-degree graphs)
- Triangle removal lemma and connections to additive combinatorics

# Examples
**Example** (p. 177): The regularity lemma provides the partition used in the proof of the Erdos-Stone theorem, where a dense enough regularity graph R contains K^r by Turan's theorem.

# Relationships
## Builds Upon
- **Epsilon-regular partition**, **Epsilon-regular pair**, **Density of pair**

## Enables
- **Regularity graph** — Constructed from a regular partition
- **Embedding lemma** — Uses regular partitions to embed subgraphs
- **Erdos-Stone theorem** — Proved using the regularity lemma (Section 7.5)

# Common Errors
- **Error**: Applying the regularity lemma to sparse graphs expecting useful results
  **Correction**: For sparse graphs, all pair densities tend to 0, making the lemma trivial and useless

# Common Confusions
- **Confusion**: Thinking the regularity lemma says all pairs are regular
  **Clarification**: Up to epsilon*k^2 pairs may be irregular; the lemma controls the fraction of irregular pairs

# Source Reference
Chapter 7, Section 7.4, Lemma 7.4.1, pages 177-183 (pdf pages 186-192). Full proof given.

# Verification Notes
- Statement: Directly from p. 177
- Proof: Detailed energy-increment argument across Lemmas 7.4.2-7.4.4
- Confidence: HIGH — central result of the section with complete proof
