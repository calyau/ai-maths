---
# === CORE IDENTIFICATION ===
concept: Discrete Subgroup of a Lie Group
slug: discrete-subgroup-of-lie-group

# === CLASSIFICATION ===
category: arithmetic-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Arithmetic Subgroups"
chapter_number: 7
pdf_page: 402
section: "Applications to manifolds"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
extends: []
related:
  - arithmetic-subgroup
  - lattice-in-lie-group
  - torsion-free-arithmetic-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do arithmetic subgroups relate to discrete subgroups of Lie groups?"
---

# Quick Definition

A discrete subgroup of a Lie group $G$ is a subgroup $\Gamma$ such that every point of $\Gamma$ has an open neighbourhood containing no other point of $\Gamma$. Arithmetic subgroups of $G(\mathbb{Q})$ are always discrete in $G(\mathbb{R})$.

# Core Definition

A subgroup $\Gamma$ of a locally compact group $G$ is discrete if every point of $\Gamma$ is isolated in the subspace topology. For algebraic groups: "$\mathrm{GL}_n(\mathbb{Z})$ is discrete in $\mathrm{GL}_n(\mathbb{R})$, and it follows that every arithmetic subgroup $\Gamma$ of a group $G$ is discrete in $G(\mathbb{R})$." (Milne, p. 402)

# Prerequisites

- **Lie group** — discrete subgroups are subgroups of Lie groups

# Key Properties

1. Every arithmetic subgroup of $G(\mathbb{Q})$ is discrete in $G(\mathbb{R})$
2. If $\Gamma$ is discrete and torsion-free, then $\Gamma$ acts freely on $G(\mathbb{R})/K$ for any compact $K$
3. The quotient $\Gamma \backslash G(\mathbb{R})/K$ is a smooth manifold when $\Gamma$ is discrete and torsion-free (Theorem 7.1)
4. Discreteness is preserved by passing to commensurable subgroups (Exercise 11-1)

# Construction / Recognition

## To Construct:
1. Start with an algebraic group $G$ over $\mathbb{Q}$
2. Take an arithmetic subgroup $\Gamma$ of $G(\mathbb{Q})$
3. $\Gamma$ is automatically discrete in $G(\mathbb{R})$

## To Recognize:
1. Check that $\Gamma \cap U$ is finite for every compact subset $U$ of $G$

# Context & Application

Discrete subgroups are the bridge between algebraic groups and differential geometry. A discrete torsion-free subgroup $\Gamma$ of $G(\mathbb{R})$ produces a locally symmetric manifold $\Gamma \backslash G(\mathbb{R})/K$. This construction is fundamental to the theory of Shimura varieties and to the study of moduli spaces.

# Examples

**Example 1** (p. 402): $\mathbb{Z}^{n^2}$ is discrete in $\mathbb{R}^{n^2}$, hence $\mathrm{GL}_n(\mathbb{Z})$ is discrete in $\mathrm{GL}_n(\mathbb{R})$.

**Example 2** (p. 402): For any algebraic group $G$ over $\mathbb{Q}$ and compact subgroup $K$ of $G(\mathbb{R})$, a discrete torsion-free $\Gamma \subset G(\mathbb{R})$ yields a smooth manifold $\Gamma \backslash G(\mathbb{R})/K$ (Theorem 7.1).

# Relationships

## Enables
- **Lattice in Lie group** — discrete subgroups of finite covolume are lattices
- **Connected Shimura variety** — constructed from discrete subgroups acting on symmetric spaces

## Related
- **Arithmetic subgroup** — arithmetic subgroups are discrete in $G(\mathbb{R})$
- **Torsion-free arithmetic group** — needed for free actions on symmetric spaces

# Common Errors

- **Error**: Assuming all discrete subgroups are arithmetic
  **Correction**: Non-arithmetic lattices exist in $\mathrm{SL}_2(\mathbb{R})$ (from Riemann surfaces of genus $\geq 2$)

# Common Confusions

- **Confusion**: Thinking discrete implies finite
  **Clarification**: Discrete subgroups can be infinite (e.g., $\mathbb{Z} \subset \mathbb{R}$); discrete only means isolated points

# Source Reference

Chapter VII: Arithmetic Subgroups, Section 7, page 402. Theorem 7.1.

# Verification Notes

- Definition source: Synthesized from p. 402
- Confidence: HIGH — standard definition, clearly stated in context
- Uncertainties: None
- Cross-reference status: Verified
