---
# === CORE IDENTIFICATION ===
concept: Normalizer Condition for Sylow Subgroups
slug: normalizer-condition-for-sylow

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
pdf_page: 94
section: "Nilpotent groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sylow-p-subgroup
  - normalizer
extends: []
related:
  - normalizer-growth-in-nilpotent-groups
  - nilpotent-iff-direct-product-of-sylow
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When does a subgroup containing the normalizer of a Sylow subgroup equal its own normalizer?"
---

# Quick Definition

If P is a Sylow p-subgroup of G and H is a subgroup containing N_G(P), then N_G(H) = H. This is because any element normalizing H would conjugate P to another Sylow subgroup of H, which can be conjugated back within H.

# Core Definition

**Lemma 6.19.** Let P be a Sylow p-subgroup of a finite group G. For any subgroup H of G containing N_G(P), we have N_G(H) = H.

(Milne, Lemma 6.19, p. 94)

# Prerequisites

- **sylow-p-subgroup** -- P is a Sylow p-subgroup
- **normalizer** -- N_G(P) and N_G(H)

# Key Properties

1. The proof: if g normalizes H, then gPg^{-1} is a Sylow subgroup of H, hence conjugate to P within H, so hg normalizes P for some h in H, giving g in H
2. This combines with Lemma 6.20 to show all Sylow subgroups of nilpotent groups are normal

# Relationships

## Builds Upon
- **sylow-p-subgroup** -- the Sylow subgroup whose normalizer is involved

## Enables
- **nilpotent-iff-direct-product-of-sylow** -- key lemma in the proof

# Source Reference

Chapter 6, Lemma 6.19, p. 94.

# Verification Notes

- Definition source: Direct from Lemma 6.19
- Confidence rationale: HIGH -- explicit lemma with proof
- Uncertainties: None
