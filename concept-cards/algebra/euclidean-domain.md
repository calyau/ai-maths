---
concept: Euclidean Domain
slug: euclidean-domain
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
aliases: []
prerequisites:
  - integral-domain
  - division-with-remainder
extends:
  - integral-domain
related:
  - principal-ideal-domain
  - unique-factorization-domain
  - euclidean-algorithm
contrasts_with: []
answers_questions:
  - "What is a Euclidean domain?"
  - "What distinguishes a PID from a UFD?"
---

# Quick Definition

A Euclidean domain is an integral domain equipped with a size function such that division with remainder is always possible: for any a != 0 and b, there exist q and r with b = aq + r and either r = 0 or sigma(r) < sigma(a).

# Core Definition

An integral domain R is a Euclidean domain if there is a size function sigma on R (mapping nonzero elements to nonneg integers) such that for any elements a, b with a != 0, there exist q, r in R with b = aq + r, and either r = 0 or sigma(r) < sigma(a) (Artin, formula 12.2.4, p. 371).

# Prerequisites

- **Integral domain** -- A Euclidean domain is a domain with extra structure
- **Division with remainder** -- The key property

# Key Properties

1. Every Euclidean domain is a PID (Proposition 12.2.7)
2. Every PID is a UFD (Proposition 12.2.14)
3. The hierarchy is: Euclidean domain => PID => UFD

# Examples

**Example 1** (p. 371): Z is Euclidean with sigma(a) = |a|.

**Example 2** (p. 371): F[x] over a field F is Euclidean with sigma(f) = deg f.

**Example 3** (p. 371): Z[i] is Euclidean with sigma(a) = |a|^2 = N(a).

# Relationships

## Builds Upon
- **Integral domain** -- A Euclidean domain is a special domain

## Enables
- **Principal ideal domain** -- Every Euclidean domain is a PID
- **Euclidean algorithm** -- Computing gcds in Euclidean domains

# Source Reference

Chapter 12: Factoring, Section 12.2, formula 12.2.4, Proposition 12.2.5, pages 371-372.

# Verification Notes

- Definition source: Direct from formula 12.2.4
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
