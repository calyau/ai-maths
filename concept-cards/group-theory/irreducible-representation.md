---
# === CORE IDENTIFICATION ===
concept: Irreducible Representation
slug: irreducible-representation

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
  - "simple representation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linear-representation
  - g-invariant-subspace
  - simple-module
extends:
  - linear-representation
related:
  - f-g-module
  - irreducible-character
  - schur-lemma
contrasts_with:
  - completely-reducible-representation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an irreducible representation?"
  - "What is a simple representation?"
---

# Quick Definition

A representation G -> GL(V) is irreducible (or simple) if V is nonzero and has no G-invariant subspaces other than 0 and V.

# Core Definition

Let G -> GL(V) be a linear representation. When V is **simple** as an F[G]-module (i.e., nonzero with no proper nonzero submodules), the representation is said to be **irreducible** (or **simple**). Milne prefers the term "simple" but notes that "irreducible" is the traditional terminology. (Milne, Chapter 7, p. 104)

# Prerequisites

- **Linear representation** — irreducibility is a property of representations
- **G-invariant subspace** — irreducible means no proper nonzero G-invariant subspaces
- **Simple module** — the module-theoretic formulation

# Key Properties

1. V is nonzero and has no proper nonzero G-invariant subspaces
2. End_{F[G]}(V) is a division algebra (Schur's lemma, 7.24)
3. Over an algebraically closed field, End_{F[G]}(V) = F (by 7.31)
4. The number of isomorphism classes of irreducible representations equals the number of conjugacy classes of G (7.41a)
5. For G abelian, all irreducible representations are 1-dimensional

# Construction / Recognition

1. Given a representation G -> GL(V)
2. Check that V is nonzero
3. Verify that no proper nonzero subspace of V is G-invariant
4. Equivalently, verify that V is simple as an F[G]-module

# Context & Application

Irreducible representations are the atoms of representation theory. By Maschke's theorem, every representation (over suitable fields) decomposes as a direct sum of irreducible representations. The character theory of a finite group is essentially the study of its irreducible representations.

# Examples

**Example 1** (p. 102, 7.3a): For C_n over a field containing a primitive nth root of unity, the eigenspaces V_i (1-dimensional) are irreducible representations.

**Example 2** (p. 114, 7.41): If F[G] = M_{f_1}(F) x ... x M_{f_t}(F), there are exactly t irreducible representations (up to isomorphism), one for each matrix factor.

# Relationships

## Builds Upon
- **linear-representation** — irreducible is a property of linear representations
- **simple-module** — the module-theoretic equivalent

## Enables
- **irreducible-character** — the character of an irreducible representation
- **character-table** — rows indexed by irreducible representations
- **decomposition-of-f-g** — F[G] decomposes via irreducible representations

## Related
- **schur-lemma** — describes endomorphisms of irreducible representations

## Contrasts With
- **completely-reducible-representation** — reducible representations that decompose into irreducibles

# Common Errors

- **Error**: Thinking irreducible representations must be 1-dimensional
  **Correction**: Only for abelian groups; nonabelian groups can have irreducible representations of dimension > 1

# Common Confusions

- **Confusion**: Confusing "irreducible" with "faithful"
  **Clarification**: Irreducible means no proper subrepresentations; faithful means injective homomorphism. Neither implies the other.

# Source Reference

Chapter 7: Representations of Finite Groups, p. 104 (7.9) and p. 113 (7.41).

# Verification Notes

- Definition source: Direct from p. 104
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
