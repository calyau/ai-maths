---
# === CORE IDENTIFICATION ===
concept: Nilpotent Subgroups and Quotients
slug: nilpotent-subgroups-and-quotients

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
pdf_page: 92
section: "Nilpotent groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - nilpotent-group
extends: []
related:
  - solvability-closure-properties
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Are subgroups and quotients of nilpotent groups nilpotent?"
---

# Quick Definition

Subgroups and quotients of nilpotent groups are nilpotent. However, unlike solvable groups, an extension of nilpotent groups need not be nilpotent.

# Core Definition

**Proposition 6.13.**
(a) A subgroup of a nilpotent group is nilpotent.
(b) A quotient of a nilpotent group is nilpotent.

However, an extension of nilpotent groups need NOT be nilpotent (equation (27), p. 94): N and G/N nilpotent does not imply G nilpotent.

(Milne, Proposition 6.13, p. 92-93)

# Prerequisites

- **nilpotent-group** -- the property being studied

# Key Properties

1. For subgroups: Z^i(H) contains Z^i(G) intersect H, proved by induction
2. For quotients: images of the central series give a central series
3. The extension failure is a KEY difference from solvable groups
4. The exception: if N is contained in Z(G), then G/N nilpotent of class m implies G nilpotent of class <= m+1 (Corollary 6.16)

# Examples

**Example 1** (p. 94): The Borel subgroup B has U abelian and B/U abelian, but B is not nilpotent.

# Relationships

## Builds Upon
- **nilpotent-group** -- the property being studied

## Related
- **solvability-closure-properties** -- solvable groups DO have the extension property

# Common Errors

- **Error**: Assuming extensions of nilpotent groups are nilpotent (by analogy with solvable groups)
  **Correction**: This is FALSE. Central extensions preserve nilpotency, but general extensions do not.

# Source Reference

Chapter 6, Proposition 6.13, pp. 92-93. Extension failure: p. 94.

# Verification Notes

- Definition source: Direct from Proposition 6.13
- Confidence rationale: HIGH -- explicit proposition
- Uncertainties: None
