---
concept: Missing Colour Technique
slug: missing-colour-technique
category: graph-colouring
subcategory: edge-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.3 Colouring edges"
extraction_confidence: high
aliases:
  - "Vizing fan"
prerequisites:
  - edge-colouring
extends: []
related:
  - vizing-theorem
  - alpha-beta-path
contrasts_with: []
answers_questions:
  - "What is the missing colour technique in Vizing's theorem?"
---

# Quick Definition
In a (Delta+1)-edge-colouring of G - e, each vertex v uses at most Delta colours, leaving at least one "missing" colour. The proof of Vizing's theorem exploits the interaction of missing colours at endpoints of uncoloured edges with alpha/beta alternating paths.

# Core Definition
"In such a colouring, the edges at a given vertex v use at most d(v) <= Delta colours, so some colour beta in {1,...,Delta+1} is missing at v" (Diestel, p. 120). The proof constructs a sequence of edges whose missing colours interact.

# Prerequisites
- **Edge colouring**

# Key Properties
1. At each vertex, at least one colour from {1,...,Delta+1} is unused
2. Colour swapping along alpha/beta paths can redistribute missing colours
3. The proof of Vizing's theorem builds a "fan" of edges with interacting missing colours
4. A key contradiction arises when alpha/beta paths from different vertices must connect

# Context & Application
The missing colour technique is the main tool in Vizing's theorem proof. It converts a partial colouring into a complete one by carefully redistributing "available" colours via alternating path swaps.

# Relationships
## Enables
- **Vizing's theorem** -- The proof technique

## Related
- **Alpha/beta path** -- Used to redistribute colours

# Source Reference
Chapter 5, Section 5.3, pages 119-121.

# Verification Notes
- From Vizing's theorem proof
- Confidence: HIGH
