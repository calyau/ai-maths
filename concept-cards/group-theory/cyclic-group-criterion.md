---
# === CORE IDENTIFICATION ===
concept: Cyclic Group Criterion
slug: cyclic-group-criterion

# === CLASSIFICATION ===
category: sylow-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "The Sylow Theorems; Applications"
chapter_number: 5
pdf_page: 85
section: "Exercises"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - sylow-p-subgroup
extends: []
related:
  - cauchys-theorem-from-sylow
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When is a finite group cyclic?"
---

# Quick Definition

A finite group (not necessarily commutative) is cyclic if, for each n > 0, it contains at most n elements of order dividing n. This criterion uses the Sylow theorems in its proof.

# Core Definition

**Exercise 5-1.** Show that a finite group (not necessarily commutative) is cyclic if, for each n > 0, it contains at most n elements of order dividing n.

(Milne, Exercise 5-1, p. 85)

# Prerequisites

- **group** -- the ambient group
- **sylow-p-subgroup** -- the proof uses Sylow theory

# Key Properties

1. The condition says that x^n = 1 has at most n solutions for every n
2. This is automatically satisfied by cyclic groups (and by subgroups of the multiplicative group of a field)
3. The content of the exercise is the converse: this condition *forces* the group to be cyclic
4. This is used to prove that finite subgroups of F* are cyclic

# Relationships

## Builds Upon
- **sylow-p-subgroup** -- the proof technique

## Related
- **cauchys-theorem-from-sylow** -- element order control

# Source Reference

Chapter 5, Exercise 5-1, p. 85.

# Verification Notes

- Definition source: From Exercise 5-1
- Confidence rationale: MEDIUM -- exercise statement, proof not given
- Uncertainties: Proof details are left as exercise
