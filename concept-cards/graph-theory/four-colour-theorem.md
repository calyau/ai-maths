---
concept: Four Colour Theorem
slug: four-colour-theorem
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
extraction_confidence: medium
aliases:
  - "4CT"
  - "Theorem 5.1.1"
  - "four color theorem"
prerequisites:
  - chromatic-number
  - planar-graph
extends: []
related:
  - five-colour-theorem
  - grotzsch-theorem
  - chromatic-number
contrasts_with: []
answers_questions:
  - "What is the maximum chromatic number of a planar graph?"
  - "Can every planar graph be coloured with four colours?"
---

# Quick Definition
The Four Colour Theorem states that every planar graph is 4-colourable: chi(G) <= 4 for every planar graph G.

# Core Definition
**Theorem 5.1.1** (Four Colour Theorem): "Every planar graph is 4-colourable" (Diestel, p. 112).

# Prerequisites
- **Chromatic number** -- The theorem bounds chi(G)
- **Planar graph** -- Applies specifically to planar graphs

# Key Properties
1. chi(G) <= 4 for every planar graph G
2. The bound is tight: some planar graphs (e.g., K^4) require 4 colours
3. Implies every map can be coloured with at most 4 colours
4. The proof is computer-assisted and not given in Diestel
5. The five colour theorem (chi <= 5) has an elementary proof

# Context & Application
The Four Colour Theorem has one of the most celebrated histories in mathematics. Conjectured by Francis Guthrie in 1852, it was first proved by Appel and Haken in 1977 using computer verification. The proof involves showing that every plane triangulation contains one of ~1500 "unavoidable configurations," each of which is "reducible." A shorter computer-assisted proof was given by Robertson, Sanders, Seymour, and Thomas (1997).

# Examples
**Example**: K^4 (planar) requires exactly 4 colours.

**Example**: Every planar bipartite graph needs only 2 colours.

**Example**: Every triangle-free planar graph needs only 3 colours (Grotzsch's theorem).

# Relationships
## Builds Upon
- **Chromatic number**, **Planar graph**

## Related
- **Five colour theorem** -- Weaker result with elementary proof
- **Grotzsch's theorem** -- Triangle-free planar graphs are 3-colourable

# Common Errors
- **Error**: Attempting to prove the 4CT by elementary methods
  **Correction**: All known proofs require computer verification of many cases

# Common Confusions
- **Confusion**: Thinking the 4CT applies to all graphs
  **Clarification**: Only planar graphs are guaranteed 4-colourable; non-planar graphs may require arbitrarily many colours

# Source Reference
Chapter 5, Section 5.1, Theorem 5.1.1, page 112. Notes pp. 137-138 for historical context.

# Verification Notes
- Theorem stated without proof
- Confidence: MEDIUM -- theorem stated as fact; proof not given (computer-assisted)
- Historical context from Notes section
