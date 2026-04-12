---
# === CORE IDENTIFICATION ===
concept: Dihedral Product Decomposition
slug: dihedral-product-decomposition

# === CLASSIFICATION ===
category: structure-theory
subcategory: products
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Products"
chapter_number: 10
pdf_page: 59
section: null

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - direct-product
  - internal-direct-product-criterion
extends: []
related:
  - kleins-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When does a dihedral group decompose as a direct product?"
---

# Quick Definition

When $n$ is odd, the dihedral group $D_{2n}$ is isomorphic to $D_n \times \mathbb{Z}_2$.

# Core Definition

Exercise 10.11 states: "Show that $D_{2n}$ is isomorphic to $D_n \times \mathbb{Z}_2$ when $n$ is odd" (Armstrong, p. 63). The decomposition uses the central element (rotation by $\pi$, which commutes with all other symmetries when $n$ is odd) as the generator of the $\mathbb{Z}_2$ factor.

# Prerequisites

- **Direct product** — The decomposition is as a direct product
- **Internal direct product criterion** — Theorem 10.2 provides the method

# Key Properties

1. $D_{2n} \cong D_n \times \mathbb{Z}_2$ when $n$ is odd
2. The decomposition fails when $n$ is even
3. The $\mathbb{Z}_2$ factor comes from the central element of order 2

# Construction / Recognition

## To Verify for Odd $n$:
1. Identify the rotation by $\pi$ in $D_{2n}$ (rotation by $\pi$ about the centre)
2. Show it commutes with all elements
3. Apply Theorem 10.2

# Context & Application

This is an application of the internal direct product criterion to dihedral groups, paralleling the decomposition of $O_n$ for odd $n$. The restriction to odd $n$ mirrors the restriction in the $O_n \cong SO_n \times \mathbb{Z}_2$ result.

# Examples

**Example**: $D_6 \cong D_3 \times \mathbb{Z}_2$ (since 3 is odd). $D_3 \cong S_3$, so $D_6 \cong S_3 \times \mathbb{Z}_2$.

# Relationships

## Builds Upon
- **Direct product** — The decomposition structure
- **Internal direct product criterion** — The method of proof

## Related
- **Klein's group** — $D_2 \cong \mathbb{Z}_2 \times \mathbb{Z}_2$ is a related decomposition

# Common Errors

- **Error**: Applying the decomposition when $n$ is even.
  **Correction**: The decomposition $D_{2n} \cong D_n \times \mathbb{Z}_2$ holds only for odd $n$.

# Common Confusions

- **Confusion**: Thinking all dihedral groups decompose as products.
  **Clarification**: Most dihedral groups do not decompose as direct products. The decomposition $D_{2n} \cong D_n \times \mathbb{Z}_2$ is specific to odd $n$.

# Source Reference

Chapter 10: Products, Exercise 10.11, page 63 (pdf p. 63).

# Verification Notes

- Statement: Exercise 10.11
- Confidence: MEDIUM — stated as exercise without proof in source; standard result
