---
concept: Elementary Divisors
slug: elementary-divisors
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
aliases: []
prerequisites:
  - invariant-factors
extends: []
related:
  - structure-theorem-finitely-generated-modules-pid
contrasts_with:
  - invariant-factors
answers_questions:
  - "What are elementary divisors?"
---

# Quick Definition

Elementary divisors are the prime power factors obtained by further decomposing the invariant factors. They give the finest decomposition of a finitely generated module over a PID into cyclic summands.

# Core Definition

Every finite abelian group is a direct sum of cyclic groups of prime power orders (Artin, Corollary 14.7.6). These prime power orders are the elementary divisors of the group, and they are uniquely determined (Theorem 14.7.7). The elementary divisors are obtained by factoring each invariant factor into prime powers.

# Prerequisites

- **Invariant factors** -- Elementary divisors refine the invariant factor decomposition

# Key Properties

1. The elementary divisors are uniquely determined by the module (14.7.7)
2. They are obtained by factoring invariant factors: if d_i = p_1^{a_1} ... p_r^{a_r}, each prime power contributes an elementary divisor
3. Two finite abelian groups are isomorphic iff they have the same elementary divisors

# Context & Application

The elementary divisor decomposition is often more convenient than the invariant factor decomposition for recognizing isomorphism types. For instance, counting elements of specific orders distinguishes groups with different elementary divisors.

# Examples

**Example 1** (p. 447): C_2 + C_2 + C_4 has elementary divisors 2, 2, 4, while C_4 + C_4 has elementary divisors 4, 4. These groups are not isomorphic because C_4 + C_4 has four elements of order dividing 2, while C_2 + C_2 + C_4 has eight.

# Relationships

## Builds Upon
- **Invariant factors** -- Elementary divisors are prime power factors of invariant factors

## Contrasts With
- **Invariant factors** -- Invariant factors have the divisibility condition; elementary divisors are prime powers

# Source Reference

Chapter 14: Linear Algebra in a Ring, Section 14.7, pages 446-448. Corollary 14.7.6, Theorem 14.7.7.

# Verification Notes

- Definition source: Direct from Artin, Corollary 14.7.6
- Confidence rationale: Explicitly stated with uniqueness proof
- Uncertainties: None
- Cross-reference status: Verified
