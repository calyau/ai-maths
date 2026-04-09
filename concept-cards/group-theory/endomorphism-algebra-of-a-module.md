---
# === CORE IDENTIFICATION ===
concept: Endomorphism Algebra of a Module
slug: endomorphism-algebra-of-a-module

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
pdf_page: 107
section: "Semisimple modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "End_A(V)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - f-algebra
  - simple-module
extends: []
related:
  - opposite-algebra
  - schur-lemma
  - centralizer-of-a-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is End_A(V)?"
  - "How does the endomorphism algebra relate to the opposite algebra?"
---

# Quick Definition

For an A-module V, End_A(V) is the F-algebra of all A-linear endomorphisms of V. For V = _A A, End_A(V) is isomorphic to A^opp.

# Core Definition

For an A-module V, the **endomorphism algebra** End_A(V) is the set of A-linear maps V -> V, forming an F-algebra under composition. For the left regular module _A A, right multiplication x -> xa defines an A-linear endomorphism, and End_A(_A A) is isomorphic to A^opp (as F-algebras). More generally, End_A(V) = M_n(A^opp) for a free module V of rank n. (Milne, 7.16, pp. 107-108)

# Prerequisites

- **F-algebra** — endomorphism algebras are F-algebras
- **Simple module** — Schur's lemma describes End_A(S) for simple S

# Key Properties

1. End_A(_A A) = A^opp (7.16)
2. End_A(mS) = M_m(End_A(S)) for a direct sum of m copies of a simple module S (7.34, equation 32)
3. End_A(S) is a division algebra when S is simple (Schur's lemma)
4. For non-isomorphic simple modules S_i, S_j: Hom_A(S_i, S_j) = 0

# Construction / Recognition

1. Take all A-linear maps V -> V
2. This forms an F-algebra under composition
3. For V = _A A, identify End_A(V) with A^opp via right multiplication

# Context & Application

The endomorphism algebra is fundamental to understanding the structure of modules and algebras. The double centralizer theorem says A = C(C(A)) in End_F(V) when V is a faithful semisimple A-module. The Wedderburn structure theory relies heavily on endomorphism algebras.

# Examples

**Example 1** (p. 107, 7.16): End_A(_A A) = A^opp, where the isomorphism sends phi to phi(1).

**Example 2** (p. 112, equation 32): End_A(mM_0) = M_m(End_A(M_0)).

# Relationships

## Builds Upon
- **f-algebra** — endomorphism algebras are F-algebras

## Enables
- **double-centralizer-theorem** — uses End_F(V) and its subalgebras
- **wedderburn-theorem** — A = End_D(S) = M_n(D^opp)

## Related
- **opposite-algebra** — End_A(_A A) = A^opp
- **schur-lemma** — End_A(S) is a division algebra for simple S

## Contrasts With
- End_F(V) (all F-linear endomorphisms, not just A-linear ones)

# Source Reference

Chapter 7: Representations of Finite Groups, 7.16 (pp. 107-108) and 7.34 (pp. 111-112).

# Verification Notes

- Definition source: Direct from 7.16 and 7.34
- Confidence rationale: HIGH — explicit computation
- Uncertainties: None
