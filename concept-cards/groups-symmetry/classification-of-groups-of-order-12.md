---
# === CORE IDENTIFICATION ===
concept: Classification of Groups of Order 12
slug: classification-of-groups-of-order-12

# === CLASSIFICATION ===
category: finite-group-classification
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "The Sylow Theorems"
chapter_number: 20
pdf_page: 120
section: "Classification of Groups of Order 12"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - first-sylow-theorem
  - second-sylow-theorem
  - third-sylow-theorem
  - direct-product
extends: []
related:
  - dicyclic-group
  - dihedral-group
  - alternating-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How many groups of order 12 are there up to isomorphism?"
  - "How do the Sylow theorems help classify groups of small order?"
---

# Quick Definition

There are exactly five groups of order 12 up to isomorphism: $\mathbb{Z}_{12}$, $\mathbb{Z}_6 \times \mathbb{Z}_2$, $D_6$, the dicyclic group of order 12, and $A_4$.

# Core Definition

Armstrong proves that every group of order 12 is isomorphic to one of:
1. $\mathbb{Z}_{12}$ (cyclic)
2. $\mathbb{Z}_6 \times \mathbb{Z}_2$
3. $D_6$ (dihedral group of order 12)
4. The dicyclic group of order 12
5. $A_4$ (alternating group on 4 letters)

(Armstrong, pp. 122--124)

# Prerequisites

- **First/Second/Third Sylow theorems** -- the classification begins by counting Sylow subgroups
- **Direct product** -- several cases produce direct products

# Key Properties

1. The Sylow theorems give $t_3 \in \{1, 4\}$ (Sylow 3-subgroups) and $t_2 \in \{1, 3\}$ (Sylow 2-subgroups)
2. **Case 1** ($t_3 = 1$): normal Sylow 3-subgroup $H = \langle x \rangle \cong \mathbb{Z}_3$, Sylow 2-subgroup $K$ of order 4
   - $K$ cyclic: yields $\mathbb{Z}_{12}$ (subcase i) or the dicyclic group (subcase ii)
   - $K \cong \mathbb{Z}_2 \times \mathbb{Z}_2$: yields $\mathbb{Z}_6 \times \mathbb{Z}_2$ (subcase iii) or $D_6$ (subcase iv)
3. **Case 2** ($t_3 = 4$): four conjugate Sylow 3-subgroups use 8 elements, forcing a unique normal Sylow 2-subgroup $K \cong \mathbb{Z}_2 \times \mathbb{Z}_2$, yielding $A_4$ (subcase vi)

# Construction / Recognition

## How to Identify Which Group of Order 12:
1. Check if the group is abelian. If yes: $\mathbb{Z}_{12}$ (has element of order 12) or $\mathbb{Z}_6 \times \mathbb{Z}_2$ (maximum order 6)
2. If non-abelian, count Sylow 3-subgroups:
   - $t_3 = 1$: the Sylow 3-subgroup is normal. Check Sylow 2-subgroup: cyclic gives dicyclic, Klein gives $D_6$
   - $t_3 = 4$: must be $A_4$

# Context & Application

This is the culminating application of the Sylow theorems in the chapter. It demonstrates the power of combining Sylow theory with direct product characterisations to completely classify groups of a given order.

# Examples

**Subcase (ii)** (p. 122): The dicyclic group arises when $K = \langle y \rangle$ is cyclic of order 4 and $yxy^{-1} = x^2$. The element $z = xy^2$ has order 6, and $G$ has presentation with $z^6 = e$, $y^2 = z^3$, $yz = z^{-1}y$.

**Subcase (vi)** (p. 124): $A_4$ arises when $t_3 = 4$ and $K \cong \mathbb{Z}_2 \times \mathbb{Z}_2$. Conjugation by an order-3 element permutes the three non-identity elements of $K$ as a 3-cycle.

# Relationships

## Builds Upon
- **Sylow theorems** -- the starting point for the case analysis
- **Direct product** -- identifies abelian cases

## Related
- **Dicyclic group** -- one of the five groups of order 12
- **Dihedral group** -- $D_6$ is one of the five
- **Alternating group** -- $A_4$ is one of the five

# Common Errors

- **Error**: Overlooking the dicyclic group as a possibility.
  **Correction**: When $K$ is cyclic and $yxy^{-1} = x^2$, one obtains the dicyclic group, not a dihedral or semi-direct product.

# Common Confusions

- **Confusion**: Thinking $D_6$ and $A_4$ are isomorphic (both have order 12 and are non-abelian).
  **Clarification**: $D_6$ has an element of order 6 while $A_4$ does not. $A_4$ has a normal Klein four-group while $D_6$ has a normal cyclic subgroup of order 6.

# Source Reference

Chapter 20: The Sylow Theorems, "Classification of Groups of Order 12," pages 122--124. Cases (a)(i)--(d)(vi).

# Verification Notes

- Classification: Complete case analysis from pp. 122--124
- All five groups verified against source
- Confidence: HIGH -- exhaustive classification with complete proof
