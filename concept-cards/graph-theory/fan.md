---
concept: Fan
slug: fan
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 76
section: "3.3 Menger's theorem"
extraction_confidence: high
aliases:
  - "a-B fan"
prerequisites:
  - path
extends: []
related:
  - fan-version-mengers-theorem
  - independent-paths
contrasts_with: []
answers_questions:
  - "What is a fan in graph theory?"
---

# Quick Definition
An a-B fan is a set of a-B paths that are pairwise disjoint except at the common vertex a.

# Core Definition
A set of a-B paths is called an **a-B fan** if any two of the paths have only a in common (Diestel, p. 76).

# Prerequisites
- **Path** — a fan consists of paths

# Key Properties
1. All paths start at the same vertex a
2. All paths end in the set B
3. The paths are internally disjoint (share only the vertex a)
4. The size of a maximum fan equals the minimum a-B separator size minus a (Corollary 3.3.4)

# Context & Application
Fans are used in connectivity arguments. The fan version of Menger's theorem (Corollary 3.3.4) relates fans to separators. Fans are used in the proof that alpha(G) <= kappa(G) implies Hamiltonicity (Proposition 10.1.2).

# Examples
**Example** (Proposition 10.1.2, p. 287): A v-C fan of size >= min{k, |C|} from a vertex v to a cycle C is used to find a longer cycle.

# Relationships
## Builds Upon
- **Path**

## Related
- **Fan version of Menger's theorem** — counts maximum fans
- **Independent paths** — a fan consists of independent a-B paths

# Source Reference
Chapter 3, Section 3.3, p. 76 (pdf p. 76).

# Verification Notes
- Definition from p. 76
- Confidence: HIGH — explicitly defined
