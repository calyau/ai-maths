---
concept: Kempe Chain
slug: kempe-chain
category: graph-colouring
subcategory: vertex-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.1 Colouring maps and planar graphs"
extraction_confidence: high
aliases:
  - "H_{i,j}"
  - "Kempe chain argument"
  - "colour interchange"
prerequisites:
  - vertex-colouring
extends: []
related:
  - five-colour-theorem
  - brooks-theorem
contrasts_with: []
answers_questions:
  - "What is a Kempe chain?"
  - "How does the colour interchange technique work?"
---

# Quick Definition
A Kempe chain (or H_{i,j} subgraph) is the subgraph induced by vertices coloured i or j. Interchanging colours i and j within a connected component of H_{i,j} produces another valid colouring. This technique is used in proofs of the five colour theorem and Brooks' theorem.

# Core Definition
"Given i, j in {1,...,5}, let H_{i,j} be the subgraph of H induced by the vertices coloured i or j" (Diestel, p. 113). Interchanging colours i and j in a connected component of H_{i,j} yields another valid colouring.

# Prerequisites
- **Vertex colouring** -- Kempe chains are defined relative to a colouring

# Key Properties
1. Each connected component of H_{i,j} is a path or cycle using only colours i and j
2. Swapping i and j in one component preserves the colouring's validity
3. Used to recolour vertices and free up colours for new vertices
4. Central technique in proofs involving planar graph colouring

# Context & Application
Kempe chains were introduced by Kempe in 1879 in his (incorrect) proof of the four colour conjecture. The technique remains fundamental: it is used correctly in the five colour theorem proof, Brooks' theorem, and Vizing's theorem. The failure of Kempe's original argument (interaction between multiple chains) led Heawood to discover the correct five colour theorem.

# Relationships
## Enables
- **Five colour theorem** -- Proof uses Kempe chain interchange
- **Brooks' theorem** -- Proof uses colour interchange arguments

# Source Reference
Chapter 5, Section 5.1, page 113 (five colour theorem proof).

# Verification Notes
- Technique from p. 113
- Confidence: HIGH -- used explicitly in proofs
