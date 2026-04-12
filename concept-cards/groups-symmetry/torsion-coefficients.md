---
# === CORE IDENTIFICATION ===
concept: Torsion Coefficients
slug: torsion-coefficients

# === CLASSIFICATION ===
category: abelian-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Finitely Generated Abelian Groups"
chapter_number: 21
pdf_page: 126
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "invariant factors"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - classification-of-fg-abelian-groups
extends: []
related:
  - rank-of-abelian-group
  - smith-normal-form
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the torsion coefficients of a finitely generated abelian group?"
  - "How do torsion coefficients determine the finite part of a f.g. abelian group?"
---

# Quick Definition

The torsion coefficients of a finitely generated abelian group $G \cong \mathbb{Z}_{m_1} \times \cdots \times \mathbb{Z}_{m_k} \times \mathbb{Z}^s$ are the integers $m_1, \ldots, m_k$ satisfying $m_1 \mid m_2 \mid \cdots \mid m_k$. They determine the finite (torsion) part of $G$ uniquely.

# Core Definition

In the canonical decomposition $\mathbb{Z}_{m_1} \times \mathbb{Z}_{m_2} \times \cdots \times \mathbb{Z}_{m_k} \times \mathbb{Z}^s$, the numbers $m_1, \ldots, m_k$ are the **torsion coefficients** (Armstrong, p. 126).

# Prerequisites

- **Classification of f.g. abelian groups** -- torsion coefficients are defined via the canonical decomposition

# Key Properties

1. $m_1 \mid m_2 \mid \cdots \mid m_k$ (divisibility chain)
2. Each $m_i \ge 2$
3. The torsion coefficients are unique (Theorem 21.4)
4. The product $m_1 m_2 \cdots m_k$ equals the order of the torsion subgroup
5. $m_k$ is the exponent of the torsion subgroup (the largest order of any torsion element)

# Construction / Recognition

## To Find Torsion Coefficients:
1. Express the group in canonical form $\mathbb{Z}_{m_1} \times \cdots \times \mathbb{Z}_{m_k} \times \mathbb{Z}^s$
2. Ensure $m_1 \mid m_2 \mid \cdots \mid m_k$
3. The $m_i$ are the torsion coefficients

## From Non-Canonical Form:
Use row and column operations on the relation matrix to find Smith normal form (Chapter 22).

# Context & Application

Torsion coefficients, together with the rank, completely determine a finitely generated abelian group up to isomorphism.

# Examples

**Example (i)** (p. 127): $\mathbb{Z}_6 \times \mathbb{Z}_{10} \cong \mathbb{Z}_2 \times \mathbb{Z}_{30}$, so the torsion coefficients are 2, 30 (not 6, 10).

**Exercise 21.1** (p. 131): Find torsion coefficients of:
(a) $\mathbb{Z}_{10} \times \mathbb{Z}_{15} \times \mathbb{Z}_{20}$
(b) $\mathbb{Z}_{28} \times \mathbb{Z}_{42}$
(c) $\mathbb{Z}_9 \times \mathbb{Z}_{14} \times \mathbb{Z}_6 \times \mathbb{Z}_{16}$

# Relationships

## Builds Upon
- **Classification of f.g. abelian groups** -- defines the context

## Related
- **Rank** -- the other invariant in the classification
- **Smith normal form** -- the computational tool for finding torsion coefficients

# Common Errors

- **Error**: Reading off torsion coefficients from a non-canonical decomposition.
  **Correction**: Must first convert to canonical form with the divisibility chain $m_1 \mid m_2 \mid \cdots \mid m_k$. For example, $\mathbb{Z}_6 \times \mathbb{Z}_{10}$ has torsion coefficients 2, 30 -- not 6, 10.

# Common Confusions

- **Confusion**: Confusing torsion coefficients with elementary divisors (prime-power decomposition).
  **Clarification**: Torsion coefficients satisfy a divisibility chain. Elementary divisors are prime powers. Both determine the group, but Armstrong uses the torsion coefficient form.

# Source Reference

Chapter 21: Finitely Generated Abelian Groups, page 126. Definition following Theorem 21.1.

# Verification Notes

- Definition: Direct from p. 126
- Confidence: HIGH -- explicitly named and defined
