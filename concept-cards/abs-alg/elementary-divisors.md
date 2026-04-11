---
concept: Elementary Divisors
slug: elementary-divisors
category: group-theory
subcategory: direct-semidirect-products
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Direct and Semidirect Products and Abelian Groups"
chapter_number: 5
pdf_page: 162
section: "5.2 The Fundamental Theorem of Finitely Generated Abelian Groups"
extraction_confidence: high
aliases:
  - "elementary divisor decomposition"
  - "primary decomposition"
prerequisites:
  - fundamental-theorem-finitely-generated-abelian-groups
  - invariant-factors
  - sylow-p-subgroup
extends:
  - fundamental-theorem-finitely-generated-abelian-groups
related:
  - invariant-factors
contrasts_with:
  - invariant-factors
answers_questions:
  - "What are the elementary divisors of a finite abelian group?"
  - "How do elementary divisors differ from invariant factors?"
---

# Quick Definition
The elementary divisors of a finite abelian group are the prime-power factors in the decomposition G = Z_{p_1^{b_1}} x Z_{p_2^{b_2}} x ... x Z_{p_t^{b_t}}, obtained by decomposing each Sylow subgroup into cyclic factors. They are the invariant factors of the individual Sylow subgroups.

# Core Definition
Theorem 5: Let G be a finite abelian group of order n = p_1^{a_1} ... p_k^{a_k}. Then (1) G = A_1 x ... x A_k where |A_i| = p_i^{a_i}; (2) each A_i decomposes as Z_{p^{b_1}} x ... x Z_{p^{b_t}} with b_1 >= ... >= b_t >= 1 and b_1 + ... + b_t = a_i; (3) this decomposition is unique (Dummit & Foote, p. 162). The integers p_j^{b_{ij}} are called the elementary divisors. The number of abelian groups of order p^a equals the number of partitions of a.

# Prerequisites
- **Fundamental theorem of finitely generated abelian groups** — Elementary divisors provide an equivalent form
- **Invariant factors** — Related alternative decomposition
- **Sylow p-subgroup** — Each A_i is a Sylow subgroup

# Key Properties
1. Elementary divisors are prime powers
2. For each prime p, the exponents form a partition of the p-part of the order
3. The number of abelian groups of order p^a = number of partitions of a
4. The number of abelian groups of order n = product of partition counts for each prime power
5. Two abelian groups are isomorphic iff they have the same elementary divisors

# Examples
**Example 1** (p. 164): Abelian groups of order p^5 correspond to 7 partitions of 5: (5), (4,1), (3,2), (3,1,1), (2,2,1), (2,1,1,1), (1,1,1,1,1).

**Example 2** (p. 166): Z_6 x Z_15 has elementary divisors 2, 3, 3, 5 (not the same as Z_10 x Z_9 which has 2, 5, 9).

# Relationships
## Builds Upon
- **Fundamental theorem of finitely generated abelian groups**
## Contrasts With
- **Invariant factors** — Elementary divisors are prime powers; invariant factors satisfy divisibility

# Source Reference
Chapter 5, Section 5.2, Theorem 5, pages 162-168.

# Verification Notes
- Definition source: Direct from Theorem 5, p. 162
- Confidence: HIGH
- Uncertainties: None
