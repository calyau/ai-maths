---
concept: Ideal Class
slug: ideal-class
category: number-theory
subcategory: class-group
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Quadratic Number Fields"
chapter_number: 13
pdf_page: 394
section: "Ideal Classes"
extraction_confidence: high
aliases:
  - "similarity class of ideals"
prerequisites:
  - ideal
  - ring-of-integers
extends: []
related:
  - class-group
  - class-number
contrasts_with: []
answers_questions:
  - "What is an ideal class?"
---

# Quick Definition

Two nonzero ideals A and A' are similar if A' = lambda*A for some complex number lambda. Similarity classes are called ideal classes. The class of the unit ideal consists of the principal ideals.

# Core Definition

Two nonzero ideals A and A' of R are similar if A' = lambda*A for some complex number lambda (Artin, formula 13.7.1, p. 410). Similarity classes are called ideal classes. The class (R) consists exactly of the principal ideals (Lemma 13.7.2). Geometrically, similar ideals are lattices that are similar geometric figures.

# Prerequisites

- **Ideal** -- Ideal classes are equivalence classes of ideals
- **Ring of integers** -- Context is the ring R

# Key Properties

1. The class of R = the class of principal ideals
2. Two ideals are similar iff they are "the same shape" as lattices
3. The number of ideal classes is the class number of R
4. R is a PID iff the class number is 1

# Examples

**Example 1** (p. 399): In Z[sqrt(-5)], there are exactly two ideal classes: principal ideals and non-principal ideals similar to (2, 1+delta).

# Relationships

## Builds Upon
- **Ideal** -- Classes are equivalence classes of ideals

## Enables
- **Class group** -- The set of ideal classes forms a group

# Source Reference

Chapter 13: Quadratic Number Fields, Section 13.7, pages 410-411.

# Verification Notes

- Definition source: Direct from formula 13.7.1 and Lemma 13.7.2
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
