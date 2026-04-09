---
# === CORE IDENTIFICATION ===
concept: Normalizer Growth in Nilpotent Groups
slug: normalizer-growth-in-nilpotent-groups

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
aliases:
  - normalizer condition

# === TYPED RELATIONSHIPS ===
prerequisites:
  - nilpotent-group
  - normalizer
extends: []
related:
  - nilpotent-iff-direct-product-of-sylow
  - maximal-subgroups-of-nilpotent-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Does the normalizer of a proper subgroup always strictly contain it in a nilpotent group?"
---

# Quick Definition

In a finite nilpotent group, every proper subgroup is strictly contained in its normalizer: H properly contained in G implies H properly contained in N_G(H). This "normalizer growth" property fails for non-nilpotent groups.

# Core Definition

**Lemma 6.20.** Let H be a proper subgroup of a finite nilpotent group G. Then H != N_G(H), i.e., H is properly contained in its normalizer.

Proof: By induction on |G|. Since G is nilpotent, Z(G) != 1. If Z(G) is not contained in H, then Z(G) * H properly contains H and normalizes H. If Z(G) subset H, pass to G/Z(G) and apply induction (normalizers correspond under the quotient map).

(Milne, Lemma 6.20, p. 94-95)

# Prerequisites

- **nilpotent-group** -- the hypothesis
- **normalizer** -- N_G(H) is the key object

# Key Properties

1. This fails for non-nilpotent groups: in S_3, the normalizer of a Sylow 2-subgroup equals itself
2. Combined with Lemma 6.19, this shows all Sylow subgroups of a nilpotent group are normal
3. The proof crucially uses the nontriviality of Z(G) for nilpotent groups

# Relationships

## Builds Upon
- **nilpotent-group** -- the hypothesis

## Enables
- **nilpotent-iff-direct-product-of-sylow** -- key lemma in the proof

# Source Reference

Chapter 6, Lemma 6.20, pp. 94-95.

# Verification Notes

- Definition source: Direct from Lemma 6.20
- Confidence rationale: HIGH -- explicit lemma with proof
- Uncertainties: None
