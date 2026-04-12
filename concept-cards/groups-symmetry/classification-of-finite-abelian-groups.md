---
# === CORE IDENTIFICATION ===
concept: Classification of Finite Abelian Groups
slug: classification-of-finite-abelian-groups

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
section: "Corollary 21.2"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "fundamental theorem of finite abelian groups"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - classification-of-fg-abelian-groups
extends:
  - classification-of-fg-abelian-groups
related:
  - torsion-coefficients
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are finite abelian groups classified?"
---

# Quick Definition

Any finite abelian group is isomorphic to $\mathbb{Z}_{m_1} \times \mathbb{Z}_{m_2} \times \cdots \times \mathbb{Z}_{m_k}$ where $m_1 \mid m_2 \mid \cdots \mid m_k$. This is the special case of the f.g. abelian classification with rank $s = 0$.

# Core Definition

**(21.2) Corollary.** Any finite abelian group is isomorphic to a direct product of cyclic groups $\mathbb{Z}_{m_1} \times \mathbb{Z}_{m_2} \times \cdots \times \mathbb{Z}_{m_k}$ for which $m_1 \mid m_2 \mid \cdots \mid m_k$. Here the rank $s$ is zero (Armstrong, p. 126).

# Prerequisites

- **Classification of f.g. abelian groups** -- this is the finite case

# Key Properties

1. The group has order $m_1 m_2 \cdots m_k$
2. The largest order of any element is $m_k$ (the exponent)
3. The decomposition is unique (Theorem 21.4)

# Construction / Recognition

## To Classify a Finite Abelian Group of Order $n$:
1. Factor $n$ into prime powers
2. List all ways to write $n = m_1 m_2 \cdots m_k$ with $m_1 \mid m_2 \mid \cdots \mid m_k$ and each $m_i \ge 2$
3. Each such factorisation gives a distinct group

# Context & Application

This is the most commonly cited form of the classification theorem. It gives a complete enumeration of finite abelian groups of any given order.

# Examples

**Example (ii)** (p. 127): An abelian group of order 12 is $\mathbb{Z}_{12}$ (torsion coefficients: 12) or $\mathbb{Z}_2 \times \mathbb{Z}_6$ (torsion coefficients: 2, 6).

**Exercise 21.4** (p. 131): Classifying abelian groups of orders 81, 144, and 216.

# Relationships

## Builds Upon
- **Classification of f.g. abelian groups** -- the finite case

## Related
- **Torsion coefficients** -- the complete invariant for finite abelian groups

# Common Errors

- **Error**: Listing $\mathbb{Z}_4 \times \mathbb{Z}_6$ as a group of order 24 in canonical form.
  **Correction**: Since $4 \nmid 6$, this is not in canonical form. Rewrite: $\mathbb{Z}_4 \times \mathbb{Z}_6 \cong \mathbb{Z}_4 \times \mathbb{Z}_2 \times \mathbb{Z}_3 \cong \mathbb{Z}_2 \times \mathbb{Z}_{12}$.

# Source Reference

Chapter 21: Finitely Generated Abelian Groups, Corollary 21.2, page 126.

# Verification Notes

- Corollary: Direct from p. 126
- Confidence: HIGH -- explicit corollary of the main theorem
