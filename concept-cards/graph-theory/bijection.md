---
concept: Bijection
slug: bijection

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
  - "bijective map"
  - "injective"
  - "surjective"

prerequisites: []
extends: []
related:
  - cardinality
contrasts_with: []

answers_questions:
  - "What is a bijection?"
  - "What is an injection?"
---

# Quick Definition
A bijection is a map that is both injective (one-to-one) and surjective (onto). Two sets have the same cardinality if and only if there is a bijection between them.

# Core Definition
A bijective map between sets A and B establishes |A| = |B|. An injective map A -> B establishes |A| <= |B|. The Cantor-Bernstein theorem states that if there are injective maps A -> B and B -> A, then there is a bijection A -> B (Diestel, p. 357).

# Prerequisites
This is a foundational concept.

# Key Properties
1. A bijection is one-to-one and onto
2. A bijection N -> A is an enumeration of A
3. The Cantor-Bernstein theorem provides a bijection from two injections

# Relationships
## Related
- **cardinality** — defined via bijections

# Source Reference
Appendix A: Infinite Sets, page 357 (pdf p. 367).

# Verification Notes
- Direct from p. 357
- Confidence: HIGH
