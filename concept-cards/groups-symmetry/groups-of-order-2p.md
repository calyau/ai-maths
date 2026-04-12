---
# === CORE IDENTIFICATION ===
concept: Groups of Order 2p
slug: groups-of-order-2p

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cauchy-theorem
  - index-2-subgroups-are-normal
  - lagrange-theorem
extends:
  - classification-groups-order-6
related:
  - cyclic-group
  - dihedral-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What groups can have order 2p for an odd prime p?"
---

# Quick Definition

If $p$ is an odd prime, any group of order $2p$ is either cyclic ($\mathbb{Z}_{2p}$) or dihedral ($D_p$).

# Core Definition

**(15.5) Theorem.** If $p$ is an odd prime, any group of order $2p$ is either cyclic or dihedral (Armstrong, Ch. 15, p. 89).

**Proof sketch.** Use Cauchy's theorem to find $x$ of order $p$ and $y$ of order 2. The subgroup $\langle x \rangle$ has index 2 and is therefore normal. The six elements $e, x, \ldots, x^{p-1}, y, xy, \ldots, x^{p-1}y$ fill out $G$. The order of $xy$ is either $2p$ (giving cyclic), $2$ (giving $yx = x^{-1}y$, hence dihedral), or $p$ (shown to lead to a contradiction via a coset argument).

# Prerequisites

- **Cauchy's theorem** — Provides elements of orders 2 and $p$
- **Index-2 subgroups are normal** — $\langle x \rangle$ has index 2
- **Lagrange's theorem** — Constrains the order of $xy$

# Key Properties

1. Generalises the order-6 classification to all orders $2p$
2. The key step is showing $xy$ cannot have order $p$
3. The dihedral case arises from $yx = x^{-1}y$

# Construction / Recognition

## To Classify:
1. Find $x$ of order $p$, $y$ of order 2 (by Cauchy)
2. Check whether $xy = yx$
3. If yes: $G \cong \mathbb{Z}_{2p}$
4. If no: $G \cong D_p$

# Context & Application

Armstrong notes this was foreshadowed at the end of the order-6 classification (Theorem 13.2). The normal subgroup machinery of Chapter 15 allows a cleaner proof than was possible in Chapter 13.

# Examples

**Example 1**: Groups of order 6 ($p = 3$): $\mathbb{Z}_6$ or $D_3$.

**Example 2**: Groups of order 10 ($p = 5$): $\mathbb{Z}_{10}$ or $D_5$ (Exercise 13.4).

**Example 3**: Groups of order 14 ($p = 7$): $\mathbb{Z}_{14}$ or $D_7$.

# Relationships

## Builds Upon
- **Classification of groups of order 6** — The special case $p = 3$

## Related
- **Cyclic group** — One possibility
- **Dihedral group** — The other possibility

# Common Errors

- **Error**: Applying this to $p = 2$ (order 4)
  **Correction**: The theorem requires $p$ to be an odd prime. Groups of order 4 include $\mathbb{Z}_4$ and $\mathbb{Z}_2 \times \mathbb{Z}_2$, neither of which is dihedral (since $D_2 \cong \mathbb{Z}_2 \times \mathbb{Z}_2$).

# Common Confusions

- **Confusion**: Thinking this extends to orders $3p$, $4p$, etc.
  **Clarification**: The result is specific to $2p$. For $3p$ and beyond, additional group structures can appear.

# Source Reference

Chapter 15: Quotient Groups, Theorem (15.5), p. 89 (pdf).

# Verification Notes

- Definition source: Direct from Theorem (15.5)
- Confidence rationale: HIGH — explicit theorem with proof
- Uncertainties: None
