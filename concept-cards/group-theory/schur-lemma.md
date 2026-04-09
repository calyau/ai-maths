---
# === CORE IDENTIFICATION ===
concept: "Schur's Lemma"
slug: schur-lemma

# === CLASSIFICATION ===
category: module-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 109
section: "Simple F-algebras and their modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Schur's lemma"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simple-module
  - division-algebra
extends: []
related:
  - irreducible-representation
  - wedderburn-theorem
  - double-centralizer-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does Schur's lemma say?"
  - "What is the endomorphism algebra of a simple module?"
---

# Quick Definition

For every F-algebra A and simple A-module S, the endomorphism algebra End_A(S) is a division algebra.

# Core Definition

**Lemma 7.24 (Schur's Lemma).** For every F-algebra A and simple A-module S, End_A(S) is a division algebra. (Milne, Lemma 7.24, p. 109)

# Prerequisites

- **Simple module** — the lemma applies to simple modules
- **Division algebra** — the conclusion is that End_A(S) is a division algebra

# Key Properties

1. Every nonzero A-linear endomorphism of S is an isomorphism
2. Proof: Ker(gamma) is a submodule of S, hence 0 or S. If 0, gamma is injective (and surjective by dimension count), hence an isomorphism.
3. Over an algebraically closed field F, End_A(S) = F (since the only division algebra over F is F by 7.31)
4. For two non-isomorphic simple modules S, S': Hom_A(S, S') = 0

# Construction / Recognition

Schur's lemma is a recognition tool: given a simple A-module S:
1. Any nonzero A-linear map S -> S is an isomorphism
2. Any nonzero A-linear map between simple modules S -> S' is an isomorphism (hence S = S')
3. End_A(S) forms a division algebra

# Context & Application

Schur's lemma is one of the most fundamental results in representation theory. It is used in:
- The proof of the Wedderburn structure theorem (7.25): D = End_A(S) is a division algebra
- The orthogonality relations for characters
- Understanding why irreducible characters form an orthonormal basis
Over C, Schur's lemma says that any G-linear map between irreducible representations is a scalar multiple of the identity (or zero if the representations are non-isomorphic).

# Examples

**Example 1** (p. 109): If S is simple and gamma: S -> S is A-linear and nonzero, then Ker(gamma) = 0 (since S is simple), so gamma is an isomorphism.

# Relationships

## Builds Upon
- **simple-module** — applies to simple modules only

## Enables
- **wedderburn-theorem** — the centralizer D = End_A(S) is a division algebra
- **orthogonality-relations** — Schur's lemma underlies the orthogonality of characters

## Related
- **division-algebra** — the endomorphism algebra is a division algebra
- **irreducible-representation** — same as simple module in rep theory

## Contrasts With
- Endomorphism algebras of non-simple modules (not division algebras in general)

# Common Errors

- **Error**: Applying Schur's lemma to non-simple (reducible) modules
  **Correction**: The module must be simple; for non-simple modules, End_A(V) may contain non-invertible elements

# Common Confusions

- **Confusion**: Thinking Schur's lemma says End_A(S) = F
  **Clarification**: Over a general field, End_A(S) is a division algebra which may be larger than F. Only over algebraically closed fields does End_A(S) = F.

# Source Reference

Chapter 7: Representations of Finite Groups, Lemma 7.24, p. 109.

# Verification Notes

- Definition source: Direct from Lemma 7.24
- Confidence rationale: HIGH — explicit named lemma with proof
- Uncertainties: None
