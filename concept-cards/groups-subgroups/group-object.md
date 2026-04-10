---
# === CORE IDENTIFICATION ===
concept: Group Object
slug: group-object

# === CLASSIFICATION ===
category: algebraic-groups
subcategory: category-theory
tier: foundational

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 21
section: "Some category theory"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - yoneda-lemma
extends:
  - monoid-object
related:
  - affine-group
  - affine-group-scheme
contrasts_with:
  - monoid-object

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine group scheme?"
  - "What must I know before understanding Hopf algebras?"
---

# Quick Definition

A group object in a category C with finite products is an object G together with morphisms m: G x G -> G, e: * -> G, and inv: G -> G such that the group axiom diagrams commute. Equivalently, it is an object G such that Hom(T, G) is a group for all T, naturally in T.

# Core Definition

A **group object** in a category C with finite products is an object G together with a morphism m: G x G -> G such that the induced map G(T) x G(T) -> G(T) makes G(T) = Hom(T, G) into a group for every T in C (2.5, p. 21).

Equivalently (2.6), (G, m) is a group object if and only if there exist maps e: * -> G and inv: G -> G making the associativity, identity, and inverse diagrams commute (diagrams (35) and (36), p. 46).

To give a group object in C is the same as giving a functor C -> Grp such that the underlying functor to Set is representable (2.7, p. 21).

# Prerequisites

- **Yoneda lemma** — Used to show equivalence between the morphism and functor perspectives
- **Monoid object** — A group object is a monoid object with an inversion morphism

# Key Properties

1. The inversion morphism inv is uniquely determined by m and e (footnote 11, p. 47)
2. A group object in Alg_k^{opp} is exactly a commutative Hopf algebra (Section 5f, p. 47)
3. A group object in the category of affine schemes over k is an affine group scheme (Section 6b, p. 55)

# Examples

**Example 1** (p. 47): An affine group over k is a group object in Alg_k^{opp}. The morphism m corresponds to the comultiplication Delta: A -> A tensor A.

**Example 2** (p. 58): An affine group scheme is a group object in the category of affine schemes over k.

# Relationships

## Extends
- **Monoid object** — A group object is a monoid object with inversion

## Enables
- **Affine group** — Affine groups are group objects in Alg_k^{opp}
- **Affine group scheme** — Group objects in the category of affine schemes

# Source Reference

Chapter I, Section 2b, 2.5-2.7, p. 21.

# Verification Notes

- Definition source: Direct from 2.5, p. 21
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
