---
concept: Trisecting the Angle
slug: trisecting-the-angle
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
  - "trisection of the angle"
  - "impossibility of angle trisection"
prerequisites:
  - constructible-number
  - ruler-compass-construction
extends: []
related:
  - doubling-the-cube
contrasts_with: []
answers_questions:
  - "Why can't a general angle be trisected with ruler and compass?"
---

# Quick Definition

It is impossible to trisect a general angle using only ruler and compass. This is proved by showing that cos(20 degrees) has degree 3 over Q, which is not a power of 2.

# Core Definition

The impossibility of trisecting a general angle by ruler and compass is proved as follows (Artin, Lemma 15.5.8): Let alpha = 2*cos(20 degrees). Then alpha is a root of x^3 - 3x - 1, which is irreducible over Q. So alpha has degree 3 over Q. Since 3 is not a power of 2, cos(20 degrees) is not constructible. Since a 60-degree angle IS constructible, and trisecting it would require constructing 20 degrees, no general trisection method exists.

# Prerequisites

- **Constructible number** -- Must have degree a power of 2 over Q
- **Ruler and compass construction** -- The allowed tools

# Key Properties

1. cos(20 degrees) satisfies x^3 - 3x - 1 = 0 (via the identity for cos(3*theta))
2. This polynomial is irreducible over Q (no rational roots)
3. Degree 3 is not a power of 2
4. Many specific angles CAN be trisected (e.g., 45 degrees -> 15 degrees)
5. The impossibility is about a GENERAL method, not specific cases

# Context & Application

This is one of three famous Greek impossibility results proved using field theory. The proof elegantly reduces a geometric question to an algebraic one about polynomial degrees.

# Examples

**Example 1** (p. 467): The proof uses alpha = 2*cos(theta) where theta = pi/9, giving alpha^3 = 3*alpha + 1.

# Relationships

## Builds Upon
- **Constructible number** -- The degree criterion

## Related
- **Doubling the cube** -- Another classical impossibility

# Source Reference

Chapter 15: Fields, Section 15.5, pages 467-468. Lemma 15.5.8.

# Verification Notes

- Definition source: Direct from Artin, Lemma 15.5.8
- Confidence rationale: Complete proof given
- Uncertainties: None
- Cross-reference status: Verified
