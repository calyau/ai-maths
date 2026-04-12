---
# === CORE IDENTIFICATION ===
concept: Semidirect Product
slug: semidirect-product

# === CLASSIFICATION ===
category: automorphisms
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Automorphisms"
chapter_number: 23
pdf_page: 138
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "H x_phi J"
  - "semidirect product of H by J"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - automorphism-group
  - homomorphism
  - normal-subgroup
  - direct-product
extends:
  - direct-product
related:
  - euclidean-group
  - dihedral-group
contrasts_with:
  - direct-product

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a direct product from a semidirect product?"
  - "How do I construct a semidirect product?"
  - "What is a semidirect product?"
---

# Quick Definition

The semidirect product H x_phi J of groups H and J, determined by a homomorphism phi: J -> Aut(H), is a group whose elements are ordered pairs (x, y) with x in H, y in J, and whose multiplication "twists" by applying automorphisms from phi.

# Core Definition

"Suppose we are given groups H, J and a homomorphism phi: J -> Aut(H). We shall construct a new group H x_phi J called the semidirect product of H and J determined by phi as follows. Its elements are ordered pairs (x, y) where x in H, y in J, and multiplication is defined by (x, y)(x', y') = (x . phi(y)(x'), y . y')" (Armstrong, Ch. 23, p. 138). The identity element is (e_H, e_J) and the inverse of (x, y) is (phi(y)^{-1}(x^{-1}), y^{-1}).

# Prerequisites

- **Automorphism group** -- The homomorphism phi maps into Aut(H)
- **Homomorphism** -- phi: J -> Aut(H) must be a group homomorphism
- **Normal subgroup** -- H sits inside H x_phi J as a normal subgroup
- **Direct product** -- The semidirect product generalizes the direct product

# Key Properties

1. The multiplication rule is (x, y)(x', y') = (x . phi(y)(x'), y . y')
2. The identity is (e_H, e_J) and the inverse of (x, y) is (phi(y)^{-1}(x^{-1}), y^{-1})
3. The function (x, y) -> y is a homomorphism from H x_phi J onto J with kernel isomorphic to H
4. H sits inside H x_phi J as a normal subgroup via x -> (x, e_J)
5. J sits inside H x_phi J as a subgroup via y -> (e_H, y), but this copy is not necessarily normal
6. If phi sends every element of J to the identity automorphism, the semidirect product reduces to the direct product H x J

# Construction / Recognition

## To Construct a Semidirect Product
1. Start with groups H and J
2. Define a homomorphism phi: J -> Aut(H)
3. The underlying set is H x J (ordered pairs)
4. Define multiplication: (x, y)(x', y') = (x . phi(y)(x'), y . y')
5. Verify associativity (which follows because phi is a homomorphism)

## To Recognize a Semidirect Product (Theorem 23.3)
1. Given a group G with subgroups H and J
2. Check that H is normal in G
3. Check that HJ = G
4. Check that H intersect J = {e}
5. If all conditions hold, G is isomorphic to H x_phi J where phi(y)(x) = yxy^{-1}

# Context & Application

The semidirect product is Armstrong's key construction in Chapter 23. It generalizes the direct product by allowing J to act non-trivially on H through automorphisms. The Euclidean group E_2 is a semidirect product of translations by the orthogonal group (Example (ii), p. 138). The dihedral group D_n is a semidirect product Z_n x_phi Z_2 (Example (i), p. 138).

**Historical/structural note:** The semidirect product is "the" way to build non-abelian groups from known pieces when one piece is a normal subgroup.

# Examples

**Example 1** (p. 138): S_3 is isomorphic to Z_3 x_phi Z_2, where phi sends the generator of Z_2 to the non-trivial automorphism of Z_3 (the inversion map). Here H = <(123)> and J = <(12)>.

**Example 2** (p. 138): The Euclidean group E_2 is the semidirect product T x_phi O, where T is the translation subgroup and O is the orthogonal group, with phi induced by conjugation.

**Example 3** (Exercise 23.10, p. 138): Z_n x Z_2 (with the inversion action) is isomorphic to D_n, and SO_2 x Z_2 is isomorphic to O_2.

# Relationships

## Builds Upon
- **Direct product** -- The semidirect product generalizes the direct product

## Enables
- **Euclidean group** -- E_2 = T x_phi O is a semidirect product
- **Wallpaper group** -- Understanding wallpaper group structure uses semidirect products

## Contrasts With
- **Direct product** -- In a direct product, both factors are normal and phi is trivial; in a semidirect product, only H need be normal

# Common Errors

- **Error**: Forgetting that the first coordinate of the product uses phi(y)(x') rather than just x'
  **Correction**: The "twist" by phi(y) is essential; (x, y)(x', y') = (x . phi(y)(x'), y . y'), not (xx', yy')

- **Error**: Assuming both H and J are normal in the semidirect product
  **Correction**: Only H is guaranteed to be normal; J is normal iff the semidirect product is actually a direct product

# Common Confusions

- **Confusion**: Thinking the semidirect product depends only on the groups H and J
  **Clarification**: The same groups H and J can yield non-isomorphic semidirect products for different choices of phi

- **Confusion**: Confusing the semidirect product with the direct product when both factors are abelian
  **Clarification**: Even when H and J are abelian, the semidirect product H x_phi J can be non-abelian if phi is non-trivial (e.g., D_n = Z_n x_phi Z_2)

# Source Reference

Chapter 23: Automorphisms, pages 131-137 (pdf pp. 138-144). The construction appears on p. 138, followed by Theorem 23.3 (recognition criterion) and Examples (i)-(ii).

# Verification Notes

- Definition: Directly quoted from Armstrong p. 138
- Theorem 23.3: Complete statement and proof in source
- Examples: All from source text
- Confidence: HIGH -- explicit construction with full proof of associativity
- Cross-references: Verified against planned extractions
- Uncertainties: None
