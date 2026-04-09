---
# === CORE IDENTIFICATION ===
concept: Trisecting an Angle
slug: trisecting-an-angle

# === CLASSIFICATION ===
category: field-theory
subcategory: geometric-constructions
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Fields"
chapter_number: 21
pdf_page: 274
section: "21.3 Geometric Constructions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "angle trisection"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - constructible-number
  - tower-theorem
extends: []
related:
  - doubling-the-cube
  - squaring-the-circle
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why is trisecting an arbitrary angle impossible with straightedge and compass?"
---

# Quick Definition

Trisecting an arbitrary angle using only straightedge and compass is impossible. The proof shows that constructing a $20°$ angle (trisecting $60°$) requires solving an irreducible cubic, giving $[\mathbb{Q}(\cos 20°):\mathbb{Q}] = 3$, which is not a power of 2.

# Core Definition

Trisecting an arbitrary angle is impossible with straightedge and compass (Judson, p. 288). The proof shows that the $60°$ angle cannot be trisected: constructing a $20°$ angle requires $\alpha = \cos 20°$, which satisfies $8x^3 - 6x - 1 = 0$ (derived from $\cos 3\theta = 4\cos^3\theta - 3\cos\theta$). This polynomial is irreducible over $\mathbb{Q}$, so $[\mathbb{Q}(\alpha):\mathbb{Q}] = 3$, which is not a power of 2.

# Prerequisites

- **Constructible number** — Constructible numbers require degree a power of 2
- **Tower theorem** — Provides the degree constraint

# Key Properties

1. An angle $\theta$ is constructible if and only if $\cos\theta$ is constructible
2. The triple-angle formula: $\cos 3\theta = 4\cos^3\theta - 3\cos\theta$
3. For $\theta = 20°$: $\cos 60° = 1/2$ leads to $8\alpha^3 - 6\alpha - 1 = 0$
4. This cubic is irreducible over $\mathbb{Q}$, giving degree 3 (not a power of 2)
5. Some specific angles can be trisected (e.g., $90°$), but not all

# Context & Application

This problem demonstrates that impossibility results in mathematics are not about human ingenuity but about structural constraints. No matter how clever the construction, the algebraic degree prevents success.

# Examples

**Example 1** (p. 288): A $60°$ angle cannot be trisected because $\cos 20°$ satisfies the irreducible polynomial $8x^3 - 6x - 1$, giving $[\mathbb{Q}(\cos 20°):\mathbb{Q}] = 3$.

# Relationships

## Builds Upon
- **Constructible number** — Uses the degree characterization

## Related
- **Doubling the cube** — Another impossible construction with degree 3
- **Squaring the circle** — Another impossible construction (transcendence)

# Source Reference

Chapter 21: Fields, Section 21.3, pages 288–289.

# Verification Notes

- Definition source: Direct from p. 288
- Confidence: HIGH — explicit proof
- Cross-reference status: Verified
- Uncertainties: None
