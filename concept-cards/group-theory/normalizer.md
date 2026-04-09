---
# === CORE IDENTIFICATION ===
concept: Normalizer
slug: normalizer

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
  - "N_G(H)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - stabilizer
  - group-action
extends:
  - stabilizer
related:
  - centralizer
  - normal-subgroup
contrasts_with:
  - centralizer

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the normalizer of a subgroup?"
---

# Quick Definition

The normalizer $N_G(H)$ of a subgroup $H$ is $\{g \in G \mid gHg^{-1} = H\}$, the largest subgroup of $G$ in which $H$ is normal.

# Core Definition

"Let $G$ act on $G$ by conjugation, and let $H$ be a subgroup of $G$. The stabilizer of $H$ is called the normalizer $N_G(H)$ of $H$ in $G$: $N_G(H) = \{g \in G \mid gHg^{-1} = H\}$. Clearly $N_G(H)$ is the largest subgroup of $G$ containing $H$ as a normal subgroup" (Milne, Example 4.6, p. 59).

# Prerequisites

- **Stabilizer** — The normalizer is the stabilizer of $H$ under conjugation on subsets
- **Group action** — Conjugation action on subgroups/subsets

# Key Properties

1. $H \trianglelefteq N_G(H)$
2. $N_G(H)$ is the largest subgroup of $G$ containing $H$ as a normal subgroup
3. $H \trianglelefteq G$ iff $N_G(H) = G$
4. Number of conjugates of $H$ is $(G : N_G(H))$ (orbit-stabilizer)

# Context & Application

The normalizer tells you "how normal" a subgroup is. It is essential in Sylow theory and in counting arguments involving conjugate subgroups.

# Examples

**Example 1** (p. 60): The number of conjugates $gHg^{-1}$ of $H$ is $(G : N_G(H))$.

# Relationships

## Builds Upon
- **stabilizer** — Normalizer is stabilizer of a subgroup under conjugation

## Related
- **normal-subgroup** — $H \trianglelefteq G$ iff $N_G(H) = G$
- **centralizer** — $C_G(H) \leq N_G(H)$

## Contrasts With
- **centralizer** — Centralizer requires commuting; normalizer requires stabilizing the subgroup as a set

# Source Reference

Chapter 4: Groups Acting on Sets, "Stabilizers", Example 4.6, page 59.

# Verification Notes

- Definition source: Direct from Example 4.6, p. 59
- Confidence: HIGH — explicit definition
- Uncertainties: None
