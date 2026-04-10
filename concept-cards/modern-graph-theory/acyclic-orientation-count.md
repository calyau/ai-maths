---
concept: Acyclic Orientation Count from Tutte Polynomial
slug: acyclic-orientation-count
category: tutte-polynomial
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 356
section: "X.4 Special Values of the Tutte Polynomial"
extraction_confidence: high
aliases: []
prerequisites:
  - tutte-polynomial
  - special-values-tutte-polynomial
extends: []
related:
  - chromatic-polynomial-from-tutte
contrasts_with: []
answers_questions:
  - "What information does the Tutte polynomial encode?"
---

# Quick Definition
$T_G(2,0)$ counts all acyclic orientations of $G$, and $T_G(1,0)$ counts acyclic orientations with a unique source at any fixed vertex $u$.

# Core Definition
$a(G) = T_G(2,0)$ (number of acyclic orientations, from $|p_G(-1)|$). Theorem 8 (p. 356): "For every connected graph $G$ and every vertex $u \in V(G)$, $a_u(G) = T_G(1,0)$," where $a_u(G)$ is the number of acyclic orientations with $u$ as the unique source.

# Prerequisites
- **Tutte polynomial** — Evaluated at special points
- **Special values of the Tutte polynomial** — Context for these evaluations

# Key Properties
1. $T_G(2,0) = a(G)$: total acyclic orientations
2. $T_G(1,0) = a_u(G)$: acyclic orientations with unique source $u$ (independent of $u$!)
3. Proved by verifying deletion-contraction for bridges, loops, and general edges
4. $T_G(0,2)$: totally cyclic orientations (Exercise 10)

# Source Reference
Chapter X, Section X.4, Theorem 8, pages 356-357.

# Verification Notes
- Definition source: Direct from Theorem 8
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
