---
concept: Algebraic Closure
slug: algebraic-closure
category: field-theory
subcategory: constructions
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Fields"
chapter_number: 15
pdf_page: 453
section: "15.10 The Fundamental Theorem of Algebra"
extraction_confidence: medium
aliases:
  - "algebraically closed field"
prerequisites:
  - field-extension
  - algebraic-element
extends: []
related:
  - fundamental-theorem-algebra
  - splitting-field
contrasts_with: []
answers_questions:
  - "What is an algebraic closure?"
  - "What is an algebraically closed field?"
---

# Quick Definition

A field F is algebraically closed if every polynomial of positive degree with coefficients in F has a root in F. The algebraic closure of a field F is the smallest algebraically closed field containing F. The field C of complex numbers is algebraically closed (the Fundamental Theorem of Algebra).

# Core Definition

A field F is algebraically closed if every polynomial of positive degree with coefficients in F has a root in F (Artin, p. 483). The Fundamental Theorem of Algebra asserts that C is algebraically closed (Theorem 15.10.1). Equivalently, every polynomial over an algebraically closed field splits completely into linear factors.

# Prerequisites

- **Field extension** -- Algebraic closure involves extending fields
- **Algebraic element** -- All elements of the closure are algebraic over the original field

# Key Properties

1. C is algebraically closed (FTA, 15.10.1)
2. Every polynomial over an algebraically closed field splits into linear factors
3. An algebraically closed field has no proper algebraic extensions
4. Every field has an algebraic closure (existence theorem, stated without proof)

# Context & Application

Algebraic closures provide the "universal" ambient field in which all polynomial equations can be solved. Working in an algebraic closure simplifies many arguments in Galois theory.

# Examples

**Example 1** (p. 483): C is the algebraic closure of R. Every polynomial with real coefficients factors into linear factors over C.

# Relationships

## Builds Upon
- **Field extension** -- The algebraic closure is an extension

## Related
- **Fundamental Theorem of Algebra** -- C is algebraically closed
- **Splitting field** -- Splitting fields are subfields of the algebraic closure

# Source Reference

Chapter 15: Fields, Section 15.10, pages 483-485.

# Verification Notes

- Definition source: Direct from Artin, p. 483
- Confidence rationale: Definition clear; existence theorem stated without full proof
- Uncertainties: Existence of algebraic closure for general fields not fully proved
- Cross-reference status: Verified
