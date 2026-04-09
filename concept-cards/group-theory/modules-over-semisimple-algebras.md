---
# === CORE IDENTIFICATION ===
concept: Modules over Semisimple F-algebras
slug: modules-over-semisimple-algebras

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
  - semisimple-f-algebra
  - wedderburn-artin-theorem
extends:
  - modules-over-simple-algebras
related:
  - decomposition-of-f-g
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do modules over a semisimple algebra decompose?"
  - "How many simple modules does a semisimple algebra have?"
---

# Quick Definition

For a semisimple F-algebra A = A_1 x ... x A_t (product of simple algebras), each simple A_i has a unique simple module S_i. Every A-module is isomorphic to a direct sum of the S_i, and the multiplicities determine the isomorphism class.

# Core Definition

**Theorem 7.37.** Let A be a semisimple F-algebra with A = A_1 x ... x A_t (A_i simple). For each A_i, let S_i be a simple A_i-module. Then: (a) Each S_i is a simple A-module, and every simple A-module is isomorphic to exactly one S_i. (b) Every A-module is isomorphic to direct sum r_i S_i for some r_i in N, and two such modules are isomorphic iff r_i = r'_i for all i. (Milne, Theorem 7.37, pp. 112-113)

# Prerequisites

- **Semisimple F-algebra** — A is a semisimple algebra
- **Wedderburn-Artin theorem** — A decomposes as a product of simple algebras

# Key Properties

1. The number of simple modules equals the number of simple factors t
2. Every module decomposes uniquely (up to isomorphism) as direct sum r_i S_i
3. The multiplicities r_i are invariants of the module
4. This gives a complete classification of all A-modules

# Construction / Recognition

1. Write A = A_1 x ... x A_t with each A_i simple
2. For each A_i, find the unique simple module S_i
3. Any A-module decomposes as direct sum r_i S_i
4. The r_i are determined by the module

# Context & Application

This theorem provides the complete classification of F[G]-modules: there are exactly t = (number of conjugacy classes) simple modules, and every module is determined by the multiplicities with which these occur. This is the algebraic underpinning of character theory.

# Examples

**Example 1** (p. 113, 7.37): For F[G] = M_{f_1}(F) x ... x M_{f_t}(F), the simple modules are S_1, ..., S_t with dim S_i = f_i.

# Relationships

## Builds Upon
- **semisimple-f-algebra** — the algebra
- **wedderburn-artin-theorem** — gives the product decomposition
- **modules-over-simple-algebras** — each factor contributes one simple module

## Enables
- **decomposition-of-f-g** — applying to A = F[G]
- Character theory: modules determined by multiplicities of simples

## Contrasts With
- Modules over non-semisimple algebras (indecomposable != simple)

# Source Reference

Chapter 7: Representations of Finite Groups, Theorem 7.37, pp. 112-113.

# Verification Notes

- Definition source: Direct from Theorem 7.37
- Confidence rationale: HIGH — explicit theorem
- Uncertainties: None
