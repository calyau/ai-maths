---
# === CORE IDENTIFICATION ===
concept: Conjugacy Classes of A4
slug: conjugacy-classes-of-a4

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - conjugacy-class
  - cycle-structure-conjugacy
  - alternating-group
extends: []
related:
  - normal-subgroup
  - subgroups-of-a4
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the conjugacy classes of A4?"
  - "How do conjugacy classes in A_n differ from those in S_n?"
---

# Quick Definition

$A_4$ has four conjugacy classes: $\{\varepsilon\}$, $\{(12)(34), (13)(24), (14)(23)\}$, $\{(123), (124), (134), (234)\}$, and $\{(132), (142), (143), (243)\}$.

# Core Definition

In $S_4$, conjugacy is determined by cycle structure. But in $A_4$, the conjugacy classes can split because the conjugating element $g$ may need to be odd. Armstrong shows (Ch. 14, Example (iv), p. 82) that the eight 3-cycles of $A_4$ split into two classes of four:

- If $g(123)g^{-1} = (132)$, then $g$ must be a transposition $(23)$, $(13)$, or $(12)$, all of which are odd permutations. So $(123)$ and $(132)$ are NOT conjugate in $A_4$.

# Prerequisites

- **Conjugacy class** — The concept being computed
- **Cycle structure and conjugacy in $S_n$** — In $S_n$, cycle structure determines conjugacy, but this may fail in subgroups
- **Alternating group** — $A_4$ is the group under study

# Key Properties

1. Four conjugacy classes of sizes 1, 3, 4, 4 (total: 12 = $|A_4|$)
2. The 3-cycles split into two classes (unlike in $S_4$)
3. The three double transpositions form a single class $\{(12)(34), (13)(24), (14)(23)\}$
4. This class, together with $\{\varepsilon\}$, forms a normal subgroup (the Klein four-group $V$)

# Construction / Recognition

## Key Subtlety:
1. In $S_n$, same cycle structure = conjugate
2. In $A_n$, same cycle structure does NOT guarantee conjugacy
3. Must check whether the conjugating element can be chosen to be even

# Context & Application

Armstrong gives a geometric interpretation via the regular tetrahedron. The four 3-cycles $(123)$, $(124)$, $(134)$, $(234)$ correspond to clockwise rotations about vertex axes, while $(132)$, $(142)$, $(143)$, $(243)$ are the anticlockwise rotations. These form distinct conjugacy classes because you cannot conjugate a clockwise rotation to an anticlockwise one using only even permutations.

The union $\{\varepsilon, (12)(34), (13)(24), (14)(23)\}$ is a key example of a normal subgroup of $A_4$ (used in Ch. 15, Example (ii)).

# Examples

**Example 1** (p. 82): The four conjugacy classes of $A_4$:
- $\{\varepsilon\}$ (size 1)
- $\{(12)(34), (13)(24), (14)(23)\}$ (size 3)
- $\{(123), (124), (134), (234)\}$ (size 4)
- $\{(132), (142), (143), (243)\}$ (size 4)

**Example 2** (p. 82): Geometric interpretation: the last two classes correspond to clockwise and anticlockwise rotations about vertex axes of a regular tetrahedron.

# Relationships

## Builds Upon
- **Cycle structure conjugacy** — Shows why cycle structure does not suffice in $A_n$

## Enables
- **Normal subgroup** — $V = \{\varepsilon, (12)(34), (13)(24), (14)(23)\}$ is normal in $A_4$
- **Quotient group** — $A_4 / V \cong \mathbb{Z}_3$ (Ch. 15, Example (ii))

# Common Errors

- **Error**: Assuming 3-cycles in $A_4$ form a single conjugacy class (as they do in $S_4$)
  **Correction**: In $A_4$, the eight 3-cycles split into two classes of four, because the conjugating element may be odd

# Common Confusions

- **Confusion**: Thinking conjugacy in a subgroup is the same as conjugacy in the ambient group
  **Clarification**: Conjugacy in $A_n$ is finer than in $S_n$. Elements conjugate in $S_n$ may fail to be conjugate in $A_n$.

# Source Reference

Chapter 14: Conjugacy, Example (iv), pp. 82-83 (pdf).

# Verification Notes

- Definition source: Direct from Example (iv), p. 82
- Geometric interpretation: From p. 83
- Confidence rationale: HIGH — explicit computation with explanation of splitting
- Uncertainties: None
