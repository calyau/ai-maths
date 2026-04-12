---
concept: Doubling the Cube
slug: doubling-the-cube
category: field-theory
subcategory: impossibility-results
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Fields"
chapter_number: 15
pdf_page: 453
section: "15.5 Ruler and Compass Constructions"
extraction_confidence: high
aliases:
  - "duplication of the cube"
  - "Delian problem"
prerequisites:
  - constructible-number
extends: []
related:
  - trisecting-the-angle
  - squaring-the-circle
contrasts_with: []
answers_questions:
  - "Why can't you double the cube with ruler and compass?"
---

# Quick Definition

Doubling the cube -- constructing the cube root of 2 -- is impossible with ruler and compass because cube_root(2) has degree 3 over Q, which is not a power of 2.

# Core Definition

The problem of doubling the cube asks to construct a cube with twice the volume of a given cube. This requires constructing cube_root(2). Since x^3 - 2 is irreducible over Q (by the rational root test), cube_root(2) has degree 3 over Q. Since 3 is not a power of 2, cube_root(2) is not constructible (Artin, Corollary 15.5.7).

# Prerequisites

- **Constructible number** -- Degree over Q must be a power of 2

# Key Properties

1. cube_root(2) is algebraic of degree 3 over Q
2. 3 is not a power of 2
3. Therefore cube_root(2) is not constructible

# Context & Application

This is one of the three classical Greek impossibility results, along with trisecting the angle and squaring the circle. The proof via field theory is remarkably elegant.

# Examples

**Example 1**: x^3 - 2 is irreducible over Q by the rational root test (possible roots +/-1, +/-2 are not roots).

# Relationships

## Builds Upon
- **Constructible number** -- The degree criterion

## Related
- **Trisecting the angle** -- Another classical impossibility
- **Squaring the circle** -- Third classical impossibility (requires transcendence of pi)

# Source Reference

Chapter 15: Fields, Section 15.5, pages 463-470. Corollary 15.5.7.

# Verification Notes

- Definition source: Standard application of Artin's Corollary 15.5.7
- Confidence rationale: Straightforward application
- Uncertainties: None
- Cross-reference status: Verified
