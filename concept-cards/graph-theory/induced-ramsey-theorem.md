---
concept: Induced Ramsey Theorem
slug: induced-ramsey-theorem
category: ramsey-theory
subcategory: induced-ramsey
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 268
section: "9.3 Induced Ramsey theorems"
extraction_confidence: high
aliases:
  - "Theorem 9.3.1"
  - "Nesetril-Rodl theorem"
prerequisites:
  - ramsey-graph
  - ramsey-theorem-finite
  - ramsey-theorem-general
related:
  - bipartite-ramsey-lemma
answers_questions:
  - "Does every graph have a Ramsey graph?"
---

# Quick Definition
Every graph H has a Ramsey graph G: a graph such that every 2-colouring of E(G) yields a monochromatic induced copy of H. Moreover, G can be chosen with omega(G) = omega(H).

# Core Definition
**Theorem 9.3.1** (Deuber, Erdos-Hajnal-Posa, Rodl, independently ~1973): Every graph has a Ramsey graph. That is, for every graph H there exists a graph G such that, for every partition {E_1, E_2} of E(G), G has an induced subgraph isomorphic to H with E(H) subset E_1 or E(H) subset E_2.

Two proofs are given:
1. **First proof** (Deuber-style): Inductive construction using vertex replacement G[U -> H], building graphs G^0, ..., G^n.
2. **Second proof** (Nesetril-Rodl): Constructive, preserving the clique number omega(G) = omega(H). Uses bipartite Ramsey graphs (Lemma 9.3.3) applied iteratively. (Diestel, pp. 259-268)

# Prerequisites
- **Ramsey graph** — The theorem proves these exist
- **Ramsey's theorem (finite)** — Used in both proofs
- **Ramsey theorem (general)** — The general version is used for the bipartite construction

# Key Properties
1. One of the fundamental results of graph Ramsey theory
2. The first proof uses vertex-replacement G[U -> H]
3. The second proof preserves clique number: omega(G) = omega(H)
4. The bipartite case (Lemma 9.3.3) is a key ingredient
5. Proved independently by three groups around 1973

# Context & Application
The induced Ramsey theorem "changes the character of the problem dramatically" compared to classical Ramsey theory. What is needed is a careful CONSTRUCTION of G, not just a proof that G is "big enough." The two very different proofs each showcase distinctive Ramsey-theoretic techniques.

# Relationships
## Builds Upon
- **Ramsey graph**, **Ramsey's theorem**

## Related
- **Bipartite Ramsey lemma** (Lemma 9.3.3) — Every bipartite graph has a bipartite Ramsey graph

# Source Reference
Chapter 9, Section 9.3, Theorem 9.3.1, pages 259-268 (pdf pages 268-278). Two complete proofs.

# Verification Notes
- Confidence: HIGH — two complete proofs given
