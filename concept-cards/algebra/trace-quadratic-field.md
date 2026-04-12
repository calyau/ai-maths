---
concept: Trace in a Quadratic Field
slug: trace-quadratic-field
category: number-theory
subcategory: quadratic-fields
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Quadratic Number Fields"
chapter_number: 13
pdf_page: 394
section: "Algebraic Integers"
extraction_confidence: high
aliases: []
prerequisites:
  - quadratic-field
extends: []
related:
  - norm-quadratic-field
contrasts_with: []
answers_questions:
  - "What is the trace in a quadratic field?"
---

# Quick Definition

The trace of alpha = a + b*sqrt(d) in Q[sqrt(d)] is Tr(alpha) = alpha + alpha-bar = 2a. The norm and trace are the coefficients of the minimal polynomial x^2 - Tr(alpha)*x + N(alpha).

# Core Definition

For alpha = a + b*delta in Q[delta] (delta^2 = d), the conjugate is alpha' = a - b*delta. The trace is Tr(alpha) = alpha + alpha' = 2a, and the norm is N(alpha) = alpha*alpha' = a^2 - b^2*d. The element alpha is a root of x^2 - 2ax + (a^2 - b^2*d) (Artin, formula 13.1.3, p. 395).

# Prerequisites

- **Quadratic field** -- Trace is defined for elements of Q[sqrt(d)]

# Key Properties

1. Tr(alpha) = 2a for alpha = a + b*sqrt(d)
2. alpha is an algebraic integer iff both 2a and a^2 - b^2*d are integers
3. The trace is additive: Tr(alpha + beta) = Tr(alpha) + Tr(beta)

# Examples

**Example 1** (p. 395): For alpha = 3 + 2*sqrt(-5), Tr(alpha) = 6 and N(alpha) = 9 + 20 = 29.

# Relationships

## Related
- **Norm (quadratic field)** -- Norm and trace together determine the minimal polynomial

# Source Reference

Chapter 13: Quadratic Number Fields, Section 13.1, formula 13.1.3, page 395.

# Verification Notes

- Definition source: Direct from formula 13.1.3
- Confidence rationale: Explicit formula
- Uncertainties: None
- Cross-reference status: Verified
