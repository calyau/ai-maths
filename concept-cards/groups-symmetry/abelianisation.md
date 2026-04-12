---
# === CORE IDENTIFICATION ===
concept: Abelianisation
slug: abelianisation

# === CLASSIFICATION ===
category: normal-subgroups-quotients
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Quotient Groups"
chapter_number: 15
pdf_page: 86
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "abelianization"
  - "$G/[G,G]$"
  - "abelian quotient"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - commutator-subgroup
  - quotient-group
extends: []
related:
  - abelian-group
  - homomorphism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does it mean to abelianise a group?"
  - "What is the largest abelian quotient of a group?"
---

# Quick Definition

The abelianisation of a group $G$ is the quotient group $G/[G,G]$, which is the largest abelian group that $G$ maps onto. In forming $G/[G,G]$ we "force" all elements to commute.

# Core Definition

In forming $G/[G,G]$ we say that we **abelianise** $G$ (Armstrong, Ch. 15, p. 91). By Theorem (15.6), $G/[G,G]$ is abelian, and any normal subgroup $H$ for which $G/H$ is abelian must contain $[G,G]$. So $[G,G]$ is the smallest normal subgroup with abelian quotient, and $G/[G,G]$ is the largest abelian quotient.

# Prerequisites

- **Commutator subgroup** — $[G,G]$ is the subgroup being divided out
- **Quotient group** — The abelianisation is a quotient group

# Key Properties

1. $G/[G,G]$ is always abelian
2. It is the "largest" abelian quotient: any abelian quotient of $G$ is a quotient of $G/[G,G]$
3. $G/[G,G] \cong G$ iff $G$ is already abelian
4. $G/[G,G]$ is trivial iff $G$ is perfect ($[G,G] = G$)

# Construction / Recognition

## To Compute:
1. Find the commutator subgroup $[G,G]$
2. Form the quotient $G/[G,G]$
3. The result is the abelianisation

# Context & Application

Abelianisation is a fundamental construction that strips away the non-abelian structure of $G$. Armstrong computes it for several groups, showing how the quotient captures the "abelian part" of the group.

# Examples

**Example 1** (p. 90): $S_n/[S_n, S_n] = S_n/A_n \cong \mathbb{Z}_2$ for $n \ge 3$.

**Example 2** (p. 91): For odd $n$: $D_n/[D_n, D_n] = D_n/\langle r \rangle \cong \mathbb{Z}_2$. For even $n$: $D_n/[D_n, D_n] = D_n/\langle r^2 \rangle \cong \mathbb{Z}_2 \times \mathbb{Z}_2$.

**Example 3** (p. 91): $Q/[Q, Q] = Q/\{\pm 1\} \cong \mathbb{Z}_2 \times \mathbb{Z}_2$.

# Relationships

## Builds Upon
- **Commutator subgroup** — Divided out to form the abelianisation
- **Quotient group** — The abelianisation is a quotient

## Related
- **Abelian group** — The abelianisation is always abelian
- **Homomorphism** — The natural map $G \to G/[G,G]$ is a homomorphism

# Common Errors

- **Error**: Thinking abelianisation preserves the order of $G$
  **Correction**: $|G/[G,G]| = |G|/|[G,G]|$, which is generally much smaller than $|G|$

# Common Confusions

- **Confusion**: Thinking the abelianisation of a non-abelian group is trivial
  **Clarification**: The abelianisation is trivial only when $[G,G] = G$. For most groups, the abelianisation is a non-trivial abelian group.

# Source Reference

Chapter 15: Quotient Groups, p. 91 (pdf).

# Verification Notes

- Definition source: Direct from p. 91
- Confidence rationale: HIGH — explicitly named
- Uncertainties: None
