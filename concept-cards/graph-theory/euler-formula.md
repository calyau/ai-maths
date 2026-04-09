---
concept: "Euler's Formula"
slug: euler-formula
category: planar-graphs
subcategory: plane-graphs
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.2 Plane graphs"
extraction_confidence: high
aliases:
  - "Euler's formula for plane graphs"
  - "v - e + f = 2"
  - "n - m + l = 2"
  - "Theorem 4.2.9"
prerequisites:
  - plane-graph
  - face
  - face-boundary
extends: []
related:
  - euler-characteristic
  - maximal-planar-graph
  - plane-triangulation
contrasts_with: []
answers_questions:
  - "What is Euler's formula for plane graphs?"
  - "How are vertices, edges, and faces related in a plane graph?"
---

# Quick Definition
Euler's formula states that for any connected plane graph with n vertices, m edges, and l faces, n - m + l = 2.

# Core Definition
**Theorem 4.2.9** (Euler's Formula): "Let G be a connected plane graph with n vertices, m edges, and l faces. Then n - m + l = 2" (Diestel, p. 91).

# Prerequisites
- **Plane graph** -- The formula applies to plane graphs
- **Face** -- Faces must be counted including the outer face
- **Face boundary** -- The proof uses properties of face boundaries (Lemma 4.2.2)

# Key Properties
1. Holds for all connected plane graphs
2. The formula is n - m + l = 2
3. Generalizes to surfaces: n - m + l = chi(S) where chi is the Euler characteristic
4. For disconnected plane graphs with c components: n - m + l = 1 + c
5. Implies m <= 3n - 6 for plane graphs with n >= 3 (Corollary 4.2.10)
6. Implies m <= 2n - 4 for triangle-free plane graphs

# Construction / Recognition
## To Verify Euler's Formula
1. Count vertices n
2. Count edges m
3. Count faces l (including the outer face)
4. Check n - m + l = 2

# Context & Application
Euler's formula (1752) is one of the foundational results of both graph theory and topology. It provides the key tool for showing that certain graphs are non-planar: K^5 has 10 > 3(5) - 6 = 9 edges, and K_{3,3} has 9 > 2(6) - 4 = 8 edges (since K_{3,3} is triangle-free). The formula also generalizes to graphs embedded on surfaces, where the right-hand side becomes the Euler characteristic chi(S) of the surface.

# Examples
**Example** (p. 91): A plane tree with n vertices has n - 1 edges and 1 face, giving n - (n-1) + 1 = 2.

**Example** (p. 92): K^5 has n = 5, and any plane graph on 5 vertices has at most 3(5) - 6 = 9 edges, but K^5 has 10 edges. Hence K^5 is not planar.

**Example** (p. 92): K_{3,3} has n = 6, m = 9, and being triangle-free requires m <= 2(6) - 4 = 8. Since 9 > 8, K_{3,3} is not planar.

# Relationships
## Builds Upon
- **Plane graph**, **Face**, **Face boundary**

## Enables
- **Corollary 4.2.10** -- m <= 3n - 6 for planar graphs
- **Non-planarity proofs** -- K^5 and K_{3,3} are shown non-planar
- **Five colour theorem** -- Uses the edge bound d(G) < 6
- **Euler characteristic** -- Generalization to arbitrary surfaces

## Related
- **Plane triangulation** -- Achieves equality m = 3n - 6
- **Maximal planar graph** -- Characterized by having 3n - 6 edges

# Common Errors
- **Error**: Forgetting to count the outer face
  **Correction**: The outer (unbounded) face must be included in the face count l

- **Error**: Applying the formula to disconnected graphs without modification
  **Correction**: For disconnected graphs, use n - m + l = 1 + c where c is the number of components

# Common Confusions
- **Confusion**: Thinking Euler's formula applies to abstract (non-embedded) graphs
  **Clarification**: The formula requires a specific plane embedding; "faces" are only defined for plane graphs

# Source Reference
Chapter 4: Planar Graphs, Section 4.2 "Plane graphs," Theorem 4.2.9, pages 90-91. Corollary 4.2.10, page 91.

# Verification Notes
- Theorem statement directly quoted from p. 91
- Proof is by induction on m, using Lemma 4.2.2
- Confidence: HIGH -- central named theorem with complete proof
