---
# === CORE IDENTIFICATION ===
concept: Commensurable Subgroups
slug: commensurable-subgroups

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
pdf_page: 397
section: "Commensurable groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - commensurable groups

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subgroup
extends: []
related:
  - arithmetic-subgroup
  - lattice-in-lie-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding arithmetic subgroups?"
---

# Quick Definition

Two subgroups $H_1$ and $H_2$ of a group are commensurable if their intersection $H_1 \cap H_2$ has finite index in both $H_1$ and $H_2$. Commensurability is an equivalence relation.

# Core Definition

"Subgroups $H_1$ and $H_2$ of a group are said to be *commensurable* if $H_1 \cap H_2$ is of finite index in both $H_1$ and $H_2$." (Milne, p. 397)

# Prerequisites

- **Subgroup** — commensurability is a relation between subgroups

# Key Properties

1. Commensurability is an equivalence relation (reflexive, symmetric, and transitive)
2. Transitivity: if $H_1, H_2$ and $H_2, H_3$ are commensurable, then $H_1 \cap H_2 \cap H_3$ has finite index in all three
3. If $\Gamma$ is discrete (resp. cocompact, resp. of finite covolume), then so is every subgroup commensurable with $\Gamma$ (Exercise 11-1)
4. Properties like discreteness, cocompactness, and finite covolume are invariants of commensurability classes

# Construction / Recognition

## To Check Commensurability:
1. Compute the intersection $H_1 \cap H_2$
2. Verify that $(H_1 : H_1 \cap H_2) < \infty$
3. Verify that $(H_2 : H_1 \cap H_2) < \infty$

# Context & Application

Commensurability is the fundamental equivalence relation in the theory of arithmetic subgroups. An arithmetic subgroup of $G(\mathbb{Q})$ is defined as any subgroup commensurable with $G(\mathbb{Q})_L$ for some lattice $L$, so the definition is intrinsically about commensurability classes. Similarly, lattices in Lie groups are studied up to commensurability.

# Examples

**Example 1** (p. 397): The subgroups $a\mathbb{Z}$ and $b\mathbb{Z}$ of $\mathbb{R}$ are commensurable if and only if $a/b \in \mathbb{Q}$. For instance, $6\mathbb{Z}$ and $4\mathbb{Z}$ are commensurable (they intersect in $12\mathbb{Z}$).

**Example 2** (p. 397): $\mathbb{Z}$ and $\sqrt{2}\mathbb{Z}$ are *not* commensurable because $\mathbb{Z} \cap \sqrt{2}\mathbb{Z} = \{0\}$, which has infinite index in both.

**Example 3** (p. 397): Lattices $L$ and $L'$ in a real vector space $V$ are commensurable if and only if they generate the same $\mathbb{Q}$-subspace of $V$.

# Relationships

## Enables
- **Arithmetic subgroup** — defined via commensurability with $G(\mathbb{Q})_L$
- **Lattice in Lie group** — lattice properties are commensurability invariants

# Common Errors

- **Error**: Checking only that $H_1 \cap H_2$ has finite index in $H_1$ and concluding commensurability
  **Correction**: Must check finite index in *both* $H_1$ and $H_2$

# Common Confusions

- **Confusion**: Thinking commensurable subgroups must be conjugate
  **Clarification**: Commensurability is weaker than conjugacy; commensurable subgroups need not be conjugate

# Source Reference

Chapter VII: Arithmetic Subgroups, Section 1, page 397.

# Verification Notes

- Definition source: Direct quote from p. 397
- Confidence: HIGH — explicit definition with examples
- Uncertainties: None
- Cross-reference status: Verified
