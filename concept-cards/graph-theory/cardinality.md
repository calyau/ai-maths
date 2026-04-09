---
concept: Cardinality
slug: cardinality

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
  - "|A|"

prerequisites: []
extends: []
related:
  - bijection
  - finite-set
  - infinite-set
  - countable-set
  - uncountable-set
contrasts_with: []

answers_questions:
  - "What is the cardinality of a set?"
  - "When do two sets have the same cardinality?"
---

# Quick Definition
Two sets A and B have the same cardinality, written |A| = |B|, if there exists a bijection between them. We write |A| <= |B| if there exists an injection from A to B.

# Core Definition
If there exists a bijective map between A and B, we write |A| = |B| and say that A and B have the same cardinality. This is an equivalence relation, and we may think of the cardinality |A| of A as the equivalence class containing A. We write |A| <= |B| if there exists an injective map A -> B. This is a partial ordering: if there are injective maps A -> B and B -> A, there is also a bijection A -> B (Cantor-Bernstein theorem) (Diestel, p. 357).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Same cardinality is an equivalence relation
2. The ordering |A| <= |B| is well-defined and is a partial ordering
3. For every set there exists a bigger one (e.g., |A| < |power set of A|)
4. The Cantor-Bernstein theorem: injections in both directions imply a bijection

# Context & Application
Cardinality is used in Chapter 8 (Infinite Graphs) to classify the sizes of infinite sets and graphs.

# Relationships
## Enables
- **finite-set**, **infinite-set**, **countable-set**, **uncountable-set** — all defined via cardinality

# Source Reference
Appendix A: Infinite Sets, page 357 (pdf p. 367).

# Verification Notes
- Direct from p. 357
- Confidence: HIGH
