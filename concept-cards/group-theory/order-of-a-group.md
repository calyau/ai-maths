---
# === CORE IDENTIFICATION ===
concept: Order of a Group
slug: order-of-a-group

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
  - "|G|"
  - cardinality of a group

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - order-of-an-element
  - p-group
  - groups-of-small-order
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the order of a group?"
  - "What does |G| denote?"
---

# Quick Definition

The order of a group G, denoted |G|, is its cardinality — the number of elements in the group. A group may have finite or infinite order.

# Core Definition

The **order** |G| of a group G is its cardinality (p. 8).

# Prerequisites

- **Group** — order is a property of a group

# Key Properties

1. |G| is a positive integer for finite groups, or infinite
2. Isomorphic groups have the same order
3. The order of a direct product is the product of orders: |G x H| = |G| * |H|
4. The symmetric group S_n has order n! (1.4, p. 8)
5. The dihedral group D_n has order 2n (1.17, p. 13)

# Construction / Recognition

## To Recognize:
1. Count the number of distinct elements in G

# Context & Application

The order of a group is one of the most basic invariants used in classification. The table of groups of small order (p. 14) organizes groups by their order. The order constrains which group structures are possible — for instance, every group of prime order is cyclic (1.28).

# Examples

**Example 1** (p. 8, 1.4): |S_n| = n!. For example, |S_3| = 6.

**Example 2** (p. 13, 1.17): |D_n| = 2n. For example, |D_3| = 6.

**Example 3** (p. 13, 1.18): |Q| = 8 (the quaternion group).

# Relationships

## Builds Upon
- **group** — order is a property of a group

## Enables
- **p-group** — defined as a group whose order is a power of a prime
- **groups-of-small-order** — classification by order

## Related
- **order-of-an-element** — the order of an element a is the order of the cyclic subgroup <a>
- **isomorphism-of-groups** — isomorphic groups have the same order

# Common Errors

- **Error**: Confusing the order of a group with the order of an element
  **Correction**: |G| is the size of the group; the order of an element a is the smallest positive n with a^n = e

# Common Confusions

- **Confusion**: Assuming groups of the same order must be isomorphic
  **Clarification**: There can be multiple non-isomorphic groups of the same order (e.g., C_4 and V_4 both have order 4)

# Source Reference

Chapter 1: Basic Definitions and Results, page 8.

# Verification Notes

- Definition source: Direct from text, p. 8
- Confidence rationale: HIGH — explicitly defined
- Uncertainties: None
- Cross-reference status: Verified against planned cards
