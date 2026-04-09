---
# === CORE IDENTIFICATION ===
concept: Group Order
slug: group-order

# === CLASSIFICATION ===
category: group-theory
subcategory: group-properties
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Groups"
chapter_number: 3
pdf_page: 49
section: "Definitions and Examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - order of a group
  - finite order
  - infinite order

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - finite-group
  - order-of-element
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
  - "How do I find the order of an element in a group?"
---

# Quick Definition

The order of a finite group $G$, denoted $|G|$, is the number of elements it contains. If $G$ has infinitely many elements, it has infinite order.

# Core Definition

"A group is finite, or has finite order, if it contains a finite number of elements; otherwise, the group is said to be infinite or to have infinite order. The order of a finite group is the number of elements that it contains. If $G$ is a group containing $n$ elements, we write $|G| = n$" (Judson, p. 49).

# Prerequisites

- **Group** — Order is a property of groups

# Key Properties

1. $|G|$ is a positive integer for finite groups
2. $|\mathbb{Z}_n| = n$
3. $|\mathbb{Z}| = \infty$
4. $|S_3| = 6$ (symmetries of equilateral triangle)
5. $|GL_2(\mathbb{R})| = \infty$

# Construction / Recognition

## To Determine $|G|$:
1. Count the number of distinct elements in $G$
2. If the count is finite, $|G|$ equals that count
3. If $G$ has infinitely many elements, $|G| = \infty$

# Context & Application

Group order is a fundamental invariant used in classifying groups. Many theorems in group theory relate the order of a group to the orders of its subgroups and elements (e.g., Lagrange's theorem).

# Examples

**Example 1** (p. 49): $|\mathbb{Z}_5| = 5$.

**Example 2** (p. 49): $|\mathbb{Z}| = \infty$.

**Example 3** (p. 48): $|U(8)| = 4$ (elements: $\{1, 3, 5, 7\}$).

# Relationships

## Builds Upon
- **group** — Order is a property of groups

## Related
- **finite-group** — Groups with finite order
- **order-of-element** — Order of an element vs. order of the group

# Common Confusions

- **Confusion**: Confusing the order of a group with the order of an element
  **Clarification**: Group order = number of elements; element order = smallest power giving identity

# Source Reference

Chapter 3: Groups, Section 3.2, page 49.

# Verification Notes

- Definition source: Direct quote from p. 49
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
