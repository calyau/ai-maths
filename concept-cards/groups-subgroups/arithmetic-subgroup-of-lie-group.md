---
# === CORE IDENTIFICATION ===
concept: Arithmetic Subgroup of a Lie Group
slug: arithmetic-subgroup-of-lie-group

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
pdf_page: 410
section: "The theorem of Margulis"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - arithmetic-subgroup
  - lie-group
extends:
  - arithmetic-subgroup
related:
  - margulis-arithmeticity-theorem
  - lattice-in-lie-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an arithmetic subgroup?"
  - "How do arithmetic subgroups relate to discrete subgroups of Lie groups?"
---

# Quick Definition

An arithmetic subgroup of a semisimple real Lie group $H$ is a subgroup $\Gamma$ obtained (up to commensurability) as the image of an arithmetic subgroup of an algebraic group $G$ over $\mathbb{Q}$ under a surjection $G_{\mathbb{R}} \to H$ with compact kernel.

# Core Definition

"Let $H$ be a semisimple algebraic group over $\mathbb{R}$. A subgroup $\Gamma$ of $H(\mathbb{R})$ is *arithmetic* if there exists an algebraic group $G$ over $\mathbb{Q}$, a surjective map $\varphi: G_{\mathbb{R}} \to H$ such that the kernel of $\varphi(\mathbb{R}): G(\mathbb{R}) \to H(\mathbb{R})$ is compact, and an arithmetic subgroup $\Gamma'$ of $G(\mathbb{R})$ such that $\varphi(\Gamma')$ is commensurable with $\Gamma$." (Definition 15.1, Milne, p. 410)

# Prerequisites

- **Arithmetic subgroup** — the algebraic notion for groups over $\mathbb{Q}$
- **Lie group** — the ambient group for the more general definition

# Key Properties

1. This definition extends the notion of arithmetic subgroup from algebraic groups over $\mathbb{Q}$ to real Lie groups
2. The compact kernel condition ensures that the image of an arithmetic subgroup remains "large"
3. The definition is up to commensurability
4. For $H = G(\mathbb{R})^+$ with $G$ a semisimple group over $\mathbb{Q}$, this recovers the standard notion

# Construction / Recognition

## To Construct:
1. Start with a semisimple algebraic group $G$ over $\mathbb{Q}$
2. Find a surjection $\varphi: G_{\mathbb{R}} \to H$ with compact kernel
3. Take an arithmetic subgroup $\Gamma'$ of $G(\mathbb{Q})$
4. The image $\varphi(\Gamma')$ (or any group commensurable with it) is arithmetic in $H(\mathbb{R})$

# Context & Application

This more general definition is needed for Margulis's arithmeticity theorem, which characterizes all lattices in semisimple Lie groups. The compact kernel condition allows, for example, $G(\mathbb{R})$ to have compact factors that are "divided out" in the map to $H$.

# Examples

**Example 1** (p. 410): Let $B$ be a quaternion algebra over a totally real field $F$ with $B \otimes_{\mathbb{Q}} \mathbb{R} \simeq M_2(\mathbb{R}) \times \mathbb{H}^{d-1}$. The norm-1 group $G$ has $G(\mathbb{R}) \simeq \mathrm{SL}_2(\mathbb{R}) \times (\mathbb{H}^1)^{d-1}$. Projecting to $H = \mathrm{SL}_2(\mathbb{R})$ (kernel is $(\mathbb{H}^1)^{d-1}$, compact) gives arithmetic subgroups of $\mathrm{SL}_2(\mathbb{R})$.

**Example 2** (p. 410): All commensurability classes of arithmetic subgroups of $\mathrm{SL}_2(\mathbb{R})$ arise from quaternion algebras over totally real fields.

# Relationships

## Builds Upon
- **Arithmetic subgroup** — the more restrictive notion for groups over $\mathbb{Q}$

## Enables
- **Margulis arithmeticity theorem** — uses this definition in its statement

## Related
- **Lattice in Lie group** — arithmetic subgroups of Lie groups are lattices

# Common Errors

- **Error**: Defining arithmetic subgroups of Lie groups as simply $G(\mathbb{Z})$ for some embedding
  **Correction**: The definition requires a $\mathbb{Q}$-algebraic group $G$, a surjection with compact kernel, and commensurability

# Common Confusions

- **Confusion**: Thinking every arithmetic subgroup of a Lie group $H$ comes from an algebraic group structure on $H$ itself
  **Clarification**: The algebraic group $G$ may be larger than $H$ (e.g., $G(\mathbb{R})$ may have compact factors)

# Source Reference

Chapter VII: Arithmetic Subgroups, Section 15, Definition 15.1, page 410.

# Verification Notes

- Definition source: Direct quote from Definition 15.1
- Confidence: HIGH — explicit definition
- Uncertainties: None
- Cross-reference status: Verified
