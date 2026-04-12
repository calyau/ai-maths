---
concept: Number Field
slug: number-field
category: field-theory
subcategory: field-types
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Fields"
chapter_number: 15
pdf_page: 453
section: "15.1 Examples of Fields"
extraction_confidence: high
aliases:
  - "algebraic number field"
prerequisites:
  - field-extension
extends: []
related:
  - prime-field
  - algebraic-element
contrasts_with:
  - function-field
answers_questions:
  - "What is a number field?"
---

# Quick Definition

A number field is a subfield of C. It is an extension of Q, and the most commonly studied number fields are algebraic number fields, all of whose elements are algebraic numbers.

# Core Definition

A number field K is a subfield of C (Artin, p. 453). Any subfield of C contains Q, so it is a field extension of Q. Algebraic number fields are those whose elements are all algebraic over Q. Quadratic number fields Q(sqrt(d)) were studied in Chapter 13.

# Prerequisites

- **Field extension** -- Number fields are extensions of Q

# Key Properties

1. Every number field contains Q
2. Algebraic number fields have elements that are all algebraic over Q
3. Quadratic number fields are the simplest examples: Q(sqrt(d))
4. Number fields are central to algebraic number theory

# Context & Application

Number fields are one of the three main classes of fields studied in algebra (along with finite fields and function fields). They are the setting for Galois theory over Q.

# Examples

**Example 1** (p. 453): Q(sqrt(2)), Q(sqrt(-3)) are quadratic number fields.

**Example 2** (p. 453): Q(cube_root(2)) is a cubic number field.

# Relationships

## Builds Upon
- **Field extension** -- Number fields are extensions of Q

## Contrasts With
- **Function field** -- Extensions of C(t) rather than Q

# Source Reference

Chapter 15: Fields, Section 15.1, page 453.

# Verification Notes

- Definition source: Direct from Artin, p. 453
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
