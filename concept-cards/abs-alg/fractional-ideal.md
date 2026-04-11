---
concept: Fractional Ideal
slug: fractional-ideal
category: commutative-algebra
subcategory: ring-structures
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Artinian Rings, Discrete Valuation Rings, and Dedekind Domains"
chapter_number: 16
pdf_page: 762
section: "16.2 Discrete Valuation Rings"
extraction_confidence: high
aliases:
  - "invertible ideal"
prerequisites:
  - integral-domain
extends:
  - ideal
related:
  - dedekind-domain
  - ideal-class-group
contrasts_with: []
answers_questions:
  - "What is a fractional ideal?"
---

# Quick Definition
A fractional ideal of an integral domain R is an R-submodule A of the fraction field K such that dA ⊆ R for some nonzero d ∈ R. It is invertible if AA' = R for some fractional ideal A'.

# Core Definition
A **fractional ideal** of an integral domain R with fraction field K is an R-submodule A of K such that dA ⊆ R for some nonzero d ∈ R. A fractional ideal is **invertible** if there exists a fractional ideal A' with AA' = R. In a Dedekind domain, every nonzero fractional ideal is invertible.

# Prerequisites
- **integral-domain** — R must be a domain with fraction field K

# Key Properties
1. Ordinary ideals are fractional ideals (take d = 1)
2. Principal fractional ideals (a) = Ra for a ∈ K× are always invertible
3. In a Dedekind domain, all nonzero fractional ideals are invertible

# Relationships
## Enables
- **ideal-class-group** — Defined using invertible fractional ideals modulo principal ones

# Source Reference
Chapter 16, Sections 16.2-16.3, pages 762-764.

# Verification Notes
- Confidence: HIGH — explicit definition
