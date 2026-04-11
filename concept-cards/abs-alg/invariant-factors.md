---
concept: Invariant Factors
slug: invariant-factors
category: group-theory
subcategory: direct-semidirect-products
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Direct and Semidirect Products and Abelian Groups"
chapter_number: 5
pdf_page: 159
section: "5.2 The Fundamental Theorem of Finitely Generated Abelian Groups"
extraction_confidence: high
aliases:
  - "invariant factor decomposition"
prerequisites:
  - fundamental-theorem-finitely-generated-abelian-groups
  - direct-product
  - cyclic-group
extends:
  - fundamental-theorem-finitely-generated-abelian-groups
related:
  - elementary-divisors
contrasts_with:
  - elementary-divisors
answers_questions:
  - "What are the invariant factors of a finitely generated abelian group?"
  - "How do invariant factors relate to elementary divisors?"
---

# Quick Definition
The invariant factors of a finitely generated abelian group G are the unique integers n_1 >= n_2 >= ... >= n_s >= 2 with n_{i+1} | n_i such that the torsion part of G is isomorphic to Z_{n_1} x Z_{n_2} x ... x Z_{n_s}. The type of G is (n_1, n_2, ..., n_s).

# Core Definition
The integers n_1, n_2, ..., n_s in Theorem 3 are called the invariant factors of G. The description G = Z^r x Z_{n_1} x ... x Z_{n_s} is called the invariant factor decomposition of G (Dummit & Foote, p. 159). Two finitely generated abelian groups are isomorphic iff they have the same free rank and the same list of invariant factors. For a finite group, the order equals n_1 * n_2 * ... * n_s. Every prime divisor of |G| divides n_1.

# Prerequisites
- **Fundamental theorem of finitely generated abelian groups** — Invariant factors are part of this theorem
- **Direct product** — The decomposition is a direct product
- **Cyclic group** — Factors are cyclic

# Key Properties
1. n_1 >= n_2 >= ... >= n_s >= 2
2. n_{i+1} | n_i (divisibility condition)
3. |G| = n_1 * n_2 * ... * n_s (for finite groups)
4. Every prime dividing |G| divides n_1
5. The exponent of G equals n_1
6. Invariant factors uniquely determine the group up to isomorphism

# Examples
**Example 1** (p. 163): For abelian groups of order 180: the invariant factor lists are (180), (90, 2), (60, 3), (30, 6).

# Relationships
## Builds Upon
- **Fundamental theorem of finitely generated abelian groups**
## Related
- **Elementary divisors** — An alternative way to describe the same decomposition
## Contrasts With
- **Elementary divisors** — Invariant factors satisfy divisibility; elementary divisors are prime powers

# Source Reference
Chapter 5, Section 5.2, pages 159-168.

# Verification Notes
- Definition source: Direct from p. 159
- Confidence: HIGH
- Uncertainties: None
