---
# === CORE IDENTIFICATION ===
concept: Nonabelian Group
slug: nonabelian-group

# === CLASSIFICATION ===
category: group-theory
subcategory: group-properties
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Groups"
chapter_number: 3
pdf_page: 47
section: "Definitions and Examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - noncommutative group

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends:
  - group
related:
  - symmetry
  - general-linear-group
  - quaternion-group
contrasts_with:
  - abelian-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
---

# Quick Definition

A nonabelian (or noncommutative) group is a group in which the operation is not commutative: there exist elements $a, b$ with $ab \neq ba$.

# Core Definition

"Groups not satisfying [the commutative] property are said to be nonabelian or noncommutative" (Judson, p. 47).

# Prerequisites

- **Group** — A nonabelian group is a group

# Key Properties

1. There exist $a, b \in G$ such that $ab \neq ba$
2. In general, $(gh)^n \neq g^n h^n$ (Theorem 3.23)
3. The smallest nonabelian group has order 6 ($S_3$)

# Construction / Recognition

## To Show a Group is Nonabelian:
1. Find two specific elements $a, b \in G$ with $ab \neq ba$
2. A single counterexample suffices

# Context & Application

Nonabelian groups arise naturally as symmetry groups of geometric objects and as matrix groups. They are more complex and richer in structure than abelian groups.

# Examples

**Example 1** (p. 48): The symmetry group $S_3$ is nonabelian: $\mu_1 \rho_1 \neq \rho_1 \mu_1$.

**Example 2** (p. 48): $GL_2(\mathbb{R})$ is nonabelian since matrix multiplication is not commutative.

**Example 3** (p. 48): The quaternion group $Q_8 = \{\pm 1, \pm I, \pm J, \pm K\}$ is nonabelian: $IJ = K$ but $JI = -K$.

# Relationships

## Builds Upon
- **group** — A nonabelian group is a group

## Related
- **symmetry** — Symmetry groups are typically nonabelian
- **general-linear-group** — A nonabelian group
- **quaternion-group** — A nonabelian group of order 8

## Contrasts With
- **abelian-group** — Commutative groups

# Common Confusions

- **Confusion**: Thinking $ab \neq ba$ for ALL pairs in a nonabelian group
  **Clarification**: Some pairs may still commute; only one non-commuting pair is needed

# Source Reference

Chapter 3: Groups, Section 3.2, pages 47-49.

# Verification Notes

- Definition source: Direct from p. 47
- Confidence: HIGH — explicit definition with examples
- Cross-reference status: Verified
- Uncertainties: None
