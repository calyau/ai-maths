---
concept: "Alpha/Beta Path"
slug: alpha-beta-path
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
  - "alternating colour path"
  - "Vizing fan"
prerequisites:
  - edge-colouring
extends: []
related:
  - vizing-theorem
  - konig-edge-colouring-theorem
contrasts_with: []
answers_questions:
  - "What is an alpha/beta path in edge colouring?"
---

# Quick Definition
In the proof of Vizing's theorem, an alpha/beta path from vertex v is the unique maximal path starting at v whose edges alternate between colours alpha and beta.

# Core Definition
"For any other colour alpha, there is a unique maximal walk (possibly trivial) starting at v, whose edges are coloured alternately alpha and beta. This walk is a path; we call it the alpha/beta-path from v" (Diestel, p. 120).

# Prerequisites
- **Edge colouring** -- Defined within edge colouring context

# Key Properties
1. Unique for each starting vertex and colour pair
2. Used to swap colours without creating conflicts
3. Central tool in Vizing's and Konig's theorem proofs
4. Analogous to Kempe chains for vertex colouring

# Relationships
## Enables
- **Vizing's theorem** -- Key proof technique
- **Konig's theorem** -- Alternating path argument

# Source Reference
Chapter 5, Section 5.3, page 120.

# Verification Notes
- From Vizing's theorem proof
- Confidence: HIGH
