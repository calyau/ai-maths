---
concept: Associates
slug: associates
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
aliases:
  - "associate elements"
prerequisites:
  - divisibility
  - unit-element
extends: []
related:
  - unique-factorization-domain
contrasts_with: []
answers_questions:
  - "What are associate elements in a ring?"
---

# Quick Definition

Two elements a and b of an integral domain are associates if each divides the other, equivalently if b = ua for some unit u. Associates generate the same principal ideal.

# Core Definition

Elements a and b of an integral domain are associates if each divides the other, or equivalently if b = ua where u is a unit. In terms of ideals, a and b are associates if and only if (a) = (b) (Artin, formula 12.2.1, p. 370).

# Prerequisites

- **Divisibility** -- Associates are defined via mutual divisibility
- **Unit element** -- Associates differ by a unit factor

# Key Properties

1. Being associates is an equivalence relation
2. In unique factorization, factorizations differing only by associate factors are considered equivalent
3. In Z, associates are +/-n; in F[x], associates of a monic polynomial are its nonzero scalar multiples

# Examples

**Example 1** (p. 372): In Z[i], 2 + i and 1 - 2i are associates since -i(2+i) = 1 - 2i.

# Relationships

## Builds Upon
- **Divisibility** -- Associates divide each other

## Related
- **Unique factorization domain** -- Factorization is unique up to associates

# Source Reference

Chapter 12: Factoring, Section 12.2, formula 12.2.1, page 370.

# Verification Notes

- Definition source: Direct from formula 12.2.1
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
