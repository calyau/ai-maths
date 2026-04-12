---
# === CORE IDENTIFICATION ===
concept: Torus
slug: torus

# === CLASSIFICATION ===
category: group-actions
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Actions, Orbits, and Stabilizers"
chapter_number: 17
pdf_page: 98
section: "Exercise 17.9"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "C x C"
  - "S^1 x S^1"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
  - direct-product
extends: []
related:
  - product-action
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the torus in the context of group actions?"
---

# Quick Definition

The torus $C \times C$ ($= S^1 \times S^1$) is the product of two circles. Armstrong uses it to illustrate actions of $\mathbb{R}$ on the torus, including irrational-slope flows whose orbits are dense.

# Core Definition

The group $C \times C$ is called the **torus** (Armstrong, Exercise 17.9, p. 102). Here $C = S^1 = \{e^{ix} \mid x \in \mathbb{R}\}$ is the circle group.

Armstrong considers three actions of $\mathbb{R}$ on the torus:
- (a) $t$ sends $(e^{ix}, e^{iy})$ to $(e^{i(x+t)}, e^{iy})$ -- orbits are horizontal circles
- (b) $t$ sends $(e^{ix}, e^{iy})$ to $(e^{i(x+t)}, e^{i(y+t)})$ -- orbits are diagonal circles
- (c) $t$ sends $(e^{ix}, e^{iy})$ to $(e^{i(x+t)}, e^{i(y+t\sqrt{2})})$ -- orbits are dense

# Prerequisites

- **Group action** -- the torus is a space acted upon
- **Direct product** -- the torus is a product of two circle groups

# Key Properties

1. As a topological space, $C \times C$ is a torus (donut shape)
2. As a group, it is the direct product of two copies of the circle group
3. Actions of $\mathbb{R}$ on the torus with irrational slope produce dense orbits

# Context & Application

The torus provides a rich source of examples illustrating how different actions of the same group on the same space can produce qualitatively different orbit structures, from closed curves to dense subsets.

# Relationships

## Related
- **Product action** -- the torus naturally supports product actions
- **Group action** -- the torus is a fundamental example space

# Source Reference

Chapter 17: Actions, Orbits, and Stabilizers, Exercise 17.9, page 102.

# Verification Notes

- Definition: From Exercise 17.9, p. 102
- Confidence: MEDIUM -- defined in an exercise
