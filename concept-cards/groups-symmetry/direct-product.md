---
# === CORE IDENTIFICATION ===
concept: Direct Product
slug: direct-product

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
  - "G x H"
  - "external direct product"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - kleins-group
  - cyclicity-criterion
  - central-inversion
  - internal-direct-product-criterion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do direct products relate to the constituent groups?"
  - "What is a direct product of groups?"
---

# Quick Definition

The direct product $G \times H$ has elements $(g, h)$ with $g \in G$, $h \in H$, and multiplication $(g,h)(g',h') = (gg', hh')$.

# Core Definition

"The direct product $G \times H$ of two groups $G$ and $H$ is constructed as follows. Its elements are ordered pairs $(g, h)$ where $g \in G$ and $h \in H$, with multiplication defined by $(g,h)(g',h') = (gg', hh')$" (Armstrong, p. 59). The identity is $(e, e)$ and the inverse of $(g, h)$ is $(g^{-1}, h^{-1})$.

The construction extends to $n$ factors: $G_1 \times G_2 \times \cdots \times G_n$ with componentwise multiplication $(x_1, \ldots, x_n)(x'_1, \ldots, x'_n) = (x_1 x'_1, \ldots, x_n x'_n)$ (p. 59).

# Prerequisites

This is a foundational construction for combining groups.

# Key Properties

1. $|G \times H| = |G| \cdot |H|$ (for finite groups)
2. $G \times H \cong H \times G$ via $(g, h) \mapsto (h, g)$
3. $G \times H$ is abelian iff both $G$ and $H$ are abelian
4. $G$ is isomorphic to the subgroup $\{(g, e) \mid g \in G\}$ of $G \times H$
5. If $G \times H$ is abelian, then both $G$ and $H$ are abelian (and conversely)
6. Changing the order of factors produces an isomorphic group

# Construction / Recognition

## To Construct $G \times H$:
1. Form all ordered pairs $(g, h)$ with $g \in G$, $h \in H$
2. Define multiplication componentwise: $(g, h)(g', h') = (gg', hh')$
3. Identity is $(e_G, e_H)$; inverse of $(g, h)$ is $(g^{-1}, h^{-1})$

# Context & Application

Direct products are a fundamental way to build new groups from known ones. Armstrong uses them to describe full symmetry groups of Platonic solids: the full symmetry group of the cube is $S_4 \times \mathbb{Z}_2$, and those of the dodecahedron/icosahedron are $A_5 \times \mathbb{Z}_2$.

# Examples

**Example** (p. 59): $\mathbb{Z}_2 \times \mathbb{Z}_3$ has six elements and is cyclic (isomorphic to $\mathbb{Z}_6$) because $\gcd(2, 3) = 1$.

**Example** (p. 60): $\mathbb{Z}_2 \times \mathbb{Z}_2$ has four elements, each non-identity element of order 2. It is not cyclic and is known as Klein's group.

**Example** (p. 60): $\mathbb{R}^n$ is the direct product of $n$ copies of $\mathbb{R}$.

# Relationships

## Enables
- **Klein's group** — $\mathbb{Z}_2 \times \mathbb{Z}_2$
- **Cyclicity criterion** — When $\mathbb{Z}_m \times \mathbb{Z}_n$ is cyclic
- **Full symmetry groups** — $S_4 \times \mathbb{Z}_2$, $A_5 \times \mathbb{Z}_2$

## Related
- **Internal direct product criterion** — When a group decomposes as a direct product of its subgroups

# Common Errors

- **Error**: Forgetting to multiply in each component separately.
  **Correction**: In $G \times H$, the first components multiply in $G$ and the second components multiply in $H$. They do not interact.

# Common Confusions

- **Confusion**: Thinking $G \times H$ is always a "bigger" group than $G$ or $H$.
  **Clarification**: $|G \times H| = |G| \cdot |H|$, so it is larger unless one factor is trivial. But the structure may be simpler than expected (e.g., $\mathbb{Z}_2 \times \mathbb{Z}_3 \cong \mathbb{Z}_6$).

# Source Reference

Chapter 10: Products, pages 59-62 (pdf pp. 59-62). Definition on p. 59; examples on pp. 59-60.

# Verification Notes

- Definition: Direct quote from p. 59
- Properties: All explicit or immediate from definition
- Confidence: HIGH — explicit definition with multiple examples
