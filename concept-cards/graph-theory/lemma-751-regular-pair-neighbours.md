---
concept: Regular Pair Neighbourhood Lemma
slug: lemma-751-regular-pair-neighbours
category: extremal-graph-theory
subcategory: regularity
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 194
section: "7.5 Applying the regularity lemma"
extraction_confidence: high
aliases:
  - "Lemma 7.5.1"
prerequisites:
  - epsilon-regular-pair
  - density-of-pair
related:
  - embedding-lemma
answers_questions:
  - "What can we say about vertex degrees in regular pairs?"
---

# Quick Definition
In an epsilon-regular pair (A, B) of density d, for any Y subset B with |Y| >= epsilon|B|, all but fewer than epsilon|A| vertices in A have at least (d-epsilon)|Y| neighbours in Y.

# Core Definition
**Lemma 7.5.1**: Let (A, B) be an epsilon-regular pair of density d, and let Y subset B have size |Y| >= epsilon|B|. Then all but fewer than epsilon|A| of the vertices in A have (each) at least (d-epsilon)|Y| neighbours in Y.

Proof: If X is the set of vertices with fewer than (d-epsilon)|Y| neighbours, then d(X,Y) < d - epsilon = d(A,B) - epsilon, contradicting epsilon-regularity since |Y| >= epsilon|B|. (Diestel, p. 184)

# Prerequisites
- **Epsilon-regular pair** — The lemma applies to regular pairs
- **Density of pair** — Density d appears in the bound

# Key Properties
1. Most vertices have about d|Y| neighbours in large subsets Y
2. At most epsilon|A| "bad" vertices exist
3. The key technical tool for the embedding lemma proof

# Relationships
## Enables
- **Embedding lemma** — Uses this to maintain large target sets during embedding

# Source Reference
Chapter 7, Section 7.5, Lemma 7.5.1, page 184 (pdf page 194).

# Verification Notes
- Confidence: HIGH — lemma with proof
