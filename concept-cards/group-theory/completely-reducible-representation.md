---
# === CORE IDENTIFICATION ===
concept: Completely Reducible Representation
slug: completely-reducible-representation

# === CLASSIFICATION ===
category: representation-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 104
section: "The group algebra; semisimplicity"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "semisimple representation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linear-representation
  - irreducible-representation
  - semisimple-module
extends:
  - linear-representation
related:
  - maschke-theorem
  - f-g-module
contrasts_with:
  - irreducible-representation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a completely reducible representation?"
  - "What is a semisimple representation?"
---

# Quick Definition

A representation is completely reducible (semisimple) if V is isomorphic to a direct sum of irreducible representations.

# Core Definition

A linear representation G -> GL(V) is **completely reducible** (or **semisimple**) when V is semisimple as an F[G]-module, i.e., isomorphic to a direct sum of simple (irreducible) submodules. (Milne, Chapter 7, p. 104)

# Prerequisites

- **Linear representation** — completely reducible is a property of representations
- **Irreducible representation** — the summands are irreducible
- **Semisimple module** — the module-theoretic equivalent

# Key Properties

1. V decomposes as V = S_1 + ... + S_k with each S_i irreducible
2. The decomposition is unique up to isomorphism and reordering (7.11)
3. Every representation is completely reducible when char(F) does not divide |G| (Maschke's theorem)
4. Equivalently: every G-invariant subspace has a G-invariant complement

# Construction / Recognition

1. Apply Maschke's theorem if char(F) does not divide |G| -- automatically completely reducible
2. Otherwise, find a decomposition V = S_1 + ... + S_k with each S_i irreducible
3. Equivalently, verify that every G-invariant subspace has a G-invariant complement

# Context & Application

Maschke's theorem guarantees that in the most important cases (characteristic zero or characteristic coprime to |G|), every representation is completely reducible. This is what makes the character-theoretic approach to representation theory possible.

# Examples

**Example 1** (p. 105, 7.9): Every F[G]-module is completely reducible when char(F) does not divide |G|.

**Example 2** (p. 102): Over a field of characteristic p, the representation C_p -> GL_2(F) via (1, 1; 0, 1) is NOT completely reducible.

# Relationships

## Builds Upon
- **irreducible-representation** — the building blocks
- **semisimple-module** — the module-theoretic formulation

## Enables
- Character theory — characters of completely reducible representations are sums of irreducible characters

## Related
- **maschke-theorem** — guarantees complete reducibility

## Contrasts With
- **irreducible-representation** — irreducible = no decomposition; completely reducible = decomposes fully

# Common Errors

- **Error**: Assuming all representations are completely reducible
  **Correction**: This fails when char(F) divides |G|

# Common Confusions

- **Confusion**: Thinking "completely reducible" means "reducible"
  **Clarification**: An irreducible representation is also completely reducible (as a direct sum of one summand). "Completely reducible" means "decomposes into irreducibles", not "has proper subrepresentations"

# Source Reference

Chapter 7: Representations of Finite Groups, p. 104.

# Verification Notes

- Definition source: Direct from p. 104
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
