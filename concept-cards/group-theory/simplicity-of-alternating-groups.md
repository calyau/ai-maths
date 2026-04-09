---
# === CORE IDENTIFICATION ===
concept: Simplicity of Alternating Groups
slug: simplicity-of-alternating-groups

# === CLASSIFICATION ===
category: group-actions
subcategory: permutation-groups
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Groups Acting on Sets"
chapter_number: 4
pdf_page: 68
section: "Permutation groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - alternating-group
  - simple-group
extends: []
related:
  - classification-of-finite-simple-groups
  - solvable-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "For which n is the alternating group A_n simple?"
---

# Quick Definition

The alternating group $A_n$ is simple for $n \geq 5$; this is the key fact behind the unsolvability of the general quintic by radicals.

# Core Definition

"The group $A_n$ is simple if $n \geq 5$" (Milne, Theorem 4.33, Galois, p. 68).

# Prerequisites

- **Alternating group** — The group whose simplicity is established
- **Simple group** — The property being proved

# Key Properties

1. $A_n$ is simple for $n \geq 5$ (Theorem 4.33)
2. Proof strategy: any nontrivial normal subgroup of $A_n$ contains a 3-cycle (Lemma 4.36), and any normal subgroup containing a 3-cycle contains all 3-cycles, hence equals $A_n$ (Lemma 4.35)
3. Corollary: for $n \geq 5$, the only normal subgroups of $S_n$ are $1$, $A_n$, and $S_n$ (Corollary 4.37)
4. $A_2 = 1$, $A_3 \simeq C_3$ (simple), $A_4$ is not simple (has normal subgroup $V$)

# Context & Application

The simplicity of $A_n$ ($n \geq 5$) implies $S_n$ and $A_n$ are not solvable, which by Galois theory means the general polynomial of degree $\geq 5$ cannot be solved by radicals.

# Examples

**Example 1** (p. 68): $A_4$ is not simple: the Klein four-group $V = \{1, (12)(34), (13)(24), (14)(23)\}$ is a normal (in fact characteristic) subgroup.

**Example 2** (p. 68): $A_5$ is simple and is the smallest noncommutative simple group (order 60).

# Relationships

## Builds Upon
- **alternating-group**, **simple-group**

## Related
- **classification-of-finite-simple-groups** — $A_n$ ($n \geq 5$) is one of the infinite families
- **solvable-group** — $A_n$, $S_n$ not solvable for $n \geq 5$

# Source Reference

Chapter 4: Groups Acting on Sets, "Permutation groups", Theorem 4.33, pages 68-69.

# Verification Notes

- Definition source: Theorem 4.33 (attributed to Galois), p. 68
- Confidence: HIGH — explicit theorem with full proof
- Uncertainties: None
