---
concept: Comb
slug: comb
category: infinite-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Graphs"
chapter_number: 8
pdf_page: 206
section: "8.1 Basic notions, facts and techniques"
extraction_confidence: high
aliases:
  - "infinite comb"
prerequisites:
  - ray
  - path
extends: []
related:
  - star-comb-lemma
  - end-of-a-graph
contrasts_with: []
answers_questions:
  - "What is a comb in graph theory?"
---

# Quick Definition
A comb is the union of a ray R with infinitely many disjoint finite paths having precisely their first vertex on R. The ray R is its spine, and the last vertices of those paths are its teeth.

# Core Definition
The union of a ray R with infinitely many disjoint finite paths having precisely their first vertex on R is a *comb*; the last vertices of those paths are the *teeth* of this comb, and R is its *spine*. If such a path is trivial (a single vertex), then its unique vertex lies on R and also counts as a tooth (Diestel, p. 206).

# Prerequisites
- **Ray** — The spine of a comb is a ray
- **Path** — The teeth are connected to the spine by finite paths

# Key Properties
1. A comb has a spine (a ray) and teeth (endpoints of paths from the spine)
2. The paths from spine to teeth are pairwise disjoint
3. Trivial paths are allowed: a vertex on R can be a tooth
4. A comb with teeth in a set U witnesses that U "converges" to the end of the spine

# Context & Application
Combs appear in the star-comb lemma, which says that for any infinite set of vertices in a connected graph, one can find either a comb with teeth in that set or a subdivided infinite star with leaves in it. In locally finite graphs, the comb alternative always holds.

# Examples
**Example 1** (p. 206, Fig. 8.1.1): A comb with white teeth and spine R = x_0x_1... is depicted.

# Relationships
## Builds Upon
- **Ray** — The spine is a ray

## Enables
- **Star-comb lemma** — Combs are one of the two alternatives

## Related
- **End of a graph** — The teeth of a comb converge to the end of its spine

# Source Reference
Chapter 8, Section 8.1, page 206, Figure 8.1.1.

# Verification Notes
- Definition directly from p. 206
- Confidence: HIGH — explicit definition with figure
