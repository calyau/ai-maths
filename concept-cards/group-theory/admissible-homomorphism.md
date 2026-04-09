---
# === CORE IDENTIFICATION ===
concept: Admissible Homomorphism
slug: admissible-homomorphism

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
aliases:
  - A-homomorphism

# === TYPED RELATIONSHIPS ===
prerequisites:
  - a-group-operators
  - admissible-subgroup
extends: []
related:
  - jordan-holder-for-a-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an admissible homomorphism between groups with operators?"
---

# Quick Definition

An admissible homomorphism (or A-homomorphism) between A-groups is a group homomorphism gamma: G -> G' such that gamma(^alpha x) = ^alpha gamma(x) for all alpha in A and x in G. It is a homomorphism that respects the operator action.

# Core Definition

An *A-homomorphism* (or *admissible homomorphism*) of A-groups is a homomorphism gamma: G -> G' such that gamma(^alpha x) = ^alpha gamma(x) for all alpha in A, x in G.

(Milne, p. 96)

# Prerequisites

- **a-group-operators** -- both domain and codomain must be A-groups
- **admissible-subgroup** -- kernels and images of admissible homomorphisms are admissible

# Key Properties

1. The kernel of an admissible homomorphism is an admissible normal subgroup
2. The image is an admissible subgroup
3. The isomorphism theorems hold with "admissible" throughout
4. An admissible isomorphism is an A-homomorphism that is also a bijection

# Relationships

## Builds Upon
- **a-group-operators** -- the framework

## Enables
- **jordan-holder-for-a-groups** -- uses admissible isomorphisms

# Source Reference

Chapter 6, p. 96. Theorems 6.26-6.28.

# Verification Notes

- Definition source: Direct from p. 96
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
