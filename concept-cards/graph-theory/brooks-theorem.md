---
concept: "Brooks' Theorem"
slug: brooks-theorem
category: graph-colouring
subcategory: vertex-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.2 Colouring vertices"
extraction_confidence: high
aliases:
  - "Theorem 5.2.4"
  - "Brooks 1941"
prerequisites:
  - chromatic-number
  - greedy-colouring
extends: []
related:
  - colouring-number
  - vizing-theorem
contrasts_with: []
answers_questions:
  - "When is chi(G) strictly less than Delta(G) + 1?"
  - "What is Brooks' theorem?"
---

# Quick Definition
Brooks' theorem states that for a connected graph G that is neither complete nor an odd cycle, chi(G) <= Delta(G). The only connected graphs needing Delta + 1 colours are complete graphs and odd cycles.

# Core Definition
**Theorem 5.2.4** (Brooks 1941): "Let G be a connected graph. If G is neither complete nor an odd cycle, then chi(G) <= Delta(G)" (Diestel, p. 115).

# Prerequisites
- **Chromatic number** -- The theorem bounds chi(G)
- **Greedy colouring** -- The greedy bound Delta + 1 is improved by 1

# Key Properties
1. chi(G) <= Delta(G) unless G is K^n or an odd cycle
2. Proved by induction on |G| with Delta >= 3
3. The proof uses Kempe chain arguments (H_{i,j} subgraphs)
4. For Delta <= 2: G is a path (chi = 2) or cycle (chi in {2,3})

# Context & Application
Brooks' theorem is one of the fundamental results in graph colouring. It shows that the trivial greedy bound of Delta + 1 colours can always be improved to Delta colours, except for two well-understood families. The theorem also holds for list colouring (the list-colouring analogue is true).

# Examples
**Example**: K^5 has Delta = 4 and chi = 5 = Delta + 1 (exception: complete graph).

**Example**: C_5 has Delta = 2 and chi = 3 = Delta + 1 (exception: odd cycle).

**Example**: The Petersen graph has Delta = 3 and chi = 3 = Delta (Brooks applies).

# Relationships
## Builds Upon
- **Chromatic number**, **Greedy colouring**

## Related
- **Colouring number** -- col(G) provides another bound
- **Vizing's theorem** -- Analogous "Delta or Delta + 1" result for edge colouring

# Common Errors
- **Error**: Applying Brooks' theorem to disconnected graphs without checking components
  **Correction**: Apply Brooks' theorem to each component separately

# Source Reference
Chapter 5, Section 5.2, Theorem 5.2.4, pages 115-117.

# Verification Notes
- Full proof given pp. 115-117
- Confidence: HIGH -- named classical theorem with complete proof
