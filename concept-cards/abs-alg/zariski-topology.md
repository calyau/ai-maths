---
concept: Zariski Topology
slug: zariski-topology
category: algebraic-geometry
subcategory: topology
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Commutative Rings and Algebraic Geometry"
chapter_number: 15
pdf_page: 699
section: "15.2 Radicals and Affine Varieties"
extraction_confidence: high
aliases:
  - "Zariski closed"
  - "Zariski open"
prerequisites:
  - affine-algebraic-set
extends: []
related:
  - affine-variety
  - prime-spectrum
contrasts_with: []
answers_questions:
  - "What is the Zariski topology on affine space?"
---

# Quick Definition
The Zariski topology on affine n-space A^n is the topology whose closed sets are the affine algebraic sets. It is a coarse topology — for infinite fields it is never Hausdorff.

# Core Definition
The **Zariski topology** on affine n-space over a field k is the topology in which the closed sets are the affine algebraic sets in A^n (Definition, p. 700). Properties (3)-(5) of algebraic sets (closure under arbitrary intersection, finite union, and inclusion of ∅ and A^n) ensure the topology axioms are satisfied. More generally, the Zariski topology on any algebraic set V is defined using ideals of the coordinate ring k[V].

# Prerequisites
- **affine-algebraic-set** — The closed sets of the topology

# Key Properties
1. Closed sets are affine algebraic sets
2. The topology is T_1 (points are closed) but not T_2 (Hausdorff) for infinite k
3. In A^1 over an infinite field, closed sets are ∅, finite sets, and k
4. Any two nonempty open sets intersect nontrivially (for infinite k)
5. Morphisms of algebraic sets are continuous in the Zariski topology
6. The Zariski closure of A ⊆ A^n is Z(I(A)) (Proposition 15)

# Context & Application
The Zariski topology provides the topological framework for algebraic geometry. Despite being very coarse compared to the Euclidean topology, it captures the algebraic structure faithfully. The notion extends to Spec R for general commutative rings.

# Examples
**Example** (p. 700): On R^1, the Zariski closed sets are ∅, R, and finite subsets. The interval [0,1] is closed in the Euclidean topology but not Zariski closed.

# Relationships
## Builds Upon
- **affine-algebraic-set** — The algebraic sets define the topology

## Enables
- **prime-spectrum** — The Zariski topology on Spec R generalizes this construction

# Source Reference
Chapter 15, Section 15.2, Definition and discussion, pages 699-702.

# Verification Notes
- Confidence: HIGH — explicit definition and thorough discussion
