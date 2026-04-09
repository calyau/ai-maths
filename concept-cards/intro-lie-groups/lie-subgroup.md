---
# === CORE IDENTIFICATION ===
concept: Lie Subgroup
slug: lie-subgroup

# === CLASSIFICATION ===
category: lie-groups
subcategory: subgroups
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups: Basic Definitions"
chapter_number: 2
pdf_page: 9
section: "2.1"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "embedded Lie subgroup"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
extends: []
related:
  - immersed-subgroup
  - lie-subalgebra
  - coset-space
contrasts_with:
  - immersed-subgroup

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Lie group?"
  - "How do the classical groups relate to each other?"
---

# Quick Definition

A Lie subgroup $H$ of a Lie group $G$ is a subgroup that is also an embedded submanifold. Equivalently, it is a closed subgroup of $G$.

# Core Definition

**Definition 2.6** (Kirillov): A Lie subgroup $H$ of a Lie group $G$ is a subgroup which is also a submanifold.

**Theorem 2.8**: (1) Any Lie subgroup is closed in $G$. (2) Any closed subgroup of a Lie group is a Lie subgroup.

# Prerequisites

- **Lie group** — the ambient group

# Key Properties

1. "Submanifold" means embedded submanifold (Remark 2.7); $H$ is locally closed.
2. Lie subgroups are automatically closed (Theorem 2.8 part 1).
3. Conversely, any closed subgroup is a Lie subgroup (Theorem 2.8 part 2).
4. The Lie algebra of $H$ is a Lie subalgebra of $\mathfrak{g}$: $\mathfrak{h} = T_1 H \subset \mathfrak{g}$ (Theorem 3.19).

# Construction / Recognition

## To Construct/Create:
1. Take a closed subgroup $H \subset G$.
2. By Theorem 2.8, it automatically has Lie subgroup structure.

## To Identify/Recognize:
1. Check that $H$ is a subgroup of $G$.
2. Check that $H$ is closed in $G$ (sufficient by Theorem 2.8).

# Context & Application

Lie subgroups are the natural notion of "sub-object" in the category of Lie groups. Most classical groups are defined as Lie subgroups of $\mathrm{GL}(n, \mathbb{K})$.

# Examples

**Example** (p. 14-16): All classical groups $\mathrm{SL}(n, \mathbb{K})$, $\mathrm{O}(n, \mathbb{K})$, $\mathrm{SO}(n, \mathbb{K})$, $\mathrm{U}(n)$, $\mathrm{SU}(n)$, $\mathrm{Sp}(2n, \mathbb{K})$ are Lie subgroups of $\mathrm{GL}(n, \mathbb{K})$.

**Example** (p. 12): The stabilizer $\mathrm{Stab}_G(m)$ of a point under a group action is a Lie subgroup (Theorem 3.26).

# Relationships

## Builds Upon
- **Lie group** — the ambient group

## Enables
- **Coset space** — $G/H$ is a manifold when $H$ is a Lie subgroup
- **Lie subalgebra** — $T_1H$ is a Lie subalgebra of $\mathfrak{g}$

## Related
- **Classical groups** — all are Lie subgroups of $\mathrm{GL}(n)$

## Contrasts With
- **Immersed subgroup** — a weaker notion where $H$ need not be closed or embedded

# Common Errors

- **Error**: Confusing Lie subgroups with immersed subgroups.
  **Correction**: A Lie subgroup must be an embedded (closed) submanifold. An immersed subgroup like the irrational winding on the torus is not a Lie subgroup.

# Common Confusions

- **Confusion**: Terminology varies across books; some use "Lie subgroup" for what Kirillov calls "immersed subgroup."
  **Clarification**: In this text, Lie subgroup always means embedded (= closed) submanifold. See Remark 2.7.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.1, Definition 2.6 and Theorem 2.8, pages 9-10.

# Verification Notes

- Definition source: Direct from Definition 2.6
- Confidence rationale: Explicit definition and theorem in source
- Uncertainties: None
- Cross-reference status: Verified with Theorem 2.8, Remark 2.7, Theorem 3.19
