---
concept: Perfect Graph Theorem
slug: perfect-graph-theorem
category: perfect-graphs
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 178
section: "V.5 Perfect Graphs"
extraction_confidence: high
aliases:
  - "Theorem V.20"
  - "Lovász-Fulkerson theorem"
  - "Weak Perfect Graph Theorem"
prerequisites:
  - perfect-graph
  - replacement-theorem-for-perfect-graphs
extends:
  - perfect-graph
related:
  - perfect-graph-conjecture
  - fractional-independence-number
contrasts_with: []
answers_questions:
  - "What is the Perfect Graph Theorem?"
  - "Is the complement of a perfect graph also perfect?"
---

# Quick Definition
The complement of a perfect graph is perfect. This fundamental result was proved by Lovász and Fulkerson in the early 1970s.

# Core Definition
**Theorem 20** (Bollobás, p. 178): The complement of a perfect graph is perfect.

The proof uses induction on n and the replacement theorem (Theorem 19). It assumes for contradiction that G̅ is not perfect, constructs a graph G* by substituting complete graphs of specific sizes for vertices, shows G* is perfect by the replacement theorem, then derives a contradiction between ω(G*) and χ(G*).

# Prerequisites
- **Perfect graph** — the class of graphs being studied
- **Replacement theorem for perfect graphs** — key lemma in the proof

# Key Properties
1. G perfect ⟹ G̅ perfect
2. The proof is non-trivial and ingenious
3. An alternative proof uses: G is perfect iff |H| ≤ ω(H)·ω(H̅) for all induced H (Lovász 1972)
4. The perfect graph theorem is an immediate consequence of the Strong Perfect Graph Theorem (Berge's conjecture)

# Context & Application
The perfect graph theorem is the cornerstone of perfect graph theory. It reveals a deep symmetry: the property of having χ = ω for all induced subgraphs is preserved under complementation, even though clique number and independence number are swapped.

# Examples
**Example** (p. 175): Bipartite graphs are perfect, so their complements are perfect (recovering Theorem 15).

# Relationships
## Builds Upon
- **Perfect graph** definition
- **Replacement theorem** — key technical tool

## Enables
- Polynomial algorithms for χ, ω, α on perfect graphs
- **Fractional independence number** characterization

## Related
- **Perfect graph conjecture** — would imply the perfect graph theorem

# Common Errors
- **Error**: Thinking the proof is straightforward from definitions
  **Correction**: The proof requires the non-trivial replacement theorem and a clever counting argument

# Source Reference
Chapter V: Colouring, Section V.5, Theorem 20, pages 178–180.

# Verification Notes
- Definition source: Direct theorem statement from p. 178
- Confidence rationale: Explicit theorem with complete proof
- Uncertainties: None
- Cross-reference status: Verified
