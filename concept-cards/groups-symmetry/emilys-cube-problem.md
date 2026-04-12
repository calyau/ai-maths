---
# === CORE IDENTIFICATION ===
concept: "Emily's Cube Colouring Problem"
slug: emilys-cube-problem

# === CLASSIFICATION ===
category: group-actions
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Counting Orbits"
chapter_number: 18
pdf_page: 105
section: "Emily's Problem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "cube colouring problem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - counting-theorem
  - conjugate-fixed-point-sets
extends: []
related:
  - colouring-problems
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How many distinct ways can the faces of a cube be painted with two colours?"
---

# Quick Definition

Painting each face of a cube either red or green, there are 10 genuinely different coloured cubes (up to rotation). This is Armstrong's motivating example for the Counting Theorem.

# Core Definition

There are $2^6 = 64$ total coloured cubes (6 faces, 2 colours). The rotational symmetry group $S_4$ (order 24) acts on these. Using the Counting Theorem with conjugacy class representatives $e, r, r^2, s, t$ (Armstrong, pp. 105--107):

$$\frac{1}{24}\{(6 \times 2^3) + (3 \times 2^4) + (8 \times 2^2) + (6 \times 2^3) + 2^6\} = 10$$

# Prerequisites

- **Counting theorem** -- the formula used
- **Conjugate fixed-point sets** -- allows computation by conjugacy class

# Key Properties

1. The symmetry group is $S_4$ (rotational symmetry group of the cube), order 24
2. Five conjugacy classes: identity (1), face rotations $r$ (6), half-turns $r^2$ (3), vertex rotations $s$ (8), edge rotations $t$ (6)
3. Fixed-point counts: $|X^e| = 64$, $|X^r| = 8$, $|X^{r^2}| = 16$, $|X^s| = 4$, $|X^t| = 8$
4. Result: 10 distinct coloured cubes

# Construction / Recognition

## Computing $|X^g|$:
- $r$ (face rotation by $90^\circ$): cycles 4 vertical faces, so those 4 must match. Free: top, bottom, verticals. $|X^r| = 2^3 = 8$
- $s$ (vertex rotation by $120^\circ$): cycles faces in two groups of 3. $|X^s| = 2^2 = 4$
- $r^2$ (face rotation by $180^\circ$): pairs vertical faces. Free: top, bottom, 2 pairs. $|X^{r^2}| = 2^4 = 16$
- $t$ (edge rotation by $180^\circ$): swaps top/bottom and pairs side faces. $|X^t| = 2^3 = 8$

# Context & Application

This is the first worked example in Chapter 18, used to motivate the Counting Theorem. Armstrong frames it as a competition between children Emily and Jerome.

# Relationships

## Builds Upon
- **Counting theorem** -- applied directly

## Related
- **Colouring problems** -- this is the prototypical example

# Source Reference

Chapter 18: Counting Orbits, pages 105--107. Complete worked solution on pp. 106--107.

# Verification Notes

- All numerical values verified against source
- Confidence: HIGH -- complete worked example
