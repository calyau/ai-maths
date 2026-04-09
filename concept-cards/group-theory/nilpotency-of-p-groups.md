---
# === CORE IDENTIFICATION ===
concept: Nilpotency of p-Groups
slug: nilpotency-of-p-groups

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
  - p-group
  - central-extension-and-nilpotency
extends: []
related:
  - solvability-of-p-groups
  - nilpotent-iff-direct-product-of-sylow
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Is every finite p-group nilpotent?"
---

# Quick Definition

Every finite p-group is nilpotent. The proof uses the nontriviality of Z(G) for p-groups and induction via central extensions.

# Core Definition

**Corollary 6.17.** A finite p-group is nilpotent.

Proof: By induction on |G|. Since Z(G) != 1 (by 4.16), G/Z(G) is nilpotent by induction, and then Corollary 6.16 shows G is nilpotent.

(Milne, Corollary 6.17, p. 94)

# Prerequisites

- **p-group** -- the hypothesis
- **central-extension-and-nilpotency** -- the key tool: G/Z(G) nilpotent plus Z(G) central gives G nilpotent

# Key Properties

1. This is stronger than solvability of p-groups
2. The nilpotency class of a p-group can be arbitrarily large
3. Combined with Theorem 6.18, this says every finite nilpotent group is a direct product of p-groups

# Relationships

## Builds Upon
- **central-extension-and-nilpotency** -- the induction step

## Related
- **solvability-of-p-groups** -- weaker consequence
- **nilpotent-iff-direct-product-of-sylow** -- finite nilpotent = direct product of p-groups

# Source Reference

Chapter 6, Corollary 6.17, p. 94.

# Verification Notes

- Definition source: Direct from Corollary 6.17
- Confidence rationale: HIGH -- explicit corollary
- Uncertainties: None
