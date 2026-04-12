---
# === CORE IDENTIFICATION ===
concept: Internal Direct Product Criterion
slug: internal-direct-product-criterion

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
  - "Theorem 10.2"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - direct-product
extends: []
related:
  - central-inversion
  - full-symmetry-groups-of-solids
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When is a group isomorphic to the direct product of two of its subgroups?"
---

# Quick Definition

A group $G$ is isomorphic to $H \times K$ if $H$ and $K$ are subgroups with $HK = G$, $H \cap K = \{e\}$, and every element of $H$ commutes with every element of $K$.

# Core Definition

"(10.2) Theorem. If $H$ and $K$ are subgroups of $G$ for which $HK = G$, if they have only the identity element in common, and if every element of $H$ commutes with every element of $K$, then $G$ is isomorphic to $H \times K$" (Armstrong, p. 61).

The isomorphism $\varphi: H \times K \to G$ is defined by $\varphi(x, y) = xy$. It preserves multiplication because elements of $H$ commute with elements of $K$: $\varphi((x,y)(x',y')) = xx'yy' = xyx'y' = \varphi(x,y)\varphi(x',y')$. Injectivity follows from $H \cap K = \{e\}$, and surjectivity from $HK = G$.

# Prerequisites

- **Direct product** — The theorem characterizes when a group is a direct product

# Key Properties

1. Three conditions needed: (a) $HK = G$, (b) $H \cap K = \{e\}$, (c) elements of $H$ commute with elements of $K$
2. The isomorphism $\varphi(x, y) = xy$ maps $H \times K$ to $G$
3. Condition (c) is essential for the homomorphism property
4. Condition (b) ensures injectivity
5. Condition (a) ensures surjectivity

# Construction / Recognition

## To Show $G \cong H \times K$:
1. Verify $H$ and $K$ are subgroups of $G$
2. Verify $HK = G$ (every element of $G$ is a product $xy$ with $x \in H$, $y \in K$)
3. Verify $H \cap K = \{e\}$
4. Verify every element of $H$ commutes with every element of $K$

# Context & Application

This theorem is the tool for decomposing symmetry groups. Armstrong applies it to show $O_3 \cong SO_3 \times \mathbb{Z}_2$ (via $H = SO_3$, $K = \{I, -I\}$) and to compute full symmetry groups of Platonic solids.

# Examples

**Example** (p. 61): $O_3 \cong SO_3 \times \{I, J\} \cong SO_3 \times \mathbb{Z}_2$. Here $H = SO_3$, $K = \{I, J\}$. The three conditions hold: $O_3 = SO_3 \cdot \{I, J\}$ (every element of $O_3$ is either in $SO_3$ or equals $AJ$ for $A \in SO_3$), $SO_3 \cap \{I, J\} = \{I\}$, and $J$ commutes with everything.

**Example** (p. 62): The full symmetry groups of the cube and octahedron are $S_4 \times \mathbb{Z}_2$, and those of the dodecahedron and icosahedron are $A_5 \times \mathbb{Z}_2$.

# Relationships

## Builds Upon
- **Direct product** — Characterizes when a group is an internal direct product

## Related
- **Central inversion** — The factor $\{I, J\} \cong \mathbb{Z}_2$ in symmetry group decompositions
- **Full symmetry groups of solids** — Main application

# Common Errors

- **Error**: Forgetting to check the commutativity condition (c).
  **Correction**: All three conditions are needed. If elements of $H$ do not commute with elements of $K$, the map $\varphi(x,y) = xy$ is not a homomorphism.

# Common Confusions

- **Confusion**: Thinking $HK = G$ and $H \cap K = \{e\}$ are sufficient.
  **Clarification**: Without commutativity, $G$ might be a semidirect product rather than a direct product. The semidirect product is a more general construction (not covered in this chapter).

# Source Reference

Chapter 10: Products, pages 61-62 (pdf pp. 61-62). Theorem 10.2 with proof.

# Verification Notes

- Theorem: Direct from p. 61
- Proof: Complete on pp. 61-62
- Applications: pp. 61-62
- Confidence: HIGH — theorem with complete proof
