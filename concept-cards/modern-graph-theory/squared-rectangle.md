---
concept: Squared Rectangle
slug: squared-rectangle
category: electrical-networks
subcategory: squaring
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Electrical Networks"
chapter_number: 2
pdf_page: 46
section: "II.2 Squaring the Square"
extraction_confidence: high
aliases:
  - perfect squared rectangle
prerequisites:
  - electrical-network
  - planar-graph
  - resistance-and-conductance
extends: []
related:
  - perfect-squared-square
  - dehns-theorem
contrasts_with: []
answers_questions:
  - "What is a squared rectangle?"
  - "How do electrical networks relate to squared rectangles?"
---

# Quick Definition

A squared rectangle is a rectangle subdivided into finitely many squares of distinct sizes. The connection between squared rectangles and electrical networks enables systematic construction: each squared rectangle corresponds to a planar network with unit edge resistances.

# Core Definition

"Is there a perfect squared square? In other words, is it possible to subdivide a closed square into finitely many (but at least two) square regions of distinct sizes that intersect only at their boundaries?" (Bollobás, p. 54). A squared rectangle has order equal to the number of squares in the subdivision. The correspondence works via: horizontal lines become vertices, squares become edges, and the side length of a square equals the current in the corresponding edge.

# Prerequisites

- **Electrical network** — Squared rectangles correspond to networks
- **Planar graph** — The network must be planar
- **Resistance and conductance** — Unit resistance edges

# Key Properties

1. Each squared rectangle corresponds to a planar electrical network with unit resistances
2. The side length of each square equals the potential drop (current) in the corresponding edge
3. The total resistance equals the ratio of the rectangle's height to width
4. A squared rectangle of order $k$ uses $k$ squares
5. The process is reversible: every suitable network gives a squared rectangle

# Construction / Recognition

1. Take a connected planar graph with unit resistances
2. Calculate total resistance from $s$ to $t$
3. If resistance equals 1, the network may correspond to a squared square
4. If all edge currents are distinct, obtain a perfect squaring

# Context & Application

The squared rectangle problem illustrates the power of the electrical network approach. Moron found the first perfect squared rectangle in 1925 (the $33 \times 32$ rectangle of order 9).

# Examples

**Example** (p. 54): Fig. II.6 shows Moron's perfect squaring of the $33 \times 32$ rectangle with 9 squares.

**Example** (p. 55): Fig. II.7 shows the electrical network corresponding to Moron's rectangle.

# Relationships

## Builds Upon
- **Electrical network**, **Planar graph**, **Resistance and conductance**

## Enables
- **Perfect squared square** — The search for squared squares

## Related
- **Dehn's theorem** — Rational side ratios for squared rectangles

# Common Errors

- **Error**: Thinking any planar network gives a squared rectangle
  **Correction**: The total resistance must equal the height/width ratio, and currents must yield valid square sizes

# Common Confusions

- **Confusion**: Confusing "squared rectangle" with "squared square"
  **Clarification**: A squared rectangle tiles a rectangle with squares; a squared square tiles a square

# Source Reference

Chapter II: Electrical Networks, Section II.2, pages 54-56.

# Verification Notes

- Definition source: Direct from p. 54
- Confidence rationale: Explicitly described with examples
- Uncertainties: None
- Cross-reference status: Verified
