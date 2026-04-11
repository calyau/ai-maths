---
concept: Integral Closure
slug: integral-closure
category: commutative-algebra
subcategory: ring-extensions
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Commutative Rings and Algebraic Geometry"
chapter_number: 15
pdf_page: 715
section: "15.3 Integral Extensions and Hilbert's Nullstellensatz"
extraction_confidence: high
aliases:
  - "normalization"
  - "integrally closed"
  - "normal domain"
prerequisites:
  - integral-extension
extends: []
related:
  - dedekind-domain
  - discrete-valuation-ring
contrasts_with: []
answers_questions:
  - "What is the integral closure of a ring?"
  - "When is a domain integrally closed?"
---

# Quick Definition
The integral closure of R in S is the set of all elements of S integral over R. An integral domain is integrally closed (or normal) if it equals its integral closure in its fraction field.

# Core Definition
The **integral closure** of R in S is the set of elements of S that are integral over R. The integral closure of an integral domain R in its field of fractions is called the **normalization** of R. An integral domain is **integrally closed** (or **normal**) if it is integrally closed in its field of fractions (Definition, p. 715). By Corollary 25, the integral closure of R in S is itself integrally closed in S.

# Prerequisites
- **integral-extension** — Elements must be integral over R

# Key Properties
1. Every UFD is integrally closed (Example 3, p. 717)
2. The integral closure is integrally closed (Corollary 25)
3. The process stabilizes: taking integral closure twice gives the same ring
4. k[x,y]/(x^2-y^3) is not integrally closed

# Examples
**Example** (p. 717): Z, k[x], k[x,y] are all integrally closed since they are UFDs.

# Relationships
## Builds Upon
- **integral-extension** — Integral closure collects all integral elements

## Enables
- **dedekind-domain** — Dedekind domains are integrally closed Noetherian domains of Krull dimension 1

# Source Reference
Chapter 15, Section 15.3, Definition and Examples, pages 715-717.

# Verification Notes
- Confidence: HIGH — explicit definition
