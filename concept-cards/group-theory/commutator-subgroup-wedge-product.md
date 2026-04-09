---
# === CORE IDENTIFICATION ===
concept: Commutator Map and Exterior Product
slug: commutator-subgroup-wedge-product

# === CLASSIFICATION ===
category: nilpotent-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Subnormal Series; Solvable and Nilpotent Groups"
chapter_number: 6
pdf_page: 95
section: "Nilpotent groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - nilpotent-group
  - metabelian-group
  - commutator-subgroup
extends: []
related:
  - ores-conjecture
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do commutators relate to exterior products for nilpotent groups of class 2?"
---

# Quick Definition

For a nilpotent group G of class 2 with central extension 1 -> A -> G -> B -> 1 (A, B abelian, A subset Z(G)), taking commutators induces a map from the exterior square of B to A. The image is the commutator subgroup, and the image of pure tensors is the set of actual commutators. This can produce examples where G' contains elements that are not commutators.

# Core Definition

**Aside 6.24.** Consider a nilpotent group G of class 2:

1 -> A -> G -> B -> 1, with A, B commutative, A subset Z(G).

Taking commutators induces a map wedge^2 B -> A (and every such map occurs for some extension). The image of this map is the commutator subgroup and the image of the pure tensors b wedge b' is the set of actual commutators. This can be used to give examples of groups whose commutator subgroup doesn't consist entirely of commutators.

(Milne, Aside 6.24, p. 95)

# Prerequisites

- **nilpotent-group** -- G has class 2
- **metabelian-group** -- the setting
- **commutator-subgroup** -- the image of the commutator map

# Key Properties

1. The commutator map [,]: G x G -> A factors through wedge^2 B -> A
2. Elements of wedge^2 B that are not pure tensors correspond to elements of G' that are not commutators
3. This gives a systematic source of "non-commutator" elements in G'

# Relationships

## Related
- **ores-conjecture** -- the question of which elements of G' are commutators

# Source Reference

Chapter 6, Aside 6.24, p. 95.

# Verification Notes

- Definition source: Direct from Aside 6.24
- Confidence rationale: HIGH -- explicit aside
- Uncertainties: None
