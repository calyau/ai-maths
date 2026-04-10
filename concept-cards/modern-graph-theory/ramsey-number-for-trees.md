---
concept: Ramsey Number for Trees (Chvátal's Theorem)
slug: ramsey-number-for-trees
category: ramsey-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 199
section: "VI.3 Ramsey Theory For Graphs"
extraction_confidence: high
aliases:
  - "Theorem VI.12"
  - "Chvátal's tree-complete Ramsey theorem"
prerequisites:
  - graphical-ramsey-number
  - chromatic-surplus
extends: []
related:
  - ramsey-number-lower-bound
contrasts_with: []
answers_questions:
  - "What is the Ramsey number r(Kₛ, T) for a tree T?"
---

# Quick Definition
For every tree T of order t and s ≥ 2: r(Kₛ, T) = (s−1)(t−1) + 1. This is one of the few families where exact graphical Ramsey numbers are known.

# Core Definition
**Theorem 12** (Bollobás, p. 199): Let s, t ≥ 2, then for every tree T of order t, r(Kₛ, T) = (s−1)(t−1) + 1.

The lower bound comes from Theorem 11 (general lower bound). The upper bound: a graph of order (s−1)(t−1)+1 whose complement has no Kₛ must have χ ≥ t, hence contains a critical subgraph of minimum degree ≥ t−1, which must contain any tree of order t.

# Prerequisites
- **Graphical Ramsey number** — the quantity being determined
- **Chromatic surplus** — used in the lower bound

# Key Properties
1. r(Kₛ, T) = (s−1)(t−1) + 1 for every tree T of order t
2. Every tree T is "Kₛ-good" (equality in the general lower bound)
3. The proof uses the degeneracy/greedy argument: high chromatic number ⟹ high minimum degree ⟹ contains any tree

# Relationships
## Related
- **Graphical Ramsey number** — exact value for tree vs. complete graph

# Source Reference
Chapter VI: Ramsey Theory, Section VI.3, Theorem 12, page 199.

# Verification Notes
- Definition source: Direct theorem statement from p. 199
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
