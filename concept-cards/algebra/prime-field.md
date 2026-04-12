---
concept: Prime Field
slug: prime-field
category: field-theory
subcategory: basic-definitions
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
  - "F_p"
prerequisites:
  - field
extends: []
related:
  - finite-field
  - field-extension
contrasts_with: []
answers_questions:
  - "What is a prime field?"
---

# Quick Definition

A prime field is the smallest subfield of any field. In characteristic zero, the prime field is Q; in characteristic p, it is F_p = Z/pZ.

# Core Definition

Every field contains a smallest subfield, called its prime field. Any subfield of C contains Q, so Q is the prime field of characteristic zero. A finite field of characteristic p contains F_p = Z/pZ as its prime field (Artin, p. 453).

# Prerequisites

- **Field** -- Prime fields are the simplest fields

# Key Properties

1. Every field has characteristic 0 or prime p
2. In characteristic 0, the prime field is Q
3. In characteristic p, the prime field is F_p with p elements
4. Every field extension starts from a prime field

# Context & Application

Prime fields are the starting point for all field extensions. Number fields are extensions of Q, and finite fields are extensions of F_p.

# Examples

**Example 1** (p. 453): Q is the prime field contained in every number field.

**Example 2** (p. 453): F_p is the prime field contained in every finite field of characteristic p.

# Relationships

## Enables
- **Field extension** -- All extensions start from a prime field
- **Finite field** -- Finite fields are extensions of F_p

# Source Reference

Chapter 15: Fields, Section 15.1, page 453.

# Verification Notes

- Definition source: Direct from Artin, p. 453
- Confidence rationale: Explicitly described
- Uncertainties: None
- Cross-reference status: Verified
