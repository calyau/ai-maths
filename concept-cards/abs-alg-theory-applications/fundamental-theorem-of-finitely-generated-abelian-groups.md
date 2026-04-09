---
concept: Fundamental Theorem of Finitely Generated Abelian Groups
slug: fundamental-theorem-of-finitely-generated-abelian-groups
category: group-structure
subcategory: classification-theorems
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Structure of Groups"
chapter_number: 13
pdf_page: 175
section: "Finite Abelian Groups"
extraction_confidence: high
aliases: []
prerequisites:
  - fundamental-theorem-of-finite-abelian-groups
  - finitely-generated-group
extends:
  - fundamental-theorem-of-finite-abelian-groups
related: []
contrasts_with: []
answers_questions:
  - "How are finitely generated abelian groups classified?"
---

# Quick Definition

Every finitely generated abelian group is isomorphic to $\mathbb{Z}_{p_1^{\alpha_1}} \times \cdots \times \mathbb{Z}_{p_n^{\alpha_n}} \times \mathbb{Z} \times \cdots \times \mathbb{Z}$, a direct product of cyclic groups of prime power order and copies of $\mathbb{Z}$.

# Core Definition

**Theorem 13.10**: "Every finitely generated abelian group $G$ is isomorphic to a direct product of cyclic groups of the form $\mathbb{Z}_{p_1^{\alpha_1}} \times \mathbb{Z}_{p_2^{\alpha_2}} \times \cdots \times \mathbb{Z}_{p_n^{\alpha_n}} \times \mathbb{Z} \times \cdots \times \mathbb{Z}$, where the $p_i$'s are primes (not necessarily distinct)" (Judson, p. 175).

# Prerequisites

- **Fundamental Theorem of Finite Abelian Groups** — The finite case
- **Finitely generated group** — Applies to finitely generated groups

# Key Properties

1. Generalizes the finite case by allowing copies of $\mathbb{Z}$ (infinite cyclic factors)
2. The number of $\mathbb{Z}$ factors (the rank) is an invariant
3. The torsion subgroup consists of the finite-order elements

# Relationships

## Builds Upon
- **Fundamental Theorem of Finite Abelian Groups** — The finite case is a special case

# Source Reference

Chapter 13: The Structure of Groups, Section 13.1, p. 175. Theorem 13.10.

# Verification Notes

- Definition source: Theorem 13.10 (stated without proof; proof referenced to other texts)
- Confidence: HIGH — explicitly stated theorem
