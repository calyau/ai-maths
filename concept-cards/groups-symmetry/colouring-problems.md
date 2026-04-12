---
# === CORE IDENTIFICATION ===
concept: Colouring Problems
slug: colouring-problems

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
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "counting colourings"
  - "Polya counting"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - counting-theorem
  - conjugate-fixed-point-sets
extends: []
related:
  - fixed-point-set
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I count distinct colourings of an object up to symmetry?"
  - "How do I apply the Counting Theorem to colouring problems?"
---

# Quick Definition

Colouring problems ask how many genuinely different ways an object can be decorated when two decorations that differ only by a symmetry are considered the same. These are solved by applying the Counting Theorem with the appropriate symmetry group.

# Core Definition

Armstrong frames colouring problems as orbit-counting problems. The set $X$ consists of all possible colourings (without regard to symmetry), and the symmetry group $G$ acts on $X$. Two colourings are "the same" if they lie in the same orbit. The Counting Theorem gives the number of distinct orbits as $\frac{1}{|G|}\sum_{g \in G} |X^g|$ (Armstrong, pp. 105--108).

# Prerequisites

- **Counting theorem** -- provides the formula for the number of distinct orbits
- **Conjugate fixed-point sets** -- allows computation by conjugacy classes

# Key Properties

1. $X$ is the set of all colourings (before accounting for symmetry)
2. $G$ is the symmetry group relevant to the problem
3. Two colourings are equivalent iff one is the image of the other under some $g \in G$
4. The number of distinct colourings equals the number of orbits
5. For each conjugacy class representative $g$, determine $|X^g|$ by analysing which colourings are preserved by $g$

# Construction / Recognition

## Procedure for Solving a Colouring Problem:
1. Identify the parts being coloured and the available colours
2. Count $|X|$ = (number of colours)$^{(\text{number of parts})}$
3. Identify the symmetry group $G$ acting on the colourings
4. List the conjugacy classes of $G$ with sizes
5. For each class representative $g$, find which colourings are fixed by $g$ (parts permuted by $g$ must all share the same colour)
6. Compute $|X^g|$ for each representative
7. Apply: number of distinct colourings $= \frac{1}{|G|}\sum (\text{class size}) \times |X^g|$

# Context & Application

Armstrong opens Chapter 18 with a motivating problem about children painting cube faces. The method applies to any combinatorial enumeration problem where symmetry identifies equivalent configurations, from molecular chemistry to pattern design.

# Examples

**Emily's Problem** (p. 105): Painting each face of a cube red or green. $|X| = 2^6 = 64$ colourings, $G = S_4$ (rotations of cube), $|G| = 24$. Result: 10 distinct cubes.

**Jerome's Problem** (p. 107): Painting stripes on subdivided cube faces. The symmetry group is $A_4$ (not $S_4$), giving 12 distinct cubes.

**Mobius Band** (p. 107): Painting 10 squares with 3 colours, symmetry group $D_{10}$, $|G| = 20$. Result: 3210 distinct painted bands.

**Dodecahedron** (Exercise 18.2, p. 108): Colouring faces red, white, or blue yields 9,099 distinct colourings.

# Relationships

## Builds Upon
- **Counting theorem** -- the core formula
- **Conjugate fixed-point sets** -- computational simplification

## Related
- **Fixed-point set** -- $|X^g|$ for a rotation $g$ counts colourings fixed by that rotation

# Common Errors

- **Error**: Using the wrong symmetry group.
  **Correction**: Jerome's problem uses $A_4$, not $S_4$, because the stripe pattern is not preserved by all rotations of the cube. Always verify which symmetries preserve the structure being decorated.

- **Error**: Forgetting that $|X^g|$ counts the number of colourings (not parts) fixed by $g$.
  **Correction**: A colouring is fixed by $g$ when every part that $g$ permutes to another part has the same colour as that other part.

# Common Confusions

- **Confusion**: Thinking two colourings are different if they look different from one viewpoint.
  **Clarification**: Two colourings are the same if one can be transformed into the other by any symmetry in $G$.

# Source Reference

Chapter 18: Counting Orbits, pages 105--109. Emily's problem pp. 105--107, Jerome's problem p. 107, Mobius band pp. 107--108.

# Verification Notes

- All numerical results verified against source text
- Confidence: HIGH -- the chapter is devoted to this application
