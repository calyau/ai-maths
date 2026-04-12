---
concept: Order of an Element
slug: order-of-an-element
category: group-theory
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Groups"
chapter_number: 2
pdf_page: 48
section: "2.4 Cyclic Groups"
extraction_confidence: high
aliases: []
prerequisites:
  - group
extends: []
related:
  - cyclic-group
  - order-of-a-group
  - lagranges-theorem
contrasts_with: []
answers_questions:
  - "What is a group?"
---

# Quick Definition

The order of an element x in a group is the smallest positive integer n such that x^n = 1. If no such n exists, x has infinite order. The order of x equals the order of the cyclic subgroup <x>.

# Core Definition

An element x of a group has order n if n is the smallest positive integer with x^n = 1, which is equivalent to saying the cyclic subgroup <x> has order n (Artin, p. 58). If x^n != 1 for all n > 0, then x has infinite order.

# Prerequisites

- **Group** — The element lives in a group

# Key Properties

1. The identity is the only element of order 1
2. The order of x divides the order of the group (Corollary 2.8.10)
3. x^k = 1 iff the order of x divides k
4. The order of x^k is n/gcd(k,n) when x has order n (Proposition 2.4.3)

# Construction / Recognition

## To Construct:
1. Compute x, x^2, x^3, ... until you reach 1
2. The number of steps is the order

## To Recognize:
1. x^n = 1 and x^k != 1 for 0 < k < n

# Context & Application

The order of an element constrains what subgroups and group structures are possible. By Lagrange's theorem, element orders divide the group order, immediately limiting possibilities.

# Examples

**Example 1** (p. 58): In S_3 with usual presentation, x = (123) has order 3, y = (12) has order 2.

**Example 2** (p. 58): [[1,1],[-1,0]] has order 6 in GL_2(R).

# Relationships

## Builds Upon
- **Group** — Order is a property of group elements

## Enables
- **Cyclic group** — The order determines the size of <x>

## Related
- **Lagrange's theorem** — Element order divides group order

# Common Errors

- **Error**: Computing x^n = 1 but not checking smaller powers
  **Correction**: The order is the SMALLEST positive n with x^n = 1

# Common Confusions

- **Confusion**: Confusing order of an element with order of the group
  **Clarification**: Element order is the size of <x>; group order is |G|

# Source Reference

Chapter 2: Groups, Section 2.4, page 58.

# Verification Notes

- Definition source: Direct from Section 2.4
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
