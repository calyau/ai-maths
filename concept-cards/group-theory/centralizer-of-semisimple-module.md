---
# === CORE IDENTIFICATION ===
concept: Centralizer of a Semisimple Module
slug: centralizer-of-semisimple-module

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - centralizer-of-a-module
  - semisimple-module
  - schur-lemma
extends: []
related:
  - wedderburn-artin-theorem
  - double-centralizer-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the structure of the centralizer of a semisimple module?"
---

# Quick Definition

If A is a subalgebra of End_F(V) and V is semisimple as an A-module, then the centralizer of A in End_F(V) is a product of simple F-algebras (hence semisimple).

# Core Definition

**Theorem 7.35.** Let V be a finite-dimensional F-vector space and A an F-subalgebra of End_F(V). If V is semisimple as an A-module, then the centralizer of A in End_F(V) is a product of simple F-algebras. Specifically, if V = direct sum r_i S_i (non-isomorphic simples), then End_A(V) = product M_{r_i}(D_i) where D_i = End_A(S_i) is a division algebra. (Milne, Theorem 7.35, p. 112)

# Prerequisites

- **Centralizer of a subalgebra** — the object being computed
- **Semisimple module** — V must be semisimple
- **Schur's lemma** — D_i = End_A(S_i) is a division algebra

# Key Properties

1. End_A(V) = product M_{r_i}(D_i) with D_i = End_A(S_i) division algebras
2. Hom_A(S_i, S_j) = 0 for i != j (by Schur's lemma)
3. The centralizer is itself a semisimple algebra

# Relationships

## Builds Upon
- **centralizer-of-a-module**, **semisimple-module**, **schur-lemma**

## Enables
- **wedderburn-artin-theorem** — proved using this result and the double centralizer theorem

# Source Reference

Chapter 7: Representations of Finite Groups, Theorem 7.35, p. 112.

# Verification Notes

- Definition source: Direct from Theorem 7.35
- Confidence rationale: HIGH — explicit theorem
- Uncertainties: None
