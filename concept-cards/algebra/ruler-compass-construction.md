---
concept: Ruler and Compass Construction
slug: ruler-compass-construction
category: field-theory
subcategory: constructions
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
  - "straightedge and compass"
prerequisites:
  - field-extension
  - degree-of-field-extension
extends: []
related:
  - constructible-number
  - trisecting-the-angle
  - doubling-the-cube
contrasts_with: []
answers_questions:
  - "What are the rules for ruler and compass construction?"
  - "How do field extensions relate to geometric constructions?"
---

# Quick Definition

Ruler and compass constructions start with two points and allow drawing lines through constructed points and circles centered at constructed points. Points of intersection become new constructed points. Each construction step extends the coordinate field by at most a quadratic extension.

# Core Definition

The rules for ruler and compass construction (Artin, p. 463, 15.5.1): Two points are given initially. If two points have been constructed, one may draw the line through them or draw a circle centered at one passing through the other. Points of intersection of constructed lines and circles are constructed. Each intersection involves solving at most a quadratic equation, so each step extends the coordinate field F to a quadratic extension F' (Proposition 15.5.5).

# Prerequisites

- **Field extension** -- Each construction step is a field extension
- **Degree of field extension** -- Each step has degree at most 2

# Key Properties

1. The ruler is a straightedge only -- no measurement allowed
2. Each construction step extends the coordinate field by degree at most 2 (15.5.5)
3. A constructible point has coordinates in a field K with [K:Q] = 2^n (Theorem 15.5.6)
4. The constructible numbers form a subfield of R (15.5.11(a))
5. If a > 0 is constructible, so is sqrt(a) (15.5.11(b))
6. Converse: every element of a field obtained by successive quadratic extensions is constructible (15.5.10)

# Context & Application

Ruler and compass constructions connect geometry to algebra through field theory. The degree criterion proves the impossibility of three classical Greek problems.

# Examples

**Example 1** (p. 463): Constructing a perpendicular through a point to a line -- requires only lines and circles.

**Example 2** (p. 464): Constructing a parallel to a given line through a given point.

**Example 3** (p. 464): Marking off a given length on a line.

# Relationships

## Builds Upon
- **Field extension** -- Each step is a field extension

## Enables
- **Constructible number** -- Numbers that can be constructed
- **Impossibility proofs** -- For trisection, duplication, quadrature

# Source Reference

Chapter 15: Fields, Section 15.5, pages 463-470. Rules (15.5.1), Proposition 15.5.5, Theorem 15.5.6.

# Verification Notes

- Definition source: Direct from Artin (15.5.1)
- Confidence rationale: Complete treatment with proofs
- Uncertainties: None
- Cross-reference status: Verified
