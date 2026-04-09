---
concept: Latin Square
slug: latin-square
category: graph-colouring
subcategory: edge-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "Exercises"
extraction_confidence: medium
aliases: []
prerequisites:
  - edge-colouring
extends: []
related:
  - konig-edge-colouring-theorem
contrasts_with: []
answers_questions:
  - "How do Latin squares relate to edge colouring?"
---

# Quick Definition
An n x n Latin square is a matrix with entries from {1,...,n} where each element appears exactly once in each row and column. Constructing Latin squares is equivalent to edge colouring the complete bipartite graph K_{n,n}.

# Core Definition
"An n x n matrix with entries from {1,...,n} is called a Latin square if every element of {1,...,n} appears exactly once in each column and exactly once in each row" (Diestel, p. 135, Exercise 20).

# Prerequisites
- **Edge colouring** -- Latin squares correspond to edge colourings of K_{n,n}

# Key Properties
1. An n x n Latin square is a proper n-edge-colouring of K_{n,n}
2. Existence guaranteed by Konig's edge colouring theorem
3. Rows and columns correspond to the two parts of K_{n,n}; entries are edge colours

# Relationships
## Related
- **Konig's theorem** -- Guarantees Latin squares exist

# Source Reference
Chapter 5, Exercise 20, page 135.

# Verification Notes
- Exercise definition
- Confidence: MEDIUM
