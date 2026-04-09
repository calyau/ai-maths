---
# === CORE IDENTIFICATION ===
concept: Wedderburn-Artin Theorem
slug: wedderburn-artin-theorem

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
pdf_page: 112
section: "Semisimple F-algebras and their modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Artin-Wedderburn theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semisimple-f-algebra
  - simple-f-algebra
  - wedderburn-theorem
  - double-centralizer-theorem
extends:
  - wedderburn-theorem
related:
  - decomposition-of-f-g
  - group-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the structure of a semisimple F-algebra?"
  - "How does the Wedderburn-Artin theorem classify semisimple algebras?"
---

# Quick Definition

Every semisimple F-algebra is isomorphic to a product of simple F-algebras, i.e., a product of matrix algebras M_{n_i}(D_i) over division algebras D_i.

# Core Definition

**Theorem 7.36.** Every semisimple F-algebra is isomorphic to a product of simple F-algebras. Combined with Wedderburn's theorem (7.25), every semisimple F-algebra is isomorphic to M_{n_1}(D_1) x ... x M_{n_t}(D_t) for division algebras D_i. (Milne, Theorem 7.36, p. 112)

# Prerequisites

- **Semisimple F-algebra** — the theorem classifies these
- **Simple F-algebra** — the factors are simple
- **Wedderburn's theorem** — each simple factor is M_n(D)
- **Double centralizer theorem** — key to the proof

# Key Properties

1. The factors are uniquely determined up to order and isomorphism
2. Over an algebraically closed field, D_i = F for all i, so A = M_{n_1}(F) x ... x M_{n_t}(F)
3. The number of simple factors equals the number of isomorphism classes of simple modules (7.37a)
4. Every module is determined by the multiplicities r_i of the simple modules S_i (7.37b)

# Construction / Recognition

1. Choose a faithful semisimple module V (e.g., _A A)
2. A = C(C(A)) in End_F(V) by the double centralizer theorem
3. C(A) is a product of simple algebras by Theorem 7.35
4. Hence C(C(A)) = A is also a product of simple algebras

# Context & Application

The Wedderburn-Artin theorem, combined with Maschke's theorem, gives a complete description of the group algebra: F[G] = M_{f_1}(F) x ... x M_{f_t}(F) over an algebraically closed field of characteristic zero (Proposition 7.40). This is the structural foundation of the entire character theory.

# Examples

**Example 1** (p. 113, 7.40): Over an algebraically closed field of characteristic zero, F[G] = M_{f_1}(F) x ... x M_{f_t}(F).

**Example 2** (p. 111, 7.33): A finite product of simple F-algebras is semisimple.

# Relationships

## Builds Upon
- **wedderburn-theorem** — classifies each simple factor
- **semisimple-f-algebra** — the algebras being classified

## Enables
- **decomposition-of-f-g** — F[G] is a product of matrix algebras
- Complete classification of F[G]-modules (7.37)

## Related
- **group-algebra** — F[G] is the primary application

## Contrasts With
- Structure of non-semisimple algebras (much more complex)

# Source Reference

Chapter 7: Representations of Finite Groups, Theorems 7.35-7.37, pp. 112-113.

# Verification Notes

- Definition source: Direct from Theorem 7.36
- Confidence rationale: HIGH — explicit theorem
- Uncertainties: None
