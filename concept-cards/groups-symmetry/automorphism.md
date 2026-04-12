---
# === CORE IDENTIFICATION ===
concept: Automorphism
slug: automorphism

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
  - group automorphism

# === TYPED RELATIONSHIPS ===
prerequisites:
  - isomorphism
  - group
extends:
  - isomorphism
related:
  - automorphism-group
  - inner-automorphism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an automorphism of a group?"
  - "How does an automorphism relate to an isomorphism?"
---

# Quick Definition

An automorphism of a group G is an isomorphism from G to itself. Automorphisms capture the internal structural symmetries of a group.

# Core Definition

"An automorphism of a group G is an isomorphism from G to G" (Armstrong, Ch. 23, p. 138). An automorphism is therefore a bijective homomorphism from a group to itself, preserving the group operation while potentially permuting elements.

# Prerequisites

- **Isomorphism** -- An automorphism is a special case of isomorphism where domain and codomain coincide
- **Group** -- The algebraic structure on which automorphisms act

# Key Properties

1. An automorphism is a bijective homomorphism from G to G
2. The composition of two automorphisms is again an automorphism
3. The inverse of an automorphism is an automorphism
4. An automorphism preserves the order of each element (Armstrong, p. 138)
5. The identity function is always an automorphism

# Construction / Recognition

## To Construct an Automorphism
1. Define a function theta: G -> G
2. Verify theta is a homomorphism: theta(xy) = theta(x)theta(y)
3. Verify theta is bijective (injective and surjective)

## To Recognize an Automorphism
1. Check that the function maps G to itself
2. Verify it preserves the group operation
3. Verify it is bijective

# Context & Application

Automorphisms reveal the internal symmetry of a group. Armstrong uses automorphisms to construct semidirect products and to analyze the Euclidean group. The concept connects group theory to geometry: the automorphisms of a group encode how the group's structure can be rearranged while remaining intact.

# Examples

**Example 1** (p. 138): The group Aut(Z) is isomorphic to Z_2. An automorphism theta of Z must send 1 to a generator, so theta(1) = 1 (identity) or theta(1) = -1 (negation map n -> -n).

**Example 2** (p. 138): The map x -> x^{-1} is an automorphism of any abelian group.

**Example 3** (p. 138): An automorphism of S_3 must permute the transpositions (12), (13), (23) among themselves, since automorphisms preserve element order. Therefore Aut(S_3) is isomorphic to S_3.

# Relationships

## Builds Upon
- **Isomorphism** -- An automorphism is an isomorphism from G to G

## Enables
- **Automorphism group** -- The set of all automorphisms forms Aut(G)
- **Inner automorphism** -- Conjugation gives a special class of automorphisms
- **Semidirect product** -- Constructed using a homomorphism into Aut(H)

## Related
- **Characteristic subgroup** -- Subgroups invariant under all automorphisms

# Common Errors

- **Error**: Assuming every bijection from G to G is an automorphism
  **Correction**: The function must also be a homomorphism; arbitrary permutations of elements typically fail to preserve the group operation

- **Error**: Assuming automorphisms fix all elements of the same order
  **Correction**: Automorphisms preserve order but may permute elements of equal order among themselves

# Common Confusions

- **Confusion**: Confusing automorphism with endomorphism
  **Clarification**: An endomorphism is any homomorphism from G to G; an automorphism must additionally be bijective

- **Confusion**: Thinking every group has non-trivial automorphisms
  **Clarification**: Some groups (like Z_2) have only the identity automorphism

# Source Reference

Chapter 23: Automorphisms, pages 131-137 (pdf pp. 138-144). See especially the opening definition and Examples (i)-(vi).

# Verification Notes

- Definition: Directly quoted from Armstrong p. 138, first sentence
- Key Properties: Items 1-3 follow from definition; item 4 explicitly stated in Example (v)
- Confidence: HIGH -- explicit, clear definition provided at chapter opening
- Cross-references: All slug references verified against planned extractions
- Uncertainties: None
