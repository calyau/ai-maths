---
# === CORE IDENTIFICATION ===
concept: Solvable vs. Nilpotent Groups
slug: solvable-vs-nilpotent

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
extraction_confidence: medium

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - solvable-group
  - nilpotent-group
extends: []
related:
  - solvable-borel-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between solvable and nilpotent groups?"
---

# Quick Definition

Every nilpotent group is solvable, but not every solvable group is nilpotent. The key distinction: nilpotent groups are built from abelian groups by *central* extensions, while solvable groups allow *arbitrary* extensions. Also, extensions of nilpotent groups need not be nilpotent, but extensions of solvable groups are always solvable.

# Core Definition

The contrast (Milne, p. 94):
- The *nilpotent groups* are those that can be obtained from commutative groups by successive **central** extensions.
- The *solvable groups* are those that can be obtained from commutative groups by successive extensions (**not necessarily central**).

Key differences:
1. Nilpotent implies solvable, but not conversely
2. Extensions of solvable groups are solvable (Proposition 6.6b); extensions of nilpotent groups need NOT be nilpotent
3. Finite nilpotent = direct product of p-groups; finite solvable has no such clean decomposition
4. Nilpotent groups have the normalizer growth property; solvable groups do not in general

(Milne, pp. 92-94)

# Prerequisites

- **solvable-group** -- one side of the comparison
- **nilpotent-group** -- the other side

# Examples

**Example 1** (p. 92, 6.12a): The Borel subgroup B of GL_2(F) is solvable (B > U > 1 with abelian quotients) but NOT nilpotent (Z(B/Z(B)) is trivial).

**Example 2**: Every p-group is nilpotent (hence solvable). But S_4 is solvable (derived series terminates) without being nilpotent (its Sylow 3-subgroup is not normal, so it is not a direct product of Sylow subgroups).

# Relationships

## Related
- **solvable-borel-subgroup** -- the canonical solvable-not-nilpotent example

# Common Confusions

- **Confusion**: Thinking that if N and G/N are nilpotent then G is nilpotent (by analogy with solvable groups)
  **Clarification**: This is FALSE for nilpotent but TRUE for solvable. Central extensions preserve nilpotency, but general extensions do not.

# Source Reference

Chapter 6, contrast stated on p. 94, Example 6.12a on p. 92.

# Verification Notes

- Definition source: Synthesis from pp. 92-94
- Confidence rationale: MEDIUM -- synthesized from multiple passages
- Uncertainties: None
