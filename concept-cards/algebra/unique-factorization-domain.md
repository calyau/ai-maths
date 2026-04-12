---
concept: Unique Factorization Domain
slug: unique-factorization-domain
category: factorization
subcategory: domain-hierarchy
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
  - "UFD"
prerequisites:
  - integral-domain
  - irreducible-element
  - prime-element
extends:
  - integral-domain
related:
  - principal-ideal-domain
  - euclidean-domain
  - fundamental-theorem-of-arithmetic
contrasts_with: []
answers_questions:
  - "What is a unique factorization domain?"
  - "What distinguishes a PID from a UFD?"
---

# Quick Definition

A unique factorization domain (UFD) is an integral domain where every nonzero non-unit element can be written as a product of irreducible elements, and this factorization is unique up to ordering and associate factors.

# Core Definition

An integral domain R is a unique factorization domain if: (1) Factoring terminates: every nonzero non-unit can be written as a product of irreducible elements, and (2) the irreducible factorization is unique up to reordering and replacing factors by associates (Artin, formula 12.2.12, p. 374).

R is a UFD if and only if factoring terminates and every irreducible element is prime (Proposition 12.2.14).

# Prerequisites

- **Integral domain** -- A UFD is a domain
- **Irreducible element** -- Factorization is into irreducibles
- **Prime element** -- In a UFD, irreducible = prime

# Key Properties

1. In a UFD, irreducible = prime
2. Every PID is a UFD (but not conversely)
3. Factoring terminates iff there is no infinite ascending chain of principal ideals
4. Any pair of elements has a gcd (Proposition 12.2.16)
5. In a UFD that is not a PID, the gcd need not be a linear combination ra + sb

# Examples

**Example 1** (p. 374): Z and F[x] are UFDs (they are PIDs, hence UFDs).

**Example 2** (p. 374): Z[sqrt(-5)] is NOT a UFD: 2 * 3 = (1+sqrt(-5))(1-sqrt(-5)) are inequivalent factorizations.

**Example 3** (p. 379): Z[x] is a UFD (Theorem 12.3.8) but not a PID.

# Relationships

## Builds Upon
- **Integral domain** -- UFDs are special domains

## Related
- **Principal ideal domain** -- Every PID is a UFD
- **Fundamental theorem of arithmetic** -- Z is a UFD

# Source Reference

Chapter 12: Factoring, Section 12.2, formula 12.2.12, Proposition 12.2.14, pages 374-376.

# Verification Notes

- Definition source: Direct from formula 12.2.12 and Proposition 12.2.14
- Confidence rationale: Explicit definition with key characterization
- Uncertainties: None
- Cross-reference status: Verified
