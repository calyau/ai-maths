---
concept: Separator on Paths
slug: separator-on-paths
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 74
section: "3.3 Menger's theorem"
extraction_confidence: high
aliases: []
prerequisites:
  - separator
  - mengers-theorem
extends:
  - separator
related:
  - alternating-walk
contrasts_with: []
answers_questions:
  - "What is a separator on a path system?"
---

# Quick Definition
An A-B separator X lies on a path system P if X consists of exactly one vertex from each path in P.

# Core Definition
An A-B separator X lies **on** P if it consists of a choice of exactly one vertex from each path in P. If such a separator exists, then k <= |X| = |P|, completing the proof of Menger's theorem (Diestel, p. 74).

# Prerequisites
- **Separator** — X is an A-B separator
- **Menger's theorem** — the concept is used in the third proof

# Key Properties
1. X picks exactly one vertex from each path
2. |X| = |P|, giving k <= |P| (the desired inequality)
3. Constructed in Lemma 3.3.3 when no alternating walk reaches B \ V[P]
4. For each path P in P, x_P is chosen as the last vertex on P reachable by an alternating walk

# Context & Application
Finding a separator on P is the key step in the third proof of Menger's theorem. It establishes k = |P| by constructing a separator of size |P|.

# Examples
**Example** (p. 75, Fig. 3.3.3): The separator X = {x_P : P in P} is constructed by choosing the "last reachable" vertex on each path.

# Relationships
## Related
- **Menger's theorem** — this completes the third proof
- **Alternating walk** — used to define x_P

# Source Reference
Chapter 3, Section 3.3, pp. 74-76 (pdf pp. 74-76).

# Verification Notes
- From Lemma 3.3.3
- Confidence: HIGH
