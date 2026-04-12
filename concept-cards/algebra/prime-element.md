---
concept: Prime Element
slug: prime-element
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
  - integral-domain
extends: []
related:
  - irreducible-element
  - prime-ideal
  - unique-factorization-domain
contrasts_with:
  - irreducible-element
answers_questions:
  - "What distinguishes an irreducible element from a prime element?"
---

# Quick Definition

A prime element p of an integral domain is a non-unit such that whenever p divides a product ab, p divides a or p divides b.

# Core Definition

An element p of an integral domain R is a prime element if p is not a unit, and whenever p divides a product ab, then p divides a or p divides b (Artin, formula 12.2.1, p. 370). In any integral domain, a prime element is irreducible (Lemma 12.2.10), but the converse may fail.

# Prerequisites

- **Divisibility** -- Prime is defined via divisibility of products
- **Integral domain** -- Context for prime elements

# Key Properties

1. Prime implies irreducible in any domain (Lemma 12.2.10)
2. The converse (irreducible implies prime) holds in PIDs (Corollary 12.2.9)
3. In a UFD, irreducible = prime (Proposition 12.2.14)
4. (p) is a prime ideal if and only if p is a prime element (Corollary 13.5.2)

# Examples

**Example 1** (p. 374): In Z[sqrt(-5)], 2 is irreducible but NOT prime: 2 | 6 = (1+sqrt(-5))(1-sqrt(-5)) but 2 does not divide either factor.

**Example 2** (p. 373): In Z and F[x], every irreducible element is prime.

# Relationships

## Builds Upon
- **Divisibility** -- Defined via divisibility

## Enables
- **Unique factorization domain** -- A domain has unique factorization iff every irreducible is prime (and factoring terminates)

## Contrasts With
- **Irreducible element** -- Prime is a strictly stronger condition in general

# Common Confusions

- **Confusion**: Assuming irreducible and prime are the same in all rings
  **Clarification**: They agree in PIDs and UFDs, but not in general integral domains

# Source Reference

Chapter 12: Factoring, Section 12.2, formula 12.2.1, page 370, Lemma 12.2.10, page 373.

# Verification Notes

- Definition source: Direct from formula 12.2.1 and Lemma 12.2.10
- Confidence rationale: Explicit definition with critical examples
- Uncertainties: None
- Cross-reference status: Verified
