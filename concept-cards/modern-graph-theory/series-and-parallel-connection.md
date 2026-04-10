---
concept: Series and Parallel Connection
slug: series-and-parallel-connection
category: electrical-networks
subcategory: network-simplification
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Electrical Networks"
chapter_number: 2
pdf_page: 46
section: "II.1 Graphs and Electrical Networks"
extraction_confidence: high
aliases:
  - resistors in series
  - resistors in parallel
prerequisites:
  - electrical-network
  - resistance-and-conductance
extends: []
related:
  - star-triangle-transformation
contrasts_with: []
answers_questions:
  - "How do series and parallel connections affect resistance?"
---

# Quick Definition

For resistors in series, resistances add: $r = r_1 + r_2$. For resistors in parallel, conductances add: $1/r = 1/r_1 + 1/r_2$, equivalently $r = r_1 r_2/(r_1 + r_2)$.

# Core Definition

"In the first case [...] the total resistance is $r = r_1 + r_2$. In the second case, when they are connected in parallel [...] the total resistance is given by $r = r_1 r_2/(r_1 + r_2)$, or $1/r = 1/r_1 + 1/r_2$. [...] What we have shown now is that for series connection the resistances add and for parallel connection the conductances add" (Bollobás, pp. 49-50).

# Prerequisites

- **Electrical network** — The context for these connections
- **Resistance and conductance** — The quantities being combined

# Key Properties

1. Series: total resistance = sum of resistances
2. Parallel: total conductance = sum of conductances
3. These are the two simplest network reduction operations
4. Can be applied iteratively to simplify complex networks

# Construction / Recognition

Series: two edges share a degree-2 vertex (not a source or sink). Parallel: two edges share both endpoints.

# Context & Application

Series and parallel reductions, together with the star-triangle transformation, are standard tools for simplifying electrical networks. Bollobás uses them to compute the resistance of a cube (p. 50) and a tetrahedron (p. 51).

# Examples

**Example** (p. 50): The total resistance of a cube across an edge, with each edge having 1 ohm, is $7/12$, computed by shorting symmetric vertices and simplifying series/parallel combinations.

# Relationships

## Builds Upon
- **Electrical network**, **Resistance and conductance**

## Enables
- Network simplification for computing total resistance

## Related
- **Star-triangle transformation** — A more general simplification

# Common Errors

- **Error**: Adding resistances for parallel connections
  **Correction**: For parallel connections, add conductances (reciprocals of resistances)

# Common Confusions

- **Confusion**: Applying series/parallel rules when the topology is neither
  **Clarification**: Series/parallel only apply when edges share a degree-2 vertex (series) or both endpoints (parallel)

# Source Reference

Chapter II: Electrical Networks, Section II.1, pages 49-50.

# Verification Notes

- Definition source: Direct from pp. 49-50
- Confidence rationale: Explicitly derived with formulas
- Uncertainties: None
- Cross-reference status: Verified
