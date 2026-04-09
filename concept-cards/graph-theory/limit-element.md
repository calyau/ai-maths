---
concept: Limit Element
slug: limit-element

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
  - "limit"
  - "limit ordinal"

prerequisites:
  - well-ordered-set
extends: []
related:
  - ordinal
  - transfinite-induction
contrasts_with:
  - successor-ordinal

answers_questions:
  - "What is a limit element in a well-ordered set?"
  - "What is a limit ordinal?"
---

# Quick Definition
An element of a well-ordered set that has no predecessor is called a limit. The number 0 is a limit (its predecessor condition is vacuous). In ordinal theory, limit ordinals are ordinals that are not successors.

# Core Definition
An element that has no predecessor is called a limit; for example, the number 1 is a limit in the well-ordered set A = {1 - 1/(n+1) | n in N} union {2 - 1/(n+1) | n in N} (Diestel, p. 358).

# Prerequisites
- **Well-ordered set** — limit elements exist in well-ordered sets

# Key Properties
1. A limit element has no immediate predecessor
2. 0 counts as a limit (the predecessor condition is vacuous)
3. In transfinite induction, the limit case and successor case are treated separately

# Relationships
## Builds Upon
- **well-ordered-set**

## Related
- **ordinal**, **transfinite-induction**

## Contrasts With
- **successor-ordinal** — has a predecessor

# Source Reference
Appendix A: Infinite Sets, page 358 (pdf p. 368).

# Verification Notes
- Direct from p. 358
- Confidence: HIGH
