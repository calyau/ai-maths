---
concept: "Thomassen's Theorem (5-Choosability)"
slug: thomassen-five-choosable
category: graph-colouring
subcategory: list-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.4 List colouring"
extraction_confidence: high
aliases:
  - "Theorem 5.4.2"
  - "Thomassen 1994"
  - "planar 5-choosability"
prerequisites:
  - list-colouring
  - choice-number
  - planar-graph
  - plane-triangulation
extends:
  - five-colour-theorem
related:
  - four-colour-theorem
contrasts_with: []
answers_questions:
  - "Are planar graphs list-colourable from lists of size 5?"
  - "Is there a list-colouring version of the five colour theorem?"
---

# Quick Definition
Every planar graph is 5-choosable: it can be properly coloured from any lists of size 5. This strengthens the five colour theorem and has a beautiful elementary proof by induction.

# Core Definition
**Theorem 5.4.2** (Thomassen 1994): "Every planar graph is 5-choosable" (Diestel, p. 122).

# Prerequisites
- **List colouring** and **Choice number** -- The theorem bounds ch(G)
- **Planar graph** -- Applies to planar graphs
- **Plane triangulation** -- The proof works with triangulations

# Key Properties
1. ch(G) <= 5 for every planar graph G
2. Implies chi(G) <= 5 (five colour theorem) as a corollary
3. The proof does NOT use Euler's formula or the five colour theorem
4. Uses a strengthened induction: outer cycle vertices get lists of size 3, interior vertices get lists of size 5, two pre-coloured vertices
5. Planar graphs are NOT 4-choosable in general (Voigt 1993)
6. This is best possible: 5-choosability cannot be improved to 4-choosability

# Construction / Recognition
## Proof Strategy
1. Reduce to plane triangulations
2. Prove stronger statement: given a triangulation with outer cycle C, two pre-coloured adjacent vertices on C, lists of size >= 3 on other C vertices, and lists of size >= 5 on interior vertices, a colouring exists
3. Induction on |G|: either C has a chord (split into two smaller problems) or remove a vertex of the outer cycle and adjust lists

# Context & Application
Thomassen's theorem demonstrates a phenomenon where proving the stronger list-colouring version is actually easier than the ordinary colouring version. The proof is more elegant than the standard five colour theorem proof because the variable list sizes allow a more flexible induction hypothesis.

# Examples
**Example** (p. 122-124): The proof constructs colourings of plane triangulations from lists, using the delicate balance of list sizes (2 pre-coloured, 3 on boundary, 5 in interior).

# Relationships
## Builds Upon
- **List colouring**, **Planar graph**, **Plane triangulation**

## Enables
- Provides an alternative proof of the five colour theorem

## Related
- **Four colour theorem** -- Stronger for ordinary colouring but does not extend to 4-choosability

# Common Confusions
- **Confusion**: Thinking planar graphs should be 4-choosable since they are 4-colourable
  **Clarification**: 4-colourability does NOT imply 4-choosability; there exist planar graphs that are not 4-choosable

# Source Reference
Chapter 5, Section 5.4, Theorem 5.4.2, pages 122-124.

# Verification Notes
- Full proof given pp. 122-124
- Confidence: HIGH -- named theorem with complete proof
