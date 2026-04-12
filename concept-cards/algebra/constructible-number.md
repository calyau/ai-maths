---
concept: Constructible Number
slug: constructible-number
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
  - "constructible real number"
prerequisites:
  - field-extension
  - degree-of-field-extension
extends: []
related:
  - trisecting-the-angle
  - doubling-the-cube
contrasts_with: []
answers_questions:
  - "What is a constructible number?"
  - "How do field extensions relate to geometric constructions?"
---

# Quick Definition

A real number a is constructible if the point (a, 0) can be constructed using ruler and compass starting from the points (0,0) and (1,0). Equivalently, a is algebraic over Q and its degree over Q is a power of 2.

# Core Definition

A real number a is constructible if there exists a chain of fields Q = F_0 in F_1 in ... in F_n = K such that K is a subfield of R, the coordinates of the constructed point are in K, and each [F_{i+1}:F_i] = 2 (Artin, Theorem 15.5.6). Therefore [K:Q] is a power of 2. Consequently, a constructible number is algebraic and its degree over Q is a power of 2 (Corollary 15.5.7).

# Prerequisites

- **Field extension** -- Constructibility involves chains of field extensions
- **Degree of field extension** -- Must be a power of 2

# Key Properties

1. The degree of a constructible number over Q is a power of 2 (15.5.7)
2. The constructible numbers form a subfield of R (Lemma 15.5.11(a))
3. If a > 0 is constructible, so is sqrt(a) (15.5.11(b))
4. The converse of 15.5.7 is false: not every number of degree 4 is constructible
5. Gauss proved: the regular p-gon (p prime) is constructible iff p = 2^r + 1

# Context & Application

Constructibility is the first major application of field theory in Artin's treatment. It elegantly proves the impossibility of three classical Greek problems: trisecting a general angle, doubling the cube, and squaring the circle.

# Examples

**Example 1** (p. 466): cos(20 degrees) has degree 3 over Q (it satisfies x^3 - 3x - 1 = 0, which is irreducible). Since 3 is not a power of 2, cos(20 degrees) is not constructible, proving that a 60-degree angle cannot be trisected.

**Example 2** (p. 467): The regular 7-gon is not constructible because the minimal polynomial x^6 + x^5 + ... + 1 has degree 6, and 6 is not a power of 2.

# Relationships

## Builds Upon
- **Degree of field extension** -- The degree must be a power of 2

## Enables
- **Impossibility proofs** -- Trisecting angle, doubling cube, etc.

## Related
- **Galois theory of cyclotomic fields** -- Determines which regular polygons are constructible

# Common Confusions

- **Confusion**: Thinking degree being a power of 2 is sufficient for constructibility
  **Clarification**: It is necessary but not sufficient. Galois theory provides a complete criterion.

# Source Reference

Chapter 15: Fields, Section 15.5, pages 463-470. Theorem 15.5.6, Corollary 15.5.7.

# Verification Notes

- Definition source: Direct from Artin, Theorem 15.5.6
- Confidence rationale: Complete treatment with classical applications
- Uncertainties: None
- Cross-reference status: Verified
