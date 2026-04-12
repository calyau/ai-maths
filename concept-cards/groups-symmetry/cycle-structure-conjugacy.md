---
# === CORE IDENTIFICATION ===
concept: Cycle Structure and Conjugacy in Symmetric Groups
slug: cycle-structure-conjugacy

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
  - "conjugacy in S_n"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - conjugacy-class
  - permutation
  - cycle-decomposition
extends: []
related:
  - symmetric-group
  - alternating-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When are two permutations conjugate in S_n?"
  - "How do conjugacy classes in S_n relate to cycle structure?"
---

# Quick Definition

Two elements of $S_n$ are conjugate if and only if they have the same cycle structure. The conjugacy classes of $S_n$ are therefore in bijection with the partitions of $n$.

# Core Definition

Two elements of $S_n$ are said to have the same **cycle structure** if, when decomposed as products of disjoint cyclic permutations, they have the same number of 2-cycles, the same number of 3-cycles, and so on (Armstrong, Ch. 14, Example (iii), p. 81).

Armstrong proves both directions:
1. Permutations with the same cycle structure are conjugate (by constructing the conjugating element $g$)
2. Conjugate permutations have the same cycle structure (since $g(a_1 a_2 \cdots a_k)g^{-1} = (g(a_1) g(a_2) \cdots g(a_k))$, a cycle of the same length)

# Prerequisites

- **Conjugacy class** — Cycle structure characterises conjugacy classes in $S_n$
- **Permutation** — Elements of $S_n$
- **Cycle decomposition** — Permutations decomposed as products of disjoint cycles

# Key Properties

1. Two permutations in $S_n$ are conjugate iff they have the same cycle structure
2. $g\theta g^{-1}$ replaces each entry $a$ in the cycle decomposition of $\theta$ by $g(a)$
3. Specifically: $g(a_1 a_2 \cdots a_k)g^{-1} = (g(a_1) g(a_2) \cdots g(a_k))$
4. The conjugating element $g$ is not unique
5. In $A_n$, conjugacy classes may split: permutations conjugate in $S_n$ need not be conjugate in $A_n$

# Construction / Recognition

## To Find g Such That $g\theta g^{-1} = \varphi$:
1. Write out the cycle decomposition of $\theta$ and $\varphi$, with cycles in decreasing length order
2. Include fixed points as 1-cycles
3. Write $\varphi$'s decomposition underneath $\theta$'s
4. Read off $g$: it sends each entry in $\theta$ to the entry below it in $\varphi$

# Context & Application

This result completely determines the conjugacy class structure of $S_n$: the number of conjugacy classes equals the number of partitions of $n$. Armstrong notes the subtlety that this characterisation may fail in subgroups of $S_n$, particularly $A_n$, where conjugacy classes can split.

# Examples

**Example 1** (p. 81): $\theta = (67)(2539)(14)$ and $\varphi = (12)(38)(5467)$ in $S_9$ have the same cycle structure (two transpositions and one 4-cycle). Lining up the cycles:
$(2539)(67)(14)(8)$
$(5467)(12)(38)(9)$
gives $g = (136)(254897)$.

**Example 2** (p. 82): In $A_4$, $(123)$ and $(132)$ have the same cycle structure but are NOT conjugate in $A_4$ (only in $S_4$), since any $g$ with $g(123)g^{-1} = (132)$ must be a transposition.

# Relationships

## Builds Upon
- **Conjugacy class** — This result characterises conjugacy classes in $S_n$

## Related
- **Symmetric group** — The result applies to $S_n$
- **Alternating group** — Conjugacy classes may split in $A_n$

# Common Errors

- **Error**: Assuming cycle structure determines conjugacy in $A_n$
  **Correction**: In $A_n$, permutations with the same cycle structure may lie in different conjugacy classes. The conjugating element $g$ constructed from $S_n$ may be odd.

# Common Confusions

- **Confusion**: Thinking the conjugating element $g$ is unique
  **Clarification**: Armstrong shows different cycle alignments give different $g$ values. The choice of $g$ is not canonical.

# Source Reference

Chapter 14: Conjugacy, Example (iii), pp. 81-83 (pdf).

# Verification Notes

- Definition source: Direct from Example (iii)
- Both directions proved explicitly
- Confidence rationale: HIGH — detailed proof with worked calculations
- Uncertainties: None
