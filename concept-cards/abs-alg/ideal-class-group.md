---
concept: Ideal Class Group
slug: ideal-class-group
category: commutative-algebra
subcategory: number-theory
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Artinian Rings, Discrete Valuation Rings, and Dedekind Domains"
chapter_number: 16
pdf_page: 763
section: "16.2 Discrete Valuation Rings"
extraction_confidence: high
aliases:
  - "class group"
  - "class number"
prerequisites:
  - fractional-ideal
  - dedekind-domain
extends: []
related:
  - algebraic-integer
contrasts_with: []
answers_questions:
  - "What is the ideal class group?"
  - "What does the class number measure?"
---

# Quick Definition
The ideal class group of a Dedekind domain R is the group of invertible fractional ideals modulo principal fractional ideals. Its order (the class number) measures the failure of unique factorization of elements.

# Core Definition
The **ideal class group** of a Dedekind domain R is the quotient group of invertible fractional ideals by principal fractional ideals. The **class number** is the order of this group. R is a PID iff the class number is 1 (Corollary 20, p. 775). For number fields, the class number is always finite.

# Prerequisites
- **fractional-ideal** — Elements are classes of fractional ideals
- **dedekind-domain** — The ideal class group is defined for Dedekind domains

# Key Properties
1. Trivial class group iff R is a PID
2. Measures failure of unique factorization of elements
3. Always finite for rings of integers in number fields
4. For any abelian group A, there exists a Dedekind domain with class group ≅ A

# Relationships
## Builds Upon
- **dedekind-domain** — The class group is defined for Dedekind domains

# Source Reference
Chapter 16, Sections 16.2-16.3, pages 763-775.

# Verification Notes
- Confidence: HIGH — explicit definition with key theorems
