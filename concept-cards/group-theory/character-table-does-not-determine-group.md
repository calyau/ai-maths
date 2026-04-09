---
# === CORE IDENTIFICATION ===
concept: Character Table Does Not Determine the Group
slug: character-table-does-not-determine-group

# === CLASSIFICATION ===
category: character-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 119
section: "The character table of a group"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - character-table
extends: []
related:
  - character-table-of-d4
  - character-table-of-q8
contrasts_with:
  - characters-determine-representations

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Does the character table determine the group?"
  - "Can non-isomorphic groups have the same character table?"
---

# Quick Definition

The character table does not determine a finite group up to isomorphism. The groups D_4 and Q_8 have the same character table but are not isomorphic.

# Core Definition

Non-isomorphic groups can have identical character tables. The smallest examples are D_4 (dihedral group of order 8) and Q_8 (quaternion group of order 8), which have the same character table (Examples 7.55-7.56) but are not isomorphic. For abelian groups, the character table does determine the group since G is isomorphic to (G^v)^v. (Milne, Chapter 7, pp. 118-119)

# Prerequisites

- **Character table** — the object in question

# Key Properties

1. D_4 and Q_8 have identical character tables (same 5x5 matrix of values)
2. They are the first example: order 8 is the smallest order with two non-isomorphic noncommutative groups
3. For abelian groups, the character table does determine the group
4. The character table does determine: normal subgroups, commutator subgroup, many structural invariants

# Examples

**Example 1** (pp. 118-119, 7.55-7.56): Both D_4 and Q_8 have character table with rows (1,1,1,1,1), (1,1,1,-1,-1), (1,1,-1,1,-1), (1,1,-1,-1,1), (2,-2,0,0,0).

# Relationships

## Builds Upon
- **character-table** — the invariant being tested

## Related
- The question of what invariants distinguish D_4 from Q_8

## Contrasts With
- **characters-determine-representations** — characters determine reps, but the character table doesn't determine the group

# Source Reference

Chapter 7: Representations of Finite Groups, Examples 7.55-7.56 and discussion, pp. 118-119.

# Verification Notes

- Definition source: Direct from pp. 118-119
- Confidence rationale: HIGH — explicit examples
- Uncertainties: None
