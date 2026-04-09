---
# === CORE IDENTIFICATION ===
concept: Sylow p-Subgroup of GL_n(F_p)
slug: sylow-subgroup-of-gln

# === CLASSIFICATION ===
category: sylow-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "The Sylow Theorems; Applications"
chapter_number: 5
pdf_page: 77
section: "The Sylow theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - unitriangular group as Sylow subgroup

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sylow-p-subgroup
  - general-linear-group
extends: []
related:
  - maximal-flag-and-sylow
  - sylow-first-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a concrete example of a Sylow p-subgroup?"
  - "What is the Sylow p-subgroup of GL_n(F_p)?"
---

# Quick Definition

The group of upper triangular n x n matrices over F_p with 1s on the diagonal (the unitriangular group) is a Sylow p-subgroup of GL_n(F_p), with order p^(n(n-1)/2).

# Core Definition

**Example 5.3.** Let G = GL_n(F_p). The order of G is (p^n - 1)(p^n - p)(p^n - p^2) ... (p^n - p^(n-1)), so the highest power of p dividing |G| is p^(1+2+...+(n-1)) = p^(n(n-1)/2). The group of upper triangular matrices with 1s on the diagonal (unitriangular matrices) has order p^(n(n-1)/2), and is therefore a Sylow p-subgroup.

(Milne, Example 5.3, p. 77-78)

# Prerequisites

- **sylow-p-subgroup** -- the concept being exemplified
- **general-linear-group** -- GL_n(F_p) and its order

# Key Properties

1. |GL_n(F_p)| = (p^n - 1)(p^n - p) ... (p^n - p^(n-1))
2. The p-part of this order is p^(1+2+...+(n-1)) = p^(n(n-1)/2)
3. The unitriangular group U_n(F_p) has exactly this order
4. The matrices in U_n have the form: 1s on diagonal, arbitrary entries above, 0s below

# Context & Application

This is both the canonical example of a Sylow p-subgroup and a key ingredient in the alternative proof of Sylow I (Theorem 5.12): since every finite group embeds in some GL_n(F_p), the existence of Sylow subgroups in GL_n(F_p) implies their existence in all finite groups.

# Examples

**Example 1** (p. 77-78): For GL_2(F_p), the Sylow p-subgroup is {((1, a), (0, 1)) : a in F_p}, which has order p.

**Example 2** (p. 77-78): For GL_3(F_p), the Sylow p-subgroup consists of matrices ((1,a,b),(0,1,c),(0,0,1)) with a,b,c in F_p, of order p^3.

# Relationships

## Builds Upon
- **sylow-p-subgroup** -- this is the prototypical example

## Enables
- **sylow-first-theorem** -- the alternative proof embeds G into GL_n(F_p)
- **maximal-flag-and-sylow** -- geometric interpretation of Sylow subgroups of GL_n

# Source Reference

Chapter 5, Example 5.3, pp. 77-78.

# Verification Notes

- Definition source: Direct from Example 5.3
- Confidence rationale: HIGH -- explicit construction
- Uncertainties: None
