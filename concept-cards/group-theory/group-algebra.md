---
# === CORE IDENTIFICATION ===
concept: Group Algebra
slug: group-algebra

# === CLASSIFICATION ===
category: representation-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 104
section: "The group algebra; semisimplicity"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "F[G]"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - f-algebra
extends:
  - f-algebra
related:
  - f-g-module
  - maschke-theorem
  - semisimple-f-algebra
  - decomposition-of-f-g
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the group algebra F[G] relate to linear representations?"
  - "What is the group algebra of a finite group?"
---

# Quick Definition

The group algebra F[G] is the F-vector space with basis the elements of G, endowed with the multiplication extending that on G.

# Core Definition

The **group algebra** F[G] of G is defined to be the F-vector space with basis the elements of G endowed with the multiplication extending that on G. An element of F[G] is a sum c_g g (with c_g in F, g in G). Multiplication is given by (sum c_g g)(sum c'_g g) = sum c''_g g where c''_g = sum_{g_1 g_2 = g} c_{g_1} c'_{g_2}. (Milne, Chapter 7, p. 104)

# Prerequisites

- **Group** — G provides the basis and multiplication
- **F-algebra** — F[G] is an F-algebra

# Key Properties

1. dim_F(F[G]) = |G|
2. A linear action of G on V extends uniquely to an F[G]-module structure on V
3. The submodules of V as an F[G]-module are exactly the G-invariant subspaces
4. F[G] is semisimple iff char(F) does not divide |G| (Maschke's theorem)
5. Over an algebraically closed field of characteristic zero, F[G] = M_{f_1}(F) x ... x M_{f_t}(F) with sum f_i^2 = |G|

# Construction / Recognition

1. Take the free F-vector space with basis {g : g in G}
2. Define multiplication by (c_g g)(c'_h h) = c_g c'_h (gh) and extend linearly
3. This makes F[G] into an associative F-algebra with identity element e (the group identity)

# Context & Application

The group algebra is the bridge between representation theory and algebra. Studying representations of G is equivalent to studying F[G]-modules. The structure of F[G] as an algebra (via Wedderburn theory) completely determines the representation theory of G.

# Examples

**Example 1** (p. 104): Elements of F[G] are formal sums sum c_g g with multiplication extending the group operation.

**Example 2** (p. 113, 7.40): Over an algebraically closed field of characteristic zero, F[G] = M_{f_1}(F) x ... x M_{f_t}(F) where the f_i are the degrees of the irreducible representations.

# Relationships

## Builds Upon
- **group** — provides the basis elements
- **f-algebra** — F[G] is an example of an F-algebra

## Enables
- **f-g-module** — modules over the group algebra
- **decomposition-of-f-g** — structure of F[G] as a product of matrix algebras
- **regular-representation** — G acting on F[G] by left multiplication

## Related
- **maschke-theorem** — shows F[G] is semisimple under char conditions
- **semisimple-f-algebra** — F[G] is semisimple when char(F) does not divide |G|

## Contrasts With
- Polynomial rings F[X] (commutative, infinite-dimensional)

# Common Errors

- **Error**: Confusing elements of G with elements of F[G]
  **Correction**: Elements of G form a basis for F[G]; a general element of F[G] is a formal linear combination of group elements

# Common Confusions

- **Confusion**: Thinking F[G] is commutative
  **Clarification**: F[G] is commutative iff G is abelian

# Source Reference

Chapter 7: Representations of Finite Groups, pp. 104-105.

# Verification Notes

- Definition source: Direct from p. 104
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
