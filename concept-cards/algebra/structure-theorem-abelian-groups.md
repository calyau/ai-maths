---
concept: Structure Theorem for Finite Abelian Groups
slug: structure-theorem-abelian-groups
category: module-theory
subcategory: classification
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Algebra in a Ring"
chapter_number: 14
pdf_page: 432
section: "14.7 Structure of Abelian Groups"
extraction_confidence: high
aliases:
  - "fundamental theorem of finite abelian groups"
prerequisites:
  - structure-theorem-finitely-generated-modules-pid
extends: []
related:
  - invariant-factors
  - elementary-divisors
  - direct-sum-modules
contrasts_with: []
answers_questions:
  - "How are finite abelian groups classified?"
---

# Quick Definition

Every finitely generated abelian group is a direct sum of cyclic groups. A finite abelian group decomposes uniquely as a direct sum of cyclic groups of prime power order.

# Core Definition

A finitely generated abelian group V is a direct sum of cyclic subgroups C_{d_1}, ..., C_{d_k} and a free abelian group L: V = C_{d_1} + ... + C_{d_k} + L, where d_i > 1 and d_1 | d_2 | ... | d_{k-1} (Artin, Theorem 14.7.3). Alternatively, every finite abelian group is a direct sum of cyclic groups of prime power orders (Corollary 14.7.6), and these orders are uniquely determined (Theorem 14.7.7).

# Prerequisites

- **Structure theorem for finitely generated modules over a PID** -- This is the Z-module specialization

# Key Properties

1. The decomposition into cyclic summands is essentially unique
2. Two forms: invariant factor form (d_1 | ... | d_k) and elementary divisor form (prime powers)
3. A finite abelian group is determined up to isomorphism by its elementary divisors
4. The number of isomorphism classes of abelian groups of order n depends on the prime factorization of n

# Context & Application

This is one of the most concrete applications of the structure theorem. It allows complete classification: to determine whether two finite abelian groups are isomorphic, compute their elementary divisors and compare.

# Examples

**Example 1** (p. 447): If the order is 30 = 2 * 3 * 5, then V must be C_2 + C_3 + C_5 = C_30.

**Example 2** (p. 447): C_2 + C_2 + C_4 is not isomorphic to C_4 + C_4, because the former has 8 elements of order dividing 2 while the latter has only 4.

# Relationships

## Builds Upon
- **Structure theorem for finitely generated modules over a PID** -- The Z-module case

## Related
- **Invariant factors** -- The d_i in the decomposition
- **Elementary divisors** -- The prime power form

# Common Errors

- **Error**: Assuming abelian groups of the same order are isomorphic
  **Correction**: Groups of the same order can have different decompositions (e.g., C_4 vs C_2 + C_2).

# Source Reference

Chapter 14: Linear Algebra in a Ring, Section 14.7, pages 443-448. Theorem 14.7.3, Corollary 14.7.6, Theorem 14.7.7.

# Verification Notes

- Definition source: Direct from Artin, Theorem 14.7.3
- Confidence rationale: Complete proof and examples
- Uncertainties: None
- Cross-reference status: Verified
