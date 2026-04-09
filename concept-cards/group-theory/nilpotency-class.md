---
# === CORE IDENTIFICATION ===
concept: Nilpotency Class
slug: nilpotency-class

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
aliases:
  - class of nilpotent group

# === TYPED RELATIONSHIPS ===
prerequisites:
  - nilpotent-group
  - upper-central-series
extends: []
related:
  - solvable-length
  - metabelian-group
contrasts_with:
  - solvable-length

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the nilpotency class of a group?"
  - "How is nilpotency class related to the upper central series?"
---

# Quick Definition

The nilpotency class of a nilpotent group G is the smallest m such that Z^m(G) = G. Class 0 is only {1}, class 1 is abelian, class 2 is metabelian.

# Core Definition

If G is nilpotent, the smallest m such that Z^m(G) = G is called the *(nilpotency) class* of G.

(Milne, p. 92)

# Prerequisites

- **nilpotent-group** -- nilpotency class is defined only for nilpotent groups
- **upper-central-series** -- the class is the length of this series

# Key Properties

1. Class 0: only {1}
2. Class 1: commutative groups
3. Class 2: metabelian groups (G/Z(G) is commutative)
4. G has class <= m iff [...[[g_1, g_2], g_3], ..., g_{m+1}] = 1 for all g_i (Proposition 6.15)
5. D_{2^n} has nilpotency class n (Example 6.12c)

# Context & Application

The nilpotency class measures "how far from abelian" a nilpotent group is. It determines how many central extensions are needed to build the group from abelian pieces.

# Examples

**Example 1** (p. 92): The 3x3 unitriangular group has class 2.
**Example 2** (p. 93, 6.12c): Any nonabelian group of order p^3 has class 2.
**Example 3** (p. 93, 6.12c): D_{2^n} has class n.

# Relationships

## Builds Upon
- **upper-central-series** -- the class is its length

## Related
- **metabelian-group** -- class 2 nilpotent groups

## Contrasts With
- **solvable-length** -- analogous measure for solvability; they are different invariants

# Source Reference

Chapter 6, p. 92, with examples on p. 93.

# Verification Notes

- Definition source: Direct from p. 92
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
