---
# === CORE IDENTIFICATION ===
concept: Torsion Subgroup
slug: torsion-subgroup

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
section: "Theorem 21.4"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "elements of finite order"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - finitely-generated-abelian-group
extends: []
related:
  - torsion-coefficients
  - rank-of-abelian-group
  - free-abelian-group
  - uniqueness-of-fg-abelian-invariants
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the torsion subgroup of a finitely generated abelian group?"
---

# Quick Definition

The torsion subgroup of a finitely generated abelian group $G \cong \mathbb{Z}_{m_1} \times \cdots \times \mathbb{Z}_{m_k} \times \mathbb{Z}^s$ is $H = \mathbb{Z}_{m_1} \times \cdots \times \mathbb{Z}_{m_k}$, consisting of all elements of finite order. The quotient $G/H \cong \mathbb{Z}^s$ is free abelian.

# Core Definition

In the proof of Theorem 21.4, Armstrong identifies the torsion subgroup: the elements of finite order in $G_1 = \mathbb{Z}_{m_1} \times \cdots \times \mathbb{Z}_{m_k} \times \mathbb{Z}^s$ form the subgroup $H_1 = \mathbb{Z}_{m_1} \times \cdots \times \mathbb{Z}_{m_k} \times \{e\}$. An isomorphism between $G_1$ and $G_2$ sends elements of finite order to elements of finite order, so $H_1 \cong H_2$ (Armstrong, p. 130).

# Prerequisites

- **Finitely generated abelian group** -- the ambient group

# Key Properties

1. The torsion subgroup $H$ consists of all elements of finite order
2. $H \cong \mathbb{Z}_{m_1} \times \cdots \times \mathbb{Z}_{m_k}$
3. $G/H \cong \mathbb{Z}^s$ (free abelian of rank $s$)
4. An isomorphism $G_1 \to G_2$ restricts to an isomorphism $H_1 \to H_2$
5. The torsion subgroup is preserved by isomorphisms

# Context & Application

The torsion subgroup separates the "finite" and "free" parts of a finitely generated abelian group. The uniqueness proof for the rank (Theorem 21.4) uses the fact that $G/H \cong \mathbb{Z}^s$, so an isomorphism between groups induces an isomorphism between their quotients by torsion, proving $s = t$.

# Relationships

## Builds Upon
- **Finitely generated abelian group** -- the setting

## Enables
- **Uniqueness of f.g. abelian invariants** -- the torsion/free splitting is used in the proof

## Related
- **Torsion coefficients** -- determine the torsion subgroup
- **Rank** -- determined by the quotient $G/H$
- **Free abelian group** -- $G/H$ is free abelian

# Source Reference

Chapter 21: Finitely Generated Abelian Groups, Theorem 21.4 proof, page 130.

# Verification Notes

- Definition: From the proof of Theorem 21.4, p. 130
- Confidence: HIGH -- explicitly identified in the proof
