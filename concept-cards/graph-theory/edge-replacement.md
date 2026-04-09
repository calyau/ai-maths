---
concept: Edge Replacement
slug: edge-replacement
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 57
section: "2.4 Tree-packing and arboricity"
extraction_confidence: high
aliases: []
prerequisites:
  - forest
  - spanning-tree
extends: []
related:
  - nash-williams-tutte-theorem
contrasts_with: []
answers_questions:
  - "What is edge replacement in the context of tree packing?"
---

# Quick Definition
Edge replacement is the operation of swapping an edge e' in a spanning forest Fi with an edge e not in any forest, producing a new valid k-tuple of forests.

# Core Definition
Given a k-tuple F = (F1, ..., Fk) of edge-disjoint spanning forests with maximum total edges, and an edge e not in any Fi, each Fi + e contains a cycle. Replacing an edge e' of this cycle with e gives a new k-tuple F' still in the optimal family. This is called an **edge replacement** (Diestel, p. 57).

# Prerequisites
- **Forest** — edge replacement modifies forests
- **Spanning tree** — in the optimal case, forests should be trees

# Key Properties
1. The replacement preserves the total number of edges
2. The new k-tuple is still optimal
3. Components keep their vertex sets under replacement
4. Foundation for Lemma 2.4.3: a set U exists that is connected in every Fi and contains the ends of e

# Context & Application
Edge replacement is the key technique in proving both the Nash-Williams-Tutte theorem (tree packing) and the Nash-Williams arboricity theorem. It allows local modifications while maintaining global optimality.

# Examples
**Example** (p. 57): If e is not in E[F] and Fi + e contains a cycle with edge e', then replacing e' with e gives a new valid tuple F'.

# Relationships
## Related
- **Nash-Williams-Tutte theorem** — proof uses edge replacement

# Source Reference
Chapter 2, Section 2.4, p. 57 (pdf p. 57).

# Verification Notes
- From p. 57
- Confidence: HIGH — explicitly described technique
