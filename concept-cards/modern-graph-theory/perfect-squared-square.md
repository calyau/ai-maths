---
concept: Perfect Squared Square
slug: perfect-squared-square
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
aliases: []
prerequisites:
  - squared-rectangle
  - electrical-network
extends:
  - squared-rectangle
related:
  - dehns-theorem
contrasts_with: []
answers_questions:
  - "Does a perfect squared square exist?"
---

# Quick Definition

A perfect squared square is a square subdivided into finitely many squares of distinct sizes. The smallest such square uses 21 smaller squares (due to Duijvestijn).

# Core Definition

A perfect squared square is a subdivision of a square into "finitely many (but at least two) square regions of distinct sizes that intersect only at their boundaries" (Bollobás, p. 54). The first examples were found by Sprague (1939) and by Brooks, Smith, Stone, and Tutte (1940). The smallest number of squares that can tile a square is 21 (Duijvestijn).

# Prerequisites

- **Squared rectangle** — A squared square is a special case
- **Electrical network** — Used to construct squared squares

# Key Properties

1. The minimum order is 21 (Duijvestijn's result, unique at this order)
2. First found independently by Sprague and by Brooks-Smith-Stone-Tutte
3. Corresponds to a planar network with total resistance 1 and all distinct edge currents
4. The network must be a plane graph with $s$ and $t$ on the outer face, lacking all symmetries

# Construction / Recognition

Search for plane graphs containing $s$ and $t$ on the outer face, with no symmetries and total resistance 1 from $s$ to $t$.

# Context & Application

The perfect squared square problem was a famous open problem in recreational mathematics that was solved using electrical network theory, demonstrating the power of the graph-theoretic approach.

# Examples

**Example** (p. 56): Fig. II.8 shows Duijvestijn's tiling of a square with 21 incongruent squares — the unique smallest perfect squared square.

# Relationships

## Builds Upon
- **Squared rectangle** — A squared square is a squared rectangle that is also a square

## Related
- **Dehn's theorem** — Rational constraints on tiling

# Common Errors

- **Error**: Thinking any squared rectangle can be scaled to a squared square
  **Correction**: The square constraint imposes additional structure; most squared rectangles cannot become squared squares

# Common Confusions

- **Confusion**: Thinking a perfect squared square is easy to find
  **Clarification**: The first examples required sophisticated search using electrical network theory

# Source Reference

Chapter II: Electrical Networks, Section II.2, pages 54-56; Fig. II.8.

# Verification Notes

- Definition source: Direct from p. 54
- Confidence rationale: Explicitly described with history
- Uncertainties: None
- Cross-reference status: Verified
