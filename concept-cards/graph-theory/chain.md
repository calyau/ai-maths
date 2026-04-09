---
concept: Chain
slug: chain

category: set-theory-foundations
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Sets"
chapter_number: null
pdf_page: 367
section: null

extraction_confidence: high

aliases:
  - "totally ordered set"
  - "linear order"

prerequisites:
  - partially-ordered-set
extends:
  - partially-ordered-set
related:
  - well-ordered-set
  - zorns-lemma
contrasts_with:
  - antichain

answers_questions:
  - "What is a chain in a partially ordered set?"
  - "What is a predecessor/successor in a chain?"
---

# Quick Definition
A chain is a partially ordered set in which every two elements are comparable. In a chain, x is the predecessor of y if x < y and no z satisfies x < z < y; y is then the successor of x.

# Core Definition
A chain is a partially ordered set in which every two elements are comparable. If (C, <=) is a chain, and if x, y in C satisfy x < y but no element z of C is such that x < z < y, then x is called the predecessor of y in C, and y the successor of x. A set of the form {x in C | x < z}, for a given z in C, is a proper initial segment of C (Diestel, p. 358).

# Prerequisites
- **Partially ordered set** — a chain is a special poset

# Key Properties
1. Every two elements are comparable
2. Predecessor and successor are defined for adjacent elements
3. N, Z, and R are all chains under their usual orderings
4. Initial segments {x | x < z} play a key role in ordinal theory

# Examples
**Example** (p. 358): N, Z, and R are all chains, but only N is well-ordered.

# Relationships
## Builds Upon
- **partially-ordered-set**

## Enables
- **well-ordered-set** — a well-founded chain

## Contrasts With
- **antichain** — a set of pairwise incomparable elements

# Source Reference
Appendix A: Infinite Sets, page 358 (pdf p. 368).

# Verification Notes
- Direct from p. 358
- Confidence: HIGH
