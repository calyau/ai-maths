---
# === CORE IDENTIFICATION ===
concept: Conjugation by g
slug: conjugation-by-g

# === CLASSIFICATION ===
category: conjugacy
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Conjugacy"
chapter_number: 14
pdf_page: 80
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "inner automorphism"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - isomorphism
extends: []
related:
  - conjugacy-class
  - conjugacy-equivalence-relation
  - normal-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is conjugation by an element g?"
  - "Why is conjugation an isomorphism?"
---

# Quick Definition

Conjugation by $g$ is the function $x \mapsto gxg^{-1}$ from $G$ to $G$. It is an isomorphism (automorphism) of $G$ that preserves element orders and group structure.

# Core Definition

For a fixed element $g \in G$, the function from $G$ to $G$ given by $x \to gxg^{-1}$ is an isomorphism called **conjugation by $g$** (Armstrong, Ch. 14, p. 80).

It is a bijection because it is invertible (its inverse is conjugation by $g^{-1}$), and it preserves the algebraic structure because $g(xy)g^{-1} = (gxg^{-1})(gyg^{-1})$.

# Prerequisites

- **Group** — Conjugation uses the group operation and inverses
- **Isomorphism** — Conjugation is shown to be an isomorphism

# Key Properties

1. Conjugation by $g$ is a bijection $G \to G$
2. Its inverse is conjugation by $g^{-1}$
3. It preserves products: $g(xy)g^{-1} = (gxg^{-1})(gyg^{-1})$
4. It preserves element orders: if $x$ has order $n$, so does $gxg^{-1}$
5. Conjugation by the identity is the identity map
6. Composing conjugation by $g$ and by $h$ gives conjugation by $hg$

# Construction / Recognition

## To Apply:
1. Fix $g \in G$
2. For each $x \in G$, compute $gxg^{-1}$
3. The map $x \mapsto gxg^{-1}$ is an automorphism of $G$

# Context & Application

Armstrong uses conjugation to study the internal structure of groups. The conjugation map is the key tool for computing conjugacy classes in $D_6$, $S_n$, $A_4$, and $O_2$. The preservation of algebraic structure ensures that conjugate elements share all group-theoretic properties.

# Examples

**Example 1** (p. 80): In $D_6$, conjugation by $s$ sends $r^a$ to $sr^a s = r^{6-a}$, showing that $r^a$ and $r^{6-a}$ are conjugate.

**Example 2** (p. 82): In $O_2$, conjugation by $A_\theta$ fixes rotations ($A_\theta A_\varphi A_\theta^{-1} = A_\varphi$) and conjugation by $B_\varphi$ sends $A_\theta$ to $A_{-\theta}$.

# Relationships

## Enables
- **Conjugacy class** — The image of $x$ under all conjugations forms its conjugacy class
- **Normal subgroup** — A subgroup closed under all conjugations is normal

## Related
- **Automorphism** — Conjugation by $g$ is an inner automorphism

# Common Errors

- **Error**: Thinking conjugation by $g$ and by $g^{-1}$ are the same map
  **Correction**: $gxg^{-1} \neq g^{-1}xg$ in general. They are inverse maps, not the same map.

# Common Confusions

- **Confusion**: Thinking conjugation changes the group
  **Clarification**: Conjugation is a self-map of $G$. It permutes the elements of $G$ but doesn't change $G$ itself. It is an automorphism (an isomorphism from $G$ to $G$).

# Source Reference

Chapter 14: Conjugacy, p. 80 (pdf).

# Verification Notes

- Definition source: Direct from p. 80
- Confidence rationale: HIGH — explicitly defined and used extensively
- Uncertainties: None
