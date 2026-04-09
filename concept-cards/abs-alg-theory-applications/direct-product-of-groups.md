---
# === CORE IDENTIFICATION ===
concept: Direct Product of Groups
slug: direct-product-of-groups

# === CLASSIFICATION ===
category: group-theory
subcategory: group-operations
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Groups"
chapter_number: 3
pdf_page: 52
section: "Subgroups"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - product of groups

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - cartesian-product
extends: []
related:
  - subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
---

# Quick Definition

The direct product of two groups $G_1$ and $G_2$, written $G_1 \times G_2$, is the group whose elements are ordered pairs $(g_1, g_2)$ with the operation performed coordinatewise.

# Core Definition

For groups $G_1$ and $G_2$, the direct product $G_1 \times G_2$ consists of all ordered pairs $(g_1, g_2)$ with $g_1 \in G_1$, $g_2 \in G_2$, and the operation $(a_1, a_2) \cdot (b_1, b_2) = (a_1 b_1, a_2 b_2)$ (Judson, p. 52, described via Example 3.28 for $\mathbb{Z}_2 \times \mathbb{Z}_2$).

# Prerequisites

- **Group** — Both components must be groups
- **Cartesian product** — Underlying set is the Cartesian product

# Key Properties

1. Operation is componentwise
2. Identity: $(e_1, e_2)$
3. Inverse: $(g_1, g_2)^{-1} = (g_1^{-1}, g_2^{-1})$
4. $|G_1 \times G_2| = |G_1| \cdot |G_2|$
5. $G_1 \times G_2$ is abelian iff both $G_1$ and $G_2$ are abelian

# Context & Application

Direct products allow construction of new groups from existing ones. They are used to distinguish non-isomorphic groups: $\mathbb{Z}_4 \not\cong \mathbb{Z}_2 \times \mathbb{Z}_2$ because they have different subgroup structures.

# Examples

**Example 1** (p. 52): $\mathbb{Z}_2 \times \mathbb{Z}_2 = \{(0,0), (0,1), (1,0), (1,1)\}$ with coordinatewise addition mod 2. It has three nontrivial proper subgroups, while $\mathbb{Z}_4$ has only one, proving they are different groups.

# Relationships

## Builds Upon
- **group** — Components are groups
- **cartesian-product** — Underlying set

## Related
- **subgroup** — Direct products have natural subgroups

# Common Confusions

- **Confusion**: Thinking $\mathbb{Z}_m \times \mathbb{Z}_n \cong \mathbb{Z}_{mn}$ always
  **Clarification**: This isomorphism holds if and only if $\gcd(m, n) = 1$

# Source Reference

Chapter 3: Groups, Section 3.3, Example 3.28, page 52.

# Verification Notes

- Definition source: Synthesized from Example 3.28
- Confidence: MEDIUM — concept introduced by example, not formally defined in Ch. 3
- Cross-reference status: Verified
- Uncertainties: Formal definition may appear later in the text
