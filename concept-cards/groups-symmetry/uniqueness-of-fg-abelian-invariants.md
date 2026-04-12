---
# === CORE IDENTIFICATION ===
concept: Uniqueness of Invariants for F.G. Abelian Groups
slug: uniqueness-of-fg-abelian-invariants

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - classification-of-fg-abelian-groups
extends:
  - classification-of-fg-abelian-groups
related:
  - torsion-coefficients
  - rank-of-abelian-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Are the rank and torsion coefficients of a finitely generated abelian group unique?"
---

# Quick Definition

If two finitely generated abelian groups in canonical form are isomorphic, they have the same rank $s$ and the same torsion coefficients $m_1, \ldots, m_k$. The invariants are unique.

# Core Definition

**(21.4) Theorem.** Let $G_1 = \mathbb{Z}_{m_1} \times \cdots \times \mathbb{Z}_{m_k} \times \mathbb{Z}^s$ where $m_1 \mid \cdots \mid m_k$, and $G_2 = \mathbb{Z}_{n_1} \times \cdots \times \mathbb{Z}_{n_l} \times \mathbb{Z}^t$ where $n_1 \mid \cdots \mid n_l$. If $G_1$ and $G_2$ are isomorphic then $s = t$, $k = l$ and $m_i = n_i$ for $1 \le i \le k$ (Armstrong, p. 129).

# Prerequisites

- **Classification of f.g. abelian groups** -- the existence of the canonical form

# Key Properties

1. The torsion coefficients are determined by counting solutions to $x^q = e$ for various $q$ (Lemma 21.6)
2. The rank is determined by the quotient $G/H$ where $H$ is the torsion subgroup ($G/H \cong \mathbb{Z}^s$)
3. $\mathbb{Z}^s \cong \mathbb{Z}^t$ implies $s = t$ (Lemma 21.7)

# Construction / Recognition

## Proof Strategy for Torsion Coefficients (pp. 129--130):
1. For a cyclic group $\mathbb{Z}_m$, the number of solutions to $x^q = e$ is $\gcd(m, q)$ (Lemma 21.5)
2. For $\mathbb{Z}_{m_1} \times \cdots \times \mathbb{Z}_{m_k}$, it is $\gcd(m_1, q) \cdots \gcd(m_k, q)$ (Lemma 21.6)
3. Setting $q = m_1$: $m_1^k = \gcd(n_1, m_1) \cdots \gcd(n_l, m_1)$ forces $k = l$ and $m_1 \mid n_1$
4. Setting $q = n_1$ gives $n_1 \mid m_1$, hence $m_1 = n_1$
5. Continue inductively for $m_2, m_3, \ldots$

## Proof Strategy for Rank (p. 131):
1. The torsion subgroup $H_1$ of $G_1$ maps to the torsion subgroup $H_2$ of $G_2$ under any isomorphism
2. So $G_1/H_1 \cong G_2/H_2$, i.e., $\mathbb{Z}^s \cong \mathbb{Z}^t$
3. By Lemma 21.7, $s = t$

# Context & Application

The uniqueness theorem completes the classification. Without it, we would know that every f.g. abelian group has a canonical form, but not that the form is unique.

# Relationships

## Builds Upon
- **Classification of f.g. abelian groups** -- existence of canonical form

## Related
- **Torsion coefficients** -- the proof determines these by counting $q$th roots of identity
- **Rank** -- determined via the quotient by the torsion subgroup

# Source Reference

Chapter 21: Finitely Generated Abelian Groups, Theorem 21.4 and Lemmas 21.5--21.7, pages 129--131.

# Verification Notes

- Theorem, lemmas, and proofs: Direct from pp. 129--131
- Confidence: HIGH -- explicit theorem with complete proof
