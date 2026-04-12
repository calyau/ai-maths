---
# === CORE IDENTIFICATION ===
concept: "Klein's Group"
slug: kleins-group

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
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Vierergruppe"
  - "four group"
  - "V"
  - "Klein four-group"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - direct-product
extends: []
related:
  - isomorphism
contrasts_with:
  - cyclicity-criterion

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Klein's group?"
  - "What is the Vierergruppe?"
  - "Is there a non-cyclic group of order 4?"
---

# Quick Definition

Klein's group (the Vierergruppe) is $\mathbb{Z}_2 \times \mathbb{Z}_2$, the unique non-cyclic group of order 4, in which every non-identity element has order 2.

# Core Definition

"$\mathbb{Z}_2 \times \mathbb{Z}_2$ is often called *Klein's group*" (Armstrong, p. 60). Its four elements are $(0,0)$, $(1,0)$, $(0,1)$, $(1,1)$ with addition modulo 2 in both coordinates. "Each non-identity element now has order 2, so the group is not cyclic" (p. 60). It is isomorphic to the group of plane symmetries of a chessboard (Chapter 7) and to the subgroup $\{\varepsilon, (12)(34), (13)(24), (14)(23)\}$ of $A_4$.

# Prerequisites

- **Direct product** — Klein's group is $\mathbb{Z}_2 \times \mathbb{Z}_2$

# Key Properties

1. Order 4, non-cyclic
2. Every non-identity element has order 2
3. Abelian
4. Isomorphic to the plane symmetries of a chessboard
5. Isomorphic to $\{\varepsilon, (12)(34), (13)(24), (14)(23)\} \le A_4$
6. The unique group of order 4 that is not cyclic (Exercise 10.12)

# Construction / Recognition

## To Construct:
1. Take $\mathbb{Z}_2 \times \mathbb{Z}_2$ with componentwise addition mod 2
2. Elements: $(0,0)$, $(1,0)$, $(0,1)$, $(1,1)$

## To Recognize:
1. Check the group has order 4
2. Check it is not cyclic (no element of order 4)
3. If so, it must be Klein's group (Exercise 10.12)

# Context & Application

Klein's group appears naturally in many contexts: as a subgroup of $A_4$ (the three double transpositions plus identity), as the symmetry group of a rectangle (not a square), and as the simplest example of a non-cyclic group. Exercise 10.12 proves it is the only non-cyclic group of order 4.

# Examples

**Example** (p. 60): The isomorphism to the chessboard symmetry group:
$(0,0) \to e$, $(1,0) \to q_1$, $(0,1) \to q_2$, $(1,1) \to r$.

**Example** (Exercise 10.4): $\mathbb{Z}_3 \times V \cong \mathbb{Z}_2 \times \mathbb{Z}_6$.

# Relationships

## Builds Upon
- **Direct product** — Defined as $\mathbb{Z}_2 \times \mathbb{Z}_2$

## Related
- **Isomorphism** — Multiple realizations of Klein's group

## Contrasts With
- **$\mathbb{Z}_4$** — The cyclic group of order 4 (has an element of order 4)

# Common Errors

- **Error**: Assuming every group of order 4 is cyclic.
  **Correction**: There are exactly two groups of order 4: $\mathbb{Z}_4$ (cyclic) and $\mathbb{Z}_2 \times \mathbb{Z}_2$ (Klein's group).

# Common Confusions

- **Confusion**: Thinking Klein's group must be a product of two copies of $\mathbb{Z}_2$.
  **Clarification**: While it is defined this way, it can appear as a subgroup of other groups (e.g., $A_4$) without an explicit product structure visible.

# Source Reference

Chapter 10: Products, page 60 (pdf p. 60). Example (ii); Exercise 10.12.

# Verification Notes

- Definition: Direct from p. 60
- Uniqueness as non-cyclic order-4 group: Exercise 10.12
- Confidence: HIGH — explicit definition and characterization
