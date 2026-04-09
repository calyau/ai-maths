---
# === CORE IDENTIFICATION ===
concept: Admissible Subgroup
slug: admissible-subgroup

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
pdf_page: 95
section: "Groups with operators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - A-invariant subgroup

# === TYPED RELATIONSHIPS ===
prerequisites:
  - a-group-operators
extends: []
related:
  - normal-subgroup
  - characteristic-subgroup
  - admissible-homomorphism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an admissible subgroup in the theory of groups with operators?"
---

# Quick Definition

A subgroup H of an A-group G is admissible (or A-invariant) if ^alpha x is in H for all x in H and all alpha in A. When A = G acting by conjugation, admissible = normal. When A = Aut(G), admissible = characteristic.

# Core Definition

Let G be a group with operators A. A subgroup H of G is *admissible* or *A-invariant* if

x in H implies ^alpha x in H, for all alpha in A.

An intersection of admissible groups is admissible. If H is admissible, so also are its normalizer N_G(H) and centralizer C_G(H).

(Milne, p. 95-96)

# Prerequisites

- **a-group-operators** -- the framework of groups with operators

# Key Properties

1. Intersections of admissible subgroups are admissible
2. Normalizers and centralizers of admissible subgroups are admissible
3. When A = {1}: all subgroups are admissible
4. When A = G (conjugation): admissible = normal
5. When A = Aut(G): admissible = characteristic

# Relationships

## Builds Upon
- **a-group-operators** -- the context

## Related
- **normal-subgroup** -- the A = G (conjugation) case
- **characteristic-subgroup** -- the A = Aut(G) case
- **admissible-homomorphism** -- maps that respect the operator action

# Source Reference

Chapter 6, pp. 95-96.

# Verification Notes

- Definition source: Direct from p. 95-96
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
