---
concept: Rado Graph
slug: rado-graph
category: infinite-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Graphs"
chapter_number: 8
pdf_page: 223
section: "8.3 Homogeneous and universal graphs"
extraction_confidence: high
aliases:
  - "random graph (infinite)"
  - "Erdős-Rényi graph (infinite)"
prerequisites:
  - infinite-graph
extends: []
related:
  - universal-graph
  - homogeneous-graph
  - back-and-forth-argument
  - random-graph-gnp
contrasts_with: []
answers_questions:
  - "What is the Rado graph?"
  - "What is a random graph in the infinite setting?"
---

# Quick Definition
The Rado graph R is the unique countable graph satisfying property (*): for any disjoint finite sets U and W of vertices, there exists a vertex adjacent to all of U and none of W. It is universal for all countable graphs under the induced subgraph relation.

# Core Definition
**Theorem 8.3.1** (Erdős and Rényi 1963): There exists a unique countable graph R with property (*): whenever U and W are disjoint finite sets of vertices in R, there exists a vertex v not in U or W that is adjacent to all vertices in U but to none in W. This graph is called the *Rado graph*, named after Richard Rado. It is also called the (countably infinite) *random graph* because a random graph on N with any constant edge probability p in (0,1) is isomorphic to R with probability 1 (Diestel, pp. 223-224).

# Prerequisites
- **Infinite graph** — The Rado graph is a countably infinite graph

# Key Properties
1. Uniqueness: any two countable graphs with property (*) are isomorphic (proved by back-and-forth argument)
2. Universality: R contains every countable graph as an induced subgraph
3. The Rado graph is homogeneous: every isomorphism between finite induced subgraphs extends to an automorphism
4. Deletion of finitely many vertices or edges leaves a graph isomorphic to R
5. In any partition of V(R) into two parts, at least one part induces a copy of R
6. A random graph on N with constant p in (0,1) is almost surely isomorphic to R

# Construction / Recognition
## To Construct the Rado Graph
1. Start with R_0 = K^1
2. For each n, obtain R_{n+1} from R_n by adding for every subset U of V(R_n) a new vertex joined to exactly U
3. R = union of all R_n has property (*)

# Context & Application
The Rado graph is a remarkable object sitting at the intersection of infinite graph theory, random graphs, and model theory. Its uniqueness despite being "generic" illustrates a deep symmetry phenomenon.

# Examples
**Example 1** (p. 223): The inductive construction R_0, R_1, ... produces R.

**Example 2** (p. 224): The back-and-forth technique proves uniqueness by alternately extending the isomorphism from R to R'.

# Relationships
## Enables
- **Theorem 11.3.5** — With probability 1, an infinite random graph is isomorphic to R

## Related
- **Universal graph** — R is universal for countable graphs
- **Homogeneous graph** — R is homogeneous
- **Back-and-forth argument** — Used to prove uniqueness

# Source Reference
Chapter 8, Section 8.3, pages 223-225 (Theorem 8.3.1, Proposition 8.3.2).

# Verification Notes
- Definition and properties from pp. 223-225
- Confidence: HIGH — named concept with full proof
