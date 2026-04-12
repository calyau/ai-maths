---
concept: Divisibility
slug: divisibility
category: factorization
subcategory: basic-divisibility
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Factoring"
chapter_number: 12
pdf_page: 370
section: "Unique Factorization Domains"
extraction_confidence: high
aliases: []
prerequisites:
  - integral-domain
extends: []
related:
  - associates
  - irreducible-element
  - prime-element
  - principal-ideal
contrasts_with: []
answers_questions:
  - "What does it mean for one element to divide another in a ring?"
---

# Quick Definition

In an integral domain R, element a divides b (written a | b) if b = aq for some q in R. Equivalently, (b) is contained in (a).

# Core Definition

Let R be an integral domain. Then: a divides b if b = aq for some q in R; a is a proper divisor of b if b = aq and neither a nor q is a unit; a and b are associates if each divides the other, equivalently b = ua for a unit u (Artin, formula 12.2.1, p. 370).

These concepts have ideal-theoretic interpretations: a divides b iff (b) subset (a); a is a proper divisor of b iff (b) < (a) < (1); a and b are associates iff (a) = (b) (formula 12.2.2).

# Prerequisites

- **Integral domain** -- Divisibility theory requires the cancellation law

# Key Properties

1. a | b iff (b) subset (a) -- divisibility reverses ideal containment
2. Units divide everything
3. Associates generate the same principal ideal

# Examples

**Example 1** (p. 370): In Z, 3 divides 12 since 12 = 3 * 4.

# Relationships

## Builds Upon
- **Integral domain** -- Context for divisibility

## Enables
- **Irreducible element** -- Defined via divisibility
- **Prime element** -- Defined via divisibility of products

# Source Reference

Chapter 12: Factoring, Section 12.2, formula 12.2.1, page 370.

# Verification Notes

- Definition source: Direct from formula 12.2.1
- Confidence rationale: Explicit tabular definition
- Uncertainties: None
- Cross-reference status: Verified
