---
# === CORE IDENTIFICATION ===
concept: Maximal Subgroups of Nilpotent Groups
slug: maximal-subgroups-of-nilpotent-groups

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
  - normalizer-growth-in-nilpotent-groups
  - frattinis-argument
extends: []
related:
  - nilpotent-iff-direct-product-of-sylow
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Are maximal subgroups of nilpotent groups always normal?"
  - "Does this characterize nilpotent groups?"
---

# Quick Definition

A finite group is nilpotent if and only if every maximal proper subgroup is normal. The "only if" follows from normalizer growth (Lemma 6.20); the "if" follows from Frattini's argument.

# Core Definition

**Theorem 6.23.** A finite group is nilpotent if and only if every maximal proper subgroup is normal.

(Milne, Theorem 6.23, p. 95)

# Prerequisites

- **nilpotent-group** -- the property being characterized
- **normalizer-growth-in-nilpotent-groups** -- H maximal and N_G(H) properly contains H implies N_G(H) = G
- **frattinis-argument** -- used in the converse direction

# Key Properties

1. Forward: if G is nilpotent and H is maximal, then N_G(H) properly contains H (Lemma 6.20), so N_G(H) = G, meaning H is normal
2. Converse: if every maximal subgroup is normal and P is a Sylow subgroup, then any maximal H containing N_G(P) would be normal, and Frattini gives G = H * N_G(P) = H, contradiction
3. This provides yet another characterization of finite nilpotent groups

# Relationships

## Builds Upon
- **normalizer-growth-in-nilpotent-groups** -- the forward direction
- **frattinis-argument** -- the reverse direction

## Related
- **nilpotent-iff-direct-product-of-sylow** -- another characterization

# Source Reference

Chapter 6, Theorem 6.23, p. 95.

# Verification Notes

- Definition source: Direct from Theorem 6.23
- Confidence rationale: HIGH -- explicit theorem with proof
- Uncertainties: None
