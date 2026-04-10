---
concept: Group of Multiplicative Type
slug: group-of-multiplicative-type
category: multiplicative-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 169
section: "14e Groups of multiplicative type"
extraction_confidence: high
aliases:
  - multiplicative type group
prerequisites:
  - diagonalizable-group
  - character-of-affine-group
extends:
  - diagonalizable-group
related:
  - algebraic-torus
  - character-module
contrasts_with:
  - unipotent-group
answers_questions:
  - "What is a group of multiplicative type?"
  - "How do groups of multiplicative type relate to diagonalizable groups?"
---

# Quick Definition

An affine group G is of multiplicative type if G_{k^sep} is diagonalizable, i.e., if G becomes diagonalizable after a separable extension of the base field. Groups of multiplicative type are classified by commutative groups with continuous Galois action via the character module X*(G).

# Core Definition

An affine group G is *of multiplicative type* if G_{k^sep} is diagonalizable (Definition 14.18). Define X*(G) = Hom(G_{k^sep}, G_m) with the canonical action of Gamma = Gal(k^sep/k). The functor X* is a contravariant equivalence from groups of multiplicative type over k to commutative groups with continuous Gamma-action, preserving exact sequences (Theorem 14.20). The equivalent characterizations are (Theorem 14.28): G is of multiplicative type iff G becomes diagonalizable over some field extension iff G is commutative and Hom(G, G_a) = 0 iff G is commutative and O(G) is coetale (Milne, pp. 169-173).

# Prerequisites

- **Diagonalizable group** -- Groups of multiplicative type become diagonalizable over k^sep
- **Character of affine group** -- X*(G) classifies these groups

# Key Properties

1. X* gives a contravariant equivalence to {abelian groups + continuous Gamma-action} (Theorem 14.20)
2. Rep(G) is semisimple, with simple objects indexed by Gamma-orbits on X*(G) (Theorem 14.27)
3. Equivalent to: commutative + Hom(G, G_a) = 0 (Theorem 14.28)
4. A commutative group is of multiplicative type iff Rep(G) is semisimple (Corollary 14.30)
5. In nonzero characteristic, these are the ONLY groups with semisimple representations (Aside 14.31)
6. Every connected action on a group of multiplicative type is trivial (rigidity, Theorem 14.32)

# Construction / Recognition

## To Construct:
1. Start with an abelian group M with continuous Gamma-action
2. Form k^sep[M] with the compatible semilinear Gamma-action
3. Take G = Spec of the Gamma-fixed Hopf subalgebra

## To Recognize:
1. Check that G is commutative and Hom(G, G_a) = 0
2. Or check that Rep(G) is semisimple

# Context & Application

Groups of multiplicative type are one of the three basic building blocks in the structure theory of algebraic groups (along with unipotent and semisimple groups). They generalize tori to allow torsion and non-split forms.

# Examples

**Example 1** (p. 170): Over R, with X*(G) = Z and Gamma acting by m -> -m, we get G(R) = {z in C^x | z z-bar = 1}, the circle group (compact!), versus the trivial action giving G_m(R) = R^x (non-compact).

**Example 2** (p. 170): For K/k a finite separable extension, the Weil restriction R -> (R tensor K)^x is of multiplicative type with X*(G) = Z^{Hom_k(K, k^sep)}.

# Relationships

## Builds Upon
- **Diagonalizable group** -- Split forms of groups of multiplicative type

## Enables
- **Algebraic torus** -- Tori are groups of multiplicative type with torsion-free X*
- **Solvable algebraic group** -- Multiplicative type groups appear in the structure of solvable groups

## Contrasts With
- **Unipotent group** -- Hom(unipotent, multiplicative type) = 0 (Corollary 15.15)

# Common Confusions

- **Confusion**: Thinking multiplicative type means "isomorphic to a product of G_m's"
  **Clarification**: That's a split torus. Groups of multiplicative type may not split over k; they become diagonalizable only over k^sep. They may also have torsion (e.g., mu_n).

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 14e, pages 169-173. Definition 14.18, Theorems 14.20, 14.27, 14.28.

# Verification Notes

- Definition source: Direct from Definition 14.18
- Confidence rationale: Explicit definition with multiple equivalent characterizations
- Uncertainties: None
- Cross-reference status: Verified
