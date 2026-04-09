---
# === CORE IDENTIFICATION ===
concept: Orbit-Stabilizer Theorem
slug: orbit-stabilizer-theorem

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
pdf_page: 60
section: "Transitive actions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - orbit-counting formula

# === TYPED RELATIONSHIPS ===
prerequisites:
  - orbit
  - stabilizer
  - lagrange-theorem
extends: []
related:
  - class-equation
  - transitive-action
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do orbits and stabilizers relate via the orbit-stabilizer theorem?"
---

# Quick Definition

The size of the orbit of $x_0$ equals the index of its stabilizer: $|Gx_0| = (G : \operatorname{Stab}(x_0))$.

# Core Definition

"Let $G$ act on $X$, and let $O = Gx_0$ be the orbit containing $x_0$. Then the cardinality of $O$ is $|O| = (G : \operatorname{Stab}(x_0))$" (Milne, Corollary 4.8, p. 60, equation (19)).

# Prerequisites

- **Orbit** — The set whose size is computed
- **Stabilizer** — The subgroup whose index gives the orbit size
- **Lagrange's theorem** — For finite groups, $(G : \operatorname{Stab}(x_0)) = |G|/|\operatorname{Stab}(x_0)|$

# Key Properties

1. $|Gx_0| = |G|/|\operatorname{Stab}(x_0)|$ for finite $G$
2. The bijection $g\operatorname{Stab}(x_0) \mapsto gx_0 : G/\operatorname{Stab}(x_0) \to Gx_0$ is an isomorphism of $G$-sets (Proposition 4.7)
3. Special case: the number of conjugates of $H \leq G$ is $(G : N_G(H))$ (p. 60)
4. Special case: the size of the conjugacy class of $x$ is $(G : C_G(x))$

# Construction / Recognition

## To use the orbit-stabilizer theorem:
1. Identify the action of $G$ on $X$
2. Choose a point $x_0 \in X$
3. Compute $\operatorname{Stab}(x_0)$
4. The orbit size is $(G : \operatorname{Stab}(x_0))$

# Context & Application

This is one of the most frequently used results in finite group theory. It reduces orbit-size calculations to subgroup-index calculations.

# Examples

**Example 1** (p. 60): The number of conjugates $gHg^{-1}$ of a subgroup $H$ is $(G : N_G(H))$.

**Example 2**: The conjugacy class of $x \in G$ has size $(G : C_G(x))$.

# Relationships

## Builds Upon
- **orbit**, **stabilizer**, **lagrange-theorem**

## Enables
- **class-equation** — Obtained by summing over orbits of conjugation
- **burnside-lemma** — Uses orbit sizes

# Source Reference

Chapter 4: Groups Acting on Sets, "Transitive actions", Corollary 4.8, page 60.

# Verification Notes

- Definition source: Corollary 4.8, equation (19), p. 60
- Confidence: HIGH — explicit theorem with proof
- Uncertainties: None
