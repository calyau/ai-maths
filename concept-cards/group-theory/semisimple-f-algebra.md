---
# === CORE IDENTIFICATION ===
concept: Semisimple F-algebra
slug: semisimple-f-algebra

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - f-algebra
  - semisimple-module
extends:
  - f-algebra
related:
  - simple-f-algebra
  - wedderburn-artin-theorem
  - group-algebra
  - maschke-theorem
contrasts_with:
  - simple-f-algebra

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a semisimple F-algebra?"
  - "When is the group algebra semisimple?"
---

# Quick Definition

An F-algebra A is semisimple if every A-module is semisimple. Equivalently, the left regular module _A A is semisimple.

# Core Definition

An F-algebra A is said to be **semisimple** if every A-module is semisimple. Since every A-module is a quotient of a direct sum of copies of _A A, it suffices to check that _A A is semisimple. (Milne, Chapter 7, p. 107)

# Prerequisites

- **F-algebra** — semisimple is a property of F-algebras
- **Semisimple module** — the defining condition involves semisimple modules

# Key Properties

1. Equivalent to _A A being semisimple (sufficient to check one module)
2. The isotypic components of _A A are the minimal two-sided ideals of A (7.17)
3. Every two-sided ideal is a direct sum of minimal two-sided ideals (7.17)
4. Every semisimple F-algebra is isomorphic to a product of simple F-algebras (Wedderburn-Artin, 7.36)
5. F[G] is semisimple iff char(F) does not divide |G| (Maschke)

# Construction / Recognition

1. Check that the left regular module _A A is semisimple
2. Equivalently, check that A is a product of simple F-algebras
3. For F[G]: check that char(F) does not divide |G|

# Context & Application

Semisimple algebras are the algebras for which representation theory is "nice": every module decomposes completely into simples, and the Wedderburn-Artin theorem gives their structure. The group algebra F[G] being semisimple (Maschke's theorem) is what makes the character theory of finite groups work.

# Examples

**Example 1** (p. 111): A finite product of simple F-algebras is semisimple (7.33).

**Example 2** (p. 111): F[G] is semisimple when char(F) does not divide |G| (by Maschke's theorem and 7.9).

# Relationships

## Builds Upon
- **f-algebra** — semisimple is a property of F-algebras
- **semisimple-module** — all modules must be semisimple

## Enables
- **wedderburn-artin-theorem** — structure theorem for semisimple algebras
- Complete classification of modules (7.37)

## Related
- **group-algebra** — F[G] is semisimple under Maschke's conditions
- **maschke-theorem** — provides the semisimplicity of F[G]

## Contrasts With
- **simple-f-algebra** — simple implies semisimple, but not conversely

# Common Errors

- **Error**: Thinking semisimple algebras are simple
  **Correction**: A semisimple algebra is a product of simple algebras; it need not be simple itself

# Common Confusions

- **Confusion**: Confusing "semisimple algebra" with "semisimple module"
  **Clarification**: An algebra is semisimple if all its modules are semisimple; a module is semisimple if it decomposes into simples

# Source Reference

Chapter 7: Representations of Finite Groups, p. 107 and pp. 111-113 (7.33-7.37).

# Verification Notes

- Definition source: Direct from p. 107
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
