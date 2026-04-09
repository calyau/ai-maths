---
# === CORE IDENTIFICATION ===
concept: Unique Sylow Subgroup Criterion
slug: unique-sylow-subgroup-criterion

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
pdf_page: 79
section: "The Sylow theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - normal Sylow subgroup criterion

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sylow-p-subgroup
  - sylow-second-theorem
  - normal-subgroup
extends:
  - sylow-second-theorem
related:
  - number-of-sylow-p-subgroups
  - direct-product-of-sylow-subgroups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When is a Sylow p-subgroup normal?"
  - "How do I know if a Sylow p-subgroup is unique?"
---

# Quick Definition

A Sylow p-subgroup is normal in G if and only if it is the only Sylow p-subgroup, i.e., s_p = 1. In that case, it is even characteristic.

# Core Definition

**Corollary 5.8.** A Sylow p-subgroup P is normal if and only if it is the only Sylow p-subgroup.

(Milne, Corollary 5.8, p. 79)

# Prerequisites

- **sylow-p-subgroup** -- the object in question
- **sylow-second-theorem** -- conjugacy implies normal iff unique
- **normal-subgroup** -- the concept of normality

# Key Properties

1. Normal implies unique: if P is normal, conjugation fixes P, so all Sylow p-subgroups equal P
2. Unique implies normal: the unique Sylow p-subgroup is fixed by all conjugations, hence normal
3. In fact, the unique Sylow p-subgroup is characteristic (since any automorphism sends it to a Sylow p-subgroup, of which there is only one)

# Context & Application

This is the most commonly used criterion in applications of Sylow theory. When the constraints on s_p force s_p = 1, you immediately get a normal subgroup, which is often the first step in decomposing a group as a semidirect product.

# Examples

**Example 1** (p. 81, 5.13): In a group of order 99, s_11 = 1 and s_3 = 1, so both Sylow subgroups are normal.

**Example 2** (p. 83, 5.19): For a simple group of order 60, s_2 = 1 is impossible since P would be normal, contradicting simplicity.

# Relationships

## Builds Upon
- **sylow-second-theorem** -- conjugacy is the reason normal iff unique

## Enables
- **direct-product-of-sylow-subgroups** -- when all Sylow subgroups are unique/normal
- **non-simplicity-criteria** -- s_p = 1 gives a normal subgroup, proving non-simplicity

# Source Reference

Chapter 5, Corollary 5.8, p. 79.

# Verification Notes

- Definition source: Direct from Corollary 5.8
- Confidence rationale: HIGH -- explicit corollary
- Uncertainties: None
