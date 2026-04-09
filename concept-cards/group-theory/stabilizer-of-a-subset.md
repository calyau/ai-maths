---
# === CORE IDENTIFICATION ===
concept: Stabilizer of a Subset
slug: stabilizer-of-a-subset

# === CLASSIFICATION ===
category: group-actions
subcategory: orbits-stabilizers
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Groups Acting on Sets"
chapter_number: 4
pdf_page: 59
section: "Stabilizers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - setwise stabilizer

# === TYPED RELATIONSHIPS ===
prerequisites:
  - stabilizer
extends:
  - stabilizer
related:
  - normalizer
  - block-system
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the stabilizer of a subset under a group action?"
---

# Quick Definition

The stabilizer of a subset $S \subset X$ is $\operatorname{Stab}(S) = \{g \in G \mid gS = S\}$, the subgroup of elements that map $S$ to itself as a set.

# Core Definition

"For a subset $S$ of $X$, we define the stabilizer of $S$ to be $\operatorname{Stab}(S) = \{g \in G \mid gS = S\}$" (Milne, p. 59). Note: $\operatorname{Stab}(gS) = g \cdot \operatorname{Stab}(S) \cdot g^{-1}$.

# Prerequisites

- **Stabilizer** — This extends the point-stabilizer concept to subsets

# Key Properties

1. $\operatorname{Stab}(S)$ is a subgroup of $G$
2. $\operatorname{Stab}(gS) = g \operatorname{Stab}(S) g^{-1}$ (conjugation formula)
3. $\operatorname{Stab}(x) \subset \operatorname{Stab}(S)$ for any $x \in S$ if $gx = x \implies gS = S$... but in general one needs $gS = S$, which is stronger than $gS \subset S$
4. It is possible for $gS \subset S$ but $g \notin \operatorname{Stab}(S)$ (see 1.33)

# Context & Application

Subset stabilizers appear in the theory of blocks (primitive actions) and when studying normalizers (which are stabilizers of subgroups under conjugation).

# Examples

**Example 1** (p. 59): The normalizer $N_G(H)$ is the stabilizer of $H$ under the conjugation action of $G$ on its subgroups.

# Relationships

## Builds Upon
- **stabilizer**

## Related
- **normalizer** — $N_G(H) = \operatorname{Stab}(H)$ under conjugation
- **block-system** — Blocks satisfy $\operatorname{Stab}(x) \subsetneq \operatorname{Stab}(A) \subsetneq G$

# Source Reference

Chapter 4: Groups Acting on Sets, "Stabilizers", page 59.

# Verification Notes

- Definition source: Direct from p. 59
- Confidence: HIGH — explicit definition
- Uncertainties: None
