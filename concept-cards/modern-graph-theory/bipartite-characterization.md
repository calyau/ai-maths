---
concept: Bipartite Characterization Theorem
slug: bipartite-characterization
category: graph-fundamentals
subcategory: basic-results
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.2 Paths, Cycles, and Trees"
extraction_confidence: high
aliases: []
prerequisites:
  - bipartite-graph
  - cycle
extends: []
related:
  - tree
contrasts_with: []
answers_questions:
  - "How can bipartiteness be characterized?"
---

# Quick Definition

A graph is bipartite if and only if it contains no odd cycle (Theorem 4). This provides an efficient test for bipartiteness.

# Core Definition

"**Theorem 4.** A graph is bipartite iff it does not contain an odd cycle" (Bollobás, p. 16). The proof constructs the bipartition from distance classes: pick vertex $x$, set $V_1 = \{y : d(x,y) \text{ is odd}\}$, $V_2 = V \setminus V_1$. If no odd cycle exists, no edge joins two vertices of the same class.

# Prerequisites

- **Bipartite graph** — The property being characterized
- **Cycle** — The characterization uses cycle parity

# Key Properties

1. Bipartite $\iff$ no odd cycle
2. The bipartition can be constructed via BFS distance classes
3. A bipartite graph of order $n$ has at most $\lfloor n^2/4 \rfloor$ edges
4. This maximum is achieved by $K_{\lfloor n/2 \rfloor, \lceil n/2 \rceil}$
5. Forbidding just triangles restricts the size to the same bound (Mantel's theorem)

# Construction / Recognition

## To test bipartiteness and find the bipartition
1. Pick any vertex $x$
2. Compute distances from $x$ to all other vertices
3. Place vertices at odd distance in $V_1$, vertices at even distance in $V_2$
4. The graph is bipartite iff no edge has both endpoints in the same $V_i$

# Context & Application

This characterization is algorithmically efficient (BFS suffices) and theoretically fundamental. The connection to Mantel's theorem shows that forbidding just the triangle $C_3$ is as restrictive as forbidding all odd cycles.

# Examples

**Example** (p. 17): $\lfloor n^2/4 \rfloor$ is the maximal size of a graph with no odd cycles, achieved by $K_{\lfloor n/2 \rfloor, \lceil n/2 \rceil}$.

# Relationships

## Builds Upon
- **Bipartite graph**, **Cycle**

## Enables
- Efficient bipartiteness testing
- The extremal bound $\lfloor n^2/4 \rfloor$

## Related
- **Tree** — Every tree is bipartite (since trees have no cycles at all)

# Common Errors

- **Error**: Checking only for triangles instead of all odd cycles
  **Correction**: Must check for absence of all odd cycles; however, the BFS method does this efficiently

# Common Confusions

- **Confusion**: Thinking a graph with no triangles must be bipartite
  **Clarification**: A graph with no triangles may still have odd cycles of length 5 or more (e.g., $C_5$)

# Source Reference

Chapter I: Fundamentals, Section I.2, Theorem 4, pages 16-17.

# Verification Notes

- Definition source: Direct theorem statement from p. 16
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
