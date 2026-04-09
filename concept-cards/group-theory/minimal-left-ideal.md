---
# === CORE IDENTIFICATION ===
concept: Minimal Left Ideal
slug: minimal-left-ideal

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
pdf_page: 108
section: "Simple F-algebras and their modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - f-algebra
  - simple-module
extends: []
related:
  - matrix-algebra
  - modules-over-simple-algebras
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a minimal left ideal?"
  - "How do minimal left ideals relate to simple modules?"
---

# Quick Definition

A minimal left ideal of an F-algebra A is a nonzero left ideal containing no proper nonzero left ideal. It is the same as a simple submodule of _A A.

# Core Definition

The submodules of _A A (A regarded as a left module over itself) are the left ideals in A. The simple submodules of _A A are the **minimal left ideals**. For A = M_n(D), the sets L(i) of matrices whose only nonzero column is the ith are minimal left ideals, and M_n(D) = L(1) + ... + L(n). (Milne, pp. 108-110)

# Prerequisites

- **F-algebra** — minimal left ideals are left ideals of an F-algebra
- **Simple module** — minimal left ideals are simple submodules of _A A

# Key Properties

1. Minimal left ideals are simple A-modules
2. For simple A: all minimal left ideals are isomorphic (7.28)
3. A simple algebra is a direct sum of its minimal left ideals (7.28)
4. For M_n(D): there are n minimal left ideals L(1), ..., L(n), each isomorphic to D^n

# Examples

**Example 1** (p. 108, 7.19b): In M_4(D), L(3) consists of matrices with all columns zero except the 3rd.

# Relationships

## Builds Upon
- **f-algebra** — left ideals of algebras
- **simple-module** — minimal left ideals are simple submodules

## Enables
- **wedderburn-theorem** — proof uses a minimal left ideal as a simple module
- **modules-over-simple-algebras** — minimal left ideals generate all modules

## Related
- **matrix-algebra** — L(i) in M_n(D)

# Source Reference

Chapter 7: Representations of Finite Groups, pp. 108-110 (7.19, 7.28).

# Verification Notes

- Definition source: Direct from pp. 108, 110
- Confidence rationale: HIGH — explicit construction
- Uncertainties: None
