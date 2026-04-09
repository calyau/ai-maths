---
# === CORE IDENTIFICATION ===
concept: Simple Module
slug: simple-module

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
pdf_page: 100
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "irreducible module"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - f-algebra
extends: []
related:
  - semisimple-module
  - irreducible-representation
  - schur-lemma
contrasts_with:
  - semisimple-module

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a simple module?"
  - "What is the module-theoretic analogue of an irreducible representation?"
---

# Quick Definition

An A-module M is simple if it is nonzero and contains no submodules except 0 and M.

# Core Definition

An A-module M is **simple** if it is nonzero and contains no submodules except 0 and M. (Milne, Chapter 7, p. 100)

# Prerequisites

- **F-algebra** — simple modules are modules over an F-algebra A

# Key Properties

1. Nonzero by definition
2. Has exactly two submodules: 0 and M itself
3. Every nonzero homomorphism from a simple module is injective (kernel is 0 or M)
4. Every nonzero homomorphism to a simple module is surjective (image is 0 or M)
5. End_A(S) is a division algebra for any simple A-module S (Schur's lemma, 7.24)

# Construction / Recognition

1. Check that M is nonzero
2. Verify that no proper nonzero submodule exists
3. Equivalently, check that every nonzero element generates all of M

# Context & Application

Simple modules are the building blocks of module theory, analogous to simple groups in group theory. In representation theory, simple F[G]-modules correspond to irreducible representations. Maschke's theorem guarantees that every F[G]-module decomposes into simple modules when char(F) does not divide |G|.

# Examples

**Example 1** (p. 108): Each L(i) in M_n(D) is a minimal left ideal and hence a simple M_n(D)-module.

# Relationships

## Builds Upon
- **f-algebra** — modules are over F-algebras

## Enables
- **semisimple-module** — direct sums of simple modules
- **jordan-holder-for-modules** — composition series with simple quotients
- **irreducible-representation** — same concept in representation-theoretic language

## Related
- **schur-lemma** — End_A(S) is a division algebra for simple S

## Contrasts With
- **semisimple-module** — semisimple modules decompose as direct sums of simples

# Common Errors

- **Error**: Forgetting that the zero module is not simple
  **Correction**: By definition, a simple module must be nonzero

# Common Confusions

- **Confusion**: Confusing "simple" with "semisimple"
  **Clarification**: A simple module has no proper nonzero submodules; a semisimple module is a direct sum of simple modules

# Source Reference

Chapter 7: Representations of Finite Groups, p. 100.

# Verification Notes

- Definition source: Direct from p. 100
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
