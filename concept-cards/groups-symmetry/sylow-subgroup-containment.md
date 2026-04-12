---
# === CORE IDENTIFICATION ===
concept: Sylow Subgroup Containment
slug: sylow-subgroup-containment

# === CLASSIFICATION ===
category: finite-group-classification
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "The Sylow Theorems"
chapter_number: 20
pdf_page: 120
section: "Exercise 20.13"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - first-sylow-theorem
  - second-sylow-theorem
extends:
  - first-sylow-theorem
related:
  - sylow-p-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Is every p-subgroup contained in a Sylow p-subgroup?"
---

# Quick Definition

Every subgroup $J$ of $G$ whose order is a power of a prime $p$ is contained in some Sylow $p$-subgroup of $G$.

# Core Definition

If $J$ is a subgroup of $G$ whose order is a power of a prime $p$, then $J$ must be contained in a Sylow $p$-subgroup of $G$ (Armstrong, Exercise 20.13, p. 125).

# Prerequisites

- **First Sylow theorem** -- ensures Sylow $p$-subgroups exist
- **Second Sylow theorem** -- conjugacy is used in the proof

# Key Properties

1. Every $p$-subgroup sits inside a maximal $p$-subgroup (a Sylow $p$-subgroup)
2. The proof uses the action of $J$ on the set of left cosets of a Sylow $p$-subgroup $H$ (Exercise 20.11)
3. This is a maximality statement: Sylow $p$-subgroups are the largest $p$-subgroups

# Context & Application

This result confirms that Sylow $p$-subgroups are indeed the maximal $p$-subgroups. It is useful for showing that a given $p$-subgroup extends to a Sylow subgroup.

# Relationships

## Builds Upon
- **First Sylow theorem** -- existence of Sylow subgroups
- **Second Sylow theorem** -- conjugacy used in proof

## Related
- **Sylow p-subgroup** -- the maximal $p$-subgroups

# Source Reference

Chapter 20: The Sylow Theorems, Exercise 20.13, page 125.

# Verification Notes

- Statement: From Exercise 20.13, p. 125
- Confidence: MEDIUM -- stated as an exercise
