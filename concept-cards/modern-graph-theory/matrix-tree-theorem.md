---
concept: Matrix-Tree Theorem
slug: matrix-tree-theorem
category: linear-algebra-of-graphs
subcategory: graph-matrices
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Electrical Networks"
chapter_number: 2
pdf_page: 46
section: "II.3 Vector Spaces and Matrices Associated with Graphs"
extraction_confidence: high
aliases:
  - "Kirchhoff's matrix tree theorem"
prerequisites:
  - combinatorial-laplacian
  - spanning-tree
extends: []
related:
  - kirchhoffs-theorem-spanning-trees
  - best-theorem
contrasts_with: []
answers_questions:
  - "How does the Laplacian matrix relate to spanning tree counting?"
  - "How can the number of spanning trees be computed?"
---

# Quick Definition

The matrix-tree theorem states that the number of spanning trees of a graph (or the weighted sum of spanning trees for a network) equals the common value of the first cofactors of the combinatorial Laplacian.

# Core Definition

"**Theorem 12.** With the notation above, $N^*(G) = K^*(G)$" (Bollobás, p. 65), where $N^*(G)$ is the sum of weights $w(T) = \prod c_e$ over all spanning trees $T$ and $K^*(G)$ is the common value of the first cofactors of the Laplacian $L = D - C$.

"**Corollary 13.** The number of spanning trees in a multigraph is precisely the common value of the first cofactors of the combinatorial Laplacian" (p. 66).

The proof uses induction on the number of edges and the "cut-and-fuse" relation: $N^*(G) = N^*(G - e) + c_e N^*(G/e)$ and $K^*(G) = K^*(G - e) + c_e K^*(G/e)$.

# Prerequisites

- **Combinatorial Laplacian** — The theorem concerns cofactors of the Laplacian
- **Spanning tree** — The theorem counts spanning trees

# Key Properties

1. All first cofactors of $L$ are equal
2. For unit conductances: cofactor of $L$ = number of spanning trees
3. For weighted networks: cofactor = sum of products of edge conductances over all spanning trees
4. The "cut-and-fuse" relation provides a recursive approach
5. $n^{n-2}$ spanning trees of $K_n$ (Cayley's formula) follows as a corollary

# Construction / Recognition

## To count spanning trees
1. Construct the Laplacian $L = D - A$
2. Delete any one row and the corresponding column
3. Compute the determinant of the resulting $(n-1) \times (n-1)$ matrix

# Context & Application

The matrix-tree theorem is one of the most elegant results connecting linear algebra and graph theory. It provides an efficient way to count spanning trees and is fundamental to electrical network theory. Cayley's formula ($n^{n-2}$ labelled trees on $n$ vertices) follows as a special case.

# Examples

**Example** (p. 65): The proof uses the cut-and-fuse relation: cutting edge $v_1v_2$ gives $N^*(G - v_1v_2)$, fusing gives $c_{12}N^*(G/v_1v_2)$.

**Example** (Exercise 41): Deducing Cayley's formula $n^{n-2}$ from the matrix-tree theorem applied to $K_n$.

# Relationships

## Builds Upon
- **Combinatorial Laplacian** — The theorem uses cofactors of $L$
- **Spanning tree** — The theorem counts spanning trees

## Enables
- Cayley's formula ($n^{n-2}$ labelled trees)
- Efficient spanning tree counting

## Related
- **Kirchhoff's theorem on spanning trees** — The current-distribution theorem uses the same tree counts
- **BEST theorem** — Uses oriented spanning tree counts

# Common Errors

- **Error**: Using the determinant of the full Laplacian instead of a cofactor
  **Correction**: $\det(L) = 0$ always; one must delete a row and column first

# Common Confusions

- **Confusion**: Thinking different cofactors might give different values
  **Clarification**: All first cofactors of $L$ are equal (this is proven as part of the theorem)

# Source Reference

Chapter II: Electrical Networks, Section II.3, Theorem 12, pages 65-66; Corollary 13, page 66; Theorem 14, page 66.

# Verification Notes

- Definition source: Direct theorem statement from p. 65
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
