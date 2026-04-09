---
# === CORE IDENTIFICATION ===
concept: Isotypic Component
slug: isotypic-component

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
pdf_page: 106
section: "Semisimple modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "isotypic module"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semisimple-module
  - simple-module
extends: []
related:
  - decomposition-of-f-g
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an isotypic component of a semisimple module?"
  - "How does a semisimple module decompose into isotypic components?"
---

# Quick Definition

An A-module is isotypic (of type S) if it is isomorphic to a direct sum of copies of a single simple module S. The isotypic components of a semisimple module are its maximal isotypic submodules of distinct types.

# Core Definition

An A-module is said to be **isotypic** (of type the isomorphism class of S) if it is isomorphic to a direct sum of copies of a simple module S. Every semisimple module V decomposes as V = m_1 S_1 + ... + m_r S_r with each S_i simple and no two isomorphic. The summands m_i S_i are the **isotypic components** of V. The isotypic component corresponding to S is the sum of all simple submodules of V isomorphic to S. (Milne, Chapter 7, p. 106)

# Prerequisites

- **Semisimple module** — isotypic components arise from the decomposition of semisimple modules
- **Simple module** — each isotypic component consists of copies of one simple module

# Key Properties

1. A homomorphism of semisimple modules maps each isotypic component into the isotypic component of the same type (p. 106)
2. A submodule of V stable under all endomorphisms is a sum of isotypic components (7.15)
3. The isotypic components of _A A are the minimal two-sided ideals of A (7.17, when A is semisimple)
4. The decomposition into isotypic components is canonical (unlike the decomposition into simples)

# Construction / Recognition

1. Decompose V = S_1^{m_1} + ... + S_r^{m_r} with distinct simple types
2. Each S_i^{m_i} is an isotypic component
3. Alternatively, for each simple A-module S, the isotypic component is the sum of all simple submodules isomorphic to S

# Context & Application

Isotypic components provide the canonical decomposition of a semisimple module. While the decomposition into simples is not unique as submodules, the decomposition into isotypic components is unique. For the group algebra F[G], the isotypic components of _A A correspond to the minimal two-sided ideals.

# Examples

**Example 1** (p. 106): V = m_1 S_1 + ... + m_r S_r with S_i pairwise non-isomorphic simple modules; each m_i S_i is an isotypic component.

# Relationships

## Builds Upon
- **semisimple-module** — isotypic decomposition is a refinement of semisimple decomposition
- **simple-module** — each component is a sum of copies of one simple

## Enables
- **decomposition-of-f-g** — the isotypic components of F[G] give the matrix algebra factors

## Related
- Structure of two-sided ideals in semisimple algebras (7.17)

## Contrasts With
- Decomposition into individual simple modules (not canonical)

# Source Reference

Chapter 7: Representations of Finite Groups, pp. 106-107 (after 7.14, and 7.15-7.17).

# Verification Notes

- Definition source: Direct from p. 106
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
