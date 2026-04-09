---
concept: Well-Ordered Set
slug: well-ordered-set

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
  - "well-ordering"
  - "well-founded"

prerequisites:
  - partially-ordered-set
  - chain
extends:
  - chain
related:
  - ordinal
  - well-ordering-theorem
  - transfinite-induction
contrasts_with: []

answers_questions:
  - "What is a well-ordered set?"
  - "What is a well-founded set?"
---

# Quick Definition
A partially ordered set is well-founded if every non-empty subset has a minimal element. A well-founded chain is well-ordered. In a well-ordered set, every non-minimal element has a unique successor.

# Core Definition
A partially ordered set (X, <=) is well-founded if every non-empty subset of X has a minimal element, and a well-founded chain is said to be well-ordered. Every element x of a well-ordered set X has a successor (unless x is maximal in X). However, an element need not have a predecessor, even if not minimal. An element that has no predecessor is called a limit (Diestel, p. 358).

# Prerequisites
- **Partially ordered set**, **chain** — a well-ordered set is a well-founded chain

# Key Properties
1. Every non-empty subset has a minimum element
2. Every non-maximal element has a unique successor
3. Not every element has a predecessor (limit elements)
4. N is well-ordered; Z and R are not

# Examples
**Example** (p. 358): N is well-ordered. Z and R are chains but not well-ordered. The set A = {1 - 1/(n+1) | n in N} union {2 - 1/(n+1) | n in N} is well-ordered with 1 as a limit element.

# Relationships
## Builds Upon
- **chain**

## Enables
- **ordinal** — equivalence classes of well-ordered sets
- **transfinite-induction** — proof technique for well-ordered sets

# Source Reference
Appendix A: Infinite Sets, page 358 (pdf p. 368).

# Verification Notes
- Direct from p. 358
- Confidence: HIGH
