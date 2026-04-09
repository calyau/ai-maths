---
# === CORE IDENTIFICATION ===
concept: Isomorphism Theorems for A-Groups
slug: isomorphism-theorems-for-a-groups

# === CLASSIFICATION ===
category: groups-with-operators
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Subnormal Series; Solvable and Nilpotent Groups"
chapter_number: 6
pdf_page: 96
section: "Groups with operators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - a-group-operators
  - admissible-subgroup
  - admissible-homomorphism
extends: []
related:
  - jordan-holder-for-a-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Do the isomorphism theorems hold for groups with operators?"
---

# Quick Definition

The standard isomorphism theorems (first, second, and correspondence) hold for A-groups, with all subgroups required to be admissible and all homomorphisms/isomorphisms required to be admissible. The proofs are the same as for ordinary groups with admissibility checked.

# Core Definition

**Theorem 6.26** (First Isomorphism Theorem for A-groups): For any admissible homomorphism gamma: G -> G', Ker(gamma) is an admissible normal subgroup, gamma(G) is admissible, and G/Ker(gamma) is admissibly isomorphic to gamma(G).

**Theorem 6.27** (Second Isomorphism Theorem): For admissible H, N with N normal, H intersect N is admissible normal in H, HN is admissible, and H/(H intersect N) is admissibly isomorphic to HN/N.

**Theorem 6.28** (Correspondence Theorem): Under a surjective admissible homomorphism, admissible subgroups correspond to admissible subgroups.

(Milne, Theorems 6.26-6.28, p. 96)

# Prerequisites

- **a-group-operators** -- the framework
- **admissible-subgroup** -- all subgroups must be admissible
- **admissible-homomorphism** -- all maps must be admissible

# Key Properties

1. The proofs are identical to the ordinary case, with admissibility verified at each step
2. These theorems are the foundation for the Jordan-Holder theorem for A-groups

# Relationships

## Builds Upon
- **admissible-homomorphism** -- the maps in the theorems

## Enables
- **jordan-holder-for-a-groups** -- uses these isomorphism theorems

# Source Reference

Chapter 6, Theorems 6.26-6.28, p. 96.

# Verification Notes

- Definition source: Direct from Theorems 6.26-6.28
- Confidence rationale: HIGH -- explicit theorems
- Uncertainties: None
