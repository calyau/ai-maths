---
# === CORE IDENTIFICATION ===
concept: Modules over Simple F-algebras
slug: modules-over-simple-algebras

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
  - wedderburn-theorem
extends: []
related:
  - simple-module
  - semisimple-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the modules over a simple F-algebra?"
  - "How many simple modules does a simple algebra have?"
---

# Quick Definition

Over a simple F-algebra, all simple modules are isomorphic, every module is a direct sum of copies of the unique simple module, and two modules are isomorphic iff they have the same dimension.

# Core Definition

Let A be a simple F-algebra. Then: (1) Any two simple A-modules are isomorphic (7.27c). (2) Every A-module is isomorphic to a direct sum of copies of the unique simple module S (7.29). (3) Any two A-modules of the same F-dimension are isomorphic (7.29). (Milne, Corollaries 7.27-7.29, pp. 110-111)

# Prerequisites

- **Simple F-algebra** — the module theory is over a simple algebra
- **Wedderburn's theorem** — A = M_n(D)

# Key Properties

1. There is exactly one isomorphism class of simple A-modules
2. _A A is isotypic (7.27b)
3. Every module is semisimple (7.26)
4. Module isomorphism class is determined by dimension over F
5. Minimal left ideals of A are isomorphic as left A-modules (7.28)

# Construction / Recognition

1. A simple algebra has a unique simple module S (up to isomorphism)
2. For A = M_n(D): S can be taken as any minimal left ideal L(i) = D^n
3. Every A-module V is isomorphic to mS for some m

# Context & Application

This result shows that representation theory over a simple algebra is trivial: there is only one irreducible representation. The interesting structure in representation theory comes from the semisimple (product of simples) case, where different simple factors contribute different irreducible representations.

# Examples

**Example 1** (p. 108, 7.19b): For M_n(D), the minimal left ideals L(1), ..., L(n) are all isomorphic as M_n(D)-modules.

# Relationships

## Builds Upon
- **simple-f-algebra** — the algebra in question
- **wedderburn-theorem** — classifies the algebra

## Enables
- Understanding modules over semisimple algebras (via the product decomposition)

## Related
- **simple-module** — there is a unique simple module
- **semisimple-module** — all modules are semisimple

# Source Reference

Chapter 7: Representations of Finite Groups, Theorem 7.27 and Corollaries 7.28-7.30, pp. 110-111.

# Verification Notes

- Definition source: Direct from Theorem 7.27 and corollaries
- Confidence rationale: HIGH — explicit theorem statements
- Uncertainties: None
