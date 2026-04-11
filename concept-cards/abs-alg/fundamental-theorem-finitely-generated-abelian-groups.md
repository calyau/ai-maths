---
concept: Fundamental Theorem of Finitely Generated Abelian Groups
slug: fundamental-theorem-finitely-generated-abelian-groups
category: group-theory
subcategory: direct-semidirect-products
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Direct and Semidirect Products and Abelian Groups"
chapter_number: 5
pdf_page: 158
section: "5.2 The Fundamental Theorem of Finitely Generated Abelian Groups"
extraction_confidence: high
aliases:
  - "FTFGAG"
  - "classification of finitely generated abelian groups"
  - "structure theorem for finitely generated abelian groups"
prerequisites:
  - direct-product
  - cyclic-group
  - lagranges-theorem
  - sylow-p-subgroup
extends:
  - direct-product
related:
  - invariant-factors
  - elementary-divisors
  - elementary-abelian-group
contrasts_with: []
answers_questions:
  - "How are finitely generated abelian groups classified?"
  - "What are invariant factors and elementary divisors?"
---

# Quick Definition
Every finitely generated abelian group is isomorphic to Z^r x Z_{n_1} x Z_{n_2} x ... x Z_{n_s}, where r >= 0, each n_j >= 2, and n_{i+1} | n_i. This decomposition is unique.

# Core Definition
Theorem 3: Let G be a finitely generated abelian group. Then (1) G is isomorphic to Z^r x Z_{n_1} x Z_{n_2} x ... x Z_{n_s} for some integers r, n_1, ..., n_s with r >= 0, n_j >= 2, and n_{i+1} | n_i for 1 <= i <= s-1; (2) this expression is unique (Dummit & Foote, p. 158). The integer r is the free rank (Betti number) and the n_i are the invariant factors. A finite abelian group has free rank 0. Theorem 5 gives the equivalent elementary divisor decomposition.

# Prerequisites
- **Direct product** — The decomposition is a direct product
- **Cyclic group** — The factors are cyclic groups
- **Lagrange's theorem** — Used in structure analysis
- **Sylow p-subgroup** — Primary decomposition uses Sylow subgroups

# Key Properties
1. Existence: every finitely generated abelian group decomposes as stated
2. Uniqueness: the free rank and invariant factors are unique
3. A finite abelian group has free rank 0
4. Every prime divisor of |G| divides the first invariant factor n_1
5. If |G| is squarefree, G must be cyclic (Corollary 4)
6. The number of abelian groups of order p_1^{a_1} ... p_k^{a_k} equals the product of the number of partitions of each a_i

# Examples
**Example 1** (p. 162): For n = 180 = 2^2 * 3^2 * 5, there are exactly 4 abelian groups: Z_180, Z_90 x Z_2, Z_60 x Z_3, Z_30 x Z_6.

**Example 2** (p. 164): There are exactly 7 abelian groups of order p^5, corresponding to the 7 partitions of 5.

# Relationships
## Builds Upon
- **Direct product** — The decomposition is a direct product of cyclic groups
## Enables
- **Invariant factors** — The unique integers in the decomposition
- **Elementary divisors** — An alternative decomposition
## Related
- **Elementary abelian group** — The special case where all invariant factors equal p

# Common Errors
- **Error**: Listing invariant factors that don't satisfy the divisibility condition
  **Correction**: n_{i+1} must divide n_i; for example, (6, 4) is not a valid invariant factor list since 4 does not divide 6

# Source Reference
Chapter 5, Section 5.2, Theorems 3 and 5, pages 158-168.

# Verification Notes
- Definition source: Direct from Theorem 3, p. 158
- Confidence: HIGH — major theorem
- Uncertainties: None
