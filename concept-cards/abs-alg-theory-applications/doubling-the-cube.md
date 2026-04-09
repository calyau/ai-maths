---
# === CORE IDENTIFICATION ===
concept: Doubling the Cube
slug: doubling-the-cube

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
  - "Delian problem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - constructible-number
  - tower-theorem
extends: []
related:
  - squaring-the-circle
  - trisecting-an-angle
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why is doubling the cube impossible with straightedge and compass?"
---

# Quick Definition

Doubling the cube is the ancient problem of constructing a cube with twice the volume of a given cube using only straightedge and compass. It is impossible because $\sqrt[3]{2}$ is not a constructible number.

# Core Definition

Given the edge of a cube, it is impossible to construct with a straightedge and compass the edge of a cube that has twice the volume of the original cube (Judson, p. 287).

**Proof:** A cube of volume 2 has edge length $\sqrt[3]{2}$. Since $\sqrt[3]{2}$ is a zero of the irreducible polynomial $x^3 - 2$ over $\mathbb{Q}$, we have $[\mathbb{Q}(\sqrt[3]{2}):\mathbb{Q}] = 3$. Since 3 is not a power of 2, $\sqrt[3]{2}$ is not constructible.

# Prerequisites

- **Constructible number** — The proof uses the characterization of constructible numbers
- **Tower theorem** — Degree constraints come from the tower theorem

# Key Properties

1. Requires constructing $\sqrt[3]{2}$
2. The minimal polynomial $x^3 - 2$ is irreducible over $\mathbb{Q}$
3. The degree $[\mathbb{Q}(\sqrt[3]{2}):\mathbb{Q}] = 3$ is not a power of 2
4. Therefore, the construction is impossible

# Context & Application

This is one of three famous ancient Greek construction problems, all shown to be impossible using field theory. The resolution came over two millennia after the problem was first posed, demonstrating the power of abstract algebra to settle geometric questions.

# Examples

**Example 1** (p. 287): Starting with a unit cube (edge length 1, volume 1), a cube of volume 2 would need edge length $\sqrt[3]{2} \approx 1.2599$. This length cannot be constructed.

# Relationships

## Builds Upon
- **Constructible number** — Uses the algebraic characterization

## Related
- **Squaring the circle** — Another impossible Greek construction
- **Trisecting an angle** — Another impossible Greek construction

# Source Reference

Chapter 21: Fields, Section 21.3, pages 287–288.

# Verification Notes

- Definition source: Direct from p. 287
- Confidence: HIGH — explicit impossibility proof
- Cross-reference status: Verified
- Uncertainties: None
