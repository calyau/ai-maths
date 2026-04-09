---
# === CORE IDENTIFICATION ===
concept: Jordan-Holder Theorem for A-Groups
slug: jordan-holder-for-a-groups

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
  - jordan-holder-theorem
  - a-group-operators
  - admissible-composition-series
  - isomorphism-theorems-for-a-groups
extends:
  - jordan-holder-theorem
related:
  - krull-schmidt-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Does the Jordan-Holder theorem hold for groups with operators?"
---

# Quick Definition

The Jordan-Holder theorem extends to A-groups: any two admissible composition series of an A-group have the same length and admissibly isomorphic quotients (up to reordering). The proof is identical to the original, using the isomorphism theorems for A-groups.

# Core Definition

The Jordan-Holder theorem continues to hold for A-groups. In this case the isomorphisms between the corresponding quotients of two admissible composition series are admissible. The proof is the same as that of the original theorem, because it uses only the isomorphism theorems, which also hold for A-groups.

(Milne, p. 96-97)

# Prerequisites

- **jordan-holder-theorem** -- the theorem being generalized
- **a-group-operators** -- the framework
- **admissible-composition-series** -- the objects compared
- **isomorphism-theorems-for-a-groups** -- the tools used in the proof

# Key Properties

1. The proof requires no new ideas beyond checking admissibility
2. When A = G (conjugation): quotients are isomorphic as G-groups (Example 6.29a)
3. When A = Aut(G): quotients are isomorphic as Aut(G)-groups (Example 6.29b)
4. The admissible composition factors may differ from the ordinary composition factors (since a simple A-group need not be simple as a group)

# Relationships

## Builds Upon
- **jordan-holder-theorem** -- the original theorem
- **isomorphism-theorems-for-a-groups** -- the foundation

## Related
- **krull-schmidt-theorem** -- another theorem that generalizes to A-groups

# Source Reference

Chapter 6, pp. 96-97. Examples 6.29.

# Verification Notes

- Definition source: Direct from p. 96-97
- Confidence rationale: HIGH -- explicitly stated generalization
- Uncertainties: None
