---
concept: "Dehn's Theorem"
slug: dehns-theorem
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
  - kirchhoffs-theorem-spanning-trees
extends: []
related:
  - perfect-squared-square
contrasts_with: []
answers_questions:
  - "What constraints exist on the side ratios of squared rectangles?"
---

# Quick Definition

Dehn's theorem (1903) states that if a rectangle can be tiled with squares, then the ratio of its two neighbouring sides is rational.

# Core Definition

"**Theorem 4.** If a rectangle can be tiled with squares then the ratio of two neighbouring sides of the rectangle is rational" (Bollobás, p. 56). This follows from Corollary 3 (rational conductances yield rational currents) applied to the corresponding electrical network. Sprague's extension (1940, Theorem 5) is the converse: a rectangle has a perfect squaring iff its side ratio is rational.

# Prerequisites

- **Squared rectangle** — The theorem constrains squared rectangles
- **Kirchhoff's theorem on spanning trees** — Used via the rational current corollary

# Key Properties

1. If a rectangle is tiled by squares, its side ratio must be rational
2. Equivalently, a rectangle can be tiled with squares iff it can be tiled with congruent squares
3. Sprague's extension: the converse also holds (Theorem 5)
4. The proof uses the fact that unit-resistance networks with integer external current have rational edge currents

# Construction / Recognition

Apply Corollary 3: in a network with rational conductances and rational external current, all edge currents are rational. The corresponding side ratio is a ratio of rational numbers.

# Context & Application

Dehn's theorem was first proved in 1903, long before the electrical network connection was established. The network approach provides a simpler proof.

# Examples

**Example** (p. 54): The $33 \times 32$ rectangle has rational side ratio $33/32$.

# Relationships

## Builds Upon
- **Squared rectangle**, **Kirchhoff's theorem on spanning trees**

## Enables
- Characterization of which rectangles admit perfect squarings

## Related
- **Perfect squared square** — The most constrained case

# Common Errors

- **Error**: Thinking any rectangle can be tiled with squares
  **Correction**: Only rectangles with rational side ratios can be tiled with squares

# Common Confusions

- **Confusion**: Thinking Dehn's theorem requires distinct square sizes
  **Clarification**: Dehn's theorem applies to any tiling with squares, not just perfect tilings

# Source Reference

Chapter II: Electrical Networks, Section II.2, Theorem 4, page 56; Theorem 5, page 57.

# Verification Notes

- Definition source: Direct theorem statement from p. 56
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
