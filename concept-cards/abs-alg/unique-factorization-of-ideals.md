---
concept: Unique Factorization of Ideals
slug: unique-factorization-of-ideals
category: commutative-algebra
subcategory: number-theory
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Artinian Rings, Discrete Valuation Rings, and Dedekind Domains"
chapter_number: 16
pdf_page: 766
section: "16.3 Dedekind Domains"
extraction_confidence: high
aliases: []
prerequisites:
  - dedekind-domain
extends: []
related:
  - primary-decomposition
contrasts_with: []
answers_questions:
  - "Do ideals in Dedekind domains factor uniquely?"
---

# Quick Definition
In a Dedekind domain, every nonzero proper ideal can be written uniquely as a product of prime ideals: I = P_1^{e_1} ··· P_n^{e_n}.

# Core Definition
**Theorem 15(5) / Corollary 16**: In a Dedekind domain R, every nonzero proper ideal can be written uniquely (up to order) as a product of powers of distinct prime ideals: I = P_1^{e_1} P_2^{e_2} ··· P_n^{e_n} (p. 766). This replaces unique factorization of elements (which may fail).

# Prerequisites
- **dedekind-domain** — This is a characterizing property

# Key Properties
1. Factorization exists and is unique
2. "To contain is to divide": A ⊆ B iff B | A (Proposition 17)
3. A + B = gcd(A,B) in terms of prime factorizations (Proposition 17)
4. Generalizes unique factorization of elements in PIDs/UFDs

# Relationships
## Builds Upon
- **dedekind-domain** — Unique factorization characterizes Dedekind domains

# Source Reference
Chapter 16, Section 16.3, Theorem 15(5) and Corollary 16, pages 766-768.

# Verification Notes
- Confidence: HIGH — major theorem with complete proof
