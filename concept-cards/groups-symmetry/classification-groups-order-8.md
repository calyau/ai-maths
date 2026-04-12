---
# === CORE IDENTIFICATION ===
concept: Classification of Groups of Order 8
slug: classification-groups-order-8

# === CLASSIFICATION ===
category: finite-group-classification
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Cauchy's Theorem"
chapter_number: 13
pdf_page: 75
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cauchy-theorem
  - lagrange-theorem
  - quaternion-group
  - dihedral-group
  - cyclic-group
  - direct-product
extends: []
related:
  - classification-groups-order-6
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are all the groups of order 8?"
  - "How many non-isomorphic groups of order 8 exist?"
---

# Quick Definition

There are exactly five groups of order 8 up to isomorphism: $\mathbb{Z}_8$, $\mathbb{Z}_4 \times \mathbb{Z}_2$, $\mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_2$, $D_4$, and the quaternion group $Q$.

# Core Definition

**(13.3) Theorem.** A group of order 8 is isomorphic to one of the following: $\mathbb{Z}_8$, $\mathbb{Z}_4 \times \mathbb{Z}_2$, $\mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_2$, $D_4$, $Q$ (Armstrong, p. 78).

Armstrong's proof proceeds by cases based on the maximum order of elements:

- **Order 8 element exists:** $G \cong \mathbb{Z}_8$
- **Maximum order is 4:** Choose $x$ of order 4, $y \notin \langle x \rangle$. The product $yx$ is either $xy$ or $x^3 y$, and $y^2$ is either $e$ or $x^2$, giving four sub-cases:
  - (i) $yx = xy$, $y^2 = e$: $G \cong \mathbb{Z}_4 \times \mathbb{Z}_2$
  - (ii) $yx = x^3 y$, $y^2 = e$: $G \cong D_4$
  - (iii) $yx = xy$, $y^2 = x^2$: $G \cong \mathbb{Z}_4 \times \mathbb{Z}_2$
  - (iv) $yx = x^3 y$, $y^2 = x^2$: $G \cong Q$
- **All non-identity elements have order 2:** $G \cong \mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_2$

# Prerequisites

- **Cauchy's theorem** — Guarantees elements of order 2
- **Lagrange's theorem** — Constrains element orders
- **Quaternion group** — One of the five possibilities
- **Dihedral group** — $D_4$ is one of the five possibilities
- **Cyclic group** — $\mathbb{Z}_8$ is one of the five possibilities
- **Direct product** — Used for abelian cases

# Key Properties

1. Three of the five groups are abelian ($\mathbb{Z}_8$, $\mathbb{Z}_4 \times \mathbb{Z}_2$, $\mathbb{Z}_2^3$)
2. Two are non-abelian ($D_4$, $Q$)
3. $D_4$ has five elements of order 2; $Q$ has only one
4. The abelian groups are distinguished by their maximum element order (8, 4, or 2)

# Construction / Recognition

## To Classify a Group of Order 8:
1. Find the maximum order of an element
2. If 8: $G \cong \mathbb{Z}_8$
3. If 4: find $x$ of order 4, $y \notin \langle x \rangle$; check $yx = xy$ or $x^3 y$, and $y^2 = e$ or $x^2$
4. If 2: $G \cong \mathbb{Z}_2^3$

# Context & Application

This classification, together with the order-6 result, completes Armstrong's survey of groups of small order. For orders 2, 3, 5, 7 (prime), there is one group each. For order 4, there are two ($\mathbb{Z}_4$, $\mathbb{Z}_2 \times \mathbb{Z}_2$). For order 6, two. For order 8, five.

# Examples

**Example 1** (p. 78): Case (iv): $yx = x^3 y$ and $y^2 = x^2$ give $Q$ via $x \to i$, $y \to j$.

**Example 2** (p. 78): Case (ii): $yx = x^3 y$ and $y^2 = e$ give $D_4$ via $x \to r$, $y \to s$.

# Relationships

## Builds Upon
- **Cauchy's theorem** — Elements of order 2 exist
- **Lagrange's theorem** — Element orders divide 8

## Related
- **Classification of groups of order 6** — The analogous result for order 6

# Common Errors

- **Error**: Missing case (iii), which gives a second copy of $\mathbb{Z}_4 \times \mathbb{Z}_2$
  **Correction**: Both $yx = xy, y^2 = e$ (case i) and $yx = xy, y^2 = x^2$ (case iii) give $\mathbb{Z}_4 \times \mathbb{Z}_2$, via different isomorphisms

# Common Confusions

- **Confusion**: Thinking the five groups can be distinguished by their orders alone
  **Clarification**: All five have order 8. They are distinguished by abelianness, element orders, and number of elements of order 2.

# Source Reference

Chapter 13: Cauchy's Theorem, Theorem (13.3), pp. 78-79 (pdf).

# Verification Notes

- Definition source: Direct from Theorem (13.3) with complete proof
- Confidence rationale: HIGH — explicit classification with all cases
- Uncertainties: None
