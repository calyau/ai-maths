---
concept: Dilworth's Theorem in Perfect Graph Context
slug: dilworths-theorem-perfect-graphs
category: perfect-graphs
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 177
section: "V.5 Perfect Graphs"
extraction_confidence: high
aliases:
  - "Theorem III.12"
prerequisites:
  - comparability-graph
extends: []
related:
  - perfect-graph
contrasts_with: []
answers_questions:
  - "How does Dilworth's theorem relate to perfect graphs?"
---

# Quick Definition
The minimum number of chains partitioning a poset equals the maximum antichain size. This is exactly the statement that complements of comparability graphs are perfect.

# Core Definition
**Dilworth's theorem** (Theorem III.12, cited on p. 177): For a partially ordered set P, min chain cover = max antichain. In terms of H = C(P): χ(H̅) = ω(H̅), proving complements of comparability graphs are perfect (Bollobás, p. 177).

# Prerequisites
- **Comparability graph** — context

# Key Properties
1. min chain cover = max antichain (Dilworth)
2. Equivalent to χ(C̅(P)) = ω(C̅(P))

# Relationships
## Related
- **Perfect graph** — Dilworth provides examples

# Source Reference
Chapter V: Colouring, Section V.5, page 177.

# Verification Notes
- Definition source: Referenced from Ch III
- Confidence rationale: Explicitly applied
- Uncertainties: None
- Cross-reference status: Verified
