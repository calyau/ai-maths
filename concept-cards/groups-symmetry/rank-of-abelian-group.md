---
# === CORE IDENTIFICATION ===
concept: Rank of an Abelian Group
slug: rank-of-abelian-group

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
  - "free rank"
  - "Betti number"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - classification-of-fg-abelian-groups
extends: []
related:
  - torsion-coefficients
  - free-abelian-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the rank of a finitely generated abelian group?"
---

# Quick Definition

The rank of a finitely generated abelian group $G \cong \mathbb{Z}_{m_1} \times \cdots \times \mathbb{Z}_{m_k} \times \mathbb{Z}^s$ is the integer $s$, the number of infinite cyclic factors.

# Core Definition

In the canonical decomposition $\mathbb{Z}_{m_1} \times \mathbb{Z}_{m_2} \times \cdots \times \mathbb{Z}_{m_k} \times \mathbb{Z}^s$, the number $s$ is the **rank** of the group (Armstrong, p. 126).

# Prerequisites

- **Classification of f.g. abelian groups** -- the rank is defined via the canonical decomposition

# Key Properties

1. The rank is a non-negative integer
2. The rank is 0 iff the group is finite
3. The rank equals the dimension of the real vector space spanned by images under any embedding into $\mathbb{R}^t$
4. The rank is unique: if $\mathbb{Z}^s \cong \mathbb{Z}^t$ then $s = t$ (Lemma 21.7)

# Construction / Recognition

## Proof that Rank Is Well-Defined (Lemma 21.7, p. 130):
1. Let $\varphi: \mathbb{Z}^s \to \mathbb{Z}^t$ be an isomorphism with $s \le t$
2. The image lies in the subspace spanned by $\varphi(x_1), \ldots, \varphi(x_s)$
3. This subspace must contain $\mathbb{Z}^t$, so must be all of $\mathbb{R}^t$
4. Therefore $s \ge t$, hence $s = t$

## Rank from Quotient (Theorem 21.4, p. 130):
The rank equals the rank of $G/H$ where $H$ is the torsion subgroup, since $G/H \cong \mathbb{Z}^s$.

# Context & Application

The rank measures the "free part" of a finitely generated abelian group. Together with the torsion coefficients, it completely determines the group. For finite groups, the rank is 0.

# Examples

$\mathbb{Z}_2 \times \mathbb{Z}$ has rank 1 and torsion coefficient 2.

$\mathbb{Z}^3$ has rank 3 and no torsion coefficients (free abelian group of rank 3).

# Relationships

## Builds Upon
- **Classification of f.g. abelian groups** -- the rank is one of the invariants

## Related
- **Torsion coefficients** -- the other invariants
- **Free abelian group** -- a group of rank $s$ with no torsion

# Source Reference

Chapter 21: Finitely Generated Abelian Groups, page 126. Uniqueness proof pp. 130--131.

# Verification Notes

- Definition: Direct from p. 126
- Uniqueness: Lemma 21.7, p. 130
- Confidence: HIGH -- explicitly defined
