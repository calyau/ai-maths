---
# === CORE IDENTIFICATION ===
concept: Normal Subgroups from the Character Table
slug: normal-subgroups-from-character-table

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
  - kernel-of-a-character
  - character-table
extends: []
related:
  - irreducible-character
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can normal subgroups be read from the character table?"
  - "How does the character table encode the lattice of normal subgroups?"
---

# Quick Definition

The normal subgroups of G are exactly the intersections of kernels of irreducible characters. They can be read off from the character table.

# Core Definition

It is possible to read off the normal subgroups of G from its character table. The kernel of a character can be seen in the table, and the **normal subgroups are exactly the intersections of the kernels of some set of characters**. The commutator subgroup G' is the intersection of the kernels of the linear characters. (Milne, Chapter 7, p. 119)

# Prerequisites

- **Kernel of a character** — normal subgroups are intersections of character kernels
- **Character table** — the data source

# Key Properties

1. Normal subgroups = intersections of character kernels
2. Visible from the character table alone
3. The commutator subgroup = intersection of kernels of linear (degree 1) characters
4. This does not require knowing the group multiplication

# Context & Application

This result demonstrates the power of the character table as an invariant: while it does not determine G itself (D_4 and Q_8 have the same character table), it determines the lattice of normal subgroups, the commutator subgroup, and many other structural features of G.

# Examples

**Example 1** (p. 119): For S_3, the linear characters chi_0, chi_1 have kernels S_3 and A_3 respectively. The intersection A_3 is the commutator subgroup.

# Relationships

## Builds Upon
- **kernel-of-a-character** — the building blocks
- **character-table** — the data source

## Related
- **irreducible-character** — kernels of irreducible characters generate all normal subgroups

# Source Reference

Chapter 7: Representations of Finite Groups, p. 119.

# Verification Notes

- Definition source: Direct from p. 119
- Confidence rationale: HIGH — explicit statement
- Uncertainties: None
