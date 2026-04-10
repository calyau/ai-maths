---
concept: Strong Perfect Graph Conjecture
slug: perfect-graph-conjecture
category: perfect-graphs
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 180
section: "V.5 Perfect Graphs"
extraction_confidence: high
aliases:
  - "Berge's conjecture"
  - "Strong Perfect Graph Theorem"
prerequisites:
  - perfect-graph
  - perfect-graph-theorem
extends:
  - perfect-graph-theorem
related:
  - imperfect-graph
contrasts_with: []
answers_questions:
  - "What is a perfect graph?"
  - "How can perfect graphs be characterized by forbidden subgraphs?"
---

# Quick Definition
Berge's 1960 conjecture (proved in 2006 by Chudnovsky, Robertson, Seymour and Thomas): a graph G is perfect if and only if neither G nor G̅ contains an induced odd cycle of length ≥ 5.

# Core Definition
The **Strong Perfect Graph Conjecture**, proposed by Berge in 1960 (proved 2006): A graph G is perfect if, and only if, neither G nor its complement G̅ contains an induced odd cycle of length at least 5. Equivalently, the odd cycles of length ≥ 5 and their complements are the only critically imperfect graphs (Bollobás, p. 180).

Note: At the time of the book's publication (1998), this was still a conjecture. It was proved by Chudnovsky, Robertson, Seymour and Thomas in 2002 (published 2006).

# Prerequisites
- **Perfect graph** — the class being characterized
- **Perfect graph theorem** — an immediate consequence

# Key Properties
1. A graph is perfect iff it has no odd hole or odd antihole of length ≥ 5
2. An odd hole is an induced odd cycle C_{2k+1} with k ≥ 2
3. An odd antihole is the complement of an odd hole
4. The perfect graph theorem follows immediately from this characterization
5. No critically imperfect graphs besides odd holes and antiholes are known

# Context & Application
The Strong Perfect Graph Theorem (as it's now known) is one of the deepest results in graph theory. It gives a complete forbidden-subgraph characterization of perfect graphs. The proof required decades of effort.

# Relationships
## Builds Upon
- **Perfect graph theorem** — a consequence of this conjecture/theorem

## Related
- **Imperfect graph** — characterized by containing an odd hole or antihole

# Source Reference
Chapter V: Colouring, Section V.5, page 180.

# Verification Notes
- Definition source: Direct from p. 180
- Confidence rationale: Explicitly stated as a conjecture (proved after publication)
- Uncertainties: Book states it as a conjecture; it was proved in 2002
- Cross-reference status: Verified
