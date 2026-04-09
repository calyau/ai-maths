---
# === CORE IDENTIFICATION ===
concept: Division Algebras over Algebraically Closed Fields
slug: division-algebras-over-algebraically-closed-fields

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
pdf_page: 110
section: "Simple F-algebras and their modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - division-algebra
extends: []
related:
  - wedderburn-theorem
  - decomposition-of-f-g
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What division algebras exist over an algebraically closed field?"
  - "Why does representation theory simplify over algebraically closed fields?"
---

# Quick Definition

The only division algebra over an algebraically closed field F is F itself. This is why simple F-algebras over algebraically closed fields are just matrix algebras M_n(F).

# Core Definition

**Proposition 7.31.** The only division algebra over an algebraically closed field F is F itself. The proof: for any alpha in D, the subalgebra F[alpha] is a field (integral domain of finite degree over F). Since F is algebraically closed, alpha is in F. (Milne, Proposition 7.31, p. 110)

# Prerequisites

- **Division algebra** — the objects being classified

# Key Properties

1. D = F is the only option
2. Consequence: every simple F-algebra over an algebraically closed field is M_n(F) (not M_n(D) for nontrivial D)
3. Consequence: F[G] = M_{f_1}(F) x ... x M_{f_t}(F) over algebraically closed fields

# Context & Application

This result is the reason representation theory over C (or any algebraically closed field of characteristic 0) is so clean: there are no complications from nontrivial division algebras. The Wedderburn theory simplifies maximally.

# Relationships

## Builds Upon
- **division-algebra** — classification over algebraically closed fields

## Enables
- **decomposition-of-f-g** — F[G] = product of matrix algebras over F (not over division algebras)

# Source Reference

Chapter 7: Representations of Finite Groups, Proposition 7.31, p. 110.

# Verification Notes

- Definition source: Direct from Proposition 7.31
- Confidence rationale: HIGH — explicit proposition with proof
- Uncertainties: None
