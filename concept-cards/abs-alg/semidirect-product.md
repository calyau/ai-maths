---
concept: Semidirect Product
slug: semidirect-product
category: group-theory
subcategory: direct-semidirect-products
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Direct and Semidirect Products and Abelian Groups"
chapter_number: 5
pdf_page: 184
section: "5.5 Semidirect Products"
extraction_confidence: high
aliases:
  - "semidirect product of groups"
prerequisites:
  - direct-product
  - normal-subgroup
  - automorphism
  - homomorphism
extends:
  - direct-product
related:
  - split-extension
  - complement-subgroup
  - internal-direct-product
contrasts_with:
  - direct-product
answers_questions:
  - "What distinguishes a direct product from a semidirect product?"
  - "How do you construct a semidirect product?"
---

# Quick Definition
The semidirect product H x_phi K is a group built from groups H and K using a homomorphism phi: K -> Aut(H). Elements are ordered pairs (h, k) with multiplication (h_1, k_1)(h_2, k_2) = (h_1 * phi(k_1)(h_2), k_1 k_2). The subgroup H is normal but K need not be.

# Core Definition
Theorem 10: Let H and K be groups and let phi be a homomorphism from K into Aut(H). Let G be the set of ordered pairs (h, k) with multiplication (h_1, k_1)(h_2, k_2) = (h_1 * k_1 . h_2, k_1 k_2), where k . h denotes the action of K on H determined by phi. Then (1) G is a group of order |H||K|; (2) H embeds as a normal subgroup and K as a subgroup; (3) H is normal in G; (4) H intersect K = 1; (5) for all h in H and k in K, khk^{-1} = phi(k)(h) (Dummit & Foote, p. 185). The group G is denoted H x_phi K or simply H x K.

# Prerequisites
- **Direct product** — Semidirect products generalize direct products
- **Normal subgroup** — H must be normal in the semidirect product
- **Automorphism** — phi maps K into Aut(H)
- **Homomorphism** — phi must be a group homomorphism

# Key Properties
1. |G| = |H| * |K|
2. H is normal in G, but K is generally not normal
3. H intersect K = 1
4. Conjugation by k on H equals phi(k): khk^{-1} = phi(k)(h)
5. G = H x K (direct product) iff phi is the trivial homomorphism iff K is also normal
6. Every dihedral group D_{2n} is a semidirect product Z_n x Z_2

# Construction / Recognition
## To Construct:
1. Choose groups H and K
2. Find a homomorphism phi: K -> Aut(H)
3. Define multiplication as (h_1, k_1)(h_2, k_2) = (h_1 * phi(k_1)(h_2), k_1 k_2)

## To Recognize (Theorem 12):
1. Find H normal in G with complement K (meaning G = HK, H intersect K = 1)
2. Then G = H x_phi K where phi(k) = conjugation by k on H

# Context & Application
Semidirect products are essential for constructing non-abelian groups from abelian ones. They allow classification of groups of many specific orders by reducing to: find H, K, and all homomorphisms phi: K -> Aut(H).

# Examples
**Example 1** (p. 188): D_{2n} = Z_n x Z_2 where Z_2 acts by inversion on Z_n.

**Example 2** (p. 189): The non-abelian group of order 12 with cyclic Sylow 2-subgroup is Z_3 x Z_4, where the generator of Z_4 acts by inversion on Z_3.

**Example 3** (p. 190): Two non-isomorphic non-abelian groups of order p^3 (p odd) are constructed as (Z_p x Z_p) x Z_p and Z_{p^2} x Z_p.

# Relationships
## Builds Upon
- **Direct product** — A direct product is a semidirect product with trivial phi
## Enables
- **Group classification** — Many groups of small order are classified via semidirect products
## Contrasts With
- **Direct product** — In a direct product, BOTH factors are normal; in a semidirect product, only H is

# Common Errors
- **Error**: Assuming different homomorphisms phi always give non-isomorphic groups
  **Correction**: Different phi can sometimes give isomorphic groups (step (d) of the classification strategy)

# Common Confusions
- **Confusion**: Thinking the semidirect product is commutative in H and K
  **Clarification**: H x K and K x H are generally different; the notation indicates H is the normal factor

# Source Reference
Chapter 5, Section 5.5, Theorem 10, pages 184-197.

# Verification Notes
- Definition source: Direct from Theorem 10, p. 185
- Confidence: HIGH — stated and proved
- Uncertainties: None
