---
# === CORE IDENTIFICATION ===
concept: Groups of Order 2p
slug: groups-of-order-2p

# === CLASSIFICATION ===
category: group-actions
subcategory: applications
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Groups Acting on Sets"
chapter_number: 4
pdf_page: 61
section: "The class equation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cauchy-theorem
  - semidirect-product
extends: []
related:
  - dihedral-group
  - cyclic-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are all groups of order 2p for an odd prime p?"
---

# Quick Definition

Every group of order $2p$ ($p$ an odd prime) is either cyclic ($C_{2p}$) or dihedral ($D_p$).

# Core Definition

"Every group of order $2p$, $p$ an odd prime, is cyclic or dihedral" (Milne, Corollary 4.15, p. 61).

# Prerequisites

- **Cauchy's theorem** — Gives elements of orders 2 and $p$
- **Semidirect product** — The non-cyclic case is $C_p \rtimes C_2$

# Key Properties

1. $G$ has elements $r$ of order $p$ and $s$ of order 2 (Cauchy)
2. $\langle r \rangle \trianglelefteq G$ (index 2, or because $2p \nmid 2!$)
3. If $srs^{-1} = r$ then $G \simeq C_{2p}$ (cyclic)
4. If $srs^{-1} = r^{-1}$ then $G \simeq D_p$ (dihedral)
5. These are the only cases since $i^2 \equiv 1 \pmod{p}$ has solutions $i = \pm 1$

# Examples

**Example 1**: Groups of order 6: $C_6$ and $S_3 \simeq D_3$.

**Example 2**: Groups of order 10: $C_{10}$ and $D_5$.

# Relationships

## Builds Upon
- **cauchy-theorem**, **semidirect-product**

## Related
- **dihedral-group** — The non-cyclic case
- **cyclic-group** — The abelian case

# Source Reference

Chapter 4: Groups Acting on Sets, Corollary 4.15, page 61.

# Verification Notes

- Definition source: Corollary 4.15, p. 61
- Confidence: HIGH — explicit theorem with proof
- Uncertainties: None
