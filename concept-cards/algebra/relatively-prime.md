---
concept: Relatively Prime Elements
slug: relatively-prime
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
  - "coprime"
prerequisites:
  - greatest-common-divisor
extends: []
related:
  - chinese-remainder-theorem
contrasts_with: []
answers_questions:
  - "What does it mean for elements to be relatively prime?"
---

# Quick Definition

Elements a and b of an integral domain are relatively prime if their only common factors are units, i.e., gcd(a,b) = 1. In a PID, this implies 1 = ra + sb for some r, s.

# Core Definition

When elements a and b have no common factors except units, they are said to be relatively prime (Artin, p. 372). In a PID, a and b are relatively prime if and only if 1 is a linear combination ra + sb (Corollary 12.2.9(a)).

# Prerequisites

- **Greatest common divisor** -- Relatively prime means gcd = 1

# Key Properties

1. In a PID, relatively prime implies Bezout's identity: 1 = ra + sb
2. In a general UFD, Bezout's identity may fail even for coprime elements

# Examples

**Example 1** (p. 377): In Z[x], 2 and x are relatively prime, but 1 != r*2 + s*x for any r, s in Z[x].

# Relationships

## Builds Upon
- **Greatest common divisor** -- gcd = 1

## Related
- **Chinese Remainder Theorem** -- Applies when ideals are coprime

# Source Reference

Chapter 12: Factoring, Section 12.2, page 372.

# Verification Notes

- Definition source: Direct from text
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
