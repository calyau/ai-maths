---
# === CORE IDENTIFICATION ===
concept: Quaternion Group
slug: quaternion-group

# === CLASSIFICATION ===
category: finite-group-classification
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Cauchy's Theorem"
chapter_number: 13
pdf_page: 75
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Q"
  - "$Q_8$"
  - "quaternion group Q"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - quaternion-algebra
  - dihedral-group
  - classification-groups-order-8
  - centre-of-a-group
contrasts_with:
  - dihedral-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the quaternion group?"
  - "How does Q differ from D4?"
---

# Quick Definition

The quaternion group $Q$ is a non-abelian group of order 8 consisting of the eight elements $\pm 1, \pm i, \pm j, \pm k$, where $i^2 = j^2 = k^2 = -1$ and $ij = k = -ji$.

# Core Definition

The eight symbols $\pm 1, \pm i, \pm j, \pm k$, when multiplied according to the rules $i^2 = j^2 = k^2 = -1$, $ij = -ji = k$, form a group $Q$ called the **quaternion group** (Armstrong, Ch. 13, p. 77).

# Prerequisites

- **Group** — $Q$ is verified as a group via its multiplication table

# Key Properties

1. $|Q| = 8$
2. $Q$ is non-abelian ($ij = k$ but $ji = -k$)
3. The only elements of order 2 are $\pm 1$ (specifically, $-1$ has order 2 and $1$ is the identity)
4. Every element other than $\pm 1$ has order 4
5. $Q$ is not isomorphic to $D_4$: $D_4$ has five elements of order 2, while $Q$ has only one ($-1$)
6. $Q$ is not isomorphic to any abelian group of order 8 (since it is non-abelian)
7. The centre of $Q$ is $\{\pm 1\}$ (Example (x) in Ch. 15)
8. Every proper subgroup of $Q$ is cyclic (Exercise 13.6)

# Construction / Recognition

## To Construct:
1. Start with elements $\pm 1, \pm i, \pm j, \pm k$
2. Define multiplication by the relations $i^2 = j^2 = k^2 = -1$ and $ij = k$
3. All other products follow from these relations and associativity

## To Recognize:
1. Check the group has order 8
2. Verify it is non-abelian
3. Count elements of order 2: if only one (besides identity), it is $Q$

# Context & Application

Armstrong introduces $Q$ as the fifth group of order 8, alongside $\mathbb{Z}_8$, $\mathbb{Z}_4 \times \mathbb{Z}_2$, $\mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_2$, and $D_4$. The quaternion group plays a distinguishing role in the classification (Theorem 13.3) and illustrates that non-abelian groups of order 8 need not be dihedral.

# Examples

**Example 1** (p. 77): The multiplication table of $Q$ is given. For instance, $i \cdot j = k$, $j \cdot i = -k$, $i^2 = -1$.

**Example 2** (Ch. 15, p. 91): The subgroup $\{\pm 1\}$ is normal in $Q$, and $Q/\{\pm 1\} \cong \mathbb{Z}_2 \times \mathbb{Z}_2$.

# Relationships

## Related
- **Quaternion algebra** — $Q$ is a subgroup of $\mathbb{H} - \{0\}$
- **Dihedral group** — $D_4$ is the other non-abelian group of order 8
- **Classification of groups of order 8** — $Q$ is one of five groups of order 8
- **Centre of a group** — $Z(Q) = \{\pm 1\}$

## Contrasts With
- **Dihedral group $D_4$** — Both non-abelian of order 8, but $D_4$ has five elements of order 2 while $Q$ has only one

# Common Errors

- **Error**: Thinking $i, j, k$ commute
  **Correction**: $ij = k$ but $ji = -k$; the group is non-abelian

# Common Confusions

- **Confusion**: Confusing $Q$ with $D_4$ since both are non-abelian of order 8
  **Clarification**: Count elements of order 2. $D_4$ has five ($s, rs, r^2 s, r^3 s, r^2$); $Q$ has only one ($-1$).

# Source Reference

Chapter 13: Cauchy's Theorem, pp. 77-78 (pdf). Multiplication table and comparison with $D_4$.

# Verification Notes

- Definition source: Direct from p. 77
- Multiplication rules: Explicitly given
- Confidence rationale: HIGH — explicit construction and multiplication table
- Uncertainties: None
