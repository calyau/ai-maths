---
# === CORE IDENTIFICATION ===
concept: Quaternion Algebra
slug: quaternion-algebra

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
  - "$\\mathbb{H}$"
  - "hypercomplex numbers"
  - "Hamilton's quaternions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - quaternion-group
  - special-unitary-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the quaternions?"
  - "What algebraic structure do quaternions form?"
---

# Quick Definition

A quaternion is an expression $a + bi + cj + dk$ where $a, b, c, d \in \mathbb{R}$ and $i, j, k$ satisfy $i^2 = j^2 = k^2 = -1$, $ij = k$. The set $\mathbb{H}$ of all quaternions forms a group under addition and $\mathbb{H} - \{0\}$ forms a (non-abelian) group under multiplication.

# Core Definition

A quaternion (or hypercomplex number) is an expression of the form $a + bi + cj + dk$, where $a, b, c, d$ are real numbers and $i, j, k$ satisfy $i^2 = j^2 = k^2 = -1$, $ij = -ji = k$. The set of all quaternions is denoted by $\mathbb{H}$ (Armstrong, Ch. 13, p. 77).

# Prerequisites

- **Group** — $\mathbb{H}$ and $\mathbb{H} - \{0\}$ are verified as groups

# Key Properties

1. $\mathbb{H}$ is an abelian group under addition (Exercise 13.7)
2. $\mathbb{H} - \{0\}$ is a non-abelian group under multiplication (Exercise 13.7)
3. The correspondence $a + bi + cj + dk \leftrightarrow (a, b, c, d)$ is an isomorphism from additive $\mathbb{H}$ to $\mathbb{R}^4$ (Exercise 13.7)
4. Quaternions of unit length form a subgroup $S^3$ (Exercise 13.8)
5. $S^3$ is isomorphic to $SU_2$ (Exercise 13.9)
6. The quaternion group $Q = \{\pm 1, \pm i, \pm j, \pm k\}$ is a finite subgroup of $S^3$

# Construction / Recognition

## To Construct:
1. Take four real numbers $a, b, c, d$
2. Form $q = a + bi + cj + dk$
3. Multiply using distributivity and the relations $i^2 = j^2 = k^2 = -1$, $ij = k$, $ji = -k$, etc.

# Context & Application

Armstrong introduces $\mathbb{H}$ as the ambient algebraic structure containing the quaternion group $Q$. The exercises develop the connection between quaternions and $SO_3$ via conjugation: conjugation by a non-zero quaternion sends pure quaternions to pure quaternions, inducing a rotation of $\mathbb{R}^3$ (Exercises 13.11, 13.12). This connection reappears in Chapter 16 as an example of a homomorphism.

# Examples

**Example 1** (p. 77): The multiplication rules: $ij = k$, $jk = i$, $ki = j$, and $ji = -k$, $kj = -i$, $ik = -j$.

**Example 2** (Exercise 13.8): The quaternions of unit length ($a^2 + b^2 + c^2 + d^2 = 1$) form $S^3$, the unit sphere in $\mathbb{R}^4$.

# Relationships

## Enables
- **Quaternion group** — $Q = \{\pm 1, \pm i, \pm j, \pm k\} \subset S^3 \subset \mathbb{H} - \{0\}$
- **Homomorphism $\mathbb{H} - \{0\} \to SO_3$** — Conjugation by quaternions gives rotations (Ch. 16)

## Related
- **$SU_2$** — Isomorphic to $S^3$ (Exercise 13.9)

# Common Errors

- **Error**: Assuming quaternion multiplication is commutative
  **Correction**: $ij = k$ but $ji = -k$; multiplication is non-commutative

# Common Confusions

- **Confusion**: Conflating the quaternion group $Q$ (8 elements) with the quaternion algebra $\mathbb{H}$ (uncountably many elements)
  **Clarification**: $Q$ is a finite subgroup of $\mathbb{H} - \{0\}$; $\mathbb{H}$ is the entire algebra of all quaternions

# Source Reference

Chapter 13: Cauchy's Theorem, p. 77 (pdf). Exercises 13.7-13.12.

# Verification Notes

- Definition source: Direct from p. 77
- Confidence rationale: HIGH — explicitly defined
- Uncertainties: Some properties are left as exercises
