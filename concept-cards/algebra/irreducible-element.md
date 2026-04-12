---
concept: Irreducible Element
slug: irreducible-element
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
  - divisibility
  - unit-element
extends: []
related:
  - prime-element
  - unique-factorization-domain
contrasts_with:
  - prime-element
answers_questions:
  - "What distinguishes an irreducible element from a prime element?"
---

# Quick Definition

An element a of an integral domain is irreducible if it is not a unit and has no proper divisor -- its only divisors are units and associates of itself.

# Core Definition

An element a of an integral domain is irreducible if a is not a unit, and it has no proper divisor -- its only divisors are units and associates. In ideal terms: (a) < (1), and there is no principal ideal (c) such that (a) < (c) < (1) (Artin, formula 12.2.1, p. 370).

# Prerequisites

- **Divisibility** -- Irreducibility is a divisibility concept
- **Unit element** -- Must exclude units

# Key Properties

1. In a PID, irreducible = prime (Corollary 12.2.9)
2. In general, prime implies irreducible, but NOT conversely
3. The principal ideal (a) is maximal among principal ideals if and only if a is irreducible

# Context & Application

The distinction between irreducible and prime is one of the most important subtleties in ring theory. In Z[sqrt(-5)], the element 2 is irreducible but not prime.

# Examples

**Example 1** (p. 370): In Z[sqrt(-5)], all of 2, 3, 1+sqrt(-5), 1-sqrt(-5) are irreducible.

**Example 2** (p. 374): In Z[sqrt(-5)], 2 is irreducible but NOT prime: 2 | (1+sqrt(-5))(1-sqrt(-5)) but 2 does not divide either factor.

# Relationships

## Builds Upon
- **Divisibility** -- Defined via divisibility properties

## Related
- **Unique factorization domain** -- Elements factor into irreducibles

## Contrasts With
- **Prime element** -- Prime implies irreducible; the converse holds in PIDs but fails in general

# Common Confusions

- **Confusion**: Thinking irreducible and prime are always the same
  **Clarification**: They coincide in PIDs (and hence in Z and F[x]), but in general rings like Z[sqrt(-5)], an irreducible element need not be prime

# Source Reference

Chapter 12: Factoring, Section 12.2, formula 12.2.1, page 370.

# Verification Notes

- Definition source: Direct from formula 12.2.1
- Confidence rationale: Explicit definition with key examples
- Uncertainties: None
- Cross-reference status: Verified
