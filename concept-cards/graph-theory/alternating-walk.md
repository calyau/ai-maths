---
concept: Alternating Walk
slug: alternating-walk
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
  - mengers-theorem
  - path
extends: []
related:
  - m-alternating-path
contrasts_with: []
answers_questions:
  - "What is an alternating walk in Menger's theorem?"
---

# Quick Definition
In the third proof of Menger's theorem, an alternating walk with respect to a path system P is a walk that starts outside V[P] in A and alternates between forward (non-P) and backward (P) edges, using each edge at most once.

# Core Definition
A walk W = x0 e0 x1 e1 ... e_{n-1} x_n in G with distinct edges is said to **alternate** with respect to P if it starts in A \ V[P] and satisfies: (i) P-edges are traversed backward; (ii) vertices outside V[P] occur at most once; (iii) at vertices in V[P], at least one incident edge lies in E[P] (Diestel, p. 74).

# Prerequisites
- **Menger's theorem** — alternating walks are used in the third proof
- **Path** — the walk alternates with respect to a path system

# Key Properties
1. Starts in A \ V[P] (at a vertex not on any path in P)
2. P-edges are traversed backward
3. Each edge is used at most once
4. Vertices outside V[P] appear at most once on W
5. If W reaches B \ V[P], it can be used to augment P (Lemma 3.3.2)
6. If no alternating walk reaches B \ V[P], a separator on P exists (Lemma 3.3.3)

# Context & Application
Alternating walks generalize the concept of alternating paths from matching theory (Section 2.1) to the setting of Menger's theorem. They provide the third (and most sophisticated) proof of Menger's theorem.

# Examples
**Example** (p. 74, Fig. 3.3.2): An alternating walk from A to B, traversing path edges backward and non-path edges forward.

# Relationships
## Builds Upon
- **Menger's theorem**, **path**

## Related
- **M-alternating path** — the matching theory analogue

# Source Reference
Chapter 3, Section 3.3, pp. 74-76 (pdf pp. 74-76).

# Verification Notes
- Definition from p. 74
- Confidence: HIGH — explicitly defined
