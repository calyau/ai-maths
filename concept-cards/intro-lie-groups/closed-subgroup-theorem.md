---
# === CORE IDENTIFICATION ===
concept: Closed Subgroup Theorem
slug: closed-subgroup-theorem

# === CLASSIFICATION ===
category: lie-groups
subcategory: subgroups
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups: Basic Definitions"
chapter_number: 2
pdf_page: 9
section: "2.1"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Cartan's theorem"
  - "Theorem 2.8"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
  - lie-subgroup
extends: []
related:
  - classical-group-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Lie group?"
---

# Quick Definition

Every closed subgroup of a Lie group is automatically a Lie subgroup (i.e., a smooth submanifold). Conversely, every Lie subgroup is closed.

# Core Definition

**Theorem 2.8** (Kirillov):
1. Any Lie subgroup is closed in $G$.
2. Any closed subgroup of a Lie group is a Lie subgroup.

# Prerequisites

- **Lie group** — the ambient group
- **Lie subgroup** — the concept being characterized

# Key Properties

1. Part (1) is proved using Exercise 2.1 (closure of $H$ is a subgroup, cosets are open and dense).
2. Part (2) is harder; uses Lie algebra techniques (see Section 3.6).
3. This gives a simple criterion: to show $H$ is a Lie subgroup, just show it is closed.

# Construction / Recognition

## To Construct/Create:
1. Take any closed subgroup $H \subset G$.
2. By this theorem, it automatically has smooth manifold structure.

## To Identify/Recognize:
1. A subgroup that is topologically closed.

# Context & Application

This is one of the most useful results in Lie group theory. It means that verifying a subgroup is a Lie subgroup requires only checking the topological condition of closedness.

# Examples

**Example**: All classical groups ($\mathrm{SL}(n)$, $\mathrm{O}(n)$, $\mathrm{U}(n)$, etc.) are closed in $\mathrm{GL}(n)$, hence Lie subgroups.

**Example**: The stabilizer of a continuous action is closed (preimage of a closed set), hence a Lie subgroup.

# Relationships

## Builds Upon
- **Lie subgroup** — characterizes when subgroups are Lie subgroups

## Enables
- **Easy verification** — just check closedness

## Related
- **Classical group theorem** — alternative approach using exponential map

# Common Errors

- **Error**: Applying the theorem to subgroups of infinite-dimensional groups.
  **Correction**: The theorem requires $G$ to be a finite-dimensional Lie group.

# Common Confusions

- **Confusion**: Whether a non-closed subgroup can still be a manifold.
  **Clarification**: A non-closed subgroup can be an immersed submanifold (immersed subgroup), but not an embedded one (Lie subgroup).

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.1, Theorem 2.8, pages 9-10.

# Verification Notes

- Definition source: Direct from Theorem 2.8
- Confidence rationale: Explicit theorem
- Uncertainties: Full proof of part (2) deferred to Chapter 3
- Cross-reference status: Verified with Section 3.6
