---
concept: Kempe Chain
slug: kempe-chain
category: planar-graphs
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 165
section: "V.3 Graphs on Surfaces"
extraction_confidence: high
aliases:
  - "Kempe chain argument"
  - "colour exchange path"
prerequisites:
  - vertex-colouring
extends: []
related:
  - five-colour-theorem
  - four-colour-theorem
  - vizings-theorem
contrasts_with: []
answers_questions:
  - "What is a Kempe chain and how is it used in colouring proofs?"
---

# Quick Definition
A Kempe chain is a connected component of the subgraph induced by vertices of exactly two colours in a proper colouring. Swapping these two colours on a Kempe chain preserves the colouring's validity.

# Core Definition
Given a proper colouring of G and two colours i, j, the subgraph H(i, j) consists of all vertices coloured i or j and the edges between them. Each component of H(i, j) is a Kempe chain. Interchanging colours i and j on any single Kempe chain yields another proper colouring. Named after Kempe, who used them in his (false) 1879 proof of the four-colour theorem (Bollobás, p. 165).

# Prerequisites
- **Vertex colouring** — Kempe chains arise within a proper colouring

# Key Properties
1. Each vertex in H(i,j) has degree at most 2 (at most one edge of each colour)
2. Components of H(i,j) are paths and even cycles
3. Swapping colours i, j on a single component preserves the colouring
4. The technique is used in proofs of the five-colour theorem, Vizing's theorem, and the four-colour theorem

# Construction / Recognition
## To Use a Kempe Chain Argument
1. Start with a proper k-colouring
2. Identify two colours i, j
3. Consider the subgraph H(i, j) of vertices coloured i or j
4. Identify connected components
5. Swap colours i and j on one component to obtain a new valid colouring
6. This may free up a colour at a specific vertex

# Context & Application
Kempe chains are the fundamental colour-exchange technique in graph colouring theory. They appear in proofs of the five-colour theorem, Vizing's theorem, and are central to the four-colour theorem proof. The technique also appears in Vizing's proof for edge colouring.

# Examples
**Example** (p. 162, Figure V.4): In the proof of the five-colour theorem, paths P₁₃ and P₂₄ are Kempe chains. Planarity prevents them from coexisting when they connect specific neighbours of a degree-5 vertex.

# Relationships
## Enables
- **Five colour theorem** proof
- **Vizing's theorem** proof (for edge colouring)
- **Four colour theorem** — reducibility arguments use Kempe chains

## Related
- **Reducible configuration** — reducibility is shown by Kempe chain arguments

# Common Errors
- **Error**: Assuming Kempe chain swaps always resolve conflicts
  **Correction**: In some cases (like Kempe's false 4-colour proof), the swap on one chain may destroy a previously established property

# Source Reference
Chapter V: Colouring, Section V.3, pages 162, 165.

# Verification Notes
- Definition source: Direct from proof discussions pp. 162, 165
- Confidence rationale: Explicitly named and used in multiple proofs
- Uncertainties: None
- Cross-reference status: Verified
