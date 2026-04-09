---
# === CORE IDENTIFICATION ===
concept: Metabelian Group
slug: metabelian-group

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
  - nilpotency-class
extends:
  - nilpotent-group
related:
  - groups-of-order-p-cubed
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a metabelian group?"
---

# Quick Definition

A metabelian group is a nilpotent group of class 2, meaning G/Z(G) is commutative, or equivalently, all commutators lie in the center.

# Core Definition

A group G is of class 2 if and only if G/Z(G) is commutative -- such a group is said to be *metabelian*.

(Milne, p. 92)

# Prerequisites

- **nilpotent-group** -- metabelian is nilpotent of class 2
- **nilpotency-class** -- class 2 means Z^2(G) = G

# Key Properties

1. G/Z(G) is abelian
2. All commutators [x, y] lie in Z(G)
3. [[x, y], z] = 1 for all x, y, z in G
4. Every nonabelian group of order p^3 is metabelian (Example 6.12c)

# Examples

**Example 1** (p. 92, 6.12b): The 3x3 unitriangular group over any field is metabelian.

**Example 2** (p. 93, 6.12c): Any nonabelian group of order p^3 is metabelian (G' = Z(G) has order p).

**Example 3** (p. 93, 6.12c): Q_8 (quaternion group) and D_4 (dihedral group of order 8) are metabelian.

# Relationships

## Builds Upon
- **nilpotent-group** -- metabelian = nilpotent of class 2

## Related
- **groups-of-order-p-cubed** -- all nonabelian groups of order p^3 are metabelian

# Source Reference

Chapter 6, p. 92.

# Verification Notes

- Definition source: Direct from p. 92
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
