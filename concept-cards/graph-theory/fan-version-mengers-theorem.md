---
concept: Fan Version of Menger's Theorem
slug: fan-version-mengers-theorem
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 76
section: "3.3 Menger's theorem"
extraction_confidence: high
aliases:
  - "fan lemma"
  - "Menger fan version"
prerequisites:
  - mengers-theorem
  - fan
extends:
  - mengers-theorem
related:
  - k-connected-characterization
contrasts_with: []
answers_questions:
  - "What is the fan version of Menger's theorem?"
---

# Quick Definition
For a vertex a and set B, the minimum number of vertices (other than a) separating a from B equals the maximum number of paths forming an a-B fan.

# Core Definition
**Corollary 3.3.4.** For B contained in V and a in V \ B, the minimum number of vertices != a separating a from B in G is equal to the maximum number of paths forming an a-B fan in G (Diestel, p. 76).

A set of a-B paths is an **a-B fan** if any two of the paths have only a in common.

# Prerequisites
- **Menger's theorem** — the fan version is a corollary
- **Fan** — the structure being counted

# Key Properties
1. An a-B fan consists of paths from a to B, pairwise sharing only the vertex a
2. Derived by applying Theorem 3.3.1 with A := N(a)
3. Used in the proof of Proposition 10.1.2 (Hamiltonicity)
4. A k-connected graph has a fan of size min{k, |B|} from any vertex to any set B

# Construction / Recognition
## Derivation
1. Set A := N(a), the neighbourhood of a
2. Apply Menger's theorem to find k disjoint A-B paths
3. Extend each path by prepending the edge from a to its start in N(a)
4. The result is an a-B fan

# Context & Application
The fan version is particularly useful for connectivity arguments. It says that from any vertex a, you can reach any set B via as many internally disjoint paths as the connectivity allows.

# Examples
**Example** (p. 76): Applied with A := N(a) to get a fan from a to B with size equal to the minimum separator.

# Relationships
## Builds Upon
- **Menger's theorem**

## Enables
- **Proposition 10.1.2** — used to prove alpha(G) <= kappa(G) implies Hamiltonicity

# Source Reference
Chapter 3, Section 3.3, Corollary 3.3.4, p. 76 (pdf p. 76).

# Verification Notes
- Statement from p. 76
- Confidence: HIGH — explicit corollary
