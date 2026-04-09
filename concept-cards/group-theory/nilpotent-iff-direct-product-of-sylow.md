---
# === CORE IDENTIFICATION ===
concept: Nilpotent iff Direct Product of Sylow Subgroups
slug: nilpotent-iff-direct-product-of-sylow

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
  - nilpotent-group
  - sylow-p-subgroup
  - direct-product-of-sylow-subgroups
  - normalizer-growth-in-nilpotent-groups
  - normalizer-condition-for-sylow
extends: []
related:
  - nilpotency-of-p-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When is a finite group a direct product of its Sylow subgroups?"
  - "What characterizes finite nilpotent groups?"
---

# Quick Definition

A finite group is nilpotent if and only if it is the direct product of its Sylow subgroups. This provides a complete structural description of finite nilpotent groups.

# Core Definition

**Theorem 6.18.** A finite group is nilpotent if and only if it is equal to a direct product of its Sylow subgroups.

(Milne, Theorem 6.18, p. 94)

# Prerequisites

- **nilpotent-group** -- the property being characterized
- **sylow-p-subgroup** -- the factors in the direct product
- **direct-product-of-sylow-subgroups** -- Corollary 5.9: all Sylow normal implies direct product
- **normalizer-growth-in-nilpotent-groups** -- Lemma 6.20: H properly contained in N_G(H)
- **normalizer-condition-for-sylow** -- Lemma 6.19: H containing N_G(P) satisfies N_G(H) = H

# Key Properties

1. "If" direction: direct product of p-groups is nilpotent (p-groups are nilpotent, product of nilpotent is nilpotent)
2. "Only if" direction: in a nilpotent group, every Sylow subgroup is normal
3. The proof uses two lemmas: N_G(H) = H for H containing N_G(P) (Lemma 6.19), and H properly contained in N_G(H) for proper H in nilpotent G (Lemma 6.20)
4. Combining: if P is a Sylow subgroup of nilpotent G, then N_G(P) = G, so P is normal

# Context & Application

This is the definitive structural theorem for finite nilpotent groups. It reduces their study to the study of p-groups. For finite abelian groups, this recovers the decomposition into p-primary components (Remark 6.21).

# Relationships

## Builds Upon
- **nilpotent-group** -- the property being characterized
- **direct-product-of-sylow-subgroups** -- the structural consequence

## Related
- **nilpotency-of-p-groups** -- p-groups are nilpotent (the building blocks)

# Common Confusions

- **Confusion**: Thinking every group with all Sylow subgroups normal is abelian
  **Clarification**: All Sylow subgroups normal means nilpotent (direct product of p-groups), but p-groups can be nonabelian

# Source Reference

Chapter 6, Theorem 6.18, p. 94. Lemmas 6.19 and 6.20 on pp. 94-95.

# Verification Notes

- Definition source: Direct from Theorem 6.18
- Confidence rationale: HIGH -- explicit theorem with proof
- Uncertainties: None
