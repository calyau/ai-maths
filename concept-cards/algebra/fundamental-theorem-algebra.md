---
concept: Fundamental Theorem of Algebra
slug: fundamental-theorem-algebra
category: field-theory
subcategory: main-results
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Fields"
chapter_number: 15
pdf_page: 453
section: "15.10 The Fundamental Theorem of Algebra"
extraction_confidence: high
aliases:
  - "FTA"
prerequisites:
  - field-extension
  - algebraic-closure
extends: []
related:
  - algebraically-closed-field
contrasts_with: []
answers_questions:
  - "What is the Fundamental Theorem of Algebra?"
---

# Quick Definition

The Fundamental Theorem of Algebra states that every nonconstant polynomial with complex coefficients has a complex root. Equivalently, C is algebraically closed.

# Core Definition

Every nonconstant polynomial with complex coefficients has a complex root (Artin, Theorem 15.10.1). The proof uses topological reasoning: for small radius r, f(C_r) makes a small loop near a_0 (no winding), but for large r, f(C_r) winds n times around the origin. By continuity, f must pass through the origin for some intermediate radius, giving a root.

# Prerequisites

- **Field extension** -- C is the ultimate extension of R
- **Algebraic closure** -- C is the algebraic closure of R

# Key Properties

1. C is algebraically closed: every nonconstant polynomial over C has a root in C
2. Every polynomial of degree n over C has exactly n roots (counted with multiplicity)
3. The proof requires analysis (topology or complex analysis), not pure algebra
4. C is the algebraic closure of R

# Context & Application

This theorem ensures that the complex numbers provide a "universal" field for polynomial equations. It underlies the use of C as the ambient field in Galois theory over Q.

# Examples

**Example 1** (p. 484): The proof uses the "winding number" argument: the image of a large circle under x -> f(x) winds n times around the origin.

# Relationships

## Related
- **Algebraically closed field** -- C is the prototypical algebraically closed field
- **Algebraic closure** -- C is the algebraic closure of R

# Source Reference

Chapter 15: Fields, Section 15.10, pages 483-485. Theorem 15.10.1.

# Verification Notes

- Definition source: Direct from Artin, Theorem 15.10.1
- Confidence rationale: Classic theorem with outlined proof
- Uncertainties: None
- Cross-reference status: Verified
