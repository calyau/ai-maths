---
# === CORE IDENTIFICATION ===
concept: Semisimple Module
slug: semisimple-module

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
section: "Semisimple modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "completely reducible module"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simple-module
  - f-algebra
extends:
  - simple-module
related:
  - completely-reducible-representation
  - maschke-theorem
  - isotypic-component
contrasts_with:
  - simple-module

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a semisimple module?"
  - "When does every submodule have a complement?"
---

# Quick Definition

An A-module is semisimple if it is isomorphic to a direct sum of simple modules.

# Core Definition

An A-module V is **semisimple** if it is isomorphic to a direct sum of simple modules. Equivalently (Corollary 7.13), the following conditions are equivalent: (a) V is semisimple; (b) V is a sum of simple submodules; (c) every submodule of V has a complement. (Milne, Chapter 7, pp. 100, 106)

# Prerequisites

- **Simple module** — semisimple modules are direct sums of simple modules
- **F-algebra** — modules are over F-algebras

# Key Properties

1. Every submodule of a semisimple module has a complement (7.13)
2. Sums, submodules, and quotients of semisimple modules are semisimple (7.14)
3. Decomposes uniquely (up to reordering) into isotypic components (7.11)
4. Isomorphism class determined by the multiplicities of simple summands (7.11)

# Construction / Recognition

1. Verify one of the equivalent conditions in 7.13:
   - V is a direct sum of simple modules, OR
   - V is a sum (not necessarily direct) of simple modules, OR
   - Every submodule of V has a complement
2. If V is an F[G]-module and char(F) does not divide |G|, then V is automatically semisimple (Maschke's theorem)

# Context & Application

Semisimplicity is the key structural property in representation theory. Maschke's theorem says F[G]-modules are semisimple when char(F) does not divide |G|. This allows complete decomposition of representations into irreducible components.

# Examples

**Example 1** (p. 105): When char(F) does not divide |G|, every F[G]-module is semisimple (Proposition 7.9).

**Example 2** (p. 108): M_n(D) = L(1) + ... + L(n) is a direct sum of minimal left ideals, hence semisimple as a left module over itself.

# Relationships

## Builds Upon
- **simple-module** — semisimple modules are built from simple modules

## Enables
- **isotypic-component** — semisimple modules decompose into isotypic components
- **wedderburn-artin-theorem** — structure of algebras whose modules are all semisimple

## Related
- **completely-reducible-representation** — same concept in representation language
- **maschke-theorem** — guarantees semisimplicity for F[G]-modules

## Contrasts With
- **simple-module** — simple is the irreducible case; semisimple is the completely reducible case

# Common Errors

- **Error**: Assuming every module is semisimple
  **Correction**: Semisimplicity fails when char(F) divides |G|, e.g., C_p over a field of characteristic p

# Common Confusions

- **Confusion**: Thinking the decomposition into simples is unique as submodules
  **Clarification**: The isomorphism type of the decomposition is unique (7.11), but the actual submodules in the decomposition need not be

# Source Reference

Chapter 7: Representations of Finite Groups, pp. 100, 105-106 (7.9, 7.11-7.14).

# Verification Notes

- Definition source: Direct from p. 100 and Corollary 7.13
- Confidence rationale: HIGH — explicit definition with equivalent characterizations
- Uncertainties: None
