---
concept: Krull Dimension
slug: krull-dimension
category: commutative-algebra
subcategory: ring-structures
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Artinian Rings, Discrete Valuation Rings, and Dedekind Domains"
chapter_number: 16
pdf_page: 750
section: "16.1 Artinian Rings"
extraction_confidence: high
aliases:
  - "dimension of a ring"
prerequisites:
  - prime-ideal
extends: []
related:
  - artinian-ring
  - discrete-valuation-ring
  - dedekind-domain
contrasts_with: []
answers_questions:
  - "What is the Krull dimension of a ring?"
---

# Quick Definition
The Krull dimension of a commutative ring R is the supremum of the lengths of all chains of prime ideals P_0 ⊊ P_1 ⊊ ··· ⊊ P_n in R.

# Core Definition
The **Krull dimension** of R is the supremum of lengths n of strictly increasing chains of prime ideals P_0 ⊊ P_1 ⊊ ··· ⊊ P_n. Artinian rings have Krull dimension 0. DVRs and Dedekind domains have Krull dimension 1. Fields have Krull dimension 0.

# Prerequisites
- **prime-ideal** — Dimension is measured by chains of primes

# Key Properties
1. Fields have Krull dimension 0
2. PIDs that are not fields have Krull dimension 1
3. k[x_1,...,x_n] has Krull dimension n
4. Krull dimension 0 + Noetherian = Artinian

# Relationships
## Enables
- **artinian-ring** — Artinian = Noetherian + Krull dimension 0
- **dedekind-domain** — Dedekind domains have Krull dimension 1

# Source Reference
Chapter 16, Section 16.1, page 750.

# Verification Notes
- Confidence: HIGH — standard definition used throughout
