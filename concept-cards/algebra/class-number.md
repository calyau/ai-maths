---
concept: Class Number
slug: class-number
category: number-theory
subcategory: class-group
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Quadratic Number Fields"
chapter_number: 13
pdf_page: 394
section: "Ideal Classes"
extraction_confidence: high
aliases: []
prerequisites:
  - class-group
extends: []
related:
  - unique-factorization-domain
contrasts_with: []
answers_questions:
  - "What is the class number?"
---

# Quick Definition

The class number of a ring of integers R is the order of the class group C. It is always finite. R is a UFD (equivalently, a PID) if and only if the class number is 1.

# Core Definition

The number of ideal classes in R is the class number of R (Artin, p. 410). The class number is finite (Theorem 13.7.10). R is a UFD iff the class number is 1 (Theorem 13.5.6).

# Prerequisites

- **Class group** -- The class number is |C|

# Key Properties

1. Class number 1 means R is a UFD (and PID)
2. For imaginary quadratic fields, class number 1 occurs for exactly 9 values of d (Theorem 13.2.5)
3. For d = 2 or 3 mod 4, the class number is even when d < -2

# Examples

**Example 1** (p. 413): d = -5: class number 2. d = -7: class number 1. d = -14: class number 4. d = -23: class number 3.

**Example 2** (p. 398): The nine values of d giving class number 1 are: -1, -2, -3, -7, -11, -19, -43, -67, -163.

# Relationships

## Builds Upon
- **Class group** -- Class number = |C|

## Related
- **Unique factorization domain** -- Class number 1 iff UFD

# Source Reference

Chapter 13: Quadratic Number Fields, Sections 13.3, 13.7, pages 399, 410-416.

# Verification Notes

- Definition source: Direct from text
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
