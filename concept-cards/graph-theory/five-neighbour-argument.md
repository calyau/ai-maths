---
concept: Five-Neighbour Argument
slug: five-neighbour-argument
category: graph-colouring
subcategory: planar-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.1 Colouring maps and planar graphs"
extraction_confidence: high
aliases: []
prerequisites:
  - five-colour-theorem
  - edge-bound-planar
  - kempe-chain
extends: []
related:
  - greedy-colouring
contrasts_with: []
answers_questions:
  - "Why does the five colour theorem proof work?"
  - "How is the minimum degree used in planar colouring?"
---

# Quick Definition
Since planar graphs have average degree < 6, some vertex v has degree <= 5. By induction, G - v is 5-colourable. If v has <= 4 distinctly coloured neighbours, the colouring extends; if exactly 5, Kempe chains resolve the conflict.

# Core Definition
The proof of the five colour theorem (Proposition 5.1.2) works by: (1) finding a vertex v of degree <= 5 (using d(G) < 6 from Euler's formula); (2) inductively 5-colouring G - v; (3) extending to v, using Kempe chain recolouring if all 5 colours appear on v's neighbours (Diestel, pp. 112-113).

# Prerequisites
- **Five colour theorem**, **Edge bound**, **Kempe chain**

# Key Properties
1. d(G) < 6 guarantees a vertex of degree <= 5
2. With 5 available colours and at most 5 neighbours, at most need to free one colour
3. Kempe chain argument shows two specific neighbours cannot be in the same chain
4. This is exactly where Kempe's 4CT proof fails (with 4 colours, the chains can interact)

# Context & Application
This argument pattern (minimum degree vertex + induction + recolouring) is fundamental to planar graph colouring. The same structure, with the refined Thomassen induction, proves 5-choosability.

# Relationships
## Builds Upon
- **Edge bound** (degree < 6), **Kempe chains**

## Enables
- **Five colour theorem** proof

# Source Reference
Chapter 5, Section 5.1, pages 112-113.

# Verification Notes
- Proof structure from pp. 112-113
- Confidence: HIGH
