---
concept: Five Colour Theorem
slug: five-colour-theorem
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
aliases:
  - "Proposition 5.1.2"
  - "5-colour theorem"
prerequisites:
  - chromatic-number
  - planar-graph
  - euler-formula
  - edge-bound-planar
extends: []
related:
  - four-colour-theorem
  - thomassen-five-choosable
contrasts_with: []
answers_questions:
  - "Can every planar graph be coloured with five colours?"
---

# Quick Definition
Every planar graph is 5-colourable. This is proved elementarily using Euler's formula and Kempe chain arguments.

# Core Definition
**Proposition 5.1.2** (Five Colour Theorem): "Every planar graph is 5-colourable" (Diestel, p. 112).

# Prerequisites
- **Chromatic number** -- Bounds chi(G)
- **Planar graph** -- Applies to planar graphs
- **Euler's formula** and **Edge bound** -- Used to show average degree < 6

# Key Properties
1. chi(G) <= 5 for every planar graph G
2. The proof is elementary (unlike the Four Colour Theorem)
3. Key insight: Euler's formula implies d(G) < 6, so there exists a vertex of degree <= 5
4. Uses Kempe chain argument: interchange colours along 2-coloured paths
5. The result is superseded by the 4CT but has an independent elementary proof

# Construction / Recognition
## Proof Sketch
1. By Euler's formula, d(G) < 6, so some vertex v has degree <= 5
2. By induction, G - v has a 5-colouring
3. If v has <= 4 neighbours with distinct colours, extend the colouring
4. If v has 5 neighbours with 5 distinct colours, use Kempe chains to recolour

# Context & Application
The five colour theorem was first proved by Heawood in 1890, modifying Kempe's incorrect 1879 proof of the four colour conjecture. The proof technique (Kempe chains) remains important. Thomassen later proved the stronger result that planar graphs are 5-choosable (Theorem 5.4.2), providing yet another proof of the five colour theorem.

# Examples
**Example** (p. 112-113, Fig. 5.1.1): The proof constructs a 5-colouring by removing a vertex of degree <= 5 and using Kempe chains to handle the case of 5 distinctly coloured neighbours.

# Relationships
## Builds Upon
- **Edge bound** (d(G) < 6 for planar)

## Related
- **Four colour theorem** -- Stronger result
- **Thomassen's theorem** -- Planar graphs are even 5-choosable

# Source Reference
Chapter 5, Section 5.1, Proposition 5.1.2, pages 112-113.

# Verification Notes
- Full proof given pp. 112-113
- Confidence: HIGH -- complete elementary proof in source
