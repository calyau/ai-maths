---
# === CORE IDENTIFICATION ===
concept: Squaring the Circle
slug: squaring-the-circle

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
  - "quadrature of the circle"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - constructible-number
  - transcendental-element
extends: []
related:
  - doubling-the-cube
  - trisecting-an-angle
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why is squaring the circle impossible?"
---

# Quick Definition

Squaring the circle is the problem of constructing a square with the same area as a given circle using only straightedge and compass. It is impossible because $\sqrt{\pi}$ (and hence $\pi$) is transcendental over $\mathbb{Q}$.

# Core Definition

Given a circle of radius 1, its area is $\pi$, so we must construct a square with side $\sqrt{\pi}$. This is impossible since $\pi$ and consequently $\sqrt{\pi}$ are both transcendental over $\mathbb{Q}$ (Judson, p. 288). Transcendental numbers are not constructible because constructible numbers are algebraic (Corollary 21.44).

# Prerequisites

- **Constructible number** — Constructible numbers must be algebraic
- **Transcendental element** — $\pi$ is transcendental over $\mathbb{Q}$

# Key Properties

1. Requires constructing $\sqrt{\pi}$
2. $\pi$ is transcendental over $\mathbb{Q}$ (proven by Lindemann, 1882)
3. $\sqrt{\pi}$ is also transcendental over $\mathbb{Q}$
4. All constructible numbers are algebraic, so $\sqrt{\pi}$ is not constructible

# Context & Application

Unlike doubling the cube and trisecting an angle (which fail because the degree is not a power of 2), squaring the circle fails for a more fundamental reason: $\pi$ is not even algebraic. This required proving the transcendence of $\pi$, which was not accomplished until the late 19th century.

# Examples

**Example 1** (p. 288): A circle of radius 1 has area $\pi$. A square of the same area would have side length $\sqrt{\pi} \approx 1.7725$. This length is not constructible.

# Relationships

## Builds Upon
- **Constructible number** — Constructible numbers are algebraic
- **Transcendental element** — $\pi$ is transcendental

## Related
- **Doubling the cube** — Another impossible construction
- **Trisecting an angle** — Another impossible construction

# Source Reference

Chapter 21: Fields, Section 21.3, page 288.

# Verification Notes

- Definition source: Direct from p. 288
- Confidence: HIGH — explicit proof of impossibility
- Cross-reference status: Verified
- Uncertainties: None
