---
concept: "Hadwiger's Conjecture for Small r"
slug: hadwiger-conjecture-small-r
category: extremal-graph-theory
subcategory: minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 183
section: "7.3 Hadwiger's conjecture"
extraction_confidence: high
aliases:
  - "Corollary 7.3.3"
  - "Corollary 7.3.6"
  - "Theorem 7.3.7"
prerequisites:
  - hadwiger-conjecture
related:
  - wagner-theorem
  - four-colour-theorem
answers_questions:
  - "For which values of r is Hadwiger's conjecture proved?"
---

# Quick Definition
Hadwiger's conjecture is proved for r <= 6: trivially for r <= 2, easily for r = 3,4, and for r = 5,6 it relies on the four colour theorem. It remains open for r >= 7.

# Core Definition
Status of Hadwiger's conjecture by r:
- **r <= 2**: Trivial
- **r = 3**: Graphs without K^3 minor are forests, which are 2-colourable
- **r = 4**: Proposition 7.3.1 characterizes K^4-minor-free graphs (built from triangles by pasting along K^2s); they are 3-colourable (Corollary 7.3.3)
- **r = 5**: Follows from Wagner's Theorem 7.3.4 and the 4CT (Corollary 7.3.6)
- **r = 6**: Robertson, Seymour & Thomas 1993 (Theorem 7.3.7), using 4CT
- **r >= 7**: OPEN (Diestel, pp. 172-176)

# Prerequisites
- **Hadwiger's conjecture** — This card details partial results

# Key Properties
1. The conjecture for r+1 implies it for r
2. The case r = 4 gives: edge-maximal K^4-minor-free graphs all have 2|G|-3 edges
3. The case r = 6 is "substantially more difficult" than r = 5
4. All proofs for r = 5,6 depend on the four colour theorem

# Relationships
## Builds Upon
- **Hadwiger's conjecture**

## Related
- **Wagner's theorem** — Structure theorem for K^5-minor-free graphs
- **Four colour theorem** — Required for r = 5,6

# Source Reference
Chapter 7, Section 7.3, pages 172-176 (pdf pages 183-186).

# Verification Notes
- Confidence: HIGH — well-documented status of each case
