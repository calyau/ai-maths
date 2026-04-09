---
# === CORE IDENTIFICATION ===
concept: Simple F-algebra
slug: simple-f-algebra

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
section: "Simple F-algebras and their modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - f-algebra
extends:
  - f-algebra
related:
  - division-algebra
  - wedderburn-theorem
  - matrix-algebra
  - semisimple-f-algebra
contrasts_with:
  - semisimple-f-algebra

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a simple F-algebra?"
  - "What are the simple F-algebras?"
---

# Quick Definition

An F-algebra A is simple if it contains no two-sided ideals except 0 and A.

# Core Definition

An F-algebra A is said to be **simple** if it contains no two-sided ideals except 0 and A. The kernel of any homomorphism from a simple algebra is 0 (since it is an ideal not containing 1), so homomorphisms from simple algebras are injective. (Milne, Chapter 7, p. 107)

# Prerequisites

- **F-algebra** — simple is a property of F-algebras

# Key Properties

1. No proper nonzero two-sided ideals
2. Every homomorphism from a simple algebra is injective (p. 107)
3. Every simple F-algebra is isomorphic to M_n(D) for some division algebra D (Wedderburn, 7.25)
4. Every simple F-algebra is semisimple (7.26)
5. Any two simple modules over a simple algebra are isomorphic (7.27c)
6. A semisimple algebra is simple iff _A A is isotypic (7.27)

# Construction / Recognition

1. Check that A has no proper nonzero two-sided ideals
2. Equivalently (for semisimple A): check that _A A is isotypic
3. Equivalently: check that A is isomorphic to M_n(D) for some division algebra D

# Context & Application

Simple F-algebras are the building blocks of semisimple F-algebras. By the Wedderburn-Artin theorem, every semisimple F-algebra is a product of simple F-algebras, and each simple F-algebra is a matrix algebra over a division algebra. Over an algebraically closed field, the only division algebra is the field itself, so simple = matrix algebra.

# Examples

**Example 1** (p. 108, 7.19a): M_n(D) is simple for any division algebra D.

**Example 2** (p. 108, 7.20): Quaternion algebras H(a,b) over F are simple (they are either division algebras or isomorphic to M_2(F)).

# Relationships

## Builds Upon
- **f-algebra** — simple is a property of F-algebras

## Enables
- **wedderburn-theorem** — classifies simple algebras as M_n(D)
- **wedderburn-artin-theorem** — semisimple = product of simples

## Related
- **division-algebra** — the building blocks of simple algebras
- **matrix-algebra** — M_n(D) is the general form of a simple algebra

## Contrasts With
- **semisimple-f-algebra** — simple implies semisimple, but a product of simples need not be simple

# Common Errors

- **Error**: Confusing "simple algebra" with "simple module"
  **Correction**: Simple algebra = no proper two-sided ideals; simple module = no proper submodules

# Common Confusions

- **Confusion**: Thinking simple algebras have no left ideals
  **Clarification**: Simple algebras have no proper two-sided ideals, but they do have proper left ideals (e.g., the L(i) in M_n(D))

# Source Reference

Chapter 7: Representations of Finite Groups, pp. 107-111 (7.18-7.30).

# Verification Notes

- Definition source: Direct from p. 107
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
