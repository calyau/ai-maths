---
concept: Power Set
slug: power-set

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

aliases: []

prerequisites:
  - cardinality
extends: []
related:
  - uncountable-set
contrasts_with: []

answers_questions:
  - "What is a power set?"
  - "Why is |A| < |power set of A|?"
---

# Quick Definition
The power set of A is the set of all subsets of A. For every set A, |A| < |power set of A|.

# Core Definition
For every set there exists another that is bigger; for example, |A| < |B| when B is the power set of A, the set of all its subsets (Diestel, p. 357).

# Prerequisites
- **Cardinality** — the power set is strictly larger

# Key Properties
1. The power set of A contains 2^|A| elements (for finite A)
2. |A| < |power set of A| for every set A (Cantor's theorem)
3. The power set of N has the cardinality of the continuum

# Relationships
## Builds Upon
- **cardinality**

## Related
- **uncountable-set** — power set of a countably infinite set is uncountable

# Source Reference
Appendix A: Infinite Sets, page 357 (pdf p. 367).

# Verification Notes
- Direct from p. 357
- Confidence: HIGH
