---
# === CORE IDENTIFICATION ===
concept: Abelian Variety
slug: abelian-variety

# === CLASSIFICATION ===
category: algebraic-groups
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 15
section: "Introductory overview"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
extends: []
related:
  - connected-algebraic-group
contrasts_with:
  - affine-algebraic-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

An abelian variety is a connected algebraic group that is projective as an algebraic variety. They are excluded from the theory of affine algebraic groups but appear in the structure theory: every connected algebraic group has a largest affine subgroup, with abelian variety quotient.

# Core Definition

**Abelian varieties** are connected algebraic groups that are projective when considered as algebraic varieties (p. 15). An abelian variety of dimension 1 is an elliptic curve.

Milne's book focuses exclusively on affine algebraic groups, which are exactly those realizable as closed subgroups of GL_n. However, abelian varieties appear in the structure theory: a connected algebraic group G contains a largest normal connected affine algebraic subgroup N, and G/N is an abelian variety (Barsotti-Chevalley-Rosenlicht theorem, summary 1c(b), p. 17).

# Prerequisites

- **Affine algebraic group** — Abelian varieties are the complementary class

# Key Properties

1. Connected and projective (not affine)
2. Automatically commutative (despite the name not requiring this a priori)
3. Cannot be embedded in GL_n
4. One of the five building block types of algebraic groups

# Examples

**Example 1** (p. 15): An elliptic curve Y^2Z = X^3 + bXZ^2 + cZ^3 is an abelian variety of dimension 1.

# Relationships

## Contrasts With
- **Affine algebraic group** — Abelian varieties are projective, not affine; affine groups embed in GL_n

# Source Reference

Chapter I, Section 1a (p. 15).

# Verification Notes

- Definition source: Direct from p. 15
- Confidence rationale: Explicit definition, though brief treatment
- Uncertainties: None
- Cross-reference status: Verified
