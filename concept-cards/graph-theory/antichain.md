---
concept: Antichain
slug: antichain

category: set-theory-foundations
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Sets"
chapter_number: null
pdf_page: 367
section: null

extraction_confidence: medium

aliases: []

prerequisites:
  - partially-ordered-set
extends: []
related:
  - chain
contrasts_with:
  - chain

answers_questions:
  - "What is an antichain?"
---

# Quick Definition
An antichain in a partially ordered set is a set of pairwise incomparable elements (no two elements satisfy x <= y).

# Core Definition
An antichain is a set of pairwise incomparable elements in a partially ordered set. This concept is standard in order theory and contrasts with the chain concept defined in Appendix A (Diestel, p. 358, implicitly).

# Prerequisites
- **Partially ordered set** — antichains are subsets of posets

# Key Properties
1. No two elements of an antichain are comparable
2. In a totally ordered set (chain), every antichain has at most one element

# Relationships
## Builds Upon
- **partially-ordered-set**

## Contrasts With
- **chain** — all elements comparable vs. none comparable

# Source Reference
Appendix A: Infinite Sets, page 358 (pdf p. 368).

# Verification Notes
- Standard complement to "chain"; used implicitly
- Confidence: MEDIUM — not explicitly defined in the appendix
