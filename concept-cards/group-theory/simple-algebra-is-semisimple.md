---
# === CORE IDENTIFICATION ===
concept: Simple Algebras are Semisimple
slug: simple-algebra-is-semisimple

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
  - simple-f-algebra
  - semisimple-f-algebra
  - wedderburn-theorem
extends: []
related:
  - minimal-left-ideal
  - matrix-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Is every simple F-algebra semisimple?"
---

# Quick Definition

Every simple F-algebra is semisimple: all its modules are semisimple. The proof: A = M_n(D), and _A A = L(1) + ... + L(n) is a direct sum of minimal left ideals (simple modules).

# Core Definition

**Proposition 7.26.** Every simple F-algebra A is semisimple. The proof: by Wedderburn (7.25), A = M_n(D) for some division algebra D. The sets L(i) are minimal left ideals in M_n(D), and M_n(D) = L(1) + ... + L(n) as an M_n(D)-module. This shows _A A is semisimple. (Milne, Proposition 7.26, p. 110)

# Prerequisites

- **Simple F-algebra** — the algebra
- **Semisimple F-algebra** — the property being established
- **Wedderburn's theorem** — A = M_n(D)

# Key Properties

1. Simple implies semisimple (but not conversely: a product of simples is semisimple but not simple)
2. The proof is constructive: _A A decomposes into minimal left ideals

# Relationships

## Builds Upon
- **simple-f-algebra**, **wedderburn-theorem**, **minimal-left-ideal**

## Enables
- **wedderburn-artin-theorem** — semisimple = product of simple, and each simple is semisimple

# Source Reference

Chapter 7: Representations of Finite Groups, Proposition 7.26, p. 110.

# Verification Notes

- Definition source: Direct from Proposition 7.26
- Confidence rationale: HIGH — explicit proposition
- Uncertainties: None
