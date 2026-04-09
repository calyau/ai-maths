---
# === CORE IDENTIFICATION ===
concept: Abelian Group
slug: abelian-group

# === CLASSIFICATION ===
category: group-fundamentals
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 8
section: "Definitions and examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - commutative group

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends:
  - group
related:
  - torsion-subgroup
  - cyclic-group
contrasts_with:
  - symmetric-group
  - dihedral-group
  - quaternion-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an abelian group?"
  - "What is a commutative group?"
  - "What distinguishes abelian groups from non-abelian groups?"
---

# Quick Definition

A group G is abelian (or commutative) if ab = ba for all elements a, b in G. Abelian groups are usually written in additive notation.

# Core Definition

A group is **commutative** (or **abelian**) if ab = ba for all a, b in G (1.6, p. 8). Milne notes that "'abelian group' is more common than 'commutative group', but I prefer to use descriptive names" (footnote 1, p. 8).

In a commutative group, the product of any finite (not necessarily ordered) family of elements is well defined; in particular, the empty product is e. Commutative groups are usually written additively, with the exponent law becoming ma + na = (m+n)a and m(na) = (mn)a.

When G is commutative, m(a + b) = ma + mb for m in Z and a, b in G, making G into a Z-module via the map (m, a) -> ma : Z x G -> G (p. 9).

# Prerequisites

- **Group** — an abelian group is a group with an additional property

# Key Properties

1. ab = ba for all a, b in G
2. Products are independent of ordering
3. Every commutative group is naturally a Z-module
4. The torsion elements (elements of finite order) form a subgroup G_tors (p. 9)
5. Every cyclic group is abelian
6. Usually written with additive notation (+, 0) instead of multiplicative (*, 1)

# Construction / Recognition

## To Recognize:
1. Check that ab = ba for all pairs a, b in G
2. Equivalently, check that the multiplication table is symmetric about the diagonal

# Context & Application

Abelian groups form a major subclass of groups with richer structural theory. They are the groups where the operation does not depend on the order of the operands. In the classification of groups of small order, the table (p. 14) separates commutative (c) from noncommutative (n) groups for each order.

# Examples

**Example 1** (p. 8, 1.3): (Z, +) and (Z/mZ, +) are abelian.

**Example 2** (p. 14, table): For order 4, both groups (C_4 and C_2 x C_2) are abelian.

**Example 3** (p. 13, 1.17): D_3 = S_3 is the smallest noncommutative group, so all groups of order <= 5 with the exception of... well, S_3 has order 6 and is the smallest non-abelian group.

# Relationships

## Builds Upon
- **group** — abelian groups add the commutativity axiom

## Enables
- **torsion-subgroup** — only defined in abelian groups (in general, torsion elements need not form a subgroup)
- **cyclic-group** — every cyclic group is abelian

## Related
- **direct-product-of-groups** — a direct product of abelian groups is abelian

## Contrasts With
- **symmetric-group** — S_n is noncommutative for n >= 3
- **dihedral-group** — D_n is noncommutative for n >= 3
- **quaternion-group** — Q is noncommutative

# Common Errors

- **Error**: Assuming all groups are abelian
  **Correction**: The smallest non-abelian group is S_3 = D_3, of order 6

# Common Confusions

- **Confusion**: Thinking "abelian" and "cyclic" are the same
  **Clarification**: Every cyclic group is abelian, but not conversely (e.g., C_2 x C_2 is abelian but not cyclic)

# Source Reference

Chapter 1: Basic Definitions and Results, Example 1.6, pages 8-9.

# Verification Notes

- Definition source: Direct from 1.6, p. 8
- Confidence rationale: HIGH — explicitly defined
- Uncertainties: None
- Cross-reference status: Verified against planned cards
