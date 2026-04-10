---
# === CORE IDENTIFICATION ===
concept: Yoneda Lemma
slug: yoneda-lemma

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
pdf_page: 20
section: "Some category theory"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - representable-functor
  - affine-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding Hopf algebras?"
---

# Quick Definition

The Yoneda lemma states that for a functor F: A -> Set and an object A of A, the natural transformations Hom(h^A, F) are in natural bijection with F(A), via T -> T_A(id_A).

# Core Definition

**Yoneda Lemma** (2.1, p. 20): The map T -> a_T = T_A(id_A) is a bijection Hom(h^A, F) isomorphic to F(A), with inverse a -> T_a where (T_a)_R(f) = F(f)(a) for f in h^A(R) = Hom(A, R). The bijection is natural in both A and F.

A key consequence (2.2): the contravariant functor A -> h^A from A to the functor category is fully faithful, meaning Hom(h^A, h^B) is isomorphic to Hom(B, A).

# Prerequisites

This is a foundational concept with no prerequisites within this source (beyond basic category theory).

# Key Properties

1. Hom(h^A, F) is isomorphic to F(A), naturally in A and F
2. The functor A -> h^A is fully faithful (2.2)
3. Natural transformations h^A -> h^B correspond to morphisms B -> A (contravariantly)
4. If F is representable, the representing object is unique up to unique isomorphism

# Context & Application

In the theory of algebraic groups, the Yoneda lemma is used constantly to translate between:
- Morphisms of algebras (A' -> A) and natural transformations (h^A -> h^{A'})
- Structure maps on algebras (like comultiplication) and group structures on functors
- Elements of G(R) and algebra homomorphisms O(G) -> R

The Yoneda lemma justifies the equivalence between the "algebra + comultiplication" viewpoint and the "functor to groups" viewpoint of affine groups (Summary 2.16, p. 25).

# Examples

**Example 1** (p. 20-21): Taking F = h^B gives Hom(h^A, h^B) isomorphic to Hom(B, A). This shows the functor A -> h^A is fully faithful.

**Example 2** (p. 24): The product map G x G -> G corresponds (via Yoneda) to the comultiplication Delta: O(G) -> O(G) tensor O(G), because h^{A tensor A} is isomorphic to h^A x h^A.

# Relationships

## Enables
- **Representable functor** — The Yoneda lemma characterizes representable functors
- **Affine group** — Provides the equivalence between algebra and functor descriptions

# Common Confusions

- **Confusion**: Thinking the Yoneda embedding is covariant
  **Clarification**: The functor A -> h^A = Hom(A, -) is contravariant in A; a morphism A' -> A gives h^A -> h^{A'}, not the reverse

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 2b "Some category theory", 2.1, p. 20.

# Verification Notes

- Definition source: Direct from 2.1, p. 20
- Confidence rationale: Standard result stated with full proof
- Uncertainties: None
- Cross-reference status: Verified
