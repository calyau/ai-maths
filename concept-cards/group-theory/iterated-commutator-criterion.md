---
# === CORE IDENTIFICATION ===
concept: Iterated Commutator Criterion for Nilpotency
slug: iterated-commutator-criterion

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
pdf_page: 93
section: "Nilpotent groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - nilpotent-group
  - commutator
extends: []
related:
  - nilpotency-class
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can I test nilpotency using commutators?"
---

# Quick Definition

A group G is nilpotent of class at most m if and only if all iterated commutators of length m+1 vanish: [...[[g_1, g_2], g_3], ..., g_{m+1}] = 1 for all g_1, ..., g_{m+1} in G.

# Core Definition

**Proposition 6.15.** A group G is nilpotent of class <= m if and only if

[...[[g_1, g_2], g_3], ..., g_{m+1}] = 1

for all g_1, ..., g_{m+1} in G.

(Milne, Proposition 6.15, p. 93)

# Prerequisites

- **nilpotent-group** -- the property being characterized
- **commutator** -- iterated commutators are the key objects

# Key Properties

1. This gives a purely algebraic test for nilpotency without computing the central series
2. The direction "nilpotent implies vanishing" uses Z^m(G) = G to push commutators down the central series
3. The converse builds up the central series from the vanishing condition
4. For class 1 (abelian): [g_1, g_2] = 1 for all g_1, g_2
5. For class 2 (metabelian): [[g_1, g_2], g_3] = 1 for all g_1, g_2, g_3

# Relationships

## Builds Upon
- **nilpotent-group** -- characterized by this criterion

## Related
- **nilpotency-class** -- the length of the vanishing commutator

# Source Reference

Chapter 6, Proposition 6.15, p. 93.

# Verification Notes

- Definition source: Direct from Proposition 6.15
- Confidence rationale: HIGH -- explicit proposition with proof
- Uncertainties: None
