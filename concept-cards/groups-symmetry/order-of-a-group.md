---
# === CORE IDENTIFICATION ===
concept: Order of a Group
slug: order-of-a-group

# === CLASSIFICATION ===
category: fundamentals
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Dihedral Groups"
chapter_number: 4
pdf_page: 22
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "|G|"
  - group order

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - order-of-an-element
  - dihedral-group
  - cyclic-group-zn
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
  - "How do I find all subgroups of a finite group?"
---

# Quick Definition

The order of a finite group G, written |G|, is the number of elements in G. A group with infinitely many elements is said to have infinite order.

# Core Definition

"The order of a finite group is the number of elements in the group. A group that contains infinitely many elements is said to have infinite order. We usually write |G| for the order of the group G" (Armstrong, Ch. 4, p. 25).

# Prerequisites

- **Group** — Order is a property of groups

# Key Properties

1. |G| is always a positive integer or infinity
2. |D_n| = 2n
3. |Z_n| = n
4. The order of the identity element is always 1
5. The order of each element divides the order of the group (Lagrange's Theorem, Chapter 11)

# Construction / Recognition

## To Determine:
1. For a finite group, count the distinct elements
2. For an infinite group, verify that no finite list exhausts the elements

# Context & Application

The order of a group is the most basic numerical invariant. It determines the size of the multiplication table and constrains the possible subgroups. Groups of the same order can have different structure (e.g., Z_6 and D_3 both have order 6).

# Examples

**Example 1** (p. 25): The order of D_3 is six.

**Example 2** (p. 25): The order of Z_6 is also six.

**Example 3** (p. 25): R (the additive group of reals) has infinite order.

# Relationships

## Builds Upon
- **Group** — Order is a basic group property

## Related
- **Order of an Element** — Related but distinct concept
- **Dihedral Group** — |D_n| = 2n
- **Cyclic Group Zn** — |Z_n| = n

# Common Errors

- **Error**: Confusing the order of a group with the order of an element
  **Correction**: |G| counts elements of the group; the order of an element x is the smallest positive n with x^n = e

# Common Confusions

- **Confusion**: Thinking groups of the same order must be "the same"
  **Clarification**: Z_6 and D_3 both have order 6 but are structurally different (one is abelian, the other is not)

# Source Reference

Chapter 4: Dihedral Groups, page 18 (pdf p. 25).

# Verification Notes

- Definition source: Direct quote from p. 25
- Confidence rationale: High — explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
