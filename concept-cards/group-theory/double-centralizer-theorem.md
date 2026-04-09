---
# === CORE IDENTIFICATION ===
concept: Double Centralizer Theorem
slug: double-centralizer-theorem

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
  - "bicommutant theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - centralizer-of-a-module
  - semisimple-module
  - faithful-representation
extends: []
related:
  - wedderburn-theorem
  - schur-lemma
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the double centralizer theorem?"
  - "When does C(C(A)) = A?"
---

# Quick Definition

For a faithful semisimple A-module V, the double centralizer of A in End_F(V) equals A: C(C(A)) = A.

# Core Definition

**Theorem 7.22 (Double Centralizer Theorem).** Let A be an F-algebra, and let V be a faithful semisimple A-module. Then C(C(A)) = A (centralizers taken in End_F(V)). (Milne, Theorem 7.22, p. 109)

# Prerequisites

- **Centralizer of a subalgebra** — the theorem concerns iterated centralizers
- **Semisimple module** — V must be semisimple
- **Faithful representation** — A must act faithfully on V

# Key Properties

1. Requires V to be semisimple and faithful
2. A is contained in C(C(A)) for trivial reasons; the content is the reverse inclusion
3. The proof uses Lemma 7.23: for any v_1, ..., v_n in V and b in C(C(A)), there exists a in A with a v_i = b v_i for all i
4. Applied to a basis of V, this gives b = a, hence C(C(A)) = A

# Construction / Recognition

The theorem is an existential result; it shows that A is completely determined by its centralizer in End_F(V).

# Context & Application

The double centralizer theorem is the key lemma in proving the Wedderburn structure theorem for simple algebras (7.25). It shows that A = End_D(S) where D = C(A) is the centralizer of A in End_F(S), allowing A to be identified as a matrix algebra over D^opp.

# Examples

**Example 1** (p. 108-109, 7.21): In M_n(F), the double centralizer of each of {scalar matrices}, {M_n(F)}, {diagonal matrices} equals itself.

# Relationships

## Builds Upon
- **centralizer-of-a-module** — iterated centralizers
- **semisimple-module** — needed for the complement argument in the proof
- **faithful-representation** — A embeds in End_F(V)

## Enables
- **wedderburn-theorem** — A = M_n(D^opp) via the double centralizer theorem
- **wedderburn-artin-theorem** — structure of semisimple algebras

## Related
- **schur-lemma** — D = C(A) is a division algebra when V is simple

## Contrasts With
- Without faithfulness or semisimplicity, C(C(A)) may properly contain A

# Common Errors

- **Error**: Applying the theorem when V is not semisimple
  **Correction**: Both semisimplicity and faithfulness are required

# Source Reference

Chapter 7: Representations of Finite Groups, Theorem 7.22 and Lemma 7.23, pp. 109-110.

# Verification Notes

- Definition source: Direct from Theorem 7.22
- Confidence rationale: HIGH — explicit named theorem
- Uncertainties: None
