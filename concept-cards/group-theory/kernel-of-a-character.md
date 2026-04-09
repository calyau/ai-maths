---
# === CORE IDENTIFICATION ===
concept: Kernel of a Character
slug: kernel-of-a-character

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
  - character-of-a-representation
extends: []
related:
  - character-table
  - normal-subgroups-from-character-table
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the kernel of a character?"
  - "How are normal subgroups detected from the character table?"
---

# Quick Definition

The kernel of a character chi is ker(chi) = {g in G : chi(g) = chi(e)}, which is a normal subgroup of G. Every normal subgroup is an intersection of character kernels.

# Core Definition

The **kernel of a character** chi of a representation rho: G -> GL(V) is ker(rho) = {g in G : rho(g) = id_V} = {g in G : chi(g) = chi(e) = dim V}. This is a normal subgroup of G. The normal subgroups of G are exactly the intersections of kernels of some set of irreducible characters. In particular, the commutator subgroup G' is the intersection of the kernels of the linear characters. (Milne, Chapter 7, p. 119)

# Prerequisites

- **Character of a representation** — the kernel is defined for characters

# Key Properties

1. ker(chi) = {g : chi(g) = dim V} is a normal subgroup
2. The kernel is visible from the character table (entries equal to chi(e))
3. Every normal subgroup is an intersection of character kernels
4. G' = intersection of kernels of all linear characters
5. G is simple iff every non-trivial irreducible character has trivial kernel

# Construction / Recognition

1. From the character table, identify entries where chi_i(g) = chi_i(e)
2. These g form ker(chi_i)
3. Intersect character kernels to find all normal subgroups

# Context & Application

The ability to read normal subgroups from the character table is one of the most powerful applications of character theory. It means the character table encodes a great deal of group-theoretic information, even though it does not determine the group itself.

# Examples

**Example 1** (p. 119): For S_3, the sign character chi_1 has kernel A_3 = {e, (123), (132)}, which is the commutator subgroup.

# Relationships

## Builds Upon
- **character-of-a-representation** — kernels are defined for characters

## Enables
- **normal-subgroups-from-character-table** — reading off normal subgroups

## Related
- **character-table** — kernels are visible in the table

# Source Reference

Chapter 7: Representations of Finite Groups, p. 119.

# Verification Notes

- Definition source: Direct from p. 119
- Confidence rationale: HIGH — explicit discussion
- Uncertainties: None
