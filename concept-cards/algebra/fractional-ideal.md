---
concept: Fractional Ideal
slug: fractional-ideal
category: number-theory
subcategory: ideal-theory
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Quadratic Number Fields"
chapter_number: 13
pdf_page: 394
section: "Ideal Multiplication"
extraction_confidence: medium
aliases: []
prerequisites:
  - ideal
  - ideal-multiplication
  - ring-of-integers
extends:
  - ideal
related:
  - class-group
contrasts_with: []
answers_questions:
  - "What is a fractional ideal?"
---

# Quick Definition

A fractional ideal is a nonzero R-submodule of the fraction field that can be written as (1/d)A for an ideal A and nonzero d. The class group can equivalently be defined using fractional ideals.

# Core Definition

In the context of quadratic integer rings, a fractional ideal is implicitly used when defining ideal classes: two ideals A and A' are in the same class if A' = lambda*A for some complex number lambda (Artin, formula 13.7.1, p. 410). The set lambda*A is a fractional ideal when lambda is not in R. The class group uses these implicitly to define the inverse of a class.

# Prerequisites

- **Ideal** -- Fractional ideals generalize ideals
- **Ideal multiplication** -- Products and inverses
- **Ring of integers** -- Context for the construction

# Key Properties

1. Every ideal class contains an ordinary (integral) ideal
2. The inverse of the class (A) is (A-bar), since A*A-bar = (n)
3. Fractional ideals form a group under multiplication

# Context & Application

While Artin does not formally define fractional ideals, the concept appears implicitly in the class group construction. The inverse of a class is represented by the conjugate ideal.

# Examples

**Example 1** (p. 410): If A = (2, 1+sqrt(-5)), then A-bar = (2, 1-sqrt(-5)), and A*A-bar = (2), so (1/2)*A*A-bar = R.

# Relationships

## Builds Upon
- **Ideal** -- Generalization of ideals

## Related
- **Class group** -- Fractional ideals underlie class group construction

# Source Reference

Chapter 13: Quadratic Number Fields, Sections 13.4 and 13.7, pages 401-412.

# Verification Notes

- Definition source: Synthesized from implicit usage in class group construction
- Confidence rationale: Medium -- concept is used implicitly but not formally defined with this name
- Uncertainties: Artin uses similarity of ideals rather than formal fractional ideal language
- Cross-reference status: Verified
